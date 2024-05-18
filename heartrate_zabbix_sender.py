import asyncio
from bleak import BleakClient
from zabbix_utils import Sender

# Replace these values with your actual MAC address and characteristic UUID
mac_address = "XX:XX:XX:XX:XX:XX"
characteristic_uuid = "00002a37-0000-1000-8000-00805f9b34fb" #Polar H9
zabbix_server = "zabbixserver"
zabbix_host = "zabbix host"

# Initialize Zabbix Sender
zabbix_sender = Sender(server=zabbix_server, port=10051)

async def notify_handler(sender, data):
    # Decode the received data
    heart_rate = decode_heart_rate(data)
    
    # Send the heart rate data to Zabbix
    response = zabbix_sender.send_value(zabbix_host, 'heartrate', heart_rate)
    print(f"Response from Zabbix: {response}")

def decode_heart_rate(data):
    heart_rate = int(data[1])
    return heart_rate

async def connect_and_notify(mac_address, characteristic_uuid):
    async with BleakClient(mac_address) as client:
        # Check if the device is connected
        if await client.is_connected():
            print("Connected to the device.")

            # Start notifications on the specified characteristic
            await client.start_notify(characteristic_uuid, notify_handler)
            print(f"Notifications started on characteristic: {characteristic_uuid}")

            # Keep the connection open to continue receiving notifications
            while True:
                await asyncio.sleep(1)

        else:
            print("Failed to connect to the device.")

# Run the connection and notification process
asyncio.run(connect_and_notify(mac_address, characteristic_uuid))
