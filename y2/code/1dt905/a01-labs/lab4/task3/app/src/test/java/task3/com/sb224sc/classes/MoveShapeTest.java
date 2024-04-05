package task3.com.sb224sc.classes;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import static org.junit.jupiter.api.Assertions.*;

public class MoveShapeTest {
    private final static MoveShape moveShape = new MoveShape();

    @Test
    public void testMoveableShapesEmpty() {
        List<AbstractShape> shapeList = new ArrayList<>();
        List<AbstractShape> movableShapes = MoveShape.getMovableShapes(shapeList);

        assertTrue(movableShapes.isEmpty());
    }

    @Test
    public void testMoveShapeValidChoiceShapeMoved() {
        Scanner sc = new Scanner("1\n1\n1\n");
        List<AbstractShape> shapeList = new ArrayList<>();
        shapeList.add(new Point());
        shapeList.add(new Line());

        MoveShape.moveShape(sc, shapeList);

        assertNotNull(shapeList.get(0));
        assertEquals(1, shapeList.get(0).getPosition().getX());
        assertEquals(1, shapeList.get(0).getPosition().getY());

    }

    @Test
    public void testMoveShapeInvalidChoiceErrorMessageDisplayed() {
        Scanner sc = new Scanner("invalid\n");
        List<AbstractShape> shapeList = new ArrayList<>();
        shapeList.add(new Point());
        shapeList.add(new Line());

        MoveShape.moveShape(sc, shapeList);

        assertNotNull(shapeList.get(0));

    }

    @Test
    public void testGetShapeChoiceValidChoiceReturnChoice() {
        Scanner sc = new Scanner("1\n");
        int maxChoice = 1;

        int choice = MoveShape.getShapeChoice(sc, maxChoice);

        assertEquals(1, choice);
    }

    @Test
    public void testGetShapeChoiceInvalidChoice() {
        Scanner sc = new Scanner("0\n3\n1\n");
        int maxChoice = 1;

        int choice = MoveShape.getShapeChoice(sc, maxChoice);

        assertEquals(1, choice);
    }

    @AfterAll
    public static void tearDownAfterClass() {
        moveShape.toString();
    }
}
