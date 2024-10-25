package task3.com.sb224sc.classes;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.AfterAll;

class AddRandShapeTest {
    private final static AddRandShape addRandShape = new AddRandShape();

    @Test
    void testAddRandShape() {
        AddRandShape.setFixedRandomChoice(1);
        AddRandShape.addRandShape();
        assertNotNull(PrintAllShapes.getLastAddedShape());

        AddRandShape.setFixedRandomChoice(2);
        AddRandShape.addRandShape();
        assertNotNull(PrintAllShapes.getLastAddedShape());

        AddRandShape.setFixedRandomChoice(3);
        AddRandShape.addRandShape();
        assertNotNull(PrintAllShapes.getLastAddedShape());

        AddRandShape.setFixedRandomChoice(4);
        AddRandShape.addRandShape();
        assertNotNull(PrintAllShapes.getLastAddedShape());

        PrintAllShapes.clearShapes();
        AddRandShape.setFixedRandomChoice(10);
        AddRandShape.addRandShape();
        assertNull(PrintAllShapes.getLastAddedShape());

        AddRandShape.setFixedRandomChoice(-1);
        AddRandShape.addRandShape();
        assertNotNull(PrintAllShapes.getLastAddedShape());
    }

    @AfterAll
    public static void tearDownAfterClass() {
        addRandShape.toString();
    }
}
