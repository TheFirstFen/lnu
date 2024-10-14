import time
from machine import Pin, ADC
import utime

# Define pins and variables
lightOnThreshold = 3.1
lightOffThreshold = 3.0
lightSensor = ADC(Pin(28))
LED = Pin(27, Pin.OUT)
button = Pin(26, Pin.IN, Pin.PULL_UP)
previousLightAverage = 0
dataStream = []
startTime = 0

while True:
    # Toggle LED on new press
    if button.value() == 0 and previousButtonValue == 1:
        startTime = utime.ticks_us()
        LED.value(not LED.value())
        endTime = utime.ticks_us()
        print(str(endTime - startTime) + " microseconds")
        
    # Read new data
    lightValue = lightSensor.read_u16()
    lightVoltage = lightValue / 65535 * 3.3
    
    # Take average of last 10 measurements
    dataStream.append(lightVoltage)
    if len(dataStream) > 10:
        dataStream.pop(0)
    lightAverage = sum(dataStream) / len(dataStream)
        
    # Turn on if dark, Turn off if bright
    if lightAverage > lightOnThreshold and previousLightAverage < lightOnThreshold:
        LED.value(1)
    elif lightAverage < lightOffThreshold and previousLightAverage > lightOffThreshold:
        LED.value(0)
        
    previousButtonValue = button.value()
    previousLightAverage = lightAverage
    time.sleep_ms(1)