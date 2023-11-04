package task3.com.sb224sc.classes;

public class Square extends Quadrilateral {
    /**
     * Constructor for creating a square.
     *
     * @param width Width of the square.
     */
    public Square(double width) {
        this.name = "Square";
        this.width = width;
        this.height = width;
        this.moveable = true;
    }
}
