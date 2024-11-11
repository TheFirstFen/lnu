package com.robotgame;

import java.util.Scanner;

/**
 * The MoveMenu class provides a menu for the user to choose different actions for a robot.
 * It handles user input and performs the correct actions based on the choice.
 */
public class MoveMenu {
    
    /**
     * Displays the menu options, gets the user's choice, and calls the check_input_choice method to handle the choice.
     * 
     * @param scanner the Scanner object used to get user input
     * @param robot the Robot object representing the robot
     */
    public static void menu(Scanner scanner, Robot robot) {
        System.out.println("\n1) Move up\n" +
                           "2) Move right\n" +
                           "3) Move down\n" +
                           "4) Move left\n" +
                           "5) Rest (Gain 1 to 5 energy)\n" +
                           "q) Quit"); 
        System.out.print("Your choice: ");
        String choice = scanner.nextLine();
        if (choice.equalsIgnoreCase("q")) {
            Main.exitprogram = true;
        } else {
            check_input_choice(choice, scanner, robot);
        }
    }

    /**
     * Checks the user's choice and performs the corresponding action.
     * It handles different cases based on the choice, such as moving the robot in different directions,
     * resting the robot to gain energy, or quitting the program.
     * 
     * @param choice the user's choice
     * @param scanner the Scanner object used to get user input
     * @param robot the Robot object representing the robot
     */
    public static void check_input_choice(String choice, Scanner scanner, Robot robot) {
        boolean executeDefault = true;
        if (((Robot) robot).getEnergy() == 0) {
            if (choice.equalsIgnoreCase("5")) {
                Integer restedEnergy = ((Robot) robot).rest();
                System.out.println("The robot has now rested, gained " + restedEnergy + " energy");
            } else if (choice.equalsIgnoreCase("q")) {
                Main.exitprogram = true;
            } else {
                System.out.print("No energy left please rest: ");
                String newChoice = scanner.nextLine();
                check_input_choice(newChoice, scanner, robot);
            }
        } else {
            switch (choice) {
                case "1":
                    if (((Robot) robot).getCurrentRow() != 0) {
                        Movement.moveUp(robot, null);
                        ((Robot) robot).makeStep();
                        executeDefault = false; // Don't execute default case
                    } else {
                        executeDefault = true;
                    }
                    break;
                case "2":
                    if (((Robot) robot).getCurrentColumn() != 9) {
                        Movement.moveRight(robot, null);
                        ((Robot) robot).makeStep();
                        executeDefault = false;
                    } else {
                        executeDefault = true;
                    }
                    break;
                case "3":
                    if (((Robot) robot).getCurrentRow() != 9) {
                        Movement.moveDown(robot, null);
                        ((Robot) robot).makeStep();
                        executeDefault = false;
                    } else {
                        executeDefault = true;
                    }
                    break;
                case "4":
                    if (((Robot) robot).getCurrentColumn() != 0) {
                        Movement.moveLeft(robot, null);
                        ((Robot) robot).makeStep();
                        executeDefault = false;
                    } else {
                        executeDefault = true;
                    }
                    break;
                case "5":
                    Integer restedEnergy = ((Robot) robot).rest();
                    System.out.println("The robot has now rested, gained " + restedEnergy + " energy");
                    executeDefault = false;
                    break;
                case "q":
                    Main.exitprogram = true;
                    executeDefault = false;
                    break;
                default:
                    executeDefault = false;
                    System.out.print("Incorrect input: ");
                    String newChoice = scanner.nextLine();
                    check_input_choice(newChoice, scanner, robot);
            }
        
            if (executeDefault) {
                System.out.print("Cant go there! Try again: ");
                String newChoice = scanner.nextLine();
                check_input_choice(newChoice, scanner, robot);
            }
        }
    }
}

