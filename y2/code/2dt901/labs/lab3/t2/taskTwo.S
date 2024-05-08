    .EQU LED_R, 0
    .EQU LED_Y, 1
    .EQU LED_G, 2
    .EQU LED,   25
    .EQU GPIO_OUT, 1
    .EQU sleep_time, 200

.thumb_func
.global main

main:
    MOV R0, #LED_R
    BL gpio_init
    MOV R0, #LED_R
    MOV R1, #GPIO_OUT
    BL link_gpio_set_dir
    MOV R0, #LED_Y
    BL gpio_init
    MOV R0, #LED_Y
    MOV R1, #GPIO_OUT
    BL link_gpio_set_dir
    MOV R0, #LED_G
    BL gpio_init
    MOV R0, #LED_G
    MOV R1, #GPIO_OUT
    BL link_gpio_set_dir
loop:
    MOV R0, #LED_R
    MOV R1, #1
    BL link_gpio_put
    LDR R0, =sleep_time
    BL sleep_ms
    MOV R0, #LED_R
    MOV R1, #0
    BL link_gpio_put
    MOV R0, #LED_Y
    MOV R1, #1
    BL link_gpio_put
    LDR R0, =sleep_time
    BL sleep_ms
    MOV R0, #LED_Y
    MOV R1, #0
    BL link_gpio_put
    MOV R0, #LED_G
    MOV R1, #1
    BL link_gpio_put
    LDR R0, =sleep_time
    BL sleep_ms
    MOV R0, #LED_G
    MOV R1, #0
    BL link_gpio_put
    B loop
