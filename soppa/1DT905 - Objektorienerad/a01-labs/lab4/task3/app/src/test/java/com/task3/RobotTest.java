package com.task3;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class RobotTest {
    Wolf wolf = new Wolf();
    Robot robot = new Robot();

    @Test
    public void IconTest() {
        assertEquals("🤖", robot.getIcon());
    }
    @Test
    public void healthTest() {
        assertEquals(10, robot.getHealth());
        robot.soupPickup();
        assertEquals(12, robot.getHealth());
        robot.setHealth(10);
        assertEquals(2, robot.getHealth());
    }
    @Test
    public void energyTest() {
        // Checks the get function
        assertEquals(5, robot.getEnergy());
        robot.strawberryPickup();
        assertEquals(8, robot.getEnergy());
        robot.makeStep();
        assertEquals(7, robot.getEnergy());
    }
    @Test
    public void RestTest() {
        Integer preRest = robot.getEnergy();
        robot.rest();
        assertTrue(preRest < robot.getEnergy());
    }
}
