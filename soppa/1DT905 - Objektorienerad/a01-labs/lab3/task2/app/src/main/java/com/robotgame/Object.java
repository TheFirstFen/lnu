package com.robotgame;

import com.robotgame.interfaces.IFObject;

/**
 * The Object class represents an object in a robot game.
 * It implements the IFObject interface and provides methods to get and set the current position of the object,
 * also checks if it is time to spawn or remove the object.
 */
public class Object implements IFObject {
    private Integer currentRow = 0;
    private Integer currentColumn = 0;
    private Boolean timeToSpawn = true;
    private Boolean timeToRemove = false;

    /**
     * Returns the current row of the object.
     *
     * @return The current row of the object.
     */
    public Integer getCurrentRow() {
        return currentRow;
    }

    /**
     * Returns the current column of the object.
     *
     * @return The current column of the object.
     */
    public Integer getCurrentColumn() {
        return currentColumn;
    }

    /**
     * Returns a boolean value indicating if it is time to spawn the object.
     *
     * @return True if it is time to spawn the object, false otherwise.
     */
    public Boolean getTimeToSpawn() {
        return timeToSpawn;
    }

    /**
     * Returns a boolean value indicating if it is time to remove the object.
     *
     * @return True if it is time to remove the object, false otherwise.
     */
    public Boolean getTimeToRemove() {
        return timeToRemove;
    }

    /**
     * Sets the value of timeToSpawn field.
     *
     * @param bool The boolean value to set for timeToSpawn.
     */
    public void setTimeToSpawn(Boolean bool) {
        timeToSpawn = bool;
    }

    /**
     * Sets the value of timeToRemove field.
     *
     * @param bool The boolean value to set for timeToRemove.
     */
    public void setTimeToremove(Boolean bool) {
        timeToRemove = bool;
    }

    /**
     * Sets the new position of the object with the given row and column values.
     *
     * @param row    The new row position of the object.
     * @param column The new column position of the object.
     */
    public void SetNewPos(Integer row, Integer column) {
        currentRow = row;
        currentColumn = column;
    }
}
