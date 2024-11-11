package com.task3;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class CharactersTest {
    Characters characters = new Characters();
    
    @Test
    public void SetPosTest() {
        characters.SetNewPos(4, 9);
        Integer resRow = characters.getCurrentRow();
        Integer resCol = characters.getCurrentColumn();
        assertEquals(4, resRow);
        assertEquals(9, resCol);
    }
}
