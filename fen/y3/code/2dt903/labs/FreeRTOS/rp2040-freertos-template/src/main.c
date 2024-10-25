#include <stdio.h>
#include "pico/stdlib.h"
#include "FreeRTOS.h"
#include "task.h"
#include "hardware/adc.h"

const uint BUTTON_PIN = 26;
const uint LED_PIN = 27;
const uint LIGHT_SENSOR_PIN = 28;

const double lightOnThreshold = 2.6;
const double lightOffThreshold = 2.5;
double previuosLightAverage = 0;
double lightAverage = 0;
double avg_list[10] = {0};
int previousButtonValue = 1;

void sensor_task(void *pvParameters) {
    while (true) {
        int lightValue = adc_read();
        double lightVoltage = ((double)lightValue / 4095.0) * 3.3;

        for (int i = 9; i > 0; i--) {
            avg_list[i] = avg_list[i-1];
        }
        avg_list[0] = lightVoltage;
        double voltageSum = 0;
        for (int i = 0; i < 10; i++) {
            voltageSum += avg_list[i];
        }
        lightAverage = voltageSum / 10.0;

        if (lightAverage > lightOnThreshold && previuosLightAverage < lightOnThreshold) {
            gpio_put(LED_PIN,1);
        } else if (lightAverage < lightOffThreshold && previuosLightAverage > lightOffThreshold) {
            gpio_put(LED_PIN,0);
        }
        previuosLightAverage = lightAverage;
    }
}
uint64_t getCurrentTimeTick() {
    TickType_t ticks = xTaskGetTickCount();
    uint64_t In_ticks = (uint64_t)ticks;
    return In_ticks;
}

void Button_Task(void *pvParameters) {
    while (true) {
        uint64_t timeStart = getCurrentTimeTick();
        if (gpio_get(BUTTON_PIN) == 0 && previousButtonValue == 1) {
            gpio_put(LED_PIN,!gpio_get(LED_PIN));
            uint64_t timeEnd = getCurrentTimeTick();
            printf("Current time in ticks: %llu\n", timeEnd-timeStart);
        }
        previousButtonValue = gpio_get(BUTTON_PIN);
        vTaskDelay(pdMS_TO_TICKS(1));

    }
}

int main() {
    stdio_init_all();
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);

    gpio_init(BUTTON_PIN);
    gpio_set_dir(BUTTON_PIN, GPIO_IN);
    gpio_pull_up(BUTTON_PIN);

    adc_init();
    adc_gpio_init(LIGHT_SENSOR_PIN);
    adc_select_input(2);

    xTaskCreate(sensor_task, "LED_Task", configMINIMAL_STACK_SIZE, NULL, 1, NULL);
    xTaskCreate(Button_Task, "ButtonTask", configMINIMAL_STACK_SIZE, NULL, 10, NULL);

    vTaskStartScheduler();

    while (1) {}
    return 0;
}
