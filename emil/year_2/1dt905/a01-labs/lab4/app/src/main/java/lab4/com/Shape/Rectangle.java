package lab4.com.Shape;

/**
 * A class with functions for a rectangle that extends quadrilateral
 */
public class Rectangle extends Quadrilateral {
    /**
     * Constructs a rectangle object with width, height, starting coordinates 
     * @param width The width of the rectangle
     * @param height The height of the rectangle 
     * @param x The x-coordinate of the rectangles starting point
     * @param y The y-coordinate of the rectangles starting point
     */
    public Rectangle(double width, double height, int x, int y) {
        this.name = "Rectangle";
        this.width = width;
        this.height = height;
        this.pos = new Position(x, y);
        this.isMoveable = true;
    }

    /**
     * Checks if the Rectangle is moveable.
     * @return true if the Rectangle is moveable, false otherwise.
     */
    @Override
    public boolean isMoveable() {
        return isMoveable;
    }

    /**
     * Move the Rectangle to an absolute position
     * @param newPos The new absolute position of the Rectangle
     */
    @Override
    public void moveAbsolute(Position newPos) {
        this.pos = newPos;
    }

    /**
     * Move the Rectangle relative to current position
     * @param delta The relative position to move the Rectangle by
     */
    @Override
    public void moveRelative(Position delta) {
        this.pos.add(delta);
    }
}
