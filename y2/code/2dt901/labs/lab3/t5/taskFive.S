#include "hardware/regs/addressmap.h"
#include "hardware/regs/sio.h"
#include "hardware/regs/io_bank0.h"
#include "hardware/regs/pads_bank0.h"

    .EQU SIO_BASE_ADR, 0xd0000000
    .EQU LED, 0
    .EQU ON, 1
    .EQU OFF, 2

.thumb_func
.global main
.align 4

main:
    MOV R0, #LED
    BL gpio_init
    MOV R0, #ON
    BL gpio_init
    MOV R0, #OFF
    BL gpio_init

    B loop
loop:
    MOV R0, #ON
    BL gpio_read
    BNE on
    MOV R0, #OFF
    BL gpio_read
    BNE off

    B loop
on:
    MOV R0, #LED
    BL gpio_on

    B loop
off:
    MOV R0, #LED
    BL gpio_off

    B loop
gpio_init:
    @ Initialize the GPIO
    MOV R3, #1
    LSL R3, R0              @ shift over to pin position
    LDR R2, gpiobase        @ address we want
    STR R3, [R2, #SIO_GPIO_OE_SET_OFFSET]
    STR R3, [R2, #SIO_GPIO_OUT_CLR_OFFSET]

    @ Enable input and output for the pin
    LDR R2, padsbank0
    LSL R3, R0, #2          @ pin * 4 for register address
    ADD R2, R3              @ Actual set of registers for pin
    MOV R1, #PADS_BANK0_GPIO0_IE_BITS
    LDR R4, setoffset
    ORR R2, R4
    STR R1, [R2, #PADS_BANK0_GPIO0_OFFSET]

    @ Set the function number to SIO
    LSL R0, #3              @ each GPIO has 8 bytes of registers
    LDR R2, iobank0         @ address we want
    ADD R2, R0              @ add the offset for the pin number
    MOV R1, #IO_BANK0_GPIO3_CTRL_FUNCSEL_VALUE_SIO_3
    STR R1, [R2, #IO_BANK0_GPIO0_CTRL_OFFSET]

    BX LR
gpio_on:
    @ Turn on a GPIO pin
    MOV R3, #1
    LSL R3, R0              @ shift over to pin position
    LDR R2, gpiobase        @ address we want
    STR R3, [R2, #SIO_GPIO_OUT_SET_OFFSET]

    BX LR
gpio_off:
    @ Turn off a GPIO pin
    MOV R3, #1
    LSL R3, R0              @ shift over to pin position
    LDR R2, gpiobase        @ address we want
    STR R3, [R2, #SIO_GPIO_OUT_CLR_OFFSET]

    BX LR
gpio_read:
    MOV R3, #1
    LSL R3, R0
    LDR R2, gpiobase
    LDR R3, [R2, #SIO_GPIO_IN_OFFSET]
    MOV R4, #1
    LSL R4, R0
    AND R4, R4, R3

    BX LR

.align 4
gpiobase: .word SIO_BASE        @ base of the GPIO registers
iobank0:  .word IO_BANK0_BASE   @ base of io config registers
padsbank0: .word PADS_BANK0_BASE
setoffset: .word REG_ALIAS_SET_BITS
