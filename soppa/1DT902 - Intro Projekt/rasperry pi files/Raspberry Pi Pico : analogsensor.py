from machine import Pin
from picozero import TemperatureSensor
import math



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


inpvalue = TemperatureSensor(26, conversion=calctemp)

print(inpvalue.temp)



