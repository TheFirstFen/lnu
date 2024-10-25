package lab4;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import lab4.com.Shape.*;


public class SquareTest {
    private Square square;

    @BeforeEach
    public void setUp() {
        square = new Square(5.0, 1, 2);
    }

    @Test
    public void testisMoveable() {
        assertFalse(square.isMoveable());
    }

    @Test
    public void testMoveAbsolute() {
        // Test the moveAbsolute method
        Position newPos = new Position(3, 4);
        square.moveAbsolute(newPos);
        assertEquals(newPos, square.getPosition());
    }

    @Test
    public void testMoveRelative() {
        // Test the moveRelative method
        Position delta = new Position(2, 3);
        Position expectedPos = new Position(3, 5); // (1+2, 2+3)
        square.moveRelative(delta);
        assertEquals(expectedPos.toString(), square.getPosition().toString());
    }

}
