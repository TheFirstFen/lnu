#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"

#define LED_R 0
#define ON 1
#define OFF 2
#define GPIO_OUT 1
#define GPIO_IN 0

int main() {
    gpio_init(LED_R);
    gpio_set_dir(LED_R, GPIO_OUT);

    gpio_init(ON);
    gpio_set_dir(ON, GPIO_IN);

    gpio_init(OFF);
    gpio_set_dir(OFF, GPIO_IN);

    while (1) {
        if (gpio_get(ON)) {
            gpio_put(LED_R, 1);
        } else if (gpio_get(OFF)) {
            gpio_put(LED_R, 0);
        }
    }

    return 0;
}
