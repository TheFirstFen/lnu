package lab4.com.Shape;

/**
 * A class representing the cordinates
 */
public class Position {
    /**
     * The x-coordinate of the position
     */
    public int x = 0;

    /**
     * The y-coordinate of the position
     */
    public int y = 0; 

    /**
     * Constructs a Position object with default values
     */
    public Position() {
        this.x = 0;
        this.y = 0;
    }

    /**
     * Constructs a Position object with given coordinates
     * @param x x-coordinate of the position
     * @param y y-coordinate of the position
     */
    public Position(int x, int y) {
        this.x = x;
        this.y = y;
    }

    /**
     * Returns the cordinates in a string with the format "(x, y)"
     * @return A string showing the coordinates
     */
    public String toString() {
        return "(" + x + ", " + y + ")";
    }

    /**
     * Adds the coordinates of inputs to the given Position.
     * @param pos The position to be added
     * @return The modified position after adding specific positions 
     */
    public Position add(Position pos) {
        this.x += pos.x;
        this.y += pos.y;
        return pos;
    }
}
