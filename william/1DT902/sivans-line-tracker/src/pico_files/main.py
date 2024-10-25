import urequests
import network
import json
from machine import Pin, lightsleep
import utime
trigger = Pin(2, Pin.OUT)
echo = Pin(3, Pin.IN)
led = Pin("LED", Pin.OUT)
ssid = 'LNU-iot'
password = 'modermodemet'
url = 'http://server.alfredsson.xyz/upload'
data = {'pico1': 472}
datajson = json.dumps(data)
headers = {'Content-Type': 'application/json'}
distance1 = 0
distance2 = 0
distance3 = 0
distance4 = 0
distance = [distance1, distance2, distance3, distance4]


def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    if wlan.isconnected() == True:
        return True
    return False

def send_data(datajson):
    sent = urequests.patch(url, data=datajson, headers=headers)
    print(sent.text)

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
   return distance

def calculate_line(distance):
    if distance < 130:
        return 3
    elif distance < 260:
        return 2
    elif distance < 400:
        return 1
    else:
        return 4
        
while True:
    led.on()
    is_connected = wifi_connect()
    for i in range(len(distance)):
        distance[i] = int(ultra())
        utime.sleep(0.25)  
    average = 0
    over_4 = 0
    for distances in distance:
        if distances > 400:
            over_4 += 1
        average += distances
    if over_4 != 4:
        average = average / (4 - over_4)
    else:
        average = 500
    # distance = int(ultra())
    
    data['pico1'] = calculate_line(average)
    datajson = json.dumps(data)
    if is_connected:
        send_data(datajson)
    led.off()
    # lightsleep(2000)
    # utime.sleep(0.5)
    # utime.sleep(0.5)
    # FKN SKRIV MACHINE_sleep här
