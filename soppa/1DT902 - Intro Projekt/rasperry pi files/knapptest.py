from machine import Pin

button = Pin(6, Pin.IN)
lamp = Pin(7, Pin.OUT)

lamp.value(0)

while True:
    if button.value() == 1:
        lamp.value(1)
    else:
        lamp.value(0)

