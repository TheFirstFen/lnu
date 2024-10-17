# 2DT903 : Lab 2 : [Samuel Berg(sb224sc)](mailto:sb224sc@student.lnu.se) & [Jesper Wingren(jw223rn)](mailto:jw223rn@student.lnu.se)

## Task 1

![Ex 1 circuit](./img/e1.png)

```powershell
R24 = R2 + R4
R35 = R3 + R5

Rin = R1 + (R24 * R35)/(R24 + R35)

Rf = R6     (feedback resistance)

g_closed = -(Rf/Rin) = -(R6/(R1 + (R24 * R35)/(R24 + R35)))

=> Vout = g_closed * Vin = -(R6/(R1 + (R24 * R35)/(R24 + R35))) * Vin
```

## Task 2

![Ex 2 circuit](./img/e2.png)

```powershell

```

## Task 3

### Data preview

***Image of dashboard(python implementation)***
![Image of dashboard(python implementation)](./img/dashboard.png)

[Link to dashboard(python implementation)](https://app.datacake.co/pd/0276f2c5-9a61-4e08-87d3-b2f182c03933)

[Video of the C code running](https://youtube.com/shorts/zWvzqauL3pM?feature=share)

### Code

#### Python implementation(sending sensor data to datacake via mqtt)

```python
import network
import time
import machine
import umqtt
import ubinascii
import dht
import json 

ssid = 'wifi-name'
password = 'wifi-pass'
topic = "Samuel/RPIPico"
btn = machine.Pin(0, machine.Pin.IN)
led = machine.Pin(1, machine.Pin.OUT)
dht = dht.DHT11(machine.Pin(16))

mqtt_c = None

def conn_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print(f"Connecting to Wi-Fi: {ssid}")
        wlan.connect(ssid, password)
        
        while not wlan.isconnected():
            time.sleep(1)
            print(" .", end="")
    
    print("\nConnected to Wi-Fi")
    print(wlan.ifconfig()) 

def conn_mqtt():
    global mqtt_c
    try:
        mqtt_c = umqtt.MQTTClient(client_id=ubinascii.hexlify(machine.unique_id()).decode(), server="broker.emqx.io", port=1883, user="", password="")
        mqtt_c.connect()
        print("Connected to MQTT")
    except Exception as e:
        print(f"Failed to connect to MQTT: {e}")
        mqtt_c = None

def p_msg(mqtt_c, topic, message):
    
    if mqtt_c:
        try:
            mqtt_c.publish(topic, message)
            print(f"Message published to {topic}: {message}")
        except Exception as e:
            print(f"Failed to publish message: {e}")
    else:
        print("MQTT client not connected.")
    led.off()

def msg_cb(topic, msg):
    print(f"Received message: {msg.decode()} from topic: {topic.decode()} \n")
    if msg.decode() == "Data comming..." or msg.decode() == "Btn data comming...":
        temp()
        p_msg(mqtt_c, topic, "Data ending...")
    else:
        led.on()

def sub_topic(mqtt_c, topic):
    if mqtt_c:
        mqtt_c.set_callback(msg_cb)
        try:
            mqtt_c.subscribe(topic)
            print(f"Subscribed to {topic}")
        except Exception as e:
            print(f"Failed to subscribe to topic: {e}")
    else:
        print("MQTT client not connected.")

def btn_cb():
    if btn.value() == 1:
        time.sleep(0.05)
        if btn.value() == 1:
            return True
    return False

def temp():
    dht.measure()
    temp = dht.temperature() 
    hum = dht.humidity()

    payload = json.dumps({"temp": temp, "hum": hum})
    p_msg(mqtt_c, topic, payload)

def main():
    conn_wifi()
    conn_mqtt()
    
    if mqtt_c:
        sub_topic(mqtt_c, topic)
        
        try:
            elapsed_time = time.time()
            
            while True:
                mqtt_c.check_msg()
                
                if time.time() - elapsed_time >= 300:
                    p_msg(c, topic, "Data comming...")
                    elapsed_time = time.time()
                
                if btn_cb():
                    led.on()
                    p_msg(mqtt_c, topic, "Btn data comming...")
                    time.sleep(0.5)
                led.off()
                
        except KeyboardInterrupt:
            print("Disconnecting from MQTT...")
            if mqtt_c:
                mqtt_c.disconnect()

main()
```

##### Datacake uplink code

```javascript
function Decoder(topic, payload) {
    try {
        payload = JSON.parse(payload);
        
        var Temp = payload.temp;
        var Hum = payload.hum;
        
        return [
            {
                device: "25590695-dd0b-4f08-8f74-987e68bd6ac0",
                field: "TEMP",
                value: Temp
            },
            {
                device: "25590695-dd0b-4f08-8f74-987e68bd6ac0",
                field: "HUM",
                value: Hum
            }
        ];
    } catch (error) {
        console.error("Failed", error);
        return [];
    }
}
```

#### C implementation(no networking)

```c
#include <stdio.h>
#include <dht.h>
#include "pico/stdlib.h"
#include "FreeRTOS.h"
#include "task.h"

#define BTN_PIN 0
#define LED_PIN 1
#define DHT_PIN 16

static const dht_model_t DHT_MODEL = DHT11;
dht_t dht;

// Periodically check temp & hum, if DHT returns error improper data is returned
void temp_task(void *pvParameters) {
    for (;;) {
        dht_start_measurement(&dht);
        
        float temp;
        float hum;
        dht_result_t res = dht_finish_measurement_blocking(&dht, &hum, &temp);

        if (res == DHT_RESULT_OK) {
            printf("Temperature: %.1f °C, Humidity: %.1f%%\n", temp, hum);
        } else if (res == DHT_RESULT_TIMEOUT){
            printf("DHT sensor not responding. Please check your wiring.\n");
        } else {
            assert(result == DHT_RESULT_BAD_CHECKSUM);
            puts("Bad checksum");
        }

        vTaskDelay(pdMS_TO_TICKS(2000));
    }
}

// On button press turn LED ON/OFF dependent on previous state
void btn_task(void *pvParameters) {
    bool ledState = false;

    while (1) {
        printf("Button state: %d\n", gpio_get(BTN_PIN));
        if (gpio_get(BTN_PIN)) {
            ledState = !ledState;
            gpio_put(LED_PIN, ledState);
            vTaskDelay(pdMS_TO_TICKS(500));
        }
        vTaskDelay(pdMS_TO_TICKS(50));
    }
}

int main() {
    stdio_init_all();
    
    // Init LED
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);

    // Init button
    gpio_init(BTN_PIN);
    gpio_set_dir(BTN_PIN, GPIO_IN);
    gpio_pull_up(BTN_PIN);

    // Init DHT sensor
    dht_init(&dht, DHT_MODEL, pio0, DHT_PIN, true);

    // Create tasks
    xTaskCreate(temp_task, "tempTask", configMINIMAL_STACK_SIZE, NULL, 1, NULL);
    xTaskCreate(btn_task, "btnTask", configMINIMAL_STACK_SIZE, NULL, 1, NULL);

    vTaskStartScheduler();

    while (1); // <- Shall never be reached
    return 0;
}
```

### Report


