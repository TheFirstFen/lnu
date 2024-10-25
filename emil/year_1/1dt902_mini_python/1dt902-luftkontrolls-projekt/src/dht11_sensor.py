import dht
from machine import Pin

digital_temp = dht.DHT11(Pin(0))
digital_temp.measure()
dig_temp = digital_temp.temperature()
dig_hum = digital_temp.humidity()

print(f"temp: {dig_temp}, humidity: {dig_hum}%")
