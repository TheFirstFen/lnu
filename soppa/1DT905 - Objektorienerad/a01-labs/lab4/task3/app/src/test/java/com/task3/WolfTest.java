package com.task3;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class WolfTest {
    Wolf wolf = new Wolf();
    Robot robot = new Robot();
    

    @Test
    public void IconTest() {
        assertEquals("🐺", wolf.getIcon());
    }

    @Test
    public void movementTest() {

        Integer tempCol = wolf.getCurrentColumn();
        Integer tempRow = wolf.getCurrentRow();
        wolf.lostFight();
        wolf.wonFight();
        wolf.wolfMovement(robot, wolf);
        assertEquals(tempCol, wolf.getCurrentColumn());
        assertEquals(tempRow, wolf.getCurrentRow());
    }

}
