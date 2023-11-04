all: clean
	@nasm -f elf64 -o hello.o hello.asm
	@ld -o hello hello.o
	@./hello
clean:
	@rm -f hello
	@rm -f hello.o
