package com.task3;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class MovementTest {
    Wolf wolf = new Wolf();
    Robot robot = new Robot();
    
    @Test
    public void WLeftMovementTest() {
        robot.SetNewPos(1, 1);
        wolf.SetNewPos(9, 9);
        wolf.wolfMovement(robot, wolf);
        assertEquals(8, wolf.getCurrentColumn());
    }
    @Test
    public void WRightMovementTest() {
        robot.SetNewPos(1, 9);
        wolf.SetNewPos(1, 1);
        wolf.wolfMovement(robot, wolf);
        assertEquals(2, wolf.getCurrentColumn());
    }
    @Test
    public void WUpMovementTest() {
        robot.SetNewPos(1, 1);
        wolf.SetNewPos(9, 1);
        wolf.wolfMovement(robot, wolf);
        assertEquals(8, wolf.getCurrentRow());
    }
    @Test
    public void WDownMovementTest() {
        robot.SetNewPos(9, 1);
        wolf.SetNewPos(1, 1);
        wolf.wolfMovement(robot, wolf);
        assertEquals(2, wolf.getCurrentRow());
    }

    @Test
    public void RLeftMovementTest() {
        robot.SetNewPos(1, 2);
        Movement.moveLeft(robot, null);
        assertEquals(1, robot.getCurrentColumn());
    }
    @Test
    public void RRightMovementTest() {
        robot.SetNewPos(1, 1);
        Movement.moveRight(robot, null);
        assertEquals(2, robot.getCurrentColumn());
    }
    @Test
    public void RUpMovementTest() {
        robot.SetNewPos(2, 1);
        Movement.moveUp(robot, null);
        assertEquals(1, robot.getCurrentRow());
    }
    @Test
    public void RDownMovementTest() {
        robot.SetNewPos(1, 1);
        Movement.moveDown(robot, null);
        assertEquals(2, robot.getCurrentRow());
    }
}
