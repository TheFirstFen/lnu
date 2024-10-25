; hello.asm
;
; Author: Samuel Berg
; Date: 01-Sep-2022

section .data:
    msg db "Hello, world!", 0xA
    len equ $-msg

section .text:
    global _start
_start:
    mov eax, 0x4            ; System call number (sys_write)
    mov ebx, 1              ; File descriptor (stdout)
    mov ecx, msg            ; String arg to buffer
    mov edx, len            ; Length of string arg
    int 0x80                ; Call kernel

    ; Now exit

    mov eax, 0x1            ; System call number (sys_exit)
    mov ebx, 0              ; Clear destination index register
    int 0x80                ; Call kernel
end:
