from machine import Pin
from time import sleep

led_light = Pin('LED', Pin.OUT)

try:
    while True:
        led_light.toggle()
        sleep(1)
except KeyboardInterrupt:
    print('done')
    led_light.low()