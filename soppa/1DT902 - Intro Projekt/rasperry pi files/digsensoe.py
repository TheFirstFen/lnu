from machine import Pin
import time
import dht

digsensor = dht.DHT11(Pin(4))

digsensor.measure()
temp = digsensor.temperature()
hum = digsensor.humidity()

print(temp, hum)

