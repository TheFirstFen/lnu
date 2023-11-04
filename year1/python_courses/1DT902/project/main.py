from machine import Pin
from time import sleep
import dht

d = dht.DHT11(Pin(0))

while True:
    d.measure()
    print(f"Temprature: {d.temperature()} °C and Humidity: {d.humidity()} %")
    sleep(300)


user = "sensor_one"
key = "JA4eRQhwizvMB69VA2UgXu5iP9KsgatvsCxnExjyBy3em"
