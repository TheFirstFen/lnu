import uasyncio as asyncio
from machine import Pin
from picozero import Speaker
from time import sleep
import time
import utime
from mqtt_async import MQTTClient, config


# MQTT STUFF
config["ssid"] = "Emils Galaxy"
config["wifi_pw"] = "gerp1112"
config["server"] = "mqtt.iotlab.dev"
config["port"] = 1883
config["user"] = "king"
config["password"] = "arthur"

MQTTClient.DEBUG = True

s = 0
t = 0
count = 0
buttonpress = 0
message = False

buzzer = Speaker(5)
button = Pin(6, Pin.IN)
greenled = Pin(9, Pin.OUT)
yellowled = Pin(8, Pin.OUT)
redled = Pin(7, Pin.OUT)

greenled2 = Pin(19, Pin.OUT)
yellowled2 = Pin(18, Pin.OUT)
redled2 = Pin(16, Pin.OUT)



def trafficGo():
    global buttonpress
    print("hej")
    greenled.value(1)
    redled2.value(1)
    buttonpress = 1
    checktime()


def checktime():
    global s
    t = utime.ticks_ms()
    if t - s < 4000:
        sltime = (4000 - (t - s)) / 1000
        time.sleep(sltime)
        trafficsoonStop()
    else:
        yellowled2.value(1)
        trafficsoonStop()
    

def trafficsoonStop():
    greenled.value(0)
    yellowled.value(1)
    redled2.value(1)
    time.sleep(2)
    allStop()
    
def allStop():
    yellowled.value(0)
    redled.value(1)
    redled2.value(1)
    time.sleep(1)
    pedestrianGo()
    
    
def pedestrianGo():
    global freq
    yellowled2.value(0)
    redled2.value(0)
    redled.value(1)
    greenled2.value(1)
    mt = utime.ticks_ms()
    ms = utime.ticks_ms()
    while mt - ms < 3000:
        buzzer.play(100, 0.05)
        buzzer.play(0, 0.05)
        mt = utime.ticks_ms()
    pedestriansoonStop()
    
def pedestriansoonStop():
    global freq
    mt = utime.ticks_ms()
    ms = utime.ticks_ms()
    while mt - ms < 1000:
        buzzer.play(100, 0.1)
        buzzer.play(0, 0.1)
        mt = utime.ticks_ms()
    trafficgetready()
    
    
def trafficgetready():
    global count
    global buttonpress
    global s
    greenled2.value(0)
    yellowled.value(1)
    redled2.value(1)
    time.sleep(1)
    yellowled.value(0)
    redled.value(0)
    buttonpress = 0
    count = 0
    s = utime.ticks_ms()
    


def start():
    global count
    if count == 0:
        count = 1
        s = utime.ticks_ms()
        trafficGo()
    else:
        trafficGo()
            
            
def callback(topic, msg, retained, qos):
    global message
    if msg == b'1':
        message = True
    else:
        message = False


async def conn_han(client):
    await client.subscribe("JE/j2_status", 1)




async def main(client):
    global buttonpress
    global count
    global message
    await client.connect()
    while True:
        greenled.value(1)
        await client.publish("JE/j_status", "{}".format(buttonpress), qos=1)
        if button.value() == 1 or message is True:
            yellowled2.value(1)
            if count == 0:
                buttonpress = 1
                count = 1
                await client.publish("JE/j_status", "{}".format(buttonpress), qos=1)
                trafficGo()
            else:
                buttonpress = 1
                await asyncio.sleep(5)
                print("publish", buttonpress)
                # If WiFi is down the following will pause for the duration.
                await client.publish("JE/j_status", "{}".format(buttonpress), qos=1)
                trafficGo()
            message = False
        else:
            pass


config["subs_cb"] = callback
config["connect_coro"] = conn_han
client = MQTTClient(config)

try:
    asyncio.run(main(client))
finally:
    client.disconnect()  # Prevent LmacRxBlk:1 errors


# if _name_ == "_main_":
#     main()
