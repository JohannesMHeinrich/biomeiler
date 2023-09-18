#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 12:30:00 2023
# modified: 25/10/2021
# modified: 09/11/2021
# modified: 18/09/2023 -> changed to class

@author: jmheinrich

-------------------------------------------------------------------------------
tbf
-------------------------------------------------------------------------------
"""



from datetime import datetime
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_co2_v2 import BrickletCO2V2



class bm_class_CO2():

    def __init__(self):

        self.HOST = "localhost"
        self.PORT = 4223
        self.UID = "SiQ"                                                        # Change XYZ to the UID of your CO2 Bricklet 2.0

        ipcon = IPConnection()                                                  # Create IP connection
        co2 = BrickletCO2V2(self.UID, ipcon)                                    # Create device object

        ipcon.connect(self.HOST, self.PORT)                                     # Connect to brickd

        # Don't use device before ipcon is connected

        co2.register_callback(co2.CALLBACK_ALL_VALUES, self.cb_all_values)      # Register all values callback to function cb_all_values
        co2.set_all_values_callback_configuration(1000, False)                  # Set period for all values callback to 1s (1000ms)

        input("Press key to exit ")
        ipcon.disconnect()


    # Callback function for all values callback
    def cb_all_values(self, co2_concentration, temperature, humidity):

        print(float(co2_concentration), datetime.utcnow())
        print(float(temperature/100.0), datetime.utcnow())
        print(float(humidity/100.0), datetime.utcnow())



c = bm_class_CO2()