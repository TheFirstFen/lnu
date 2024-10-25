import network
import time
import machine
import umqtt
import ubinascii
import dht
import json 

ssid = 'fen'
password = '3q1t6ibj'
topic = "Samuel/RPIPico"
btn = machine.Pin(0, machine.Pin.IN)
led = machine.Pin(1, machine.Pin.OUT)
dht = dht.DHT11(machine.Pin(16))

mqtt_c = None

def conn_wifi():
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

def conn_mqtt():
    global mqtt_c
    try:
        mqtt_c = umqtt.MQTTClient(client_id=ubinascii.hexlify(machine.unique_id()).decode(), server="broker.emqx.io", port=1883, user="", password="")
        mqtt_c.connect()
        print("Connected to MQTT")
    except Exception as e:
        print(f"Failed to connect to MQTT: {e}")
        mqtt_c = None

def p_msg(mqtt_c, topic, message):
    
    if mqtt_c:
        try:
            mqtt_c.publish(topic, message)
            print(f"Message published to {topic}: {message}")
        except Exception as e:
            print(f"Failed to publish message: {e}")
    else:
        print("MQTT client not connected.")
    led.off()

def msg_cb(topic, msg):
    print(f"Received message: {msg.decode()} from topic: {topic.decode()} \n")
    if msg.decode() == "Data comming..." or msg.decode() == "Btn data comming...":
        temp()
        p_msg(mqtt_c, topic, "Data ending...")
    else:
        led.on()

def sub_topic(mqtt_c, topic):
    if mqtt_c:
        mqtt_c.set_callback(msg_cb)
        try:
            mqtt_c.subscribe(topic)
            print(f"Subscribed to {topic}")
        except Exception as e:
            print(f"Failed to subscribe to topic: {e}")
    else:
        print("MQTT client not connected.")

def btn_cb():
    if btn.value() == 1:
        time.sleep(0.05)
        if btn.value() == 1:
            return True
    return False

def temp():
    dht.measure()
    temp = dht.temperature() 
    hum = dht.humidity()

    payload = json.dumps({"temp": temp, "hum": hum})
    p_msg(mqtt_c, topic, payload)

def main():
    conn_wifi()
    conn_mqtt()
    
    if mqtt_c:
        sub_topic(mqtt_c, topic)
        
        try:
            elapsed_time = time.time()
            
            while True:
                mqtt_c.check_msg()
                
                if time.time() - elapsed_time >= 300:
                    p_msg(c, topic, "Data comming...")
                    elapsed_time = time.time()
                
                if btn_cb():
                    led.on()
                    p_msg(mqtt_c, topic, "Btn data comming...")
                    time.sleep(0.5)
                led.off()
                
        except KeyboardInterrupt:
            print("Disconnecting from MQTT...")
            if mqtt_c:
                mqtt_c.disconnect()

main()
