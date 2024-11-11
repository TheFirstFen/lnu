package com.robotgame;

import java.util.Scanner;


/**
 * The Main class is the main part of the program. It initializes the game, 
 * starts the game loop, and handles the main logic of the game.
 */
public class Main {
    public static Boolean exitprogram = false;
    public static Boolean playerHome = false;
    private static Integer round = 1;

    /**
     * The entry point of the program. It initializes the game, starts the game loop, and handles the main logic of the game.
     * @param args
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Game game = new Game();
        Home home = game.getHome();
        Robot robot = game.getRobot();
        Wolf wolf = game.getWolf();
        Strawberry strawberry = game.getStrawberry();
        Soup soup = game.getSoup();
        GameLoop.startGame(robot, wolf, home, strawberry, soup);
        System.out.println(game.toJson());
        while (true) {
            System.out.println("Current Round: " + round);
            GameLoop.mainLoop(scanner, robot, wolf, home, strawberry, soup);
            round += 1;
            if (exitprogram) {
                System.out.println("Exiting the program...");
                break;
            } else if (playerHome) {
                GameField.updateGameField(robot, wolf, home, strawberry, soup);
                System.out.println("You won! The robot is home");
                break;
            }
        }
        scanner.close();
    }
}
