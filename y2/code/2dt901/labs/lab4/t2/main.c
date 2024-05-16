#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"

#define LED_1 1
#define LED_2 2
#define LED_3 3
#define LED_4 4
#define ON 5
#define OFF 6
#define GPIO_OUT 1
#define GPIO_IN 0

void reset();

int main() {
    // init
    gpio_init(LED_1);
    gpio_set_dir(LED_1, GPIO_OUT);

    gpio_init(LED_2);
    gpio_set_dir(LED_2, GPIO_OUT);

    gpio_init(LED_3);
    gpio_set_dir(LED_3, GPIO_OUT);

    gpio_init(LED_4);
    gpio_set_dir(LED_4, GPIO_OUT);

    gpio_init(ON);
    gpio_set_dir(ON, GPIO_IN);

    gpio_init(OFF);
    gpio_set_dir(OFF, GPIO_IN);

    int counter = 0;

    // loop
    while (1) {
        if(gpio_get(ON)) {
            counter++;
        } else if(gpio_get(OFF)) {
            counter--;
        }

        switch(counter) {
            case 0:
                reset();
                printf("%d\n", counter);
                break;
            case 1:
                reset();
                printf("%d\n", counter);
                gpio_put(LED_1, 1);
                gpio_put(LED_2, 0);
                gpio_put(LED_3, 0);
                gpio_put(LED_4, 0);
                break;
            case 2:
                reset();
                printf("%d\n", counter);
                gpio_put(LED_1, 0);
                gpio_put(LED_2, 1);
                gpio_put(LED_3, 0);
                gpio_put(LED_4, 0);
                break;
            case 3:
                reset();
                printf("%d\n", counter);
                gpio_put(LED_1, 1);
                gpio_put(LED_2, 1);
                gpio_put(LED_3, 0);
                gpio_put(LED_4, 0);
                break;
            case 4:
                reset();
                printf("%d\n", counter);
                gpio_put(LED_1, 0);
                gpio_put(LED_2, 0);
                gpio_put(LED_3, 1);
                gpio_put(LED_4, 0);
                break;
            case 5:
                reset();
                printf("%d\n", counter);
                gpio_put(LED_1, 1);
                gpio_put(LED_2, 0);
                gpio_put(LED_3, 1);
                gpio_put(LED_4, 0);
                break;
            case 6:
                reset();
                printf("%d\n", counter);
                gpio_put(LED_1, 0);
                gpio_put(LED_2, 1);
                gpio_put(LED_3, 1);
                gpio_put(LED_4, 0);
                break;
            case 7:
                reset();
                printf("%d\n", counter);
                gpio_put(LED_1, 1);
                gpio_put(LED_2, 1);
                gpio_put(LED_3, 1);
                gpio_put(LED_4, 0);
                break;
            case 8:
                reset();
                printf("%d\n", counter);
                gpio_put(LED_1, 0);
                gpio_put(LED_2, 0);
                gpio_put(LED_3, 0);
                gpio_put(LED_4, 1);
                break;
            case 9:
                reset();
                printf("%d\n", counter);
                gpio_put(LED_1, 1);
                gpio_put(LED_2, 0);
                gpio_put(LED_3, 0);
                gpio_put(LED_4, 1);
                break;
            case 10:
                reset();
                printf("%d\n", counter);
                gpio_put(LED_1, 0);
                gpio_put(LED_2, 1);
                gpio_put(LED_3, 0);
                gpio_put(LED_4, 1);
                break;
            case 11:
                reset();
                printf("%d\n", counter);
                gpio_put(LED_1, 1);
                gpio_put(LED_2, 1);
                gpio_put(LED_3, 0);
                gpio_put(LED_4, 1);
                break;
            case 12:
                reset();
                printf("%d\n", counter);
                gpio_put(LED_1, 0);
                gpio_put(LED_2, 0);
                gpio_put(LED_3, 1);
                gpio_put(LED_4, 1);
                break;
            case 13:
                reset();
                printf("%d\n", counter);
                gpio_put(LED_1, 1);
                gpio_put(LED_2, 0);
                gpio_put(LED_3, 1);
                gpio_put(LED_4, 1);
                break;
            case 14:
                reset();
                printf("%d\n", counter);
                gpio_put(LED_1, 0);
                gpio_put(LED_2, 1);
                gpio_put(LED_3, 1);
                gpio_put(LED_4, 1);
                break;
            case 15:
                reset();
                printf("%d\n", counter);
                gpio_put(LED_1, 1);
                gpio_put(LED_2, 1);
                gpio_put(LED_3, 1);
                gpio_put(LED_4, 1);
                break;
            default:
                printf("Non-displayable\n");
                printf("%d\n", counter);
                reset();
                break;
        }
    }

    return 0;
}

void reset() {
    gpio_put(LED_1, 0);
    gpio_put(LED_2, 0);
    gpio_put(LED_3, 0);
    gpio_put(LED_4, 0);
}
