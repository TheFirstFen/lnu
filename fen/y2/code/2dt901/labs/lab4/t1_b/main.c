#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"

#include "hardware/regs/addressmap.h"
#include "hardware/regs/sio.h"
#include "hardware/regs/io_bank0.h"
#include "hardware/regs/pads_bank0.h"

#define LED_R 0
#define ON 1
#define OFF 2
#define GPIO_OUT 1
#define GPIO_IN 0

#define SIO_BASE_ADR 0xd0000000

int get(int gpio);
void put(int gpio, bool val);

int main() {
    stdio_init_all();

    gpio_init(LED_R);
    gpio_set_dir(LED_R, GPIO_OUT);

    gpio_init(ON);
    gpio_set_dir(ON, GPIO_IN);

    gpio_init(OFF);
    gpio_set_dir(OFF, GPIO_IN);

    while (1) {
        if (get(ON)) {
            put(LED_R, 1);
        } else if (get(OFF)) {
            put(LED_R, 0);
        }
    }

    return 0;
}

int get(int gpio) {
    uint32_t bitmask = 1 << gpio;
    uint32_t input = *(volatile uint32_t *)(SIO_BASE_ADR + SIO_GPIO_IN_OFFSET);
    return (input & bitmask) != 0;
}

void put(int gpio, bool val) {
    if (val) {
        uint32_t bitmask = 1 << gpio;
        *(volatile uint32_t *)(SIO_BASE_ADR + SIO_GPIO_OUT_SET_OFFSET) |= bitmask;
    }else {
        uint32_t bitmask = 1 << gpio;
        *(volatile uint32_t *)(SIO_BASE_ADR + SIO_GPIO_OUT_CLR_OFFSET) |= bitmask;
    }
}
