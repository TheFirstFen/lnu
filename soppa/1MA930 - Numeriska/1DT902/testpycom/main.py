from time import sleep
from machine import Pin
from dht import DHT
from network import LoRa
import socket
import time
import ubinascii
import binascii
import struct
import pycom

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

app_eui = binascii.unhexlify('0000000000000000')
app_key = binascii.unhexlify('CD414529408449343A290B09DE7DD3F5')

lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
s.setblocking(False)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not joined yet...')

print('Network joined!')


sleep(1)

print("DevEUI: " + ubinascii.hexlify(lora.mac()).decode('utf-8').upper())

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
    time.sleep(20)

