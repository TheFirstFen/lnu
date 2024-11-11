package com.task3;

public class Wolf extends Characters {
    private Integer roundToMove = 0;
    final String wolfIcon = "🐺";

    public String getIcon() {
        return wolfIcon;
    }
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

    public void lostFight() {
        roundToMove = 5;
    }
    public void wonFight() {
        roundToMove = 3;
    }
    public Integer getRoundToMove() {
        return roundToMove;
    }
}

