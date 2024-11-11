import uasyncio as asyncio
from machine import Pin
from picozero import Speaker
from time import sleep
from mqtt_async import MQTTClient, config


# MQTT STUFF
config["ssid"] = "vårat wifi?"
config["wifi_pw"] = "finns5gavenanledning"
config["server"] = "mqtt.iotlab.dev"
config["port"] = 1883
config["user"] = "king"
config["password"] = "arthur"

MQTTClient.DEBUG = True


def callback(topic, msg, retained):
    print((topic, msg, retained))


async def conn_han(client):
    await client.subscribe("foo_topic", 1)
    

async def main(client):
    await client.connect()
    n = 0
    while True:
        await asyncio.sleep(5)
        print("publish", n)
        # If WiFi is down the following will pause for the duration.
        await client.publish("CIDMV/jesper", "{}".format(n), qos=1)
        n += 1


config["subs_cb"] = callback
config["connect_coro"] = conn_han
client = MQTTClient(config)

try:
    asyncio.run(main(client))
finally:
    client.disconnect()  # Prevent LmacRxBlk:1 errors

buzzer = Speaker(5)
button = Pin(6, Pin.IN)
greenled = Pin(9, Pin.OUT)
yellowled = Pin(8, Pin.OUT)
redled = Pin(7, Pin.OUT)

greenled2 = Pin(19, Pin.OUT)
yellowled2 = Pin(18, Pin.OUT)
redled2 = Pin(16, Pin.OUT)


def trafficGo():
    global s
    greenled.value(1)
    redled2.value(1)
    if button.value() == 1:
        checktime()


def checktime():
    global s
    t = utime.ticks_ms()
    if t - s < 4000:
        print("ja")
        yellowled2.value(1)
        sltime = (4000 - (t - s)) / 1000
        print(sltime)
        time.sleep(sltime)
        print(sltime)
        trafficsoonStop()
    else:
        yellowled2.value(1)
        print("nej")
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
    greenled2.value(0)
    yellowled.value(1)
    redled2.value(1)
    time.sleep(1)
    yellowled.value(0)
    redled.value(0)
    count = 0
    


    

s = 0
t = 0
count = 0

while True:
    if count == 0:
        count = 1
        s = utime.ticks_ms()
        trafficGo()
    else:
        trafficGo()
# if _name_ == "_main_":
#     main()
