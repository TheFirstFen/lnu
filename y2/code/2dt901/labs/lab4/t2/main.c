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
        switch(counter) {
            case 0:
                reset();
                break;
            case 1:
                reset();
                gpio_put(LED_1, 1);
                break;
            case 2:
                reset();
                gpio_put(LED_2, 1);
                break;
            case 3:
                reset();
                gpio_put(LED_1, 1);
                gpio_put(LED_2, 1);
                break;
            case 4:
                reset();
                gpio_put(LED_4, 1);
                break;
            case 5:
                reset();
                gpio_put(LED_1, 1);
                gpio_put(LED_4, 1);
                break;
            case 6:
                reset();
                gpio_put(LED_2, 1);
                gpio_put(LED_4, 1);
                break;
            case 7:
                reset();
                gpio_put(LED_1, 1);
                gpio_put(LED_2, 1);
                gpio_put(LED_4, 1);
                break;
            case 8:
                reset();
                gpio_put(LED_8, 1);
                break;
            case 9:
                reset();
                gpio_put(LED_1, 1);
                gpio_put(LED_8, 1);
                break;
            case 10:
                reset();
                gpio_put(LED_2, 1);
                gpio_put(LED_8, 1);
                break;
            case 11:
                reset();
                gpio_put(LED_1, 1);
                gpio_put(LED_2, 1);
                gpio_put(LED_8, 1);
                break;
            case 12:
                reset();
                gpio_put(LED_4, 1);
                gpio_put(LED_8, 1);
                break;
            case 13:
                reset();
                gpio_put(LED_1, 1);
                gpio_put(LED_4, 1);
                gpio_put(LED_8, 1);
                break;
            case 14:
                reset();
                gpio_put(LED_2, 1);
                gpio_put(LED_4, 1);
                gpio_put(LED_8, 1);
                break;
            case 15:
                reset();
                gpio_put(LED_1, 1);
                gpio_put(LED_2, 1);
                gpio_put(LED_4, 1);
                gpio_put(LED_8, 1);
                break;
            default:
                reset();
                gpio_put(LED, 1);
                break;
        }
    }

    return 0;
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
