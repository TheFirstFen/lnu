package com.robotgame;

import java.util.Random;

/**
 * The Collisions class checks and handles collisions between different objects.
 */
public class Collisions {
    private static Integer rows = 10;
    private static Integer columns = 10;

    /**
     * Checks for collisions between the robot and other objects.
     * If a collision is detected, it calls the correct method to handle the interaction between the robot and the collided object.
     *
     * @param robot      The robot object
     * @param wolf       The wolf object
     * @param home       The home object
     * @param strawberry The strawberry object
     * @param soup       The soup object
     */
    public static void checkCollisions(Robot robot, Wolf wolf, Home home, Strawberry strawberry, Soup soup) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                if (i == robot.getCurrentRow() && j == robot.getCurrentColumn()) {
                    if (i == wolf.getCurrentRow() && j == wolf.getCurrentColumn()) {
                        fightInteraction(robot, wolf);
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

    /**
     * Handles the interaction between the robot and the wolf when they collide.
     * It uses random numbers to determine the outcome of the fight.
     * If the robot wins, the wolf is forced to rest for 5 rounds.
     * If the robot loses, it takes damage and its health is updated.
     * If the robot's health reaches zero or below, the game is lost.
     * If the robot survives, the wolf is exhausted and has to rest for 3 rounds.
     *
     * @param robot The robot object
     * @param wolf  The wolf object
     */
    public static void fightInteraction(Robot robot, Wolf wolf) {
        Random randomDam = new Random();
        Random randomBool = new Random();
        Boolean robotWin = randomBool.nextBoolean();
        if (robotWin) {
            System.out.println("You succesfully won the fight, wolf has to rest for 5 rounds");
            ((Wolf) wolf).lostFight();
        } else {
            Integer damage = randomDam.nextInt(1, 11);
            System.out.println("You sadly lost the fight, wolf did " + damage + " damage to you.");
            ((Robot) robot).setHealth(damage);
            if (damage >= ((Robot) robot).getHealth()) {
                System.out.println("You lost! The wolf succesfully caught and killed you.");
                Main.exitprogram = true;
            } else {
                ((Wolf) wolf).wonFight();
                System.out.println("The wolf is exhausted and now has to rest for 3 rounds, Run!");
            }
        }
    }
}
