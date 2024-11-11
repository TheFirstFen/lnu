package com.robotgame;

import java.util.Random;

/**
 * The GameField class represents the game field. 
 * It contains methods for initializing the game field, setting the positions of the robot, wolf, home, strawberry, and soup, removing the strawberry and soup, and updating the game field.
 */
public class GameField {
    private static Integer rows = 10;
    private static Integer columns = 10;

    private static char[][] board = new char[rows][columns];


    /**
     * Initializes the game field by setting all elements of the board to "-".
     */
    public static void initializeField() {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                board[i][j] = '-';
            }
        }
    }

    /**
     * Sets the position of the robot on the game field.
     * 
     * @param robot The robot object.
     */
    public static void setStartPosRobot(Robot robot) {
        ((Robot) robot).SetNewPos(0, 0);
    }

    /**
     * Sets the position of the wolf on the game field.
     * 
     * @param wolf The wolf object.
     */
    public static void setStartPosWolf(Wolf wolf) {
        Random random = new Random();
        ((Wolf) wolf).SetNewPos(random.nextInt(3, 9), random.nextInt(3, 9));
    }

    /**
     * Sets the position of the home on the game field.
     * 
     * @param home The home object.
     */
    public static void setPosHome(Home home) {
        ((Home) home).SetNewPos(9, 9);
    }

    /**
     * Sets the position of the strawberry on the game field, avoiding the position of the soup.
     * 
     * @param strawberry The strawberry object.
     * @param soup The soup object.
     */
    public static void setPosStrawberry(Strawberry strawberry, Soup soup) {
        Random random = new Random();
        Integer row = random.nextInt(1, 8);
        Integer column = random.nextInt(1, 8);
        if (((Soup) soup).getCurrentRow() == row && ((Soup) soup).getCurrentColumn() == column) {
            setPosStrawberry(strawberry, soup);
        } else {
            ((Strawberry) strawberry).SetNewPos(row, column);
        }
    }

    /**
     * Sets the position of the soup on the game field, avoiding the position of the strawberry.
     * 
     * @param soup The soup object.
     * @param strawberry The strawberry object.
     */
    public static void setPosSoup(Soup soup, Strawberry strawberry) {
        Random random = new Random();
        Integer row = random.nextInt(1, 8);
        Integer column = random.nextInt(1, 8);
        if (((Strawberry) strawberry).getCurrentRow() == row && ((Strawberry) strawberry).getCurrentColumn() == column) {
            setPosSoup(soup, strawberry);
        } else {
            ((Soup) soup).SetNewPos(row, column);
        }
    }

    /**
     * Removes the strawberry from the game field by setting its position to a random position between (0, 0) and (8, 8).
     * 
     * @param strawberry The strawberry object.
     */
    public static void removeStrawberry(Strawberry strawberry) {
        Random random = new Random();
        ((Strawberry) strawberry).SetNewPos(random.nextInt(0, 8), random.nextInt(0, 8));
    }

    /**
     * Removes the soup from the game field by setting its position to a random position between (0, 0) and (8, 8).
     * 
     * @param soup The soup object.
     */
    public static void removeSoup(Soup soup) {
        Random random = new Random();
        ((Soup) soup).SetNewPos(random.nextInt(0, 8), random.nextInt(0, 8));
    }

    /**
     * Updates the game field by printing the icons of the home, wolf, robot, strawberry, and soup at their respective positions on the board. If the strawberry or soup needs to be removed, it prints '-' instead. It also prints a line of asterisks at the end.
     * 
     * @param robot The robot object.
     * @param wolf The wolf object.
     * @param home The home object.
     * @param strawberry The strawberry object.
     * @param soup The soup object.
     */
    public static void updateGameField(Robot robot, Wolf wolf, Home home,  Strawberry strawberry, Soup soup) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                if (i == home.getCurrentRow() && j == home.getCurrentColumn()) {
                    System.out.print(home.getIcon());
                } else if (i == wolf.getCurrentRow() && j == wolf.getCurrentColumn()) {
                    System.out.print(wolf.getIcon());
                } else if (i == robot.getCurrentRow() && j == robot.getCurrentColumn()) {
                    System.out.print(robot.getIcon());
                } else if (i == strawberry.getCurrentRow() && j == strawberry.getCurrentColumn() && ((Strawberry) strawberry).getTimeToSpawn().equals(true)) {
                    System.out.print(strawberry.getIcon());
                } else if (i == soup.getCurrentRow() && j == soup.getCurrentColumn() && ((Soup) soup).getTimeToSpawn().equals(true)) {
                    System.out.print(soup.getIcon());
                } else if (i == strawberry.getCurrentRow() && j == strawberry.getCurrentColumn() && ((Strawberry) strawberry).getTimeToRemove().equals(true)) {
                    System.out.print("- ");
                    ((Strawberry) strawberry).setTimeToremove(false);
                } else if (i == soup.getCurrentRow() && j == soup.getCurrentColumn() && ((Soup) soup).getTimeToRemove().equals(true)) {
                    System.out.print("- ");
                    ((Soup) soup).setTimeToremove(false);
                } else {
                    System.out.print(board[i][j] + " ");
                }
            }
            System.out.println();
        }
        System.out.println("********************");
    }
}

