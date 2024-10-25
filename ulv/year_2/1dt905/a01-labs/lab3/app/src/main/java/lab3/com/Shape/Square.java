package lab3.com.Shape;

/**
 * A class with functions for a rectangle that extends quadrilateral
 */
public class Square extends Quadrilateral {
    /**
     * Constructs a shape with side lenghts, and starting coordinates
     * @param width The side lenght of the square
     * @param x The x-coordinate of the rectangles starting point
     * @param y The y-coordinate of the rectangles starting point
     */
    public Square(double width, int x, int y) {
        this.name = "Square";
        this.width = width;
        this.height = width;
        this.pos =new Position(x, y);
        this.isMoveable = false;
    }

    /**
     * Checks if the Square is moveable.
     * @return true if the Square is moveable, false otherwise.
     */
    @Override
    public boolean isMoveable() {
        return isMoveable;
    }

    /**
     * Moves the Square by a absolute position
     * @param newPos The absolute position of the Square
     */
    @Override
    public void moveAbsolute(Position newPos) {
        this.pos = newPos;
    }

    /**
     * Moves the Square by a relative position
     * @param delta The relative position to move the Square by.
     */
    @Override
    public void moveRelative(Position delta) {
        pos.add(delta);
    }
}
