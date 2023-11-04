package task3.com.sb224sc.classes;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class PositionTest {

    @Test
    public void testDefaultConstructor() {
        Position position = new Position();
        assertEquals(0, position.x);
        assertEquals(0, position.y);
    }

    @Test
    public void testParameterizedConstructor() {
        Position position = new Position(2, 3);
        assertEquals(2, position.x);
        assertEquals(3, position.y);
    }

    @Test
    public void testAdd() {
        Position position1 = new Position(2, 3);
        Position position2 = new Position(1, 4);
        position1.add(position2);
        assertEquals(3, position1.x);
        assertEquals(7, position1.y);
    }

    @Test
    public void testToString() {
        Position position = new Position(2, 3);
        assertEquals("(2, 3)", position.toString());
    }
}
