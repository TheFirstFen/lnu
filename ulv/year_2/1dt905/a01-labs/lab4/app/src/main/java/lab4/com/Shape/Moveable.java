package lab4.com.Shape;

/**
 * Interface representing moveable objects.
 * Implementing classes need to suply the methods for movement and checking if its moveable
 */
public interface Moveable {
    /**
     * Checks if the object is moveable.
     * @return true if the object is moveable, false otherwise.
     */
    public boolean isMoveable();

    /**
     * Moves the object to a absolute position
     * @param pos the new absolute position of the object
     */
    public void moveAbsolute(Position pos);

   /**
     * Moves the object by a relative position.
     * @param pos Relative position to move object by
     */
    public void moveRelative(Position pos);

}
