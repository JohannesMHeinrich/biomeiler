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
import threading

from bm_class_CO2 import bm_class_CO2
from bm_class_6147_weather_station import bm_class_6147_weather_station
from bm_class_arduino_hum_and_temp import bm_class_arduino_hum_and_temp
from bm_class_mqtt_publish import bm_class_mqtt_publish



class c_program():

    def __init__(self):
        
        self.mqtt_publish = bm_class_mqtt_publish()
        self.client = self.mqtt_publish.connect_mqtt()
#         self.client.loop_start()
# 
#         self.c_CO2 = bm_class_CO2()
#         self.payload_CO2_CO2 = 'NaN'
# 
#         thread_CO2 = threading.Thread(target=self.start_CO2)
#         thread_CO2.start()

        self.c_CO2 = bm_class_CO2()

        self.c_6147 = bm_class_6147_weather_station()
        
        self.c_hum_and_temp = bm_class_arduino_hum_and_temp()
        self.c_hum_and_temp.start_reading_in_thread()
        
    def get_json_payload(self, _time, _name, _value):
        
        if isinstance(_time, datetime):
            _time = _time.isoformat()
        else:
            _time = datetime.utcnow().isoformat()
        
        payload = {
            'Timestamp': _time,
            str(_name): _value
        }

        return json.dumps(payload)
    
    def update_payloads(self, intervall = 900):
        
        i = 0
        
        while True:
            
            print('-> iteration ' + str(i) + '----------------')
            self.mqtt_publish.publish_bm_data_json(self.client, self.get_json_payload(self.c_CO2.time_now, 'CO2-CO2', self.c_CO2.CO2))
            print(self.get_json_payload(self.c_CO2.time_now, 'CO2-CO2', self.c_CO2.CO2))
            print(self.get_json_payload(self.c_CO2.time_now, 'CO2-temperature', self.c_CO2.temperature))
            print(self.get_json_payload(self.c_CO2.time_now, 'CO2-humidity', self.c_CO2.humidity))
            print(' ')
            
            print(self.get_json_payload(self.c_6147.time_now, 'WS-temperature', self.c_6147.temperature))
            print(self.get_json_payload(self.c_6147.time_now, 'WS-wind_speed', self.c_6147.wind_speed))
            print(self.get_json_payload(self.c_6147.time_now, 'WS-gust_speed', self.c_6147.gust_speed))
            print(self.get_json_payload(self.c_6147.time_now, 'WS-rain', self.c_6147.rain))
            print(self.get_json_payload(self.c_6147.time_now, 'WS-wind_direction', self.c_6147.wind_direction))
            print(self.get_json_payload(self.c_6147.time_now, 'WS-battery_low', self.c_6147.battery_low))
            print(' ')
            
            print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-rel_hum_1', self.c_hum_and_temp.rel_hum_1))
            print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-rel_hum_2', self.c_hum_and_temp.rel_hum_2))
            print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-rel_hum_3', self.c_hum_and_temp.rel_hum_3))
            
            print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_01', self.c_hum_and_temp.temp_01))
            print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_02', self.c_hum_and_temp.temp_02))
            print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_03', self.c_hum_and_temp.temp_03))
            print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_04', self.c_hum_and_temp.temp_04))
            print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_05', self.c_hum_and_temp.temp_05))
            print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_06', self.c_hum_and_temp.temp_06))
            print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_07', self.c_hum_and_temp.temp_07))
            print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_08', self.c_hum_and_temp.temp_08))
            print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_09', self.c_hum_and_temp.temp_09))
            print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_10', self.c_hum_and_temp.temp_10))
            print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_11', self.c_hum_and_temp.temp_11))
            print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_12', self.c_hum_and_temp.temp_12))
             
            time.sleep(intervall)
            
            i = i + 1

    def run(self):
        
        self.mqtt_publish.publish_bm_data_json(self.client, self.get_json_payload(self.c_CO2.time_now, 'CO2-CO2', self.c_CO2.CO2))

#         while True:
#             print('-----------------------')
#             print(self.get_json_payload(self.c_CO2.time_now, 'CO2-CO2', self.c_CO2.CO2))
#             print(self.get_json_payload(self.c_CO2.time_now, 'CO2-temperature', self.c_CO2.temperature))
#             print(self.get_json_payload(self.c_CO2.time_now, 'CO2-humidity', self.c_CO2.humidity))
#             print(' ')
#             
#             print(self.get_json_payload(self.c_6147.time_now, 'WS-temperature', self.c_6147.temperature))
#             print(self.get_json_payload(self.c_6147.time_now, 'WS-wind_speed', self.c_6147.wind_speed))
#             print(self.get_json_payload(self.c_6147.time_now, 'WS-gust_speed', self.c_6147.gust_speed))
#             print(self.get_json_payload(self.c_6147.time_now, 'WS-rain', self.c_6147.rain))
#             print(self.get_json_payload(self.c_6147.time_now, 'WS-wind_direction', self.c_6147.wind_direction))
#             print(self.get_json_payload(self.c_6147.time_now, 'WS-battery_low', self.c_6147.battery_low))
#             print(' ')
#             
#             print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-rel_hum_1', self.c_hum_and_temp.rel_hum_1))
#             print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-rel_hum_2', self.c_hum_and_temp.rel_hum_2))
#             print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-rel_hum_3', self.c_hum_and_temp.rel_hum_3))
#             
#             print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_01', self.c_hum_and_temp.temp_01))
#             print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_02', self.c_hum_and_temp.temp_02))
#             print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_03', self.c_hum_and_temp.temp_03))
#             print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_04', self.c_hum_and_temp.temp_04))
#             print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_05', self.c_hum_and_temp.temp_05))
#             print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_06', self.c_hum_and_temp.temp_06))
#             print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_07', self.c_hum_and_temp.temp_07))
#             print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_08', self.c_hum_and_temp.temp_08))
#             print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_09', self.c_hum_and_temp.temp_09))
#             print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_10', self.c_hum_and_temp.temp_10))
#             print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_11', self.c_hum_and_temp.temp_11))
#             print(self.get_json_payload(self.c_hum_and_temp.time_now, 'Arduino-temp_12', self.c_hum_and_temp.temp_12))
#              
# #              self.mqtt_publish.publish_bm_data_json(self.client, self.get_json_payload(self.c_CO2.time_now, 'CO2', self.c_CO2.CO2))
# 
#             time.sleep(intervall)


c = c_program()
c.update_payloads(5)
# c.run()