package task2.com.sb224sc.classes;

import task2.com.sb224sc.interfaces.*;

public abstract class AbstractShape implements IShape, IMoveable {
    protected Position pos = new Position();
    protected boolean moveable = false;

    /**
     * Checks if the object is movable.
     *
     * @return True if the object is movable, false if not.
     */
    public boolean isMoveable() {
        return moveable;
    }

    /**
     * Moves the object to an absolute position.
     *
     * @param pos New absolute position.
     */
    public void moveAbsolute(Position pos) {
        this.pos = pos;
    }

    /**
     * Moves the object by a relative position.
     *
     * @param pos Relative position to move by.
     */
    public void moveRelative(Position pos) {
        this.pos.add(pos);
    }

    /**
     * Gets the position of the object.
     *
     * @return Position of the object.
     */
    public Position getPosition() {
        return this.pos;
    }
}
