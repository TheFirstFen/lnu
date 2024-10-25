.thumb_func
.global main

main:
    MOV	R7, #100
    BL	stdio_init_all
loop:
    LDR	R0, =str
    MOV	R1, R7
    BL	printf
    SUB R7, #1
    BGE loop
    MOV R7, #100
    B	loop

.data
    .align  4
str: .asciz   "Hello World %d\n"
