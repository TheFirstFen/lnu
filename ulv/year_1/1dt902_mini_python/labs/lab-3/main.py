import time
from machine import Pin
from dht import DHT # can be found at https://github.com/JurassicPork/DHT_PyCom
import socket
from network import LoRa
import time
import ubinascii
import struct
import pycom

#connecting to the things netowrk
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
pycom.heartbeat(False)
pycom.rgbled(0x7f7f00) # yellow
time.sleep(1.5)

app_eui = ubinascii.unhexlify('0000000000000000')
app_key = ubinascii.unhexlify('50EBD5336DF9B549C1D483D2D7F9AA9B')

lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

while not lora.has_joined():
    print('Not yet joined...')
    pycom.rgbled(0x7f0000) # red
    time.sleep(3)


print("Joined network")
pycom.rgbled(0xff00)   #green


s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

s.setsockopt(socket.SOL_LORA, socket.SO_DR, 0)
s.setblocking(True)

s.bind(2)
#s.send(bytes([0x01,0x02]))
s.setblocking(False)
# get any data received...
#data = s.recv(64)
#print(data)

time.sleep(3)
pycom.heartbeat(True)
time.sleep(2)


#code to read the sensor data and send it over The things network
while True:
    pycom.heartbeat(False)
    th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0)
    result = th.read()
    temp = result.temperature
    RH = result.humidity
    print("Temp:", temp)
    print("RH:", RH)
    time.sleep(1)
    package = struct.pack('>h',int(temp)) + struct.pack('>h',int(RH))
    s.send(package)
    pycom.rgbled(0xff00)
    time.sleep(2)
    pycom.heartbeat(True)
    time.sleep(1)

    #co2, voc = ccs_read.value()
    #print('co2: ', co2)
    #print('voc: ', voc)
