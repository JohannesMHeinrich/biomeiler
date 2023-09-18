#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: j. m. heinrich - 16/11/2021

import serial
from time import sleep

ser = serial.Serial(port = '/dev/ttyS0', baudrate = 9600, bytesize = serial.EIGHTBITS, stopbits = serial.STOPBITS_ONE)

def get_firmware():
    ser.write(b'Y\r\n')
    sleep(1)
    b = str(ser.readline())
    return b

def get_CO2_UNfiltered():
    ser.write(b'z\r\n')
    sleep(1)
    b = str(ser.readline())[4:-5]
    return float(b)

def get_CO2_filtered():
    ser.write(b'Z\r\n')
    sleep(1)
    b = str(ser.readline())[4:-5]
    return float(b)

def get_Temperature():
    ser.write(b'T\r\n')
    sleep(1)
    b = str(ser.readline())[4:-5]
    return float(b)

def get_Humidity():
    ser.write(b'H\r\n')
    sleep(1)
    b = str(ser.readline())[4:-5]
    return float(b)

def get_Pressure_CC_Value():
    ser.write(b's\r\n')
    sleep(1)
    b = str(ser.readline())
    return b

def set_Pressure_CC_Value(value):
    mess = 'S ' + str(value) + '\r\n'
    mess_bytes = bytes(mess, 'utf-8')
    ser.write(mess_bytes)
    b = str(ser.readline())
    return b
    
def set_mode(value):
    mess = 'K ' + str(value) + '\r\n'
    mess_bytes = bytes(mess, 'utf-8')
    ser.write(mess_bytes)
    b = str(ser.readline())
    return b



print(get_CO2_filtered())

# while True:
#     ser.write(b'H\r\n')
#     b = str(ser.read())
#     
#     print(b)