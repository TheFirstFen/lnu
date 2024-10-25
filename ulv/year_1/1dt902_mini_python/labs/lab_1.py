from machine import Pin
from picozero import Speaker, TemperatureSensor
from math import log, pow
import time
import dht

def temp_conversion(voltage):
    A = 0.001129148
    B = 0.000234125
    C = 0.0000000876741
    R = (voltage * 10000) / (3.3 - voltage)
    B_log = B * log(R)
    R_log = log(R)
    C_pow = C * (R_log**3)
    return (1/(A + B_log + C_pow)) - 273.15

count = 0
s = 0

button = Pin(2, Pin.IN)
print(button.value())

E7 = 2637
F7 = 2794
C7 = 2093
G7 = 3136
G6 = 1568
E6 = 1319
A6 = 1760
B6 = 1976
AS6 = 1865
A7 = 3520
D7 = 2349

buzzer = Speaker(16)
mario = [E7, E7, 0, E7, 0, C7, E7, 0, G7, 0, 0, 0, G6, 0, 0, 0, C7, 0, 0, G6, 0, 0, E6, 0, 0, A6, 0, B6, 0, AS6, A6, 0, G6, E7, 0, G7, A7, 0, F7, G7, 0, E7, 0,C7, D7, B6, 0, 0, C7, 0, 0, G6, 0, 0, E6, 0, 0, A6, 0, B6, 0, AS6, A6, 0, G6, E7, 0, G7, A7, 0, F7, G7, 0, E7, 0,C7, D7, B6, 0, 0]


analog_temp = TemperatureSensor(28, conversion=temp_conversion)

digital_temp = dht.DHT11(Pin(4))
digital_temp.measure()
dig_temp = digital_temp.temperature()
dig_hum = digital_temp.humidity()

def button_press():
    global s
    global count
    t = time.ticks_ms()
    time1 = t-s
    time_left = 1000-time1
    if time1 >= 1000:
        count += 1
        print("Button was pressed: ", count)
        s = time.ticks_ms()
    else:
        print(f"Ignored button press: Time left for next press is {time_left} ms")
 
            
            
def mario_play():
    for i in mario:
        if i < 2000:
            p8 = Pin(8, Pin.OUT)
            p8.value(1)
            buzzer.play(i, 0.15)
            p8.value(0)
            if button.value() == 1:
                button_press()
        elif i > 3000:
            p9 = Pin(9, Pin.OUT)
            p9.value(1)
            buzzer.play(i, 0.15)
            p9.value(0)
            if button.value() == 1:
                button_press()
        else:
            p10 = Pin(10, Pin.OUT)
            p10.value(1)
            buzzer.play(i, 0.15)
            p10.value(0)
            if button.value() == 1:
                button_press()

while True:
    print(f"temp: {round(analog_temp.temp)}")
    print(f"temp: {dig_temp}, humidity: {dig_hum}%")
    if button.value() == 1 and count == 0:
        count += 1
        print(count)
        print(f"temp: {round(analog_temp.temp)}")
        print(f"temp: {dig_temp}, humidity: {dig_hum}%")
        mario_play()
    
        
