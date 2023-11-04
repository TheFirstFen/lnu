from machine import Pin
from picozero import Speaker, TemperatureSensor
from time import ticks_ms
from math import log, pow
import dht


def temp_conversion(voltage):
    A = 0.001129148
    B = 0.000234125
    C = 0.0000000876741
    R = (voltage * 10000) / (3.3 - voltage)
    B_log = B * log(R)
    R_log = log(R)
    C_pow = C * pow(R_log, 3)
    return (1 / (A + B_log + C_pow)) - 273.15


def temperature():
    print(f"Temprature: {round(analog_temp.temp)} °C")
    d.measure()
    print(f"Temprature: {d.temperature()} °C and Humidity: {d.humidity()} %")


count = 0
time_difference = 0
play = True


def buttonEventCallback(start):
    global count
    global time_difference
    global play

    stop = ticks_ms()
    elapsed_time = stop - start

    if elapsed_time - time_difference >= 1000 or count == 0:
        count += 1
        print(
            f"Button was pressed: {count} time(s). Time since last {elapsed_time - time_difference}ms")
        time_difference = elapsed_time
    else:
        print(
            f"Ignored button press: Time left for next press is {1000 - (elapsed_time - time_difference)}ms")

    mario = [E7, E7, 0, E7, 0, C7, E7, 0, G7, 0, 0, 0, G6, 0, 0, 0, C7, 0, 0, G6, 0, 0, E6, 0, 0, A6, 0, B6, 0, AS6, A6, 0, G6, E7, 0, G7, A7, 0, F7,
             G7, 0, E7, 0, C7, D7, B6, 0, 0, C7, 0, 0, G6, 0, 0, E6, 0, 0, A6, 0, B6, 0, AS6, A6, 0, G6, E7, 0, G7, A7, 0, F7, G7, 0, E7, 0, C7, D7, B6, 0, 0]

    if play:
        play = False
        mario_song(mario)


def mario_song(mario):
    global play
    global buzzer

    led_r = Pin(15, Pin.OUT)
    led_y = Pin(14, Pin.OUT)
    led_g = Pin(13, Pin.OUT)

    for note in mario:
        if button.value():
            buttonEventCallback(start)
        if note < 2000:
            led_r.on()
        elif note < 3000:
            led_y.on()
        else:
            led_g.on()
        buzzer.play(note, 0.15)

        led_r.off()
        led_y.off()
        led_g.off()
    play = True


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

buzzer = Speaker(1)

button = Pin(0, Pin.IN)

analog_temp = TemperatureSensor(28, conversion=temp_conversion)

d = dht.DHT11(Pin(27))

start = ticks_ms()

while True:
    if button.value():
        temperature()
        buttonEventCallback(start)
