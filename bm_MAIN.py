#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:30:00 2023

@author: jmheinrich

-------------------------------------------------------------------------------
tbf
-------------------------------------------------------------------------------
"""

from datetime import datetime, timedelta
import time
import json

from bm_class_CO2 import bm_class_CO2
from bm_class_6147_weather_station import bm_class_6147_weather_station
from bm_class_arduino_hum_and_temp import bm_class_arduino_hum_and_temp
from bm_class_mqtt_publish import bm_class_mqtt_publish



class c_program():

    def __init__(self):

        self.mqtt_publish = bm_class_mqtt_publish()
        self.client = self.mqtt_publish.connect_mqtt()
        self.client.loop_start()

        self.start_CO2()
        self.start_6147_weather_station()
        self.start_arduino_hum_and_temp()



    def start_CO2(self):

        self.c_CO2 = bm_class_CO2()

        CO2 = {
            'Timestamp': self.c_CO2.time_now,
            'CO2': self.c_CO2.CO2
        }

        payload_CO2 = json.dumps(CO2)

        self.mqtt_publish.publish_bm_data_json(self.client, payload_CO2)

    def start_6147_weather_station(self):

        self.c_6147 = bm_class_6147_weather_station()

    def start_arduino_hum_and_temp(self):

        self.c_hum_and_temp = bm_class_arduino_hum_and_temp()
        self.c_hum_and_temp.start_reading_in_thread()

    def run(self, intervall = 900):

        while True:

            print(self.c_CO2.CO2)
            print(self.c_6147.temperature)
            print(self.c_hum_and_temp.rel_hum_1)

            time.sleep(intervall)


c = c_program()
c.run(5)