package com.task3;

import java.util.Random;

public class Collisions {
    private static Integer rows = 10;
    private static Integer columns = 10;

    public static void checkCollisions(Robot robot, Wolf wolf, Home home,  Strawberry strawberry, Soup soup) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                if (i == robot.getCurrentRow() && j == robot.getCurrentColumn()) {
                    if (i == wolf.getCurrentRow() && j == wolf.getCurrentColumn()) {
                        Random randomBool = new Random();
                        Boolean robotWin = randomBool.nextBoolean();
                        Random randomDam = new Random();
                        Integer damage = randomDam.nextInt(1, 11);
                        fightInteraction(robot, wolf, robotWin, damage);
                    } else if (i == strawberry.getCurrentRow() && j == strawberry.getCurrentColumn()) {
                        GameLoop.setStrawberryRounds();
                        ((Robot) robot).strawberryPickup();
                        System.out.println("Energy increased by 3");
                    } else if (i == soup.getCurrentRow() && j == soup.getCurrentColumn()) {
                        GameLoop.setSoupRounds();
                        ((Robot) robot).soupPickup();
                        System.out.println("Health increased by 2");
                    } else if (i == home.getCurrentRow() && j == home.getCurrentColumn()) {
                        Main.playerHome = true;
                    }
                }
            }
    }
    }

    public static void fightInteraction(Robot robot, Wolf wolf, Boolean robotWin, Integer damage) {
        if (robotWin) {
            System.out.println("You succesfully won the fight, wolf has to rest for 5 rounds");
            ((Wolf) wolf).lostFight();
        } else {
            System.out.println("You sadly lost the fight, wolf did " + damage + " damage to you.");
            ((Robot) robot).setHealth(damage);
            if (0 >= ((Robot) robot).getHealth()) {
                System.out.println("You lost! The wolf succesfully caught and killed you.");
                Main.exitprogram = true;
            } else {
                ((Wolf) wolf).wonFight();
                System.out.println("The wolf is exhausted and now has to rest for 3 rounds, Run!");
            }
        }
    }

}
