import java.util.Scanner;
import java.util.Random;

public class Game {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        int secret = random.nextInt(100) + 1;
        int attempts = 0;
        System.out.println("Welcome to the game of 'Guess my number'. Guess on a number between 1 and 100.");
        
        while(attempts < 6){
            System.out.print("Your guess: ");
            String input = scanner.nextLine();
            
            if (input.equalsIgnoreCase("cheat")) {
                System.out.println("Ah, you like cheating? The number is " + secret + ".");
            }
            else if (input.equalsIgnoreCase("restart")) {
                secret = random.nextInt(100) + 1;
                System.out.println("Ok, now I am thinking of another number.");
            }
            else {
                try{
                    int guess = Integer.parseInt(input);
                    attempts++;

                    if (guess < secret) {
                        System.out.println("Too low! You have made " + attempts + " guess(es). Guess again!");
                    }
                    else if (guess > secret){
                        System.out.println("Too high! You have made " + attempts + " guess(es). Guess again!");
                    }
                    else {
                        System.out.println("You win!");
                        break;
                    }
                    if (attempts == 6) {
                        System.out.println("Sorry, you've run out of attempts. The correct number was " + secret + ".");
                    }
                    
                } catch (NumberFormatException e) {
                    System.out.println("Invalid input. Please enter a valid number, 'cheat', or 'restart'.");
                }
            }
        }
        scanner.close();
    }
}
