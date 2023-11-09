from umachine import Pin
from time import sleep_ms
from dht import DHT11
import urequests as requests
import network

NETWORK_SSID = r"#Telia-88C920"
NETWORK_PASSWORD = r"6EP+1-a+1dkJxW%4"
USERNAME = "demo"
PASSWORD = "demo"

dht11 = DHT11(Pin(0))
wlan = network.WLAN(network.STA_IF)


def connect():
    wlan.active(True)
    wlan.connect(NETWORK_SSID, NETWORK_PASSWORD)

    max_wait = 10
    while max_wait:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        print("Waiting for connection...")
        max_wait -= 1
        sleep_ms(1000)

    if wlan.status() != 3:
        raise RuntimeError("Connection Failed")
    else:
        print("Connected to WiFi")
        status = wlan.ifconfig()
        print("ip = " + status[0])


def read_dht(dht11: DHT11):
    while True:
        try:
            dht11.measure()
            return dht11.temperature(), dht11.humidity()
        except Exception as e:
            print("Failed to meassure dht11", e)
            sleep_ms(500)


# Return meassure _n_ times and return the average
def measure_average(times_to_measure):
    temps, humids = 0, 0
    for i in range(times_to_measure):
        local_temp, local_humid = read_dht(dht11)
        print(
            f"Measurement #{i+1}:",
            f"Temprature: {local_temp} °C",
            "and",
            f"Humidity: {local_humid} %",
        )
        temps += local_temp
        humids += local_humid

    temps = round(temps / times_to_measure, 1)
    humids = round(humids / times_to_measure, 1)
    print(f"AVG: Temprature: {temps} °C and Humidity: {humids} %")
    return temps, humids


while True:
    # Connect to wifi
    connect()
    temperature, humidity = measure_average(3)

    times_to_measure = 3
    req = requests.post(
        "https://termostatuller.billenius.com/sql",
        headers={
            "x-celsius": str(temperature),
            "x-humidity": str(humidity),
            "x-username": USERNAME,
            "x-password": PASSWORD,
        },
    ).content
    sleep_ms(299000)
