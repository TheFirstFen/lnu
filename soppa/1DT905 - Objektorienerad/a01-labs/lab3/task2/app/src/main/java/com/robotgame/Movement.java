package com.robotgame;

/**
 * The Movement class provides methods for moving a Robot and a Wolf in different directions.
 */
public class Movement {
    
    /**
     * Moves the given Robot or Wolf up by decreasing the row value by 1.
     * 
     * @param robot The Robot object to move up. Pass null if moving a Wolf.
     * @param wolf The Wolf object to move up. Pass null if moving a Robot.
     */
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
    
    /**
     * Moves the given Robot or Wolf right by increasing the column value by 1.
     * 
     * @param robot The Robot object to move right. Pass null if moving a Wolf.
     * @param wolf The Wolf object to move right. Pass null if moving a Robot.
     */
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
    
    /**
     * Moves the given Robot or Wolf down by increasing the row value by 1.
     * 
     * @param robot The Robot object to move down. Pass null if moving a Wolf.
     * @param wolf The Wolf object to move down. Pass null if moving a Robot.
     */
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
    
    /**
     * Moves the given Robot or Wolf left by decreasing the column value by 1.
     * 
     * @param robot The Robot object to move left. Pass null if moving a Wolf.
     * @param wolf The Wolf object to move left. Pass null if moving a Robot.
     */
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
