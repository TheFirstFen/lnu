Example: of makefile
@ = does not display in terminal
all: clean = runs clean first the all
clean: = specifies what clean does

all: clean
	@
	@
	@./
clean:
	@rm -f 
	@rm -f 
