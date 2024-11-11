import network
import time
from machine import Pin
from mqtt_async import MQTTClient

wlan = network.WLAN(network.AP_IF)
wlan.active(True)
wlan.connect("vårat wifi?","finns5gavenanledning")
time.sleep(5)
print(wlan.isconnected())

button = Pin(6, Pin.IN)

mqtt_server = 'mqtt.iotlab.dev'
client_id = 'jesper'
topic_pub = b'jesper'
topic_msg = b'Movement Detected'
config["server"] = "mqtt.iotlab.dev"
config["port"] = 1883
config["user"] = "king"
config["password"] = "arthur"

def mqtt_connect():
    client = MQTTClient(config, keepalive=3600)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
   print('Failed to connect to the MQTT Broker. Reconnecting...')
   time.sleep(5)
   machine.reset()
   

try:
   client = mqtt_connect()
except OSError as e:
   reconnect()
   
   
while True:
   if sensor.value() == 0:
        client.publish(topic_pub, topic_msg)
        time.sleep(3)
   else:
       pass