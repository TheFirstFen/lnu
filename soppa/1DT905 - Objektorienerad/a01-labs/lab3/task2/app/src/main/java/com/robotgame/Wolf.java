package com.robotgame;

/**
 * Represents a wolf character.
 * Extends the Characters class.
 */
public class Wolf extends Characters {
    private Integer roundToMove = 0;
    final String wolfIcon = "🐺";

    /**
     * Returns the icon of the wolf.
     *
     * @return The icon of the wolf.
     */
    public String getIcon() {
        return wolfIcon;
    }

    /**
     * Moves the wolf based on the position of the robot.
     * Calculates the horizontal and vertical distance between the wolf and the robot's positions
     * and moves the wolf accordingly.
     *
     * @param robot The robot character.
     * @param wolf The wolf character.
     */
    public void wolfMovement(Robot robot, Wolf wolf) {
        if (roundToMove == 0) {
            Integer robotRow = robot.getCurrentRow();
            Integer robotColumn = robot.getCurrentColumn();

            Integer horizontalDifference = robotColumn - getCurrentColumn();
            Integer verticalDifference = robotRow - getCurrentRow();

            if (Math.abs(horizontalDifference) >= Math.abs(verticalDifference)) {
                if (horizontalDifference > 0) {
                    Movement.moveRight(null, wolf);
                } else {
                    Movement.moveLeft(null, wolf);
                }
            } else {
                if (verticalDifference > 0) {
                    Movement.moveDown(null, wolf);
                } else {
                    Movement.moveUp(null, wolf);
                }
            }

        } else {
            roundToMove -= 1;
        }
    }

    /**
     * Sets the number of rounds the wolf needs to wait before moving again to 5.
     */
    public void lostFight() {
        roundToMove = 5;
    }

    /**
     * Sets the number of rounds the wolf needs to wait before moving again to 3.
     */
    public void wonFight() {
        roundToMove = 3;
    }
}

