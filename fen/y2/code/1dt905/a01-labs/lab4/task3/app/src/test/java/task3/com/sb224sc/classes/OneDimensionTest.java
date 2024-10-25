package task3.com.sb224sc.classes;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

public class OneDimensionTest {
    private OneDimensionMock oneDimension;

    @BeforeEach
    public void setUp() {
        oneDimension = new OneDimensionMock();
    }

    @Test
    public void testGetPosition() {
        Position position = oneDimension.getPosition();
        assertNotNull(position);
    }

    @Test
    public void testMoveRelative() {
        Position relativePosition = new Position(1, 2);

        oneDimension.moveRelative(relativePosition);

        assertEquals(1, oneDimension.getPosition().getX());
        assertEquals(2, oneDimension.getPosition().getY());
    }

    private static class OneDimensionMock extends OneDimension {
        OneDimensionMock() {
            name = "MockOneDimension";
            pos = new Position(0, 0);
        }
    }
}
