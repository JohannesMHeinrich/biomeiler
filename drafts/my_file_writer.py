#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: j. m. heinrich - 25/10/2021

from datetime import datetime

def my_writer(fname, list_of_values):
    date_today = datetime.today().strftime('%Y_%m_%d')
    time_now = datetime.today().strftime('%H:%M:%S')
    
    fn = 'data/' + str(date_today) + '_' + str(fname) + '.txt'
    
    with open(fn, 'a+') as f:
        f.write(time_now)
        
        for i in range(len(list_of_values)):
            f.write(', ' + str(list_of_values[i]))
            
        f.write('\n')
