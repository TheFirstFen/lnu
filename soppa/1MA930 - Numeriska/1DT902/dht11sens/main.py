import machine
from math import log


adc = machine.ADC()             # create an ADC object
apin = adc.channel(pin='P13')   # create an analog pin on P16
val = apin()
print(val)

def get_celcius(raw_adc: int) -> float:
    temp = log(((10240000 / raw_adc) - 10000))
    temp = 1 / (
        0.001129148 + (0.000234125 + (0.0000000876741 * temp * temp)) * temp
    )
    return temp - 273.15  # Convert Kelvin to Celsius

value = get_celcius(val)


print(value)           # read an analog value
