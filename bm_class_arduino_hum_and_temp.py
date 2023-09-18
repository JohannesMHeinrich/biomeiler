#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 12:30:00 2023
# modified: 26/10/2021
# modified: 09/11/2021
# modified: 18/09/2023 -> changed to class

@author: jmheinrich

-------------------------------------------------------------------------------
tbf
-------------------------------------------------------------------------------
"""



import serial
from datetime import datetime
import time
import threading



class bm_class_arduino_hum_and_temp():

    def __init__(self):

        self.ser = serial.Serial('/dev/ttyUSB0', 9600)

        self.time_now = 'NaN'

        self.rel_hum_1 = 'NaN'
        self.rel_hum_2 = 'NaN'
        self.rel_hum_3 = 'NaN'

        self.temp_01 = 'NaN'
        self.temp_02 = 'NaN'
        self.temp_03 = 'NaN'
        self.temp_04 = 'NaN'
        self.temp_05 = 'NaN'
        self.temp_06 = 'NaN'
        self.temp_07 = 'NaN'
        self.temp_08 = 'NaN'
        self.temp_09 = 'NaN'
        self.temp_10 = 'NaN'
        self.temp_11 = 'NaN'
        self.temp_12 = 'NaN'

        print('---> started class bm_class_arduino_hum_and_temp')
        print('     sleeping for 5secs for arduino to boot properly')
        time.sleep(5)

    def read_serial(self):

        while True:

            b = str(self.ser.readline()).split(',')
            
            try:
            
                self.time_now = datetime.utcnow()

                self.rel_hum_1 = float(b[0][10:-2])
                self.rel_hum_2 = float(b[1][9:-2])
                self.rel_hum_3 = float(b[2][9:-2])
                
                self.temp_01 = float(b[3][25:-2])
                self.temp_02 = float(b[4][25:-2])
                self.temp_03 = float(b[5][25:-2])
                self.temp_04 = float(b[6][25:-2])
                self.temp_05 = float(b[7][25:-2])
                self.temp_06 = float(b[8][25:-2])
                self.temp_07 = float(b[9][25:-2])
                self.temp_08 = float(b[10][25:-2])
                self.temp_09 = float(b[11][25:-2])
                self.temp_10 = float(b[12][25:-2])
                self.temp_11 = float(b[13][25:-2])
                self.temp_12 = float(b[14][25:-2])
                
            except:
                
                print("---> arduino: could not convert to floats")
                print("     trying again in 5s")
                time.sleep(5)

            time.sleep(60)

    def start_reading_in_thread(self):

        x = threading.Thread(target=self.read_serial)
        x.start()
