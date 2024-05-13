    .EQU LED_R, 0
    .EQU ON, 1
    .EQU OFF, 2
    .EQU GPIO_OUT, 1
    .EQU GPIO_IN, 0

.thumb_func
.global main

main:
    MOV R0, #LED_R
    BL gpio_init
    MOV R0, #LED_R
    MOV R1, #GPIO_OUT
    BL link_gpio_set_dir

    MOV R0, #ON
    BL gpio_init
    MOV R0, #ON
    MOV R1, #GPIO_IN
    BL link_gpio_set_dir

    MOV R0, #OFF
    BL gpio_init
    MOV R0, #OFF
    MOV R1, #GPIO_IN
    BL link_gpio_set_dir
loop:
    MOV R0, #ON
    BL link_gpio_get
    BNE on

    MOV R0, #OFF
    BL link_gpio_get
    BNE off

    B loop
on:
    MOV R0, #LED_R
    MOV R1, #1
    BL link_gpio_put

    B loop
off:
    MOV R0, #LED_R
    MOV R1, #0
    BL link_gpio_put

    B loop
