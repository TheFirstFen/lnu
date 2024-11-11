package com.robotgame;

import java.util.Scanner;

/**
 * The GameLoop class is responsible for managing the main loop of the game.
 * It initializes the game field and handles the spawning of strawberries and soup.
 */
public class GameLoop {
    private static Integer strawberryRounds = 0;
    private static Integer soupRounds = 0;

    /**
     * Initializes the game field and sets the initial positions of the robot, wolf, and home.
     * 
     * @param robot      The robot object.
     * @param wolf       The wolf object.
     * @param home       The home object.
     * @param strawberry The strawberry object.
     * @param soup       The soup object.
     */
    public static void startGame(Robot robot, Wolf wolf, Home home, Strawberry strawberry, Soup soup) {
        GameField.initializeField();
        GameField.setStartPosRobot(robot);
        GameField.setStartPosWolf(wolf);
        GameField.setPosHome(home);
    }

    /**
     * Handles the main loop of the game. Spawns strawberries and soup, updates the game field,
     * handles user input, moves the wolf, and checks for collisions.
     * 
     * @param scanner    The scanner object for user input.
     * @param robot      The robot object.
     * @param wolf       The wolf object.
     * @param home       The home object.
     * @param strawberry The strawberry object.
     * @param soup       The soup object.
     */
    public static void mainLoop(Scanner scanner, Robot robot, Wolf wolf, Home home, Strawberry strawberry, Soup soup) {
        if (strawberryRounds == 0) {
            strawberry.setTimeToSpawn(true);
            GameField.setPosStrawberry(strawberry, soup);
        }
        if (soupRounds == 0) {
            soup.setTimeToSpawn(true);
            GameField.setPosSoup(soup, strawberry);
        }
        if (strawberryRounds == 4) {
            strawberryRounds = -1;
        }
        if (soupRounds == 4) {
            soupRounds = -1;
        }
        System.out.println("Current energy: " + ((Robot) robot).getEnergy());
        System.out.println("Current health: " + ((Robot) robot).getHealth());
        GameField.updateGameField(robot, wolf, home, strawberry, soup);
        MoveMenu.menu(scanner, robot);
        ((Wolf) wolf).wolfMovement(robot, wolf);
        Collisions.checkCollisions(robot, wolf, home, strawberry, soup);
        soupRounds += 1;
        strawberryRounds += 1;
    }

    /**
     * sets the strawberry rounds counter to -1.
     */
    public static void setStrawberryRounds() {
        strawberryRounds = -1;
    }

    /**
     * sets the soup rounds counter to -1.
     */
    public static void setSoupRounds() {
        soupRounds = -1;
    }
}
