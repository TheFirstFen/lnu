package lab4;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import lab4.com.Shape.Line;
import lab4.com.Shape.Position;

public class LineTest {
    private Line line;

    @BeforeEach
    public void setUp() {
        line = new Line(1, 2);
    }

    @Test
    public void testToString() {
        assertEquals("Line (1, 2)-(0, 0)", line.toString());
    }

    @Test
    public void testIsMoveable() {
        assertFalse(line.isMoveable());
    }

    @Test
    public void testMoveAbsolute() {
        Position newPos = new Position(3, 4);
        line.moveAbsolute(newPos);
        assertEquals(newPos, line.getPosition());
    }

    @Test
    public void testMoveRelative(){
        Position delta = new Position(2, 3);
        Position expectedOut = new Position(3, 5);
        
        line.moveRelative(delta);
        assertEquals(expectedOut.toString(), line.getPosition().toString());
    }
}
