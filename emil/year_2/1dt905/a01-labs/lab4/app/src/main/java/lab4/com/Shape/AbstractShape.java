package lab4.com.Shape;

/**
 * Representing geometric shapes
 * Abstract class implementing the Shape and Moveable Interfaces.
 * Provides position traccing and movement
 */

public abstract class AbstractShape implements Shape, Moveable{

    /**
     * Position of a shape
     */
    protected Position pos = new Position();

    /**
     * Indicating on if the shape is moveable or not
     */
    protected boolean isMoveable = false;


    /**
     * Check if shape is moveable
     * @return true if the shape is moveable, false otherwise
     */
    public boolean isMoveable() {
        return isMoveable;
    }

    /**
     * Move the shape to the given values
     * @param pos The shape moves depending on (0, 0)
     */
    public void moveAbsolue(Position pos) {
        this.pos = pos;
    }

    /**
     * Move the shape by a relative position
     * @param pos Shape moves depending on current position
     */
    public void moveRelative(Position pos) {
        this.pos.add(pos);
    }

    /**
     * Gets the shapes current position 
     * @return The position of the shape
     */
    public Position getPosition() {
        return this.pos;
    }

    /**
     * Calculates the area of a shape, implemented by subclasses
     * @return The area of the shape
     */
    abstract public double area();

    /**
     * Calculates the circumference of a shape, implemented by subclasses
     * @return The circumference of the shape.
     */
    abstract public double circumference();
}
