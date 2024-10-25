@ Assembler program print out "Hello World"
@ using the Pico SDK.
@
@ R0 - first parameter to printf
@ R1 - second parameter to printer
@ R7 - index counter

.thumb_func
.global main

main:
	MOV	R7, #0
	BL	stdio_init_all
loop:
	LDR	R0, =str
	ADD	R7, #1
	MOV	R1, R7
	BL	printf
	B	loop

.data
    .align  4
str: .asciz   "Hello World %d\n"
