package task2.com.sb224sc.classes;

public abstract class Quadrilateral extends AbstractShape {
    protected double width = 1;
    protected double height = 1;
    protected String name;

    /**
     * Computes and returns the area of the shape.
     *
     * @return Area of the shape.
     */
    public double area() {
        return width * height;
    }

    /**
     * Computes and returns the circumference of the shape.
     *
     * @return Circumference of the shape.
     */
    public double circumference() {
        return width * 2 + height * 2;
    }

    /**
     * Returns a string representation of the quadrilateral.
     *
     * @return String representation of the quadrilateral.
     */
    public String toString() {
        return name + " " + pos + " w:" + width + " h:" + height;
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
     * Gets the width of the quadrilateral.
     *
     * @return Width of the quadrilateral.
     */
    public double getWidth() {
        return this.width;
    }

    /**
     * Gets the height of the quadrilateral.
     *
     * @return Height of the quadrilateral.
     */
    public double getHeight() {
        return this.height;
    }

    /**
     * Gets the position of the quadrilateral.
     *
     * @return Position of the quadrilateral.
     */
    @Override
    public Position getPosition() {
        return this.pos;
    }
}
