all: compile
	@java MainUF
	@java Main3Sum
	@java Main8 1000 100
	@python3 plots.py

compile:
	@javac ./algorithms/*.java
	@javac -cp gson.jar WriteJSON.java
	@javac Timer.java
	@javac TitlePrint.java
	@javac MainUF.java
	@javac Main3Sum.java
	@javac Main8.java