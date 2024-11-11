package com.robotgame.interfaces;

/**
 * This interface represents a character in a game.
 * It defines a set of methods for interacting with the character.
 */
public interface IFCharacter {

    /**
     * The health property represents the health of the character.
     * It is initialized with a default value of 10.
     */
    public Integer health = 10;

    /**
     * The isAlive property represents whether the character is alive or not.
     * It is initialized with a default value of true.
     */
    public Boolean isAlive = true;

    /**
     * The getCurrentRow() method returns the current row of the character.
     *
     * @return The current row of the character.
     */
    public Integer getCurrentRow();

    /**
     * The getCurrentColumn() method returns the current column of the character.
     *
     * @return The current column of the character.
     */
    public Integer getCurrentColumn();

    /**
     * The SetNewPos(Integer row, Integer column) method sets a new position for the character based on the given row and column values.
     *
     * @param row The new row position for the character.
     * @param column The new column position for the character.
     */
    public void SetNewPos(Integer row, Integer column);
}
