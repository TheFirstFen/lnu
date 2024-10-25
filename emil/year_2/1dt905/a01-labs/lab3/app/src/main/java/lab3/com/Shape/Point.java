package lab3.com.Shape;

/**
 * A class representing a point that extends OneDimension
 */
public class Point extends OneDimension {
     /**
     * Constructs a point object with initial position
     * @param x The x-coordinate of the Points position.
     * @param y The y-coordinate of the Points position.
     */
    public Point(int x, int y) {
        name = "Point";
        this.pos = new Position(x, y);
        this.isMoveable = true;
    }

    /**
     * Moves a point to a absolute position
     * @param pos New absolute position 
     */
    @Override
    public void moveAbsolute(Position pos) {
        // Intentionally left empty
    }

    /**
     * Checks if point is moveable 
     * @return true as point is moveable
     */
    @Override
    public boolean isMoveable() {
        return isMoveable;
    }
}
