package com.robotgame.interfaces;

/**
 * The IFObject interface defines a set of methods for interacting with an object in a game.
 */
public interface IFObject {

    /**
     * Returns the current row of the object.
     *
     * @return the current row of the object
     */
    public Integer getCurrentRow();

    /**
     * Returns the current column of the object.
     *
     * @return the current column of the object
     */
    public Integer getCurrentColumn();

    /**
     * Returns a boolean value indicating whether it is time to spawn the object.
     *
     * @return true if it is time to spawn the object, false otherwise
     */
    public Boolean getTimeToSpawn();

    /**
     * Returns a boolean value indicating whether it is time to remove the object.
     *
     * @return true if it is time to remove the object, false otherwise
     */
    public Boolean getTimeToRemove();

    /**
     * Sets the boolean value indicating whether it is time to spawn the object.
     *
     * @param bool the boolean value indicating whether it is time to spawn the object
     */
    public void setTimeToSpawn(Boolean bool);

    /**
     * Sets the boolean value indicating whether it is time to remove the object.
     *
     * @param bool the boolean value indicating whether it is time to remove the object
     */
    public void setTimeToremove(Boolean bool);

    /**
     * Sets a new position for the object.
     *
     * @param row the new row position for the object
     * @param column the new column position for the object
     */
    public void SetNewPos(Integer row, Integer column);
}

