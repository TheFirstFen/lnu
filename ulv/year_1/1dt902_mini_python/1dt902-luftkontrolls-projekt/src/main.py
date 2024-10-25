import time
from lib.mqtt_async import MQTTClient, config
import uasyncio as uasync
from machine import Pin, I2C, deepsleep
from picozero import Speaker
import dht
import CCS811

config["ssid"] = "LNU-iot"
config["wifi_pw"] = "modermodemet"
config['server'] = 'mqtt.iotlab.dev'
config['port'] = 1883
config['user'] = 'king'
config['password'] = 'arthur'
MQTTClient.DEBUG = True

client = MQTTClient(config)



async def main(client):
    global temp
    global hum
    global message
    await client.connect()
    counter = 0
    sda = Pin(4, Pin.IN)
    scl = Pin(5, Pin.IN)
    i2c = I2C(0, scl=scl, sda=sda)
    i2c_adress = i2c.scan()
    if i2c_adress == [91]:
        css = CCS811.CCS811(i2c=i2c, addr=91)
    else:
        css = CCS811.CCS811(i2c=i2c, addr=90)
    dht11_th = dht.DHT11(Pin(0))
    checking = 0
    while True:
        if not client.isconnected():  # check if raspberry is connected to the wifi
            while checking < 5:  # if wifi not connected, try 5 times
                client.connect()
                time.sleep(2)
                checking += 1
                if client.isconnected():  # if wifi is connected, print in terminal
                    print('Connected to WIFI')
        else:
            pass

        if counter < 10:
            css.data_ready()  # We tell the sensor it's ready to collect data
            co2 = css.eCO2  # CO2 value stored in this variable
            tvoc = css.tVOC
            counter += 1
            time.sleep(1)
        else:
            dht11_th.measure()
            temp = dht11_th.temperature()
            hum = dht11_th.humidity()
            await client.publish("MKE/temp", "{}".format(temp), qos=1)
            await client.publish("MKE/hum", "{}".format(hum), qos=1)
            css.data_ready()  # We tell the sensor it's ready to collect data
            co2 = css.eCO2  # CO2 value stored in this variable
            tvoc = css.tVOC
            await client.publish("MKE/CO2", "{}".format(co2), qos=1)
            await client.publish("MKE/Tvoc", "{}".format(tvoc), qos=1)
            time.sleep(10)


try:
    uasync.run(main(client))
finally:
    client.disconnect()
