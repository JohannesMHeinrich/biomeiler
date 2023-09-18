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
from tinkerforge.bricklet_outdoor_weather import BrickletOutdoorWeather



class bm_class_6147_weather_station():

    def __init__(self):

        self.HOST = "localhost"
        self.PORT = 4223
        self.UID = "SwJ"                                                        # Change XYZ to the UID of your CO2 Bricklet 2.0

        ipcon = IPConnection()                                                  # Create IP connection
        ow = BrickletOutdoorWeather(self.UID, ipcon)                            # Create device object

        ipcon.connect(self.HOST, self.PORT)                                               # Connect to brickd

        # Don't use device before ipcon is connected

        ow.set_station_callback_configuration(True)                             # Enable station data callbacks  
        ow.register_callback(ow.CALLBACK_STATION_DATA, cb_station_data)         # Register station data callback to function cb_station_data

        input("Press key to exit ")
        ipcon.disconnect()


    # Callback function for station data callback
    def cb_station_data(self, identifier, temperature, humidity, wind_speed, gust_speed, rain, wind_direction, battery_low):


        if wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_N:
            wind_direction = 360.0
        elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_NNE:
            wind_direction = 22.5
        elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_NE:
            wind_direction = 45.0
        elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_ENE:
            wind_direction = 67.5
        elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_E:
            wind_direction = 90.0
        elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_ESE:
            wind_direction = 112.5
        elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_SE:
            wind_direction = 135.0
        elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_SSE:
            wind_direction = 157.5
        elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_S:
            wind_direction = 180.0
        elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_SSW:
            wind_direction = 202.5
        elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_SW:
            wind_direction = 225.0
        elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_WSW:
            wind_direction = 247.5
        elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_W:
            wind_direction = 270.0
        elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_WNW:
            wind_direction = 292.5
        elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_NW:
            wind_direction = 315.0
        elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_NNW:
            wind_direction = 337.5
        elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_ERROR:
            wind_direction = -100
    
        print(float(temperature/10.0), datetime.utcnow())
        print(float(humidity), datetime.utcnow())
        print(float(wind_speed/10.0), datetime.utcnow())
        print(float(gust_speed/10.0), datetime.utcnow())
        print(float(rain/10.0), datetime.utcnow())
        print(float(wind_direction), datetime.utcnow())



c = bm_class_6147_weather_station()