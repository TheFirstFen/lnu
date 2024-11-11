from machine import Pin
 
greenled = Pin(9, Pin.OUT)
yellowled = Pin(8, Pin.OUT)
redled = Pin(7, Pin.OUT)

greenled2 = Pin(19, Pin.OUT)
yellowled2 = Pin(18, Pin.OUT)
redled2 = Pin(16, Pin.OUT)


greenled.value(0)
greenled2.value(0)
yellowled.value(0)
yellowled2.value(0)
redled.value(0)
redled2.value(0)
