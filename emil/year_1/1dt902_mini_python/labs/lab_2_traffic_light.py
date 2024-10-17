from machine import Pin
from picozero import Speaker
import time

button = Pin(3, Pin.IN)
buzzer = Speaker(16)
    

while True:
    s = 0
    t = 0
    green_car = Pin(10, Pin.OUT)
    red_walk = Pin(14, Pin.OUT)
    yellow_car = Pin(9, Pin.OUT)
    red_car = Pin(8, Pin.OUT)
    green_walk = Pin(15, Pin.OUT)
    yellow_walk = Pin(17, Pin.OUT)

    green_car.value(1)
    red_walk.value(1)
    if button.value() == 1:
        yellow_walk.value(1)
        time.sleep(2)
        green_car.value(0)
        yellow_car.value(1)
        time.sleep(1)
        
        yellow_car.value(0)
        red_car.value(1)
        
        red_walk.value(0)
        yellow_walk.value(0)
        green_walk.value(1)
        
        while s <= 2:
            buzzer.play(500, 0.1)
            buzzer.play(0, 0.1)
            s += 0.2
            
        while t <= 2:
            buzzer.play(500, 0.05)
            buzzer.play(0, 0.05)
            t += 0.1
        
        green_walk.value(0)
        yellow_car.value(1)
        red_car.value(1)
        red_walk.value(1)
        time.sleep(1)
        
        yellow_car.value(0)
        red_car.value(0)
        green_car.value(1)
        time.sleep(4)
        
        
        
        
        