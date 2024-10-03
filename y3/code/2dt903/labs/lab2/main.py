import network
import time
from machine import Pin
from umqtt import MQTTClient
import ubinascii
import machine
import dht
import json 

ssid = 'fen'
password = '3q1t6ibj'

URL = "broker.emqx.io"
Port = 1883
mqtt_user = ""
mqtt_password = ""
Topic = "U/test2"
Button = Pin(0, Pin.IN)
LED = Pin(1, Pin.OUT)
DHT = dht.DHT11(Pin(16))


client_id = ubinascii.hexlify(machine.unique_id()).decode()


client = MQTTClient(client_id, URL, Port, mqtt_user, mqtt_password)


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print(f"Connecting to Wi-Fi: {ssid}")
        wlan.connect(ssid, password)
        
        
        while not wlan.isconnected():
            time.sleep(1)
            print(".", end="")
    
    print("\nConnected to Wi-Fi")
    print(wlan.ifconfig()) 

def connect_mqtt():
    global client
    
    
    try:
        client.connect()
        print("Connected to MQTT broker")
    except Exception as e:
        print(f"Failed to connect to MQTT broker: {e}")
        return None
    
    return client

def publish_message(client, topic, message):
    try:
        client.publish(topic, message)
        print(f"Message published to {topic}: {message}")
    except Exception as e:
        print(f"Failed to publish message: {e}")

def message_callback(topic, msg):
    print(f"Received message: {msg.decode()} from topic: {topic.decode()}")
    
    if msg.decode() == "1":
        LED.on()
        DHT_Sensor()
        time.sleep(2)
        publish_message(client, Topic, "0")
    else:
        LED.off()

def subscribe_topic(client, topic):
    client.set_callback(message_callback)
    
    try:
        client.subscribe(topic)
        print(f"Subscribed to {topic}")
    except Exception as e:
        print(f"Failed to subscribe to topic: {e}")

def button_pressed():
    if Button.value() == 1:
        time.sleep(0.05)
        if Button.value() == 1:
            return True
    return False

def DHT_Sensor():
    DHT.measure()
    temp = DHT.temperature() 
    hum = DHT.humidity()
    print("Temp:", temp, "Hum:", hum)

    payload = json.dumps({"t": temp, "h": hum})
    publish_message(client, Topic, payload)

def main():
    connect_wifi()
    
    mqtt_client = connect_mqtt()
    
    if mqtt_client:
        subscribe_topic(mqtt_client, Topic)
        
        try:
            while True:
                mqtt_client.check_msg()
                
                if button_pressed():
                    publish_message(mqtt_client, Topic, "1")
                    time.sleep(0.5)
                
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            print("Disconnecting from MQTT...")
            mqtt_client.disconnect()

main()

