import network
import time
from machine import Pin
from umqtt import MQTTClient
import ubinascii
import machine
import dht
import json 

ssid = 'wifi-name'
password = 'wifi-password'
topic = "Samuel/RPIPico"
Button = Pin(0, Pin.IN)
LED = Pin(1, Pin.OUT)
DHT = dht.DHT11(Pin(16))

c = None

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print(f"Connecting to Wi-Fi: {ssid}")
        wlan.connect(ssid, password)
        
        while not wlan.isconnected():
            time.sleep(1)
            print(" .", end="")
    
    print("\nConnected to Wi-Fi")
    print(wlan.ifconfig()) 

def connect_mqtt():
    global c
    try:
        c = MQTTClient(client_id=ubinascii.hexlify(machine.unique_id()).decode(), server="broker.emqx.io", port=1883, user="", password="")
        c.connect()
        print("Connected to MQTT")
    except Exception as e:
        print(f"Failed to connect to MQTT: {e}")
        c = None

def publish_message(client, topic, message):
    if client:
        try:
            client.publish(topic, message)
            print(f"Message published to {topic}: {message}")
        except Exception as e:
            print(f"Failed to publish message: {e}")
    else:
        print("MQTT client not connected.")

def message_callback(topic, msg):
    print(f"Received message: {msg.decode()} from topic: {topic.decode()}")
    
    if msg.decode() == "1":
        LED.on()
        DHT_Sensor()
        time.sleep(2)
        publish_message(c, topic, "0")
    else:
        LED.off()

def subscribe_topic(client, topic):
    if client:
        client.set_callback(message_callback)
        try:
            client.subscribe(topic)
            print(f"Subscribed to {topic}")
        except Exception as e:
            print(f"Failed to subscribe to topic: {e}")
    else:
        print("MQTT client not connected.")

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

    payload = json.dumps({"t": temp, "h": hum})
    publish_message(c, topic, payload)

def main():
    connect_wifi()
    connect_mqtt()
    
    if c:
        subscribe_topic(c, topic)
        
        try:
            while True:
                c.check_msg()
                
                if button_pressed():
                    publish_message(c, topic, "1")
                    time.sleep(0.5)
                
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            print("Disconnecting from MQTT...")
            if c:
                c.disconnect()

main()
