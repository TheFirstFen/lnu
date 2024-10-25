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
    .EQU sleep_reset, 200

.thumb_func
.global main

main:
    BL setup

    B start
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
start:
    BL zero
loop:
    @ BL zero
    BL one
    BL two
    BL three
    BL four
    BL five
    BL six
    BL seven
    BL eight
    BL nine

    @ BL nine
    BL eight
    BL seven
    BL six
    BL five
    BL four
    BL three
    BL two
    BL one
    BL zero

    B loop
zero:
    @ Store address to loop
    PUSH {lr}

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

    BL reset

    @ Fetch address to loop
    POP {pc}

    BX lr
one:
    @ Store address to loop
    PUSH {lr}

    @ One
    MOV R0, #C
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #B
    MOV R1, #1
    BL link_gpio_put
    LDR R0, =sleep_time
    BL sleep_ms

    BL reset

    @ Fetch address to loop
    POP {pc}

    BX lr
two:
    @ Store address to loop
    PUSH {lr}

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
    MOV R0, #B
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #A
    MOV R1, #1
    BL link_gpio_put
    LDR R0, =sleep_time
    BL sleep_ms

    BL reset

    @ Fetch address to loop
    POP {pc}

    BX lr
three:
    @ Store address to loop
    PUSH {lr}

    @ Three
    MOV R0, #G
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

    BL reset

    @ Fetch address to loop
    POP {pc}

    BX lr
four:
    @ Store address to loop
    PUSH {lr}

    @ Four
    MOV R0, #G
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #F
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #C
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #B
    MOV R1, #1
    BL link_gpio_put
    LDR R0, =sleep_time
    BL sleep_ms

    BL reset

    @ Fetch address to loop
    POP {pc}

    BX lr
five:
    @ Store address to loop
    PUSH {lr}

    @ Five
    MOV R0, #G
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #F
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #D
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #C
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #A
    MOV R1, #1
    BL link_gpio_put
    LDR R0, =sleep_time
    BL sleep_ms

    BL reset

    @ Fetch address to loop
    POP {pc}

    BX lr
six:
    @ Store address to loop
    PUSH {lr}

    @ Six
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
    MOV R0, #C
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #A
    MOV R1, #1
    BL link_gpio_put
    LDR R0, =sleep_time
    BL sleep_ms

    BL reset

    @ Fetch address to loop
    POP {pc}

    BX lr
seven:
    @ Store address to loop
    PUSH {lr}

    @ Seven
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

    BL reset

    @ Fetch address to loop
    POP {pc}

    BX lr
eight:
    @ Store address to loop
    PUSH {lr}

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

    BL reset

    @ Fetch address to loop
    POP {pc}

    BX lr
nine:
    @ Store address to loop
    PUSH {lr}

    @ Nine
    MOV R0, #G
    MOV R1, #1
    BL link_gpio_put
    MOV R0, #F
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

    BL reset

    @ Fetch address to loop
    POP {pc}

    BX lr
reset:
    @ Store address to loop
    PUSH {lr}

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

    @ Fetch address to loop
    POP {pc}

    BX lr
