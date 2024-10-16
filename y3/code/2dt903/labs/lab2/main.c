#include <stdio.h>
#include "pico/stdlib.h"
#include "FreeRTOS.h"
#include "task.h"
#include "DHT.h"

define BTN_PIN 0;
define LED_PIN 1;
define DHT_PIN 16;

DHT dht;

void temp_task(void *pvParameters) {
    for (;;) {
        dht.measure();
        float temp = dht.getTemperatureFloat();
        float hum = dht.getHumidityFloat();

        if (isnan(temp) || isnan(hum)) {
            printf("Failed to read DHT sensor values!\n");
        } else {
            printf("Temperature: %.1f °C, Humidity: %.1f%%\n", temp, hum);
        }

        vTaskDelay(pdMS_TO_TICKS(2000));
    }
}

void btn_task(void *pvParameters) {
    bool ledState = false;

    while (1) {
        if (gpio_get(BTN_PIN)) {
            ledState != ledState;
            gpio_put(LED_PIN, ledState);
            vTaskDelay(pdMS_TO_TICKS(500));
        }
        vTaskDelay(pdMS_TO_TICKS(50));
    }
}

int main() {
    stdio_init_all();
    
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);

    gpio_init(BUTTON_PIN);
    gpio_set_dir(BUTTON_PIN, GPIO_IN);
    gpio_pull_up(BUTTON_PIN);

    gpio_init(DHT_PIN);
    dht = DHT11(DHT_PIN);

    xTaskCreate(temp_task, "tempTask", configMINIMAL_STACK_SIZE, NULL, 1, NULL);
    xTaskCreate(btn_task, "btnTask", configMINIMAL_STACK_SIZE, NULL, 1, NULL);

    vTaskStartScheduler();

    while (1);
    return 0;
}
