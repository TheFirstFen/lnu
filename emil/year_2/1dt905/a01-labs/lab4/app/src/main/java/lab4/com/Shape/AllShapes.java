package lab4.com.Shape;

import java.util.ArrayList;
import java.util.List;


/**
 * A class that displays the collection of shapes
 * The class allows you to add, remove, wiev shapes
 */
public class AllShapes {
    private List<AbstractShape> shapeList;


    /**
     * 
     * Initialize a new list
     */
    public AllShapes(){
        shapeList = new ArrayList <>();
    }

    /**
     * Adds a shape to the collection
     * @param shape The shape to add
     */
    public void addShape(AbstractShape shape) {
        shapeList.add(shape);
    }

    /**
     * Retrive a list of all shapes in the collection
     * @return A list of all shapes
     */
    public List<AbstractShape> getAllShapes() {
        return shapeList;
    }

    /**
     * Removes a shape from the collection
     * @param shape The shape to remove
     */
    public void removeShape(AbstractShape shape) {
        shapeList.remove(shape);
    }
    
}
