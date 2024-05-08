@ R0 - first parameter to printf
@ R1 - second parameter to printer
@ R7 - index counter

.thumb_func
.global main

main:
    MOV	R7, #100
    BL	stdio_init_all
loop:
    CMP R7, #0
    BEQ reset
    LDR	R0, =str
    SUB R7, #1
    MOV	R1, R7
    BL	printf
    B	loop
reset:
    MOV R7, #100

.data
    .align  4
str: .asciz   "Hello World %d\n"
