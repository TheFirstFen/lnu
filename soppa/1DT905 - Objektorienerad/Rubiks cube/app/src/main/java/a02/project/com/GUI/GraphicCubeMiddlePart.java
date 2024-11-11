package a02.project.com.GUI;

import javafx.scene.Group;
import javafx.scene.paint.Color;
import javafx.scene.paint.PhongMaterial;
import javafx.scene.shape.Box;

public class GraphicCubeMiddlePart {

    public static Group graphicCubeMiddlePart(Double size, PhongMaterial topColor) {
        Group cubeGroup = new Group();

        PhongMaterial black = new PhongMaterial(Color.BLACK);

        Box main = new Box(size, size, size);
        main.setMaterial(black);

        Box topColorPatch = new Box(size - 10, 0.1, size - 10);
        topColorPatch.setMaterial(topColor);
        topColorPatch.setTranslateY((-size / 2) - 0.1);
    
        cubeGroup.getChildren().addAll(main, topColorPatch);
        return cubeGroup;
    }
}