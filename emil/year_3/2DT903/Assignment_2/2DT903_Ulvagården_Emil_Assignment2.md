# Assignment 2 2DT903

## Emil Ulvagården (eu222dq@student.lnu.se)

### Part 1

```Powershell

gclosed = R1 + R6 + 1/(1/(R2 + R3) + 1/(R4 + R5))

```

### Part 2

```Powershell

```

### Part 3

Link to the dashboard where live data is displayed on datacake

[Live data](https://app.datacake.de/pd/f7116282-61f6-4d93-b25a-7cf473940cf9)

Picture of the live data from datacake with history of the latest values from the last hour in a graph. To the right there shows the latest value that has been uploaded to the mqtt server. 

![pic of Live data from datacake](./datacake_Live_data.png)

The js below is the code for the uplink decoder.

```JS

function Decoder(topic, payload) {
    try {
        // Parse the JSON payload
        payload = JSON.parse(payload);
        
        // Extract temperature and humidity
        var Temp = payload.t;  // Temperature
        var Hum = payload.h;   // Humidity
        
        return [
            {
                device: "77870f9d-679b-4a1e-aa90-b626cc8fc7ab", // Serial Number or Device ID
                field: "TEMP",
                value: Temp
            },
            {
                device: "77870f9d-679b-4a1e-aa90-b626cc8fc7ab", // Serial Number or Device ID
                field: "HUM",
                value: Hum
            }
        ];
    } catch (error) {
        console.error("Failed to decode payload:", error);
        return [];  // Return an empty array if decoding fails
    }
}

```



```Python

import network
import time
from machine import Pin
from umqtt import MQTTClient
import ubinascii
import machine
import dht
import json  # Import JSON module for handling JSON data

# Wi-Fi credentials
ssid = 'Emils Galaxy'      # Replace with your Wi-Fi network name
password = 'gerp1112'      # Replace with your Wi-Fi password

# MQTT server credentials
URL = "broker.emqx.io"
Port = 1883
mqtt_user = ""       # MQTT username (if needed)
mqtt_password = ""  # MQTT password (if needed)
Topic = "U/test1"
Button = Pin(0, Pin.IN)  # Set up the button on GPIO 0
LED = Pin(1, Pin.OUT)  # Set up the LED on GPIO 1
DHT = dht.DHT11(Pin(2))

# Device unique ID, make sure it's decoded as string
client_id = ubinascii.hexlify(machine.unique_id()).decode()

# Declare the client variable globally
client = None

# Function to connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print(f"Connecting to Wi-Fi: {ssid}")
        wlan.connect(ssid, password)
        
        # Wait until connection
        while not wlan.isconnected():
            time.sleep(1)
            print(".", end="")
    
    print("\nConnected to Wi-Fi")
    print(wlan.ifconfig())  # Print IP details

# Function to connect to MQTT server
def connect_mqtt():
    global client  # Declare client as a global variable so it's accessible in other functions
    client = MQTTClient(client_id, URL, Port, mqtt_user, mqtt_password)
    
    try:
        client.connect()
        print("Connected to MQTT broker")
    except Exception as e:
        print(f"Failed to connect to MQTT broker: {e}")
        return None
    
    return client

# Function to publish a message to a topic
def publish_message(client, topic, message):
    try:
        client.publish(topic, message)
        print(f"Message published to {topic}: {message}")
    except Exception as e:
        print(f"Failed to publish message: {e}")

# Callback function to handle received messages
def message_callback(topic, msg):
    print(f"Received message: {msg.decode()} from topic: {topic.decode()}")
    
    # Turn on the LED if the message is "1"
    if msg.decode() == "1":
        LED.on()
        DHT_Sensor()  # Read sensor data and publish it
    else:
        LED.off()

# Function to subscribe to a topic
def subscribe_topic(client, topic):
    client.set_callback(message_callback)
    
    try:
        client.subscribe(topic)
        print(f"Subscribed to {topic}")
    except Exception as e:
        print(f"Failed to subscribe to topic: {e}")

# Debouncing function
def button_pressed():
    # Check if button is pressed and apply a short delay to debounce
    if Button.value() == 1:  # Button is active-low (pressed when 1)
        time.sleep(0.05)  # Short debounce delay of 50 ms
        if Button.value() == 1:  # Check again to confirm the button is still pressed
            return True
    return False

# Function to read DHT sensor and publish data
def DHT_Sensor():
    DHT.measure()  # Trigger the DHT11 to take a measurement
    temp = DHT.temperature()  # Read temperature
    hum = DHT.humidity()  # Read humidity
    print("Temp:", temp, "Hum:", hum)

    # Create a JSON payload
    payload = json.dumps({"t": temp, "h": hum})  # Create JSON object
    publish_message(client, Topic, payload)  # Publish the JSON payload

# Main program
def main():
    # Connect to Wi-Fi
    connect_wifi()
    
    # Connect to MQTT broker
    mqtt_client = connect_mqtt()
    
    if mqtt_client:
        # Subscribe to a topic
        subscribe_topic(mqtt_client, Topic)
        
        # Initialize the last publish time
        last_publish_time = time.time()
        
        try:
            while True:
                mqtt_client.check_msg()  # Check for incoming messages
                
                # Check if the button is pressed with debouncing
                if button_pressed():
                    publish_message(mqtt_client, Topic, "1")
                    #time.sleep(0.3)  # Additional delay to prevent rapid retriggering
                
                # Check if 10 seconds have passed since the last message
                current_time = time.time()
                if current_time - last_publish_time >= 300:  # 300-second interval or 5 minutes 
                    publish_message(mqtt_client, Topic, "1")
                    last_publish_time = current_time  # Reset the last publish time
                
                time.sleep(0.1)  # Small delay to avoid hogging the CPU
                
        except KeyboardInterrupt:
            print("Disconnecting from MQTT...")
            mqtt_client.disconnect()


# Run the program
if __name__ == "__main__":
    main()


```

Save the following code on the raspberry pi pico as umqtt.py by copying the code or downloding the file from [https://github.com/micropython/micropython-lib/blob/master/micropython/umqtt.simple/umqtt/simple.py](https://github.com/micropython/micropython-lib/blob/master/micropython/umqtt.simple/umqtt/simple.py) and rename it to umqtt.py

```Python

import socket
import struct
from binascii import hexlify


class MQTTException(Exception):
    pass


class MQTTClient:
    def __init__(
        self,
        client_id,
        server,
        port=0,
        user=None,
        password=None,
        keepalive=0,
        ssl=None,
    ):
        if port == 0:
            port = 8883 if ssl else 1883
        self.client_id = client_id
        self.sock = None
        self.server = server
        self.port = port
        self.ssl = ssl
        self.pid = 0
        self.cb = None
        self.user = user
        self.pswd = password
        self.keepalive = keepalive
        self.lw_topic = None
        self.lw_msg = None
        self.lw_qos = 0
        self.lw_retain = False

    def _send_str(self, s):
        self.sock.write(struct.pack("!H", len(s)))
        self.sock.write(s)

    def _recv_len(self):
        n = 0
        sh = 0
        while 1:
            b = self.sock.read(1)[0]
            n |= (b & 0x7F) << sh
            if not b & 0x80:
                return n
            sh += 7

    def set_callback(self, f):
        self.cb = f

    def set_last_will(self, topic, msg, retain=False, qos=0):
        assert 0 <= qos <= 2
        assert topic
        self.lw_topic = topic
        self.lw_msg = msg
        self.lw_qos = qos
        self.lw_retain = retain

    def connect(self, clean_session=True):
        self.sock = socket.socket()
        addr = socket.getaddrinfo(self.server, self.port)[0][-1]
        self.sock.connect(addr)
        if self.ssl:
            self.sock = self.ssl.wrap_socket(self.sock, server_hostname=self.server)
        premsg = bytearray(b"\x10\0\0\0\0\0")
        msg = bytearray(b"\x04MQTT\x04\x02\0\0")

        sz = 10 + 2 + len(self.client_id)
        msg[6] = clean_session << 1
        if self.user:
            sz += 2 + len(self.user) + 2 + len(self.pswd)
            msg[6] |= 0xC0
        if self.keepalive:
            assert self.keepalive < 65536
            msg[7] |= self.keepalive >> 8
            msg[8] |= self.keepalive & 0x00FF
        if self.lw_topic:
            sz += 2 + len(self.lw_topic) + 2 + len(self.lw_msg)
            msg[6] |= 0x4 | (self.lw_qos & 0x1) << 3 | (self.lw_qos & 0x2) << 3
            msg[6] |= self.lw_retain << 5

        i = 1
        while sz > 0x7F:
            premsg[i] = (sz & 0x7F) | 0x80
            sz >>= 7
            i += 1
        premsg[i] = sz

        self.sock.write(premsg, i + 2)
        self.sock.write(msg)
        # print(hex(len(msg)), hexlify(msg, ":"))
        self._send_str(self.client_id)
        if self.lw_topic:
            self._send_str(self.lw_topic)
            self._send_str(self.lw_msg)
        if self.user:
            self._send_str(self.user)
            self._send_str(self.pswd)
        resp = self.sock.read(4)
        assert resp[0] == 0x20 and resp[1] == 0x02
        if resp[3] != 0:
            raise MQTTException(resp[3])
        return resp[2] & 1

    def disconnect(self):
        self.sock.write(b"\xe0\0")
        self.sock.close()

    def ping(self):
        self.sock.write(b"\xc0\0")

    def publish(self, topic, msg, retain=False, qos=0):
        pkt = bytearray(b"\x30\0\0\0")
        pkt[0] |= qos << 1 | retain
        sz = 2 + len(topic) + len(msg)
        if qos > 0:
            sz += 2
        assert sz < 2097152
        i = 1
        while sz > 0x7F:
            pkt[i] = (sz & 0x7F) | 0x80
            sz >>= 7
            i += 1
        pkt[i] = sz
        # print(hex(len(pkt)), hexlify(pkt, ":"))
        self.sock.write(pkt, i + 1)
        self._send_str(topic)
        if qos > 0:
            self.pid += 1
            pid = self.pid
            struct.pack_into("!H", pkt, 0, pid)
            self.sock.write(pkt, 2)
        self.sock.write(msg)
        if qos == 1:
            while 1:
                op = self.wait_msg()
                if op == 0x40:
                    sz = self.sock.read(1)
                    assert sz == b"\x02"
                    rcv_pid = self.sock.read(2)
                    rcv_pid = rcv_pid[0] << 8 | rcv_pid[1]
                    if pid == rcv_pid:
                        return
        elif qos == 2:
            assert 0

    def subscribe(self, topic, qos=0):
        assert self.cb is not None, "Subscribe callback is not set"
        pkt = bytearray(b"\x82\0\0\0")
        self.pid += 1
        struct.pack_into("!BH", pkt, 1, 2 + 2 + len(topic) + 1, self.pid)
        # print(hex(len(pkt)), hexlify(pkt, ":"))
        self.sock.write(pkt)
        self._send_str(topic)
        self.sock.write(qos.to_bytes(1, "little"))
        while 1:
            op = self.wait_msg()
            if op == 0x90:
                resp = self.sock.read(4)
                # print(resp)
                assert resp[1] == pkt[2] and resp[2] == pkt[3]
                if resp[3] == 0x80:
                    raise MQTTException(resp[3])
                return

    # Wait for a single incoming MQTT message and process it.
    # Subscribed messages are delivered to a callback previously
    # set by .set_callback() method. Other (internal) MQTT
    # messages processed internally.
    def wait_msg(self):
        res = self.sock.read(1)
        self.sock.setblocking(True)
        if res is None:
            return None
        if res == b"":
            raise OSError(-1)
        if res == b"\xd0":  # PINGRESP
            sz = self.sock.read(1)[0]
            assert sz == 0
            return None
        op = res[0]
        if op & 0xF0 != 0x30:
            return op
        sz = self._recv_len()
        topic_len = self.sock.read(2)
        topic_len = (topic_len[0] << 8) | topic_len[1]
        topic = self.sock.read(topic_len)
        sz -= topic_len + 2
        if op & 6:
            pid = self.sock.read(2)
            pid = pid[0] << 8 | pid[1]
            sz -= 2
        msg = self.sock.read(sz)
        self.cb(topic, msg)
        if op & 6 == 2:
            pkt = bytearray(b"\x40\x02\0\0")
            struct.pack_into("!H", pkt, 2, pid)
            self.sock.write(pkt)
        elif op & 6 == 4:
            assert 0
        return op

    # Checks whether a pending message from server is available.
    # If not, returns immediately with None. Otherwise, does
    # the same processing as wait_msg.
    def check_msg(self):
        self.sock.setblocking(False)
        return self.wait_msg()


```