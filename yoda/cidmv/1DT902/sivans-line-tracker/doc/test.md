# Tests

### Sensor test
Testing the ultrasonic-sensor is one of the easiest tests to perform. To test this a print-statement needs to be added to the code as following:
```py
import utime
trigger = Pin(2, Pin.OUT)
echo = Pin(3, Pin.IN)

def ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(10)
   trigger.low()
   utime.sleep_us(100)
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   print(distance)
   return distance

while True:
    ultra()
    utime.sleep(1)
```
When performing this test, first follow the steps in - [Hardware](./hardware.md).
However, for this test the powerbank is not needed, as it will need to run through your code editor's terminal to see the results.

When running the code, it is expected that one float will be printed per second. This float is given in centimeters. To test it's accuracy, simply move an object closer or further away from the sensor and check for the result. For more accurate tests, a ruler or measuring tape can be used.

### Testing the communication between the raspberry pico and server

In order to test the communication, the code from [main](../src\webserver/pico_files/main.py) will be needed. The variables ssid, password and url will also need to be changed to match your wifi credentials and wanted url. 

When done, run the code with the raspberry pico connected to either the powerbank or the computer. Check for changes in the database. If the variables change in the database, the communication works!

### Testing the full project

In order to check if the project is working alltogether, connect the raspberry pico wifi to the powerbank. Firstly, check if any lights on the pico shines. If not, charge the powerbank.

After this, go to the website, (in our case server.alfredsson.xyz) and check if the value of the website changes. Move an object closer and further away from the sensor to ensure different results. 