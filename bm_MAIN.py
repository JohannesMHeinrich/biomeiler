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

from bm_class_CO2 import bm_class_CO2
from bm_class_6147_weather_station import bm_class_6147_weather_station
from bm_class_arduino_hum_and_temp import bm_class_arduino_hum_and_temp



class c_program():

    def __init__(self):

        self.counter = 0

        self.start_CO2()
        self.start_6147_weather_station()
        self.start_arduino_hum_and_temp()

        self.test()

    def start_CO2(self):

        self.c_CO2 = bm_class_CO2()

    def start_6147_weather_station(self):

        self.c_6147 = bm_class_6147_weather_station()

    def start_arduino_hum_and_temp(self):

        self.c_hum_and_temp = bm_class_arduino_hum_and_temp()
        self.c_hum_and_temp.start_reading_in_thread()

    def test(self):
        while true:
            time.sleep(5)

            print(self.c_CO2.CO2)
            print(self.c_6147.temperature)
            print(self.c_hum_and_temp.rel_hum_1)


c = c_program()