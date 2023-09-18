#!/usr/bin/env python
# -*- coding: utf-8 -*-
# modified: j. m. heinrich - 25/10/2021
# modified: j. m. heinrich - 09/11/2021

HOST = "localhost"
PORT = 4223
UID = "SiQ" # Change XYZ to the UID of your CO2 Bricklet 2.0

from datetime import datetime

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_co2_v2 import BrickletCO2V2

# from my_file_writer import my_writer

# from my_py_c_influxdb_2_1 import my_py_c_influxdb_2_1


# # initialize connector to influx db
# influxDB = my_py_c_influxdb_2_1()


# Callback function for all values callback
def cb_all_values(co2_concentration, temperature, humidity):
    
    # my_writer('CO2', [str(co2_concentration) + " ppm", str(temperature/100.0) + " C", str(humidity/100.0) + " %RH"])
    
    # influxDB.write_data_point("CO2_Sensor", "CO2", float(co2_concentration), datetime.utcnow())
    # influxDB.write_data_point("CO2_Sensor", "Temperatur", float(temperature/100.0), datetime.utcnow())
    # influxDB.write_data_point("CO2_Sensor", "Feuchtigkeit", float(humidity/100.0), datetime.utcnow())

    print(float(co2_concentration), datetime.utcnow())
    print(float(temperature/100.0), datetime.utcnow())
    print(float(humidity/100.0), datetime.utcnow())
    
if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    co2 = BrickletCO2V2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register all values callback to function cb_all_values
    co2.register_callback(co2.CALLBACK_ALL_VALUES, cb_all_values)

    # Set period for all values callback to 1s (1000ms)
    co2.set_all_values_callback_configuration(1000, False)

    input("Press key to exit ")
    ipcon.disconnect()
