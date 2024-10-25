package lab4.com.Shape;

/**
 * Abstract class extending AbstractShape annd providing functions for 
 * quadrilateral shapes
 */
public abstract class Quadrilateral extends AbstractShape {
    /**
     * The width of the quadrilateral shape
     */
    protected double width = 1;

    /**
     * The height of the quadrilateral shape
     */
    protected double height = 1;

    /**
     * The name of the quadrilateral shape
     */
    protected String name;
    

    /**
     * Calculates the area of a shape
     * @return The area of the quadrilateral shape
     */
    public double area() {
        return width * height;
    }
    
     /**
     * Calculates the circumference of a shape
     * @return The circumference of the quadrilateral shape
     */
    public double circumference() {
        return width * 2 + height * 2;
    }

    /**
     * Returns the quadrilateral shape as a string with the name and position included
     * @return A string representation of the shape
     */
    public String toString() {
        return name + " " + pos + " w:" + width + " h:" + height;
    }

    /**
     * Gets the name of the quadrilateral shape
     * @return the name of the shape
     */
    public String getName() {
        return name;
    }

    /**
     * Moves a quadrilateral shape to an absolute position
     * @param pos the new absolute position of the quadrilateral shape
     */
    public void moveAbsolue(Position pos) {
        this.pos = pos;
    }

    /**
     * Moves a quadrilateral shape to an relative position 
     * @param pos The relative position to move a quadrilateral shape by
     */
    public void moveRelative(Position pos) {
        this.pos.add(pos);
    }

    /**
     * Returns the current position of the quadrilateral shape
     * @return the position of the quadrilateral shape
     */
    public Position getPosition() {
        return this.pos;
    }

}
