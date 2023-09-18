#!/usr/bin/env python
# -*- coding: utf-8 -*-
# modified: j. m. heinrich - 25/10/2021
# modified: j. m. heinrich - 09/11/2021

HOST = "localhost"
PORT = 4223
UID = "SwJ" # Change XYZ to the UID of your Outdoor Weather Bricklet

from datetime import datetime

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_outdoor_weather import BrickletOutdoorWeather

from my_file_writer import my_writer

from my_py_c_influxdb_2_1 import my_py_c_influxdb_2_1


# initialize connector to influx db
influxDB = my_py_c_influxdb_2_1()


# Callback function for station data callback
def cb_station_data(identifier, temperature, humidity, wind_speed, gust_speed, rain, wind_direction, battery_low):


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
    
    # write to .txt file
    my_writer('Weather', [str(temperature/10.0) + " C", str(humidity) + " %RH", str(wind_speed/10.0) + " m/s", str(gust_speed/10.0) + " m/s", str(rain/10.0) + " mm", str(wind_direction)])
    
    # write to influxdb 2.1
    influxDB.write_data_point("Wetterstation", "Temperatur", float(temperature/10.0), datetime.utcnow())
    influxDB.write_data_point("Wetterstation", "rel. Feuchtigkeit", float(humidity), datetime.utcnow())
    influxDB.write_data_point("Wetterstation", "Windgeschwindigkeit", float(wind_speed/10.0), datetime.utcnow())
    influxDB.write_data_point("Wetterstation", "Windboen", float(gust_speed/10.0), datetime.utcnow())
    influxDB.write_data_point("Wetterstation", "Regen", float(rain/10.0), datetime.utcnow())
    influxDB.write_data_point("Wetterstation", "Windrichtung", float(wind_direction), datetime.utcnow()) 

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    ow = BrickletOutdoorWeather(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Enable station data callbacks
    ow.set_station_callback_configuration(True)

    # Register station data callback to function cb_station_data
    ow.register_callback(ow.CALLBACK_STATION_DATA, cb_station_data)

    input("Press key to exit ")
    ipcon.disconnect()
