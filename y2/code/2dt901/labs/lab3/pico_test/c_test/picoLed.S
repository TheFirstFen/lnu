.EQU    LED_PIN, 25
.EQU    GPIO_OUT, 1
.EQU    sleep_time, 200

.thumb_func
.global main

main:
    MOV R0, #LED_PIN
    BL gpio_init
    MOV R0, #LED_PIN
    MOV R1, #GPIO_OUT

