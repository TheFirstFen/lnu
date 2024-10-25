package lab4.com.Shape;

/**
 * Abstract class extending AbstractShape and provides functions for 
 * one dimensional shapes
 */
public abstract class OneDimension extends AbstractShape {
    /**
     * The name of the one dimensional shape
     */
    protected String name;

    /**
     * Calculates the area of a shape
     * @return Double.NaN as an area of a one dimensional shape
     */
    public double area() {
        return Double.NaN;
    }

    /**
     * Calculates the circumference of a shape
     * @return Double.NaN as the circumference of a one dimensional shape
     */
    public double circumference() {
        return Double.NaN;
    }

    /**
     * Returns the one dimensional shape as a string with the name and position included
     * @return A string representation of the shape
     */
    public String toString() {
        return name + " " + pos;
    }

    /**
     * Gets the name of the one dimensional shape
     * @return the name of the shape
     */
    public String getName() {
        return name;
    }

    /**
     * Moves a one dimensional shape to an absolute position
     * @param pos the new absolute position of the one dimensional shape
     */
    public void moveAbsolue(Position pos) {
        this.pos = pos;
    }

    /**
     * Moves a one dimensional shape to an relative position 
     * @param pos The relative position to move a one dimensional shape by
     */
    public void moveRelative(Position pos) {
        this.pos.add(pos);
    }

    /**
     * Returns the current position of the one dimensional shape
     * @return the position of the one dimensional shape
     */
    @Override
    public Position getPosition() {
        return this.pos;
    }
}
