from machine import Pin
from picozero import Speaker
import utime
import time


    
def buttonPress():
    global s
    global count
    t = utime.ticks_ms()
    time1 = t - s
    if time1 >= 1000 or count == 1:
        print("button was pressed: " + str(count) + "time(s). Time since last " + str(time1) + " ms")
        count += 1
        s = utime.ticks_ms()
    else:
        print("Ignored button press: Time left for next press is " + str(1000 - time1)+ " ms")
    time.sleep(0.20)


def musicbuttonPress():
    global mario
    global pvalue
    pvalue = 1
    for i in mario:
        if i == E7 or i == F7 or i == C7 or i == G7:
            greenled.value(1)
            buzzer.play(i, 0.2)
            greenled.value(0)
            if button.value() == 1:
                buttonPress()
        elif i == G6 or i == E6 or i == A6 or i == B6:
            yellowled.value(1)
            buzzer.play(i, 0.2)
            yellowled.value(0)
            if button.value() == 1:
                buttonPress()
        elif i == AS6 or i == A7 or i == D7:
            redled.value(1)
            buzzer.play(i, 0.2)
            redled.value(0)
            if button.value() == 1:
                buttonPress()
        else:
            buzzer.play(i, 0.2)
            if button.value() == 1:
                buttonPress()
    pvalue = 0


def calctemp(inpvalue):
    A = 0.001129148
    B = 0.000234125
    C = 0.0000000876741
    x = (inpvalue * 10000) / (3.3 - inpvalue)
    Blog = B * math.log(x)
    Xlog = math.log(x)
    Cpow3 = C * math.pow(Xlog, 3)
    temp = 1 / (A + Blog + Cpow3)
    temp = temp - 273.15
    return temp




count = 1
s = 0
pvalue = 0

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

mario = [E7, E7, 0, E7, 0, C7, E7, 0, G7, 0, 0, 0, G6, 0, 0, 0, C7, 0, 0, G6, 0, 0, E6, 0, 0, A6, 0, B6, 0, AS6, A6, 0, G6, E7, 0, G7, A7, 0, F7, G7, 0, E7, 0,C7, D7, B6, 0, 0, C7, 0, 0, G6, 0, 0, E6, 0, 0, A6, 0, B6, 0, AS6, A6, 0, G6, E7, 0, G7, A7, 0, F7, G7, 0, E7, 0,C7, D7, B6, 0, 0]
    


buzzer = Speaker(5)
button = Pin(6, Pin.IN)
greenled = Pin(9, Pin.OUT)
yellowled = Pin(8, Pin.OUT)
redled = Pin(7, Pin.OUT)



while True:
    if pvalue == 0:
        if button.value() == 1:
            musicbuttonPress()





