from machine import Pin
from machine import PWM
from machine import ADC
import time, utime
import math
count = 0
start_time = utime.ticks_ms()
last_press = 0

def buttonEventCallback():
    global count, start_time, last_press
    delta_t = utime.ticks_ms() - start_time
    if delta_t >= 1000:
        count += 1
        print(f"Button was pressed: {count} time(s). Time since last {delta_t}ms")
        start_time = utime.ticks_ms()  # Reset the start time after processing a button press
    else:
        time_left = 1000 - delta_t
        print(f"Ignored button press: Time left for next press is {time_left}ms")
        last_press = delta_t


def control_lights(tone):
    light1_pin = 28
    light2_pin = 22
    light3_pin = 19
    
    light1 = Pin(light1_pin, Pin.OUT)
    light2 = Pin(light2_pin, Pin.OUT)
    light3 = Pin(light3_pin, Pin.OUT)
    tones_light1 = [2637, 2794, 3136, 3520, 1976]
    tones_light2 = [2093, 2349, 1319, 2794, 3136]
    tones_light3 = [1568, 1760, 1865, 1760, 1568]
    
    
    if tone in tones_light1:
         light1.on()
    else:
        light1.off()
    
    if tone in tones_light2:
         light2.on()
    else:
        light2.off()
    
    if tone in tones_light3:
         light3.on()
    else:
        light3.off()
    
def play_mario():
    # define frequency for each tone
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

    # set up pin PWM timer for output to buzzer or speaker
    p2 = PWM(Pin(26))  # Pin Y2 with timer 8 Channel 2

    mario = [E7, E7, 0, E7, 0, C7, E7, 0,
             G7, 0, 0, 0, G6, 0, 0, 0,
             C7, 0, 0, G6, 0, 0, E6, 0, 0,
             A6, 0, B6, 0, AS6, A6, 0, G6,
             E7, 0, G7, A7, 0, F7, G7, 0,
             E7, 0,C7, D7, B6, 0, 0,
             C7, 0, 0, G6, 0, 0, E6, 0, 0,
             A6, 0, B6, 0, AS6, A6, 0,
             G6, E7, 0, G7, A7, 0, F7,
             G7, 0, E7, 0,C7, D7, B6, 0, 0]

    for tone in mario:
        if  tone == 0:
            p2.duty_u16(0)
        else:
            p2.duty_u16(1000) # sets the duty cycle to 1000
            p2.freq(tone) # changes the frequenzy to the certain hz
        control_lights(tone)
        time.sleep(0.15)
    p2.duty_u16(0)

def music():
    button = Pin(15, Pin.IN, Pin.PULL_UP)

    is_playing = False
    try:
        while True:
            if button.value() == 0 and not is_playing:
                print(1)
                buttonEventCallback()
                is_playing = True
                play_mario()
            else:
                is_playing = False
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Done")


def theromter():
    # Pin for the analog temperature sensor
    adcpin = 27
    thermistor = ADC(adcpin)

    # Resistor values
    R1 = 10000  # 10k Resistor
    # Steinhart Constants for NTC thermistor
    A = 0.001129148
    B = 0.000234125
    C = 0.0000000876741
    voltage = 3.3
    while True:
        # Get Voltage value from ADC
        adc = thermistor.read_u16()
        
        # Convert ADC value to voltage
        Vout = (adc / 65535) * voltage  # Assuming operating voltage is 3.3V
        
        # Calculate Resistance
        Rt = (R1 * Vout) / (voltage - Vout)
        
        # Steinhart–Hart Equation
        TempK = 1 / (A + B * math.log(Rt / R1) + C * math.pow(math.log(Rt / R1), 3))
        # Convert from Kelvin to Celsius
        TempC = TempK - 273.15
        TempC/=1000
        print(round(TempC, 1), "°C")
        time.sleep(1)



from machine import Pin
from time import sleep
import dht 

sensor = dht.DHT11(Pin(26))
#sensor = dht.DHT11(Pin(22))
print(sensor)
while True:
  try:
    sleep(1)
    sensor.measure()
    hum = sensor.humidity()
    print(hum)
  except OSError as e:
    print('Failed to read sensor.')

