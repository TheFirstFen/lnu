package task3.com.sb224sc.classes;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;

public class QuadrilateralTest {
    private QuadrilateralMock quadrilateral;

    @BeforeEach
    public void setUp() {
        quadrilateral = new QuadrilateralMock();
    }

    @Test
    public void testGetPosition() {
        Position position = quadrilateral.getPosition();
        assertNotNull(position);
    }

    @Test
    public void testMoveRelative() {
        Position relativePosition = new Position(1, 2);

        quadrilateral.moveRelative(relativePosition);

        assertEquals(1, quadrilateral.getPosition().getX());
        assertEquals(2, quadrilateral.getPosition().getY());
    }

    @Test
    public void testGetWidth() {
        assertEquals(1, quadrilateral.getWidth());
    }

    @Test
    public void testGetHeight() {
        assertEquals(2, quadrilateral.getHeight());
    }

    private static class QuadrilateralMock extends Quadrilateral {
        QuadrilateralMock() {
            width = 1;
            height = 2;
            pos = new Position(0, 0);
        }
    }
}
