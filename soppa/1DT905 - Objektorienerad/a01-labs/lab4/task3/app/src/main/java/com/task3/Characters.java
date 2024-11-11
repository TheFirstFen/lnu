package com.task3;

import com.task3.interfaces.IFCharacter;

public class Characters implements IFCharacter {
    private Integer currentRow;
    private Integer currentColumn;

    public Integer getCurrentRow() {
        return currentRow;
    }

    public Integer getCurrentColumn() {
        return currentColumn;
    }

    public void SetNewPos(Integer row, Integer column) {
        currentRow = row;
        currentColumn = column;
    }

    
}