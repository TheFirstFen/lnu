package com.robotgame;

import com.robotgame.interfaces.IFCharacter;

/**
 * Creates a characters object and has methods to get and set the current position of the character.
 */
public class Characters implements IFCharacter {
    private Integer currentRow;
    private Integer currentColumn;
    public Boolean isAlive = true;

    /**
     * Returns the current row of the character.
     * @return The current row of the character.
     */
    public Integer getCurrentRow() {
        return currentRow;
    }

    /**
     * Returns the current column of the character.
     * @return The current column of the character.
     */
    public Integer getCurrentColumn() {
        return currentColumn;
    }

    /**
     * Sets the new position of the character to the decided row and column.
     * @param row The new row position of the character.
     * @param column The new column position of the character.
     */
    public void SetNewPos(Integer row, Integer column) {
        currentRow = row;
        currentColumn = column;
    }
}