// * v2 more OOP oriented

import java.util.Random;
import java.util.Scanner;

public class Game implements GameInterface {
    private int number;
    private int numGuesses;
    private boolean cheated;
    private boolean gameOver;

    public void init() {
        numGuesses = 0;
        Random rnd = new Random();
        number = rnd.nextInt(100);
        gameOver = false;
        cheated = false;
        System.out.println("Welcome to the game of \"Guess my number\". Guess on a number between 1 and 100.");
    }

    public void reset() {
        init();
    }

    public boolean guess(int guess) {
        if (gameOver) {
            System.out.println("The game is over. Please restart and try again.");
            return false;
        }

        numGuesses++;

        if (guess == number) {
            System.out.println("Correct!!! You win!!!");
            gameOver = true;
            return true;
        } else if (guess < number) {
            System.out.println("Too low! You have made " + numGuesses + " guess. Guess again!");
        } else {
            System.out.println("Too high! You have made " + numGuesses + " guess. Guess again!");
        }

        if (numGuesses == 6) {
            System.out.println("Out of guesses! The correct number was " + number + ". Game over.");
            gameOver = true;
        }

        return false;
    }

    public int cheat() {
        cheated = true;

        System.out.println("Ah, you like cheating? The number is " + number + ".");
        return number;
    }

    public void run() {
        init();
        Scanner sc = new Scanner(System.in);

        while (!gameOver) {
            System.out.print("> Your guess: ");
            String input = sc.nextLine();

            if (input.equalsIgnoreCase("cheat")) {
                if (!cheated) {
                    cheat();
                } else {
                    System.out.println("You already cheated! Guess again.");
                }
            } else if (input.equalsIgnoreCase("restart")) {
                reset();
                System.out.println("Ok, now I am thinking of another number.");
            } else {
                try {
                    int guess = Integer.parseInt(input);
                    guess(guess);
                } catch (NumberFormatException e) {
                    System.out.println("Invalid input. Please enter a valid number.");
                }
            }
        }

        sc.close();
    }

    public static void main(String[] args) throws Exception {
        Game game = new Game();

        game.run();
    }
}
