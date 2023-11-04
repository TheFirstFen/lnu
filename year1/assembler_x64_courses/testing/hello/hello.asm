; hello.asm
;
; Author: Samuel Berg
; Date: 01-Sep-2022

section .data                           
    msg db "Hello, world!", 0xA 
    len equ $-msg      
     
section .text               
    global _start           
_start:                 
    mov rax,1           ; System call number (sys_write)
    mov rdi,1           ; File descriptor (stdout)
    mov rsi,msg         ; String arg to buffer
    mov rdx,len         ; Length of string arg
    syscall             ; Call kernel
 
    ; Now exit

    mov rax,60          ; System call number (sys_exit)
    xor rdi,rdi         ; Clear destination index register
    syscall             ; Call kernel
end:    
