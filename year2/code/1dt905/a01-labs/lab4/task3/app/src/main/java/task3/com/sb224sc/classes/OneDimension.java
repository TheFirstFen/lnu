package task3.com.sb224sc.classes;

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
}
