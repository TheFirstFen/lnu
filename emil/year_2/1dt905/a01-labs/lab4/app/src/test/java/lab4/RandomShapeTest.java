package lab4;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import java.util.List;

import lab4.com.Shape.*;

public class RandomShapeTest {
    private AllShapes allShapes;

    @BeforeEach
    public void setUp() {
        allShapes = new AllShapes();
    }

    @Test
    public void testRandomLoopAddShape() {
        // To be sure none of the 4 alternatives are missed
        for(int i=0; i<100;i++){
            RandomShape.randomLoop(allShapes);
        }

        List<AbstractShape> shapes = allShapes.getAllShapes();
        assertTrue(!shapes.isEmpty(), "The collection should contain at least one shape.");
    }
}
