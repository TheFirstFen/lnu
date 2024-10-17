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
                
                # Check if 30 seconds have passed since the last message
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
