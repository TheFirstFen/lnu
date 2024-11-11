import network
import utime
import machine
from mqtt_async import config


sta_if = network.WLAN(network.STA_IF) # create station interface
ap_if = network.WLAN(network.AP_IF) #  create access-point interface


def connect():
    count = 0


 #  disconnects AP if it is up
    ap_if.active(False) #  de-activate the AP interface

    utime.sleep(1)

    if not sta_if.isconnected():
        print('connecting to hotspot...')
        sta_if.active(True)
        sta_if.ifconfig((config.WiFi_device, '255.255.255.0', config.gateway, '8.8.8.8'))
        sta_if.connect(config.hotspot, config.password)


        while (count < 5):
            count += 1

            if (sta_if.isconnected()):
                count = 0
                print (' network config:', sta_if.ifconfig())
                break

            print ('.', end = '')
            utime.sleep(1)


    if (count == 5):
        try:
            with open('errors.txt', 'a') as outfile:
                outfile.write('failed to connect' + '\n')
        except OSError:
            pass

     #  disconnect or you get errors
        disconnect()

    count = 0 #  reset count

    utime.sleep(1)


def disconnect():

 #  disconnects STA, even if it is not connected
    sta_if.disconnect()  #  This is line 59
    sta_if.active(False)

    utime.sleep(1)