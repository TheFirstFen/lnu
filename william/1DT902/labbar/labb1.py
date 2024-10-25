# kom ihåg att byta namn på script till antingen main ( boot om fel)

from machine import Pin
from time import sleep


def turn_on_off(lamp_on, lamp_off=None):
    if lamp_off != None:
        lamp_off.low()

    lamp_on.high()
    sleep(1)


RED = 16     # anode(+) long leg
YELLOW = 17  # anode(+) long leg
GREEN = 18   # anode(+) long leg

red_light = Pin(RED, Pin.OUT).low()
yellow_light = Pin(YELLOW, Pin.OUT).low()
green_light = Pin(GREEN, Pin.OUT).low()


try:
    while True:
        turn_on_off(red_light)
        turn_on_off(green_light, red_light)
        turn_on_off(yellow_light, green_light)

except KeyboardInterrupt:
    print('done')
    red_light.low()
    green_light.low()
    yellow_light.low()
