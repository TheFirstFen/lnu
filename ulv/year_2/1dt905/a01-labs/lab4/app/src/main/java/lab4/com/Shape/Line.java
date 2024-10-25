package lab4.com.Shape;


/**
 * A class representing a line that extends the OneDimension class
 */
public class Line extends OneDimension {
    private Position pos2 = new Position(0, 0);
    

    /**
     * Constructs a line object with initial positions
     * @param x x-coordinate of the starting/end point (-/+)
     * @param y y-coordinate of the starting/end point (-/+)
     */
    public Line(int x, int y) {
        name = "Line";
        this.pos = new Position(x, y);
        this.isMoveable = false;
    }

    /**
     * Returns the line as a string with the name and position included
     * @return A string representation of the line
     */
    public String toString() {
        return super.toString() + "-" + pos2;
    }

    /**
     * Checks if line is moveable
     * @return true if the line is moveable, false otherwise
     */
    @Override
    public boolean isMoveable() {
        return isMoveable;
    }

    /**
     * Moves the line to the absolute position
     * @param newPos The new absolute position to move the line to
     */
    @Override
    public void moveAbsolute(Position newPos) {
        this.pos = newPos;
    }

    /**
     * Moves the line from the relative position
     * @param delta The relative position to move the live by
     */
    @Override
    public void moveRelative(Position delta) {
        this.pos.add(delta);
    }
}
