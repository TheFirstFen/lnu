package com.task3;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

public class ObjectTest {
    Object object = new Object();
    @Test
    public void SetPosTest() {
        object.SetNewPos(2, 5);
        Integer resRow = object.getCurrentRow();
        Integer resCol = object.getCurrentColumn();
        assertEquals(2, resRow);
        assertEquals(5, resCol);
    }

    @Test
    public void timeToSpawnTest() {
        object.setTimeToSpawn(true);
        assertTrue(object.getTimeToSpawn());
    }
    @Test
    public void timeToRemoveTest() {
        object.setTimeToremove(true);
        assertTrue(object.getTimeToRemove());
    }
}
