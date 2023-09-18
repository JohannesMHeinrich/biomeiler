#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 17:00:00 2023

@author: jmheinrich

-------------------------------------------------------------------------------
tbf
-------------------------------------------------------------------------------
"""



from paho.mqtt import client as mqtt_client
import random
import time
import json



class bm_class_mqtt_publish():

    def __init__(self):


        self.broker = '141.82.98.208'
        self.port = 1883
        self.topic = "biomeiler"

        # generate client ID with pub prefix randomly
        self.client_id = f'python-mqtt-{random.randint(0, 1000)}'
        self.username = 'Sonde'
        self.password = 'Sonde1609'


    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(self.client_id)                                  # Set Connecting Client ID
        client.username_pw_set(self.username, self.password)
        client.on_connect = on_connect
        client.connect(self.broker, self.port)
        return client


    def publish(self, client):
        msg_count = 0
        while True:
            time.sleep(1)
            msg = f"messages: {msg_count}"
            result = client.publish(self.topic, msg)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(f"Send `{msg}` to topic `{self.topic}`")
            else:
                print(f"Failed to send message to topic {self.topic}")
            msg_count += 1


    def publish_bm_data_json(self, client, data):
        while True:
            time.sleep(1)
            result = client.publish(self.topic, data)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(f"Send `{data}` to topic `{self.topic}`")
            else:
                print(f"Failed to send message to topic {self.topic}")


    def run(self):
        client = self.connect_mqtt()
        client.loop_start()
        self.publish(client)



# c = bm_class_mqtt_publish()
# c.run()