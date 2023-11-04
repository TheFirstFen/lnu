package task2.com.sb224sc.classes;

public class Line extends OneDimension {
    private Position pos2 = new Position();

    public Line() {
        name = "Line";
    }

    /**
     * Returns a string representation of the lines endpoints in format
     * (x, y)-(0, 0).
     *
     * @return String representation of the line segment.
     */
    public String toString() {
        return super.toString() + "-" + pos2;
    }
}
