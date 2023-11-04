from Lab_2.internet import Internet
from machine import Pin
from picozero import Speaker
from time import sleep, time
from Lab_2.mqtt_as import MQTTClient, config
import uasyncio as asyncio


button = Pin(0, Pin.IN)

buzzer = Speaker(1)

note = 2300

car_r = Pin(15, Pin.OUT)
car_y = Pin(14, Pin.OUT)
car_g = Pin(13, Pin.OUT)
pedestrian_r = Pin(16, Pin.OUT)
pedestrian_y = Pin(17, Pin.OUT)
pedestrian_g = Pin(18, Pin.OUT)


def traffic_go():
    client.publish('s_status', 'RED')
    car_r.off()
    car_y.off()
    car_g.on()
    pedestrian_r.on()
    pedestrian_g.off()


def traffic_soon_stop():
    car_g.off()
    car_y.on()
    sleep(2)
    all_stop()


def all_stop():
    car_r.on()
    car_y.off()
    sleep(1)
    pedestrian_go()


def pedestrian_go():
    client.publish('s_status', 'GREEN')
    pedestrian_r.off()
    pedestrian_y.off()
    pedestrian_g.on()
    start_pedestrian_go = time()
    now = 0
    while now - start_pedestrian_go < 3:
        buzzer.play(note, 0.25, 5)
        buzzer.play(note, 0.1, 0)
        now = time()
    pedestrian_soon_stop()


def pedestrian_soon_stop():
    global client
    pedestrian_r.off()
    pedestrian_g.on()
    start_pedestrian_soon_stop = time()
    now = 0
    while now - start_pedestrian_soon_stop < 1:
        buzzer.play(1000, 0.4, 5)
        buzzer.play(1000, 0.2, 0)
        now = time()
    client.publish('s_status', 'RED')
    pedestrian_g.off()
    pedestrian_r.on()
    traffic_get_ready()


def traffic_get_ready():
    car_y.on()
    pedestrian_r.on()
    pedestrian_g.off()
    sleep(1)
    traffic_go()


def go():
    client.publish('s_status', 'GREEN')
    pedestrian_r.off()
    pedestrian_y.off()
    pedestrian_g.on()
    start_pedestrian_go = time()
    now = 0
    while now - start_pedestrian_go < 3:
        buzzer.play(note, 0.25, 5)
        buzzer.play(note, 0.1, 0)
        now = time()
    stop()


def stop():
    global client
    start_pedestrian_soon_stop = time()
    now = 0
    n = 0
    if n != 0:
        while now - start_pedestrian_soon_stop < 1:
            buzzer.play(1000, 0.4, 5)
            buzzer.play(1000, 0.2, 0)
            now = time()
    n += 1
    client.publish('s_status', 'RED')
    pedestrian_g.off()
    pedestrian_r.on()


def buttonEventCallback(client):
    pedestrian_y.on()
    #sleep(4)
    client.publish('s_status', 'YELLOW')
    #traffic_soon_stop()


def mqtt_connect(client):
    async def messages(client):
        async for _, msg, retained in client.queue:
            msg_d = msg.decode("UTF-8")
            print(('l_status', msg_d, retained))
            if msg_d == 'RED':
                sleep(1)
                pedestrian_go()
            elif msg_d == 'GREEN':
                pass

    async def up(client):
        while True:
            await client.up.wait()
            client.up.clear()
            await client.subscribe('SL')

    async def main(client):
        await client.connect()
        for coroutine in (up, messages):
            asyncio.create_task(coroutine(client))

    config["queue_len"] = 1
    MQTTClient.DEBUG = True
    try:
        asyncio.run(main(client))
    finally:
        client.disconnect()

config['server'] = '64.225.110.253'
config['port'] = 0  # 1883
config['user'] = 'king'
config['password'] = 'arthur'
config['ssid'] = 'Saturn'
config['wifi_pw'] = '1234567890'


Internet.connect()

client = MQTTClient(config)
mqtt_connect(client)

while True:
    stop()
    if button.value():
        buzzer.play(note, 0.5, 5)
        buttonEventCallback(client)

