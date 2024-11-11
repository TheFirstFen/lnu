package a02.project.com.GUI;

import javafx.scene.Group;
import javafx.scene.paint.Color;
import javafx.scene.paint.PhongMaterial;
import javafx.scene.shape.Box;

public class GraphicCubeSideMiddlePart {
    public static Group graphicCubeSideMiddlePart(Double size, PhongMaterial topColor, PhongMaterial sideColor) {
        Group cubeGroup = new Group();

        // Define different materials for each face
        PhongMaterial black = new PhongMaterial(Color.BLACK);

        // Create individual boxes for each face
        Box main = new Box(size, size, size);
        main.setMaterial(black);

        Box topColorPatch = new Box(size - 10, 0.1, size - 10);
        topColorPatch.setMaterial(topColor);
        topColorPatch.setTranslateY((-size / 2) - 0.1);
        
        Box frontColorPatch = new Box(size - 10, size - 10, 0.1);
        frontColorPatch.setMaterial(sideColor);
        frontColorPatch.setTranslateZ((-size / 2) - 0.1);


        cubeGroup.getChildren().addAll(main, topColorPatch, frontColorPatch);
        return cubeGroup;
    }
}