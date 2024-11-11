package a02.project.com.GUI;

import javafx.scene.shape.Box;

import javafx.scene.paint.Color;
import javafx.scene.paint.PhongMaterial;
import javafx.scene.Group;


public class GraphicCubeCornerPart {

    public static Group graphicCubeCornerPart(Double size, PhongMaterial topColor, PhongMaterial side1Color, PhongMaterial side2Color) {
        Group cubeGroup = new Group();

        PhongMaterial black = new PhongMaterial(Color.BLACK);


        Box main = new Box(size, size, size);
        main.setMaterial(black);

        Box topColorPatch = new Box(size - 10, 0.1, size - 10);
        topColorPatch.setMaterial(topColor);
        topColorPatch.setTranslateY((-size / 2) - 0.1);
        
        Box frontColorPatch = new Box(size - 10, size - 10, 0.1);
        frontColorPatch.setMaterial(side1Color);
        frontColorPatch.setTranslateZ((-size / 2) - 0.1);

        Box rightColorPatch = new Box(0.1, size - 10, size - 10);
        rightColorPatch.setMaterial(side2Color);
        rightColorPatch.setTranslateX((size / 2) + 0.1);

        cubeGroup.getChildren().addAll(main, frontColorPatch, topColorPatch, rightColorPatch);
        
        return cubeGroup;
    }

}

