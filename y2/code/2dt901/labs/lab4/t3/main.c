#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"
#include "hardware/timer.h"
#include "pico/time.h"
#include "hardware/irq.h"

#define LED_1 1 // 000X     represents to 0 or 1 at idx X
#define LED_2 2 // 00X0
#define LED_4 3 // 0X00
#define LED_8 4 // X000
#define LED 25  // used for debbuging
#define RESET 0
#define GPIO_OUT 1
#define GPIO_IN 0

volatile int counter = 0;

void display();
void gpio_cb(uint gpio, uint32_t events);
void reset();
int64_t timer_cb(alarm_id_t id, void *unused);

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

    gpio_init(RESET);
    gpio_set_dir(RESET, GPIO_IN);
    gpio_set_irq_enabled_with_callback(RESET, GPIO_IRQ_EDGE_FALL | GPIO_IRQ_EDGE_RISE, true, &gpio_cb);

    add_alarm_in_us(1000 * 1000, timer_cb, NULL, true);

    // loop
    while (1) {
        display();

        tight_loop_contents();
    }

    return 0;
}

void display() {
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

void gpio_cb(uint gpio, uint32_t events) {
    if (gpio == RESET && events & GPIO_IRQ_EDGE_FALL) {
        counter = 0;
    }
}

void reset() {
    gpio_put(LED_1, 0);
    gpio_put(LED_2, 0);
    gpio_put(LED_4, 0);
    gpio_put(LED_8, 0);
    gpio_put(LED, 0);
}

int64_t timer_cb(alarm_id_t id, void *unused) {
    if (counter < 15) {
        counter++;
    }
    return 1000 * 1000;
}
