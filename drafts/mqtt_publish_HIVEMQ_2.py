import paho.mqtt.client as mqtt
import ssl
import time

# HiveMQ Cloud connection information
broker_url = "9cfa2865b0044c9987b33f563af5e70d.s2.eu.hivemq.cloud"
port = 8883  # Note: Use port 8883 for secure MQTT over TLS/SSL
username = "bm-user"
password = ',N:>6:6L_fXr7!f'
topic = "biomeiler"

# Define callback functions
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

# Create MQTT client with TLS/SSL support
client = mqtt.Client()
client.username_pw_set(username, password)
client.tls_set_context(context=ssl.create_default_context())

client.on_connect = on_connect
client.on_message = on_message

# Connect to HiveMQ Cloud broker
client.connect(broker_url, port, 60)

# Loop to maintain the connection and publish data
while True:
    # Replace "your_data" with your actual data
    data_to_publish = "your_data"
    client.publish(topic, data_to_publish)
    print(f"Published data: {data_to_publish}")
    
    # Wait for a moment before publishing the next message
    time.sleep(5)
