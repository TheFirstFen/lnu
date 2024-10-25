from machine import Pin
from picozero import TemperatureSensor
from math import log, pow
import time
import dht

count = 0

button = Pin(2, Pin.IN)
print(button.value())

def temp_conversion(voltage):
    A = 0.001129148
    B = 0.000234125
    C = 0.0000000876741
    R = (voltage * 10000) / (3.3 - voltage)
    B_log = B * log(R)
    R_log = log(R)
    C_pow = C * (R_log**3)
    return (1/(A + B_log + C_pow)) - 273.15


analog_temp = TemperatureSensor(28, conversion=temp_conversion)

digital_temp = dht.DHT11(Pin(4))
digital_temp.measure()
dig_temp = digital_temp.temperature()
dig_hum = digital_temp.humidity()

while True:
    print(f"temp: {round(analog_temp.temp)}")
    print(f"temp: {dig_temp}, humidity: {dig_hum}%")
    if button.value() == 1:
        count += 1
        print(count)
        time.sleep(0.75)


