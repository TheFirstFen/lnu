package lab4;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import lab4.com.Shape.*;


public class RectangleTest {
    private Rectangle rect;

    @BeforeEach
    public void setUp() {
        rect = new Rectangle(5, 5, 3, 3);
    }

    @Test
    public void testisMoveable() {
        assertTrue(rect.isMoveable());
    }

    @Test
    public void testMoveAbsolute() {
        // Test the moveAbsolute method
        Position newPos = new Position(3, 4);
        rect.moveAbsolute(newPos);
        assertEquals(newPos, rect.getPosition());
    }

    @Test
    public void testMoveRelative() {
        // Test the moveRelative method
        Position delta = new Position(2, 3);
        Position expectedPos = new Position(5, 6); // (1+2, 2+3)
        rect.moveRelative(delta);
        assertEquals(expectedPos.toString(), rect.getPosition().toString());
    }

}
