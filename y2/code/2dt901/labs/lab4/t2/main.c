#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"

#define LED_1 1 // 000X     represents to 0 or 1 at idx X
#define LED_2 2 // 00X0
#define LED_4 3 // 0X00
#define LED_8 4 // X000
#define LED 25  // used for debbuging
#define INC 5
#define DEC 6
#define GPIO_OUT 1
#define GPIO_IN 0

volatile int counter = 0;

void display();
void reset();
void inc();
void dec();

int main() {
    stdio_init_all();

    // init
    gpio_init(LED);
    gpio_set_dir(LED, GPIO_OUT);

    gpio_init(LED_1);
    gpio_set_dir(LED_1, GPIO_OUT);

    gpio_init(LED_2);
    gpio_set_dir(LED_2, GPIO_OUT);

    gpio_init(LED_4);
    gpio_set_dir(LED_4, GPIO_OUT);

    gpio_init(LED_8);
    gpio_set_dir(LED_8, GPIO_OUT);

    gpio_init(INC);
    gpio_set_dir(INC, GPIO_IN);
    gpio_set_irq_enabled(INC, GPIO_IRQ_EDGE_RISE, true);
    irq_set_enabled(IO_IRQ_BANK0, true);
    gpio_add_raw_irq_handler(INC, &inc);

    gpio_init(DEC);
    gpio_set_dir(DEC, GPIO_IN);
    gpio_set_irq_enabled(DEC, GPIO_IRQ_EDGE_RISE, true);
    irq_set_enabled(IO_IRQ_BANK0, true);
    gpio_add_raw_irq_handler(DEC, &dec);

    // loop
    while (1) {
        display();

        tight_loop_contents();
    }
    return 0;
}

void display() {
    reset();
    gpio_put(LED_1, (counter & 0x01));
    gpio_put(LED_2, (counter & 0x02) >> 1);
    gpio_put(LED_4, (counter & 0x04) >> 2);
    gpio_put(LED_8, (counter & 0x08) >> 3);
}

void inc() {
    if (gpio_get_irq_event_mask(INC) & GPIO_IRQ_EDGE_RISE) {
        gpio_acknowledge_irq(INC, GPIO_IRQ_EDGE_RISE);
        if (counter < 15) {
            counter++;
        }
    }
}

void dec() {
    if (gpio_get_irq_event_mask(DEC) & GPIO_IRQ_EDGE_RISE) {
        gpio_acknowledge_irq(DEC, GPIO_IRQ_EDGE_RISE);
        if (counter > 0) {
            counter--;
        }
    }
}

void reset() {
    gpio_put(LED_1, 0);
    gpio_put(LED_2, 0);
    gpio_put(LED_4, 0);
    gpio_put(LED_8, 0);
    gpio_put(LED, 0);
}
