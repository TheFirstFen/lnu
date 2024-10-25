package lab4;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import lab4.com.Shape.*;

public class PointTest {
    Point point = new Point(1, 1);

    @Test
    public void testisMoveable() {
        assertTrue(point.isMoveable());
    }
}
