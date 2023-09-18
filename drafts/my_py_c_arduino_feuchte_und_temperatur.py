#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: j. m. heinrich - 26/10/2021
# modified: j. m. heinrich - 09/11/2021

import serial

from my_file_writer import my_writer
from datetime import datetime
import time

from my_py_c_influxdb_2_1 import my_py_c_influxdb_2_1

# initialize connector to influx db
influxDB = my_py_c_influxdb_2_1()

ser = serial.Serial('/dev/ttyUSB0', 9600)

time.sleep(5)

while True:
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
        
        my_writer('soil_moisture', [str(bf_1), str(bf_2), str(bf_3)])
        my_writer('soil_temperature', [str(T_1), str(T_2), str(T_3), str(T_4), str(T_5), str(T_6), str(T_7), str(T_8), str(T_9), str(T_10), str(T_11), str(T_12)])

        influxDB.write_data_point("CSMS_v12_Feuchtigkeiten", "rel_F_1", bf_1, time_now)
        influxDB.write_data_point("CSMS_v12_Feuchtigkeiten", "rel_F_2", bf_2, time_now)
        influxDB.write_data_point("CSMS_v12_Feuchtigkeiten", "rel_F_3", bf_3, time_now)
        influxDB.write_data_point("DS18B20_Temperaturen", "T_1", T_1, time_now)
        influxDB.write_data_point("DS18B20_Temperaturen", "T_2", T_2, time_now)
        influxDB.write_data_point("DS18B20_Temperaturen", "T_3", T_3, time_now)
        influxDB.write_data_point("DS18B20_Temperaturen", "T_4", T_4, time_now)
        influxDB.write_data_point("DS18B20_Temperaturen", "T_5", T_5, time_now)
        influxDB.write_data_point("DS18B20_Temperaturen", "T_6", T_6, time_now)
        influxDB.write_data_point("DS18B20_Temperaturen", "T_7", T_7, time_now)
        influxDB.write_data_point("DS18B20_Temperaturen", "T_8", T_8, time_now)
        influxDB.write_data_point("DS18B20_Temperaturen", "T_9", T_9, time_now)
        influxDB.write_data_point("DS18B20_Temperaturen", "T_10", T_10, time_now)
        influxDB.write_data_point("DS18B20_Temperaturen", "T_11", T_11, time_now)
        influxDB.write_data_point("DS18B20_Temperaturen", "T_12", T_12, time_now)
        
    except:
        
        print("could not convert to floats")
        print("trying again in 5s")
        time.sleep(5)