package task3.com.sb224sc.classes;

public class Position {
    public int x = 0;
    public int y = 0;

    public Position() {
        this.x = 0;
        this.y = 0;
    }

    /**
     * Parameterized constructor for a position.
     *
     * @param x x-coordinate.
     * @param y y-coordinate.
     */
    public Position(int x, int y) {
        this.x = x;
        this.y = y;
    }

    /**
     * Adds another position to this position, updating the coordinates.
     *
     * @param pos Position to add.
     * @return Updated position.
     */
    public Position add(Position pos) {
        this.x += pos.x;
        this.y += pos.y;
        return pos;
    }

    /**
     * Returns a string representation of the position in the format "(x, y)".
     *
     * @return String representation of the position.
     */
    public String toString() {
        return "(" + x + ", " + y + ")";
    }

    public int getX() {
        return this.x;
    }

    public int getY() {
        return this.y;
    }
}
