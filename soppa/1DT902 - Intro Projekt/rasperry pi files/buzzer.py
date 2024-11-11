from machine import Pin
import time
from picozero import Speaker


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

def buttonpress(argument):
    global mario
    for i in mario:
        if i == E7 or i == F7 or i == C7 or i == G7:
            greenled.value(1)
            buzzer.play(i, 0.2)
            greenled.value(0)
        elif i == G6 or i == E6 or i == A6 or i == B6:
            yellowled.value(1)
            buzzer.play(i, 0.2)
            yellowled.value(0)
        elif i == AS6 or i == A7 or i == D7:
            redled.value(1)
            buzzer.play(i, 0.2)
            redled.value(0)
        else:
            buzzer.play(i, 0.2)
    
while True:
    button.irq(handler=buttonpress, trigger=Pin.IRQ_FALLING)
    
    
