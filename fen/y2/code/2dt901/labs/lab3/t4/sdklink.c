#include "hardware/gpio.h"

void link_gpio_set_dir(int pin, int dir)
{
    gpio_set_dir(pin, dir);
}

void link_gpio_put(int pin, int val)
{
    gpio_put(pin, val);
}

bool link_gpio_get(int pin)
{
    return gpio_get(pin);
}
