#include <stdio.h>
#include <dht.h>
#include "pico/stdlib.h"
#include "FreeRTOS.h"
#include "task.h"

#define BUTTON_PIN 0
#define LED_PIN 1
#define DHT11_PIN 2

static const dht_model_t DHT_MODEL = DHT11;
dht_t dht;

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

void buttonTask(void *pvParameters) {
    bool button_pressed = false;

    while (1)
    {
        if (gpio_get(BUTTON_PIN) == 1) {
            gpio_put(LED_PIN, 1);
            printf("Button pressed!\n");
            button_pressed = true;
            vTaskDelay(pdMS_TO_TICKS(2000));
            gpio_put(LED_PIN, 0);
            button_pressed = false;
            vTaskDelay(pdMS_TO_TICKS(500));
        }
        vTaskDelay(pdMS_TO_TICKS(50));
    }
}

int main() {
    // Initialize stdio for USB or UART communication
    stdio_init_all();

    gpio_init(BUTTON_PIN);
    gpio_set_dir(BUTTON_PIN, GPIO_IN);
    gpio_pull_down(BUTTON_PIN);

    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);
    gpio_put(LED_PIN, 0);

    dht_init(&dht, DHT_MODEL, pio0, DHT11_PIN, true);

    xTaskCreate(buttonTask, "Button Task", 256, NULL, 1, NULL);
    xTaskCreate(temp_task, "Sensor Task", 512, NULL, 1, NULL);

    vTaskStartScheduler();

    while(1);
    return 0;
}
