all: clean
	@nasm -f elf32 -o sumnum.o sumnum.asm
	@ld -m elf_i386 -o sumnum sumnum.o
	@./sumnum
clean:
	@rm -f sumnum
	@rm -f sumnum.o
