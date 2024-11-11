package com.task3;

public class Movement {
    public static void moveUp(Robot robot, Wolf wolf) {
        if (wolf == null) {
            Integer column = robot.getCurrentColumn();
            Integer row = robot.getCurrentRow();
            robot.SetNewPos(row - 1, column);
        } else {
            Integer column = wolf.getCurrentColumn();
            Integer row = wolf.getCurrentRow();
            wolf.SetNewPos(row - 1, column);
        }
    }
    public static void moveRight(Robot robot, Wolf wolf) {
        if (wolf == null) {
            Integer column = robot.getCurrentColumn();
            Integer row = robot.getCurrentRow();
            robot.SetNewPos(row, column + 1);
        } else {
            Integer column = wolf.getCurrentColumn();
            Integer row = wolf.getCurrentRow();
            wolf.SetNewPos(row, column + 1);
        }
    }
    public static void moveDown(Robot robot, Wolf wolf) {
        if (wolf == null) {
            Integer column = robot.getCurrentColumn();
            Integer row = robot.getCurrentRow();
            robot.SetNewPos(row + 1, column);
        } else {
            Integer column = wolf.getCurrentColumn();
            Integer row = wolf.getCurrentRow();
            wolf.SetNewPos(row + 1, column);
        }
    }
    public static void moveLeft(Robot robot, Wolf wolf) {
        if (wolf == null) {
            Integer column = robot.getCurrentColumn();
            Integer row = robot.getCurrentRow();
            robot.SetNewPos(row, column - 1);
        } else {
            Integer column = wolf.getCurrentColumn();
            Integer row = wolf.getCurrentRow();
            wolf.SetNewPos(row, column - 1);
        }
    }
}
