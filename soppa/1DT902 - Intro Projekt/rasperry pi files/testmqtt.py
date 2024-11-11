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
        await client.publish("jesper/test", "{}".format(n), qos=1)
        n += 1


config["subs_cb"] = callback
config["connect_coro"] = conn_han
client = MQTTClient(config)

try:
    asyncio.run(main(client))
finally:
    client.disconnect()  # Prevent LmacRxBlk:1 errors

car_leds = {
    "YELLOW": Pin(8, Pin.OUT),
    "GREEN": Pin(9, Pin.OUT),
    "RED": Pin(7, Pin.OUT),
}

ped_leds = {
    "GREEN": Pin(19, Pin.OUT),
    "RED": Pin(16, Pin.OUT),
}
speaker = Speaker(5)
button = Pin(6, Pin.IN)


def reset_leds():
    for led in car_leds.values():
        led.off()
    for led in ped_leds.values():
        led.off()
    car_leds["GREEN"].on()
    ped_leds["RED"].on()


def let_peds_walk():
    car_leds["GREEN"].off()
    car_leds["YELLOW"].on()
    sleep(0.9)
    car_leds["YELLOW"].off()
    car_leds["RED"].on()

    ped_leds["RED"].off()
    ped_leds["GREEN"].on()
    for i in range(100, 1, -3):
        for freq in (2637, 1865):
            speaker.play(freq, 1 / i)
            sleep(1 / i)
    ped_leds["GREEN"].off()
    ped_leds["RED"].on()

    car_leds["YELLOW"].on()
    sleep(0.9)
    car_leds["RED"].off()
    car_leds["YELLOW"].off()
    car_leds["GREEN"].on()


def button_pressed(x=None):
    let_peds_walk()


button.irq(handler=button_pressed, trigger=Pin.IRQ_FALLING)
reset_leds()
