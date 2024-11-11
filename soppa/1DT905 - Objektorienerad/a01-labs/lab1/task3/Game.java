package task3;
import java.util.Random;
import java.util.Scanner;

class GuessGame {
    private static Integer number = generateNumber();
    private static Integer numGuesses;

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Welcome to the game of \"Guess my number\". Guess on a number between 1 and 100.\n");
        while (true) {
            if (GuessGame.numGuesses <= 5) {
                Integer tempGuess = askForGuess(scanner);
                if (tempGuess.equals(0000)) {
                    continue; // If cheat or restart was used skip the checkguess step
                } else {
                    checkGuess(tempGuess);
                }
            } else if (GuessGame.numGuesses == 10){
                break;
            } else {
                System.out.println("You lose! The correct number was " + GuessGame.number);
                break;
            }
        }
        scanner.close();
    }

    public static Integer generateNumber() {
        Random random = new Random();
        GuessGame.numGuesses = 0;
        return random.nextInt(100) + 1;
    }
    
    public static int askForGuess(Scanner scanner) {
        while (true) {
            System.out.print("> Your guess: ");
            String input = scanner.nextLine();
            if (input.equalsIgnoreCase("cheat")) {
                System.out.print("Ah, you like cheating? The number is " + GuessGame.number + "\n");
                return 0000; // return 0000 if cheat was used
            } else if (input.equalsIgnoreCase("restart")) {
                System.out.print("Ok, now im thinking of another number.\n");
                GuessGame.numGuesses = 0;
                GuessGame.number = generateNumber();
                return 0000; // return 0000 if restart was used
            }

            try {
                int guess = Integer.parseInt(input);
                return guess;
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a valid guess.");
            }
        }
    }

    public static void checkGuess (Integer guess) {
        if (guess.equals(GuessGame.number)) {
            System.out.println("Correct! You win!");
            GuessGame.numGuesses = 10;
        } else {
            GuessGame.numGuesses++;
            if (guess < GuessGame.number) {
                System.out.println("Too low! You have made " + GuessGame.numGuesses + " guess(es)");
            } else {
                System.out.println("Too High! You have made " + GuessGame.numGuesses + " guess(es)");
            }
        }
    }
}
