package com.task3;

import java.util.Random;

public class GameField {
        // Create a 2D array to represent the game board
    private static char[][] board = new char[10][10];


    public static void initializeField() {

        // Initialize the game board with empty spaces
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                board[i][j] = '-';
            }
        }
    }

    public static void setStartPosRobot(Robot robot) {
        ((Robot) robot).SetNewPos(0, 0);
    }

    public static void setStartPosWolf(Wolf wolf) {
        Random random = new Random();
        ((Wolf) wolf).SetNewPos(random.nextInt(3, 9), random.nextInt(3, 9));
    }

    public static void setPosHome(Home home) {
        ((Home) home).SetNewPos(9, 9);
    }

    public static void setPosStrawberry(Strawberry strawberry, Soup soup, Integer row, Integer column) {
        if (((Soup) soup).getCurrentRow() == row && ((Soup) soup).getCurrentColumn() == column) {
            Random random = new Random();
            Integer Nrow = random.nextInt(1, 8);
            Integer Ncolumn = random.nextInt(1, 8);
            setPosStrawberry(strawberry, soup, Nrow, Ncolumn);
        } else {
            ((Strawberry) strawberry).SetNewPos(row, column);
        }
    }

    public static void setPosSoup(Soup soup, Strawberry strawberry, Integer row, Integer column) {
        if (((Strawberry) strawberry).getCurrentRow() == row && ((Strawberry) strawberry).getCurrentColumn() == column) {
            Random random = new Random();
            Integer Nrow = random.nextInt(1, 8);
            Integer Ncolumn = random.nextInt(1, 8);
            setPosSoup(soup, strawberry, Nrow, Ncolumn);
        } else {
            ((Soup) soup).SetNewPos(row, column);
        }
    }

    public static char[][] getBoard() {
        return board;
    }

    public static void removeStrawberry(Strawberry strawberry) {
        Random random = new Random();
        ((Strawberry) strawberry).SetNewPos(random.nextInt(1, 8), random.nextInt(1, 8));
    }

    public static void removeSoup(Soup soup) {
        Random random = new Random();
        ((Soup) soup).SetNewPos(random.nextInt(1, 8), random.nextInt(1, 8));
    }

    public static void updateGameField(Robot robot, Wolf wolf, Home home,  Strawberry strawberry, Soup soup) {
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
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
                    ((Strawberry) strawberry).setTimeToremove(false);
                } else if (i == soup.getCurrentRow() && j == soup.getCurrentColumn() && ((Soup) soup).getTimeToRemove().equals(true)) {
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

