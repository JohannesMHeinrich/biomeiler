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



class bm_class_arduino_hum_and_temp():

    def __init__(self):

        self.ser = serial.Serial('/dev/ttyUSB0', 9600)

        time.sleep(5)

    def read_serial(self):

        b = str(ser.readline()).split(',')
        
        try:
        
            bf_1 = float(b[0][10:-2])
            bf_2 = float(b[1][9:-2])
            bf_3 = float(b[2][9:-2])
            
            T_1 = float(b[3][25:-2])
            T_2 = float(b[4][25:-2])
            T_3 = float(b[5][25:-2])
            T_4 = float(b[6][25:-2])

            T_5 = float(b[7][25:-2])
            T_6 = float(b[8][25:-2])
            T_7 = float(b[9][25:-2])
            T_8 = float(b[10][25:-2])
            
            T_9 = float(b[11][25:-2])
            T_10 = float(b[12][25:-2])
            T_11 = float(b[13][25:-2])
            T_12 = float(b[14][25:-2])
            
            time_now = datetime.utcnow()

            print(str(bf_1), str(bf_2), str(bf_3))
            print(str(T_1), str(T_2), str(T_3), str(T_4), str(T_5), str(T_6), str(T_7), str(T_8), str(T_9), str(T_10), str(T_11), str(T_12))
            
        except:
            
            print("could not convert to floats")
            print("trying again in 5s")
            time.sleep(5)

    def start_reading_in_loop(self):

        while True:

            self.read_serial()



c = bm_class_arduino_hum_and_temp()
c.start_reading_in_loop()