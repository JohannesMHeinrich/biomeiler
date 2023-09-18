#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: j. m. heinrich - 09/11/2021

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

class my_py_c_influxdb_2_1:

    def __init__(self):
        # You can generate an API token from the "API Tokens Tab" in the UI
        self.token = "Ql9CZi0s0P4scpNMqR6-_NdRNkQEZGQtvoAZ5qAbv7lMrQJlwM8oYnvFg5UNcsZHq4WGyAKt5QEIBHEzNPxEEg=="
        self.org = "AG_Jacob"
        self.bucket = "2021_Biomeiler"
        self.url="http://141.82.100.26:8086"
        
        self.client = InfluxDBClient(url=self.url, token=self.token, org=self.org)

        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def write_data_point(self, meas, field, value, time_now):
        data_point = [{"measurement": meas, "fields": {field: value}, "time": time_now}]
        self.write_api.write(self.bucket, self.org, data_point)
