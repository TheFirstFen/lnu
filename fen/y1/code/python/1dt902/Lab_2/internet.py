from time import sleep
import network


class Internet:
    def connect():
        ssid = 'Anonymous'
        password = '3q1t6ibj'

        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(ssid, password)

        max_wait = 10
        while max_wait > 0:
            if wlan.status() < 0 or wlan.status() >= 3:
                break
            max_wait -= 1
            print('Waiting for connection...')
            sleep(1)

        if wlan.status() != 3:
            raise RuntimeError('Connection Failed')
        else:
            print('Connected to WiFi')
            status = wlan.ifconfig()
            print('ip = ' + status[0])
