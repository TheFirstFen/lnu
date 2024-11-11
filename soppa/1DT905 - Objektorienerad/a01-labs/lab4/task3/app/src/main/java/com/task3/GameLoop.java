package com.task3;

import java.util.Random;
import java.util.Scanner;

public class GameLoop {
    private static Integer strawberryRounds = 0;
    private static Integer soupRounds = 0;

    public static void startGame(Robot robot, Wolf wolf, Home home, Strawberry strawberry, Soup soup) {
        GameField.initializeField();
        GameField.setStartPosRobot(robot);
        GameField.setStartPosWolf(wolf);
        GameField.setPosHome(home);

    }
    public static void mainLoop(Scanner scanner,Robot robot, Wolf wolf, Home home, Strawberry strawberry, Soup soup) {
        if (strawberryRounds == 0) {
            Random random = new Random();
            Integer row = random.nextInt(1, 8);
            Integer column = random.nextInt(1, 8);
            strawberry.setTimeToSpawn(true);
            GameField.setPosStrawberry(strawberry, soup, row, column);
        }
        if (soupRounds == 0) {
            Random random = new Random();
            Integer row = random.nextInt(1, 8);
            Integer column = random.nextInt(1, 8);
            soup.setTimeToSpawn(true);
            GameField.setPosSoup(soup, strawberry, row, column);
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

    public static void setStrawberryRounds() {
        strawberryRounds = -1;
    }
    public static void setSoupRounds() {
        soupRounds = -1;
    }
    // Methods for testing purposes
    public static void setRounds(Integer rounds) {
        strawberryRounds = rounds;
        soupRounds = rounds;
    }
    public static Integer getStrawberryRounds() {
        return strawberryRounds;
    }
    public static Integer getSoupRounds() {
        return soupRounds;
    }
}

