A Proof of concept for a fitness monitor:
- A Python code that connects using BLE from a heart beat sensor (Polar H9) and use Zabbix sender Python libraries (non async) to send data. There is a newer version of Zabbix libraries that have async.
- A Javascript code that read from zabbix API, find the last retrieved strava activity ID, and import the next activity that has a heart rate data into Zabbix using the new API (v7.0).

Remember to setup macros, and the variables in the Python script.
Follow intructions on how to get the Strava refresh token: https://developers.strava.com/docs/authentication/
