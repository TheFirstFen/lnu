# CCS811 library is needed locally on the raspberry pico to fully function

from machine import I2C, Pin
import time
import CCS811

# how to connect ccs811 sensor
    # Power to 3.3v, Ground to gnd
    # SDA to Pin 4
    # SCL to Pin 5
    
# data from Pins
sda = Pin(4, Pin.IN)
scl = Pin(5, Pin.IN)

counter = 0 # simple counter
read_time = 1  # Change value in seconds depending on how often to publish/print data

# Read I2C protocol
i2c = I2C(0, scl=scl, sda=sda)

# Scans for the I2C adress
i2c_adress = i2c.scan()

# I2C adress can only be either 90, 91
if i2c_adress == [91]:
    css = CCS811.CCS811(i2c=i2c, addr=91)
else:
    css = CCS811.CCS811(i2c=i2c, addr=90)

while True:
    css.data_ready()  # We tell the sensor it's ready to collect data
    time.sleep(1)
    counter += 1
        
    co2 = css.eCO2  # CO2 value stored in this variable
    tvoc = css.tVOC  # tvoc value stored in this variable
    if counter % read_time == 0:  # thi
        print('CO2 level:', co2, end=" ")
        print('Tvoc level:', tvoc)
