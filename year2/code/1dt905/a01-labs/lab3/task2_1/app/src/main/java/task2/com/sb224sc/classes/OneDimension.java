package task2.com.sb224sc.classes;

public abstract class OneDimension extends AbstractShape {
    protected String name;

    /**
     * Computes and returns the area of the shape.
     *
     * @return Area of the one-dimensional shape(always Double.NaN).
     */
    public double area() {
        return Double.NaN;
    }

    /**
     * Computes and returns the circumference of the shape.
     *
     * @return Circumference of the one-dimensional shape(always Double.NaN).
     */
    public double circumference() {
        return Double.NaN;
    }

    /**
     * Returns a string representation of the one-dimensional shape.
     *
     * @return String containing the name and position of the shape.
     */
    public String toString() {
        return name + " " + pos;
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
     * Gets the position of the one-dimensional shape.
     *
     * @return Position of the one-dimensional shape.
     */
    @Override
    public Position getPosition() {
        return this.pos;
    }
}
