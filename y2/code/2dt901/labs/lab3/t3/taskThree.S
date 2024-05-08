    .EQU G, 0
    .EQU F, 1
    .EQU E, 2
    .EQU D, 3
    .EQU C, 4
    .EQU B, 5
    .EQU A, 6
    .EQU LED, 25
    .EQU GPIO_OUT, 1
    .EQU sleep_time, 1000

.thumb_func
.global main

main:
   @ Builtin LED setup
    MOV R0, #LED
    BL gpio_init
    MOV R0, #LED
    MOV R1, #GPIO_OUT
    BL link_gpio_set_dir
setup:
    @ G setup
    MOV R0, #G
    BL gpio_init
    MOV R0, #G
    MOV R1, #GPIO_OUT
    BL link_gpio_set_dir

    @ F setup
    MOV R0, #F
    BL gpio_init
    MOV R0, #F
    MOV R1, #GPIO_OUT
    BL link_gpio_set_dir

    @ E setup
    MOV R0, #E
    BL gpio_init
    MOV R0, #E
    MOV R1, #GPIO_OUT
    BL link_gpio_set_dir

    @ D setup
    MOV R0, #D
    BL gpio_init
    MOV R0, #D
    MOV R1, #GPIO_OUT
    BL link_gpio_set_dir

    @ C setup
    MOV R0, #C
    BL gpio_init
    MOV R0, #C
    MOV R1, #GPIO_OUT
    BL link_gpio_set_dir

    @ B setup
    MOV R0, #B
    BL gpio_init
    MOV R0, #B
    MOV R1, #GPIO_OUT
    BL link_gpio_set_dir

    @ A setup
    MOV R0, #A
    BL gpio_init
    MOV R0, #A
    MOV R1, #GPIO_OUT
    BL link_gpio_set_dir
loop:
    @ Zero
    MOV R0, #F
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #E
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #D
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #C
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #B
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #A
    MOV R1, #1
    BL link_gpio_put
    LDR R0, =sleep_time
    BL sleep_ms

    @ One
    MOV R0, #F
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #E
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #D
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #A
    MOV R1, #1
    BL link_gpio_put
    LDR R0, =sleep_time
    BL sleep_ms

    @ Two
    MOV R0, #G
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #E
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #D
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #C
    MOV R1, #0
    BL link_gpio_put
    MOV R0, #A
    MOV R1, #1
    BL link_gpio_put
    LDR R0, =sleep_time
    BL sleep_ms

    @ Three
    MOV R0, #E
    MOV R1, #0
    BL link_gpio_put
    MOV R0, #C
    MOV R1, #1
    BL link_gpio_put
    LDR R0, =sleep_time
    BL sleep_ms

    @ Four
    MOV R0, #F
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #D
    MOV R1, #0
    BL link_gpio_put
    MOV R0, #A
    MOV R1, #0
    BL link_gpio_put
    LDR R0, =sleep_time
    BL sleep_ms

    @ Five
    MOV R0, #D
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #B
    MOV R1, #0
    BL link_gpio_put
    MOV R0, #A
    MOV R1, #1
    BL link_gpio_put
    LDR R0, =sleep_time
    BL sleep_ms

    @ Six
    MOV R0, #E
    MOV R1, #1
    BL link_gpio_put
    LDR R0, =sleep_time
    BL sleep_ms

    @ Seven
    MOV R0, #G
    MOV R1, #0
    BL link_gpio_put
    MOV R0, #F
    MOV R1, #0
    BL link_gpio_put
    MOV R0, #E
    MOV R1, #0
    BL link_gpio_put
    MOV R0, #D
    MOV R1, #0
    BL link_gpio_put
    MOV R0, #B
    MOV R1, #1
    BL link_gpio_put
    LDR R0, =sleep_time
    BL sleep_ms

    @ Eight
    MOV R0, #G
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #F
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #E
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #D
    MOV R1, #1
    BL link_gpio_put
    LDR R0, =sleep_time
    BL sleep_ms

    @ Nine
    MOV R0, #E
    MOV R1, #0
    BL link_gpio_put
    LDR R0, =sleep_time
    BL sleep_ms

    B loop
reset:
    @ Blank
    MOV R0, #G
    MOV R1, #0
    BL link_gpio_put
    MOV R0, #F
    MOV R1, #0
    BL link_gpio_put
    MOV R0, #E
    MOV R1, #0
    BL link_gpio_put
    MOV R0, #D
    MOV R1, #0
    BL link_gpio_put
    MOV R0, #C
    MOV R1, #0
    BL link_gpio_put
    MOV R0, #B
    MOV R1, #0
    BL link_gpio_put
    MOV R0, #A
    MOV R1, #0
    BL link_gpio_put
    LDR R0, =sleep_time
    BL sleep_ms
