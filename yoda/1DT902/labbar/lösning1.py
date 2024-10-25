from network import LoRa
import socket
import time

# Initialize LoRaWAN parameters
dev_eui = '<YOUR_DEVICE_EUI>'
app_eui = '<YOUR_APPLICATION_EUI>'
app_key = '<YOUR_APPLICATION_KEY>'

# Initialize LoRa socket
lora = LoRa(mode=LoRa.LORAWAN)
lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# Wait for LoRaWAN join to complete
while not lora.has_joined():
    time.sleep(2)
    print('Not yet joined...')

print('Joined!')

# Create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)  # Set the data rate (DR) to 5

# Main loop
while True:
    # Read sensor data or prepare your payload
    sensor_data = 'Hello, Datacake!'  # Replace with your actual sensor data or payload

    # Send data to Datacake
    s.send(sensor_data)

    # Wait for some time before sending the next data
    time.sleep(10)