package a02.project.com.GUI;

import javafx.scene.Group;
import javafx.scene.paint.Color;
import javafx.scene.paint.PhongMaterial;
import javafx.scene.transform.Rotate;
import java.util.List;
import java.util.ArrayList;


public class GraphicCube {

    public static Group graphicCube() {
        Group rubiksCube = new Group();
        
        PhongMaterial red = new PhongMaterial(Color.RED);
        PhongMaterial green = new PhongMaterial(Color.GREEN);
        PhongMaterial blue = new PhongMaterial(Color.BLUE);
        PhongMaterial yellow = new PhongMaterial(Color.YELLOW);
        PhongMaterial orange = new PhongMaterial(Color.ORANGE);
        PhongMaterial white = new PhongMaterial(Color.WHITE);
        PhongMaterial black = new PhongMaterial(Color.BLACK);

        // Layer 1
        Group cubepart111 = GraphicCubeCornerPart.graphicCubeCornerPart(50.0, white, orange, green);
        cubepart111.getTransforms().add(new Rotate(180, Rotate.Y_AXIS));
        cubepart111.setTranslateX(-50.0);
        cubepart111.setTranslateZ(100);
        Group cubepart211 = GraphicCubeSideMiddlePart.graphicCubeSideMiddlePart(50.0, white, orange);
        cubepart211.getTransforms().add(new Rotate(180, Rotate.Y_AXIS));
        cubepart211.setTranslateX(0);
        cubepart211.setTranslateZ(100);
        Group cubepart311 = GraphicCubeCornerPart.graphicCubeCornerPart(50.0, white, blue, orange);
        cubepart311.getTransforms().add(new Rotate(270, Rotate.Y_AXIS));
        cubepart311.setTranslateX(50.0);
        cubepart311.setTranslateZ(100);
        Group cubepart121 = GraphicCubeSideMiddlePart.graphicCubeSideMiddlePart(50.0, white, green);
        cubepart121.getTransforms().add(new Rotate(90, Rotate.Y_AXIS));
        cubepart121.setTranslateX(-50.0);
        cubepart121.setTranslateZ(50);
        Group cubepart221 = GraphicCubeMiddlePart.graphicCubeMiddlePart(50.0, white);
        cubepart221.setTranslateX(0);
        cubepart221.setTranslateZ(50);
        Group cubepart321 = GraphicCubeSideMiddlePart.graphicCubeSideMiddlePart(50.0, white, blue);
        cubepart321.getTransforms().add(new Rotate(270, Rotate.Y_AXIS));
        cubepart321.setTranslateX(50.0);
        cubepart321.setTranslateZ(50);
        Group cubepart131 = GraphicCubeCornerPart.graphicCubeCornerPart(50.0, white, green, red);
        cubepart131.getTransforms().add(new Rotate(90, Rotate.Y_AXIS));
        cubepart131.setTranslateX(-50.0);
        cubepart131.setTranslateZ(0);
        Group cubepart231 = GraphicCubeSideMiddlePart.graphicCubeSideMiddlePart(50.0, white, red);
        cubepart231.setTranslateX(0);
        cubepart231.setTranslateZ(0);
        Group cubepart331 = GraphicCubeCornerPart.graphicCubeCornerPart(50.0, white, red, blue);
        cubepart331.setTranslateX(50.0);
        cubepart331.setTranslateZ(0);

        // Layer 2
        Group cubepart112 = GraphicCubeSideMiddlePart.graphicCubeSideMiddlePart(50.0, orange, green);
        cubepart112.getTransforms().add(new Rotate(270, Rotate.X_AXIS));
        cubepart112.getTransforms().add(new Rotate(90, Rotate.Y_AXIS));
        cubepart112.setTranslateX(-50.0);
        cubepart112.setTranslateY(50);
        cubepart112.setTranslateZ(100);
        Group cubepart212 = GraphicCubeMiddlePart.graphicCubeMiddlePart(50.0, orange);
        cubepart212.getTransforms().add(new Rotate(270, Rotate.X_AXIS));
        cubepart212.setTranslateX(0);
        cubepart212.setTranslateY(50);
        cubepart212.setTranslateZ(100);
        Group cubepart312 = GraphicCubeSideMiddlePart.graphicCubeSideMiddlePart(50.0, orange, blue);
        cubepart312.getTransforms().add(new Rotate(270, Rotate.X_AXIS));
        cubepart312.getTransforms().add(new Rotate(270, Rotate.Y_AXIS));
        cubepart312.setTranslateX(50.0);
        cubepart312.setTranslateY(50);
        cubepart312.setTranslateZ(100);
        Group cubepart122 = GraphicCubeMiddlePart.graphicCubeMiddlePart(50.0, green);
        cubepart122.getTransforms().add(new Rotate(270, Rotate.Z_AXIS));
        cubepart122.setTranslateX(-50.0);
        cubepart122.setTranslateY(50);
        cubepart122.setTranslateZ(50);
        Group cubepart222 = GraphicCubeMiddlePart.graphicCubeMiddlePart(50.0, black);
        cubepart222.setTranslateX(0);
        cubepart222.setTranslateY(50);
        cubepart222.setTranslateZ(50);
        Group cubepart322 = GraphicCubeMiddlePart.graphicCubeMiddlePart(50.0, blue);
        cubepart322.getTransforms().add(new Rotate(90, Rotate.Z_AXIS));
        cubepart322.setTranslateX(50.0);
        cubepart322.setTranslateY(50);
        cubepart322.setTranslateZ(50);
        Group cubepart132 = GraphicCubeSideMiddlePart.graphicCubeSideMiddlePart(50.0, green, red);
        cubepart132.getTransforms().add(new Rotate(270, Rotate.Z_AXIS));
        cubepart132.setTranslateX(-50.0);
        cubepart132.setTranslateY(50);
        cubepart132.setTranslateZ(0);
        Group cubepart232 = GraphicCubeMiddlePart.graphicCubeMiddlePart(50.0, red);
        cubepart232.getTransforms().add(new Rotate(90, Rotate.X_AXIS));
        cubepart232.setTranslateX(0);
        cubepart232.setTranslateY(50);
        cubepart232.setTranslateZ(0);
        Group cubepart332 = GraphicCubeSideMiddlePart.graphicCubeSideMiddlePart(50.0, blue, red);
        cubepart332.getTransforms().add(new Rotate(90, Rotate.Z_AXIS));
        cubepart332.setTranslateX(50.0);
        cubepart332.setTranslateY(50);
        cubepart332.setTranslateZ(0);

        // Layer 3
        Group cubepart113 = GraphicCubeCornerPart.graphicCubeCornerPart(50.0, yellow, green, orange);
        cubepart113.getTransforms().add(new Rotate(90, Rotate.Y_AXIS));
        cubepart113.getTransforms().add(new Rotate(180, Rotate.Z_AXIS));
        cubepart113.setTranslateX(-50.0);
        cubepart113.setTranslateY(100);
        cubepart113.setTranslateZ(100);
        Group cubepart213 = GraphicCubeSideMiddlePart.graphicCubeSideMiddlePart(50.0, yellow, orange);
        cubepart213.getTransforms().add(new Rotate(180, Rotate.X_AXIS));
        cubepart213.setTranslateX(0);
        cubepart213.setTranslateY(100);
        cubepart213.setTranslateZ(100);
        Group cubepart313 = GraphicCubeCornerPart.graphicCubeCornerPart(50.0, yellow, orange, blue);
        cubepart313.getTransforms().add(new Rotate(180, Rotate.Y_AXIS));
        cubepart313.getTransforms().add(new Rotate(180, Rotate.Z_AXIS));
        cubepart313.setTranslateX(50.0);
        cubepart313.setTranslateY(100);
        cubepart313.setTranslateZ(100);
        Group cubepart123 = GraphicCubeSideMiddlePart.graphicCubeSideMiddlePart(50.0, yellow, green);
        cubepart123.getTransforms().add(new Rotate(180, Rotate.Z_AXIS));
        cubepart123.getTransforms().add(new Rotate(270, Rotate.Y_AXIS));
        cubepart123.setTranslateX(-50.0);
        cubepart123.setTranslateY(100);
        cubepart123.setTranslateZ(50);
        Group cubepart223 = GraphicCubeMiddlePart.graphicCubeMiddlePart(50.0, yellow);
        cubepart223.getTransforms().add(new Rotate(180, Rotate.Z_AXIS));
        cubepart223.setTranslateX(0);
        cubepart223.setTranslateY(100);
        cubepart223.setTranslateZ(50);
        Group cubepart323 = GraphicCubeSideMiddlePart.graphicCubeSideMiddlePart(50.0, yellow, blue);
        cubepart323.getTransforms().add(new Rotate(180, Rotate.Z_AXIS));
        cubepart323.getTransforms().add(new Rotate(90, Rotate.Y_AXIS));
        cubepart323.setTranslateX(50.0);
        cubepart323.setTranslateY(100);
        cubepart323.setTranslateZ(50);
        Group cubepart133 = GraphicCubeCornerPart.graphicCubeCornerPart(50.0, yellow, red, green);
        cubepart133.getTransforms().add(new Rotate(180, Rotate.Z_AXIS));
        cubepart133.setTranslateX(-50.0);
        cubepart133.setTranslateY(100);
        cubepart133.setTranslateZ(0);
        Group cubepart233 = GraphicCubeSideMiddlePart.graphicCubeSideMiddlePart(50.0, red, yellow);
        cubepart233.getTransforms().add(new Rotate(90, Rotate.X_AXIS));
        cubepart233.setTranslateX(0);
        cubepart233.setTranslateY(100);
        cubepart233.setTranslateZ(0);
        Group cubepart333 = GraphicCubeCornerPart.graphicCubeCornerPart(50.0, yellow, blue, red);
        cubepart333.getTransforms().add(new Rotate(270, Rotate.Y_AXIS));
        cubepart333.getTransforms().add(new Rotate(180, Rotate.Z_AXIS));
        cubepart333.setTranslateX(50.0);
        cubepart333.setTranslateY(100);
        cubepart333.setTranslateZ(0);

        List<GraphicCubePart> cubeParts= new ArrayList<>();
        cubeParts.add(new GraphicCubePart(cubepart111, 1, 1, 1));
        cubeParts.add(new GraphicCubePart(cubepart211, 2, 1, 1));
        cubeParts.add(new GraphicCubePart(cubepart311, 3, 1, 1));
        cubeParts.add(new GraphicCubePart(cubepart121, 1, 2, 1));
        cubeParts.add(new GraphicCubePart(cubepart221, 2, 2, 1));
        cubeParts.add(new GraphicCubePart(cubepart321, 3, 2, 1));
        cubeParts.add(new GraphicCubePart(cubepart131, 1, 3, 1));
        cubeParts.add(new GraphicCubePart(cubepart231, 2, 3, 1));
        cubeParts.add(new GraphicCubePart(cubepart331, 3, 3, 1));
        cubeParts.add(new GraphicCubePart(cubepart112, 1, 1, 2));
        cubeParts.add(new GraphicCubePart(cubepart212, 2, 1, 2));
        cubeParts.add(new GraphicCubePart(cubepart312, 3, 1, 2));
        cubeParts.add(new GraphicCubePart(cubepart122, 1, 2, 2));
        cubeParts.add(new GraphicCubePart(cubepart222, 2, 2, 2));
        cubeParts.add(new GraphicCubePart(cubepart322, 3, 2, 2));
        cubeParts.add(new GraphicCubePart(cubepart132, 1, 3, 2));
        cubeParts.add(new GraphicCubePart(cubepart232, 2, 3, 2));
        cubeParts.add(new GraphicCubePart(cubepart332, 3, 3, 2));
        cubeParts.add(new GraphicCubePart(cubepart113, 1, 1, 3));
        cubeParts.add(new GraphicCubePart(cubepart213, 2, 1, 3));
        cubeParts.add(new GraphicCubePart(cubepart313, 3, 1, 3));
        cubeParts.add(new GraphicCubePart(cubepart123, 1, 2, 3));
        cubeParts.add(new GraphicCubePart(cubepart223, 2, 2, 3));
        cubeParts.add(new GraphicCubePart(cubepart323, 3, 2, 3));
        cubeParts.add(new GraphicCubePart(cubepart133, 1, 3, 3));
        cubeParts.add(new GraphicCubePart(cubepart233, 2, 3, 3));
        cubeParts.add(new GraphicCubePart(cubepart333, 3, 3, 3));



        CubePartManager.getInstance().setCubeParts(cubeParts);
        rubiksCube.getChildren().addAll(cubepart111, cubepart211, cubepart311, cubepart121, cubepart221, cubepart321, cubepart131, cubepart231, cubepart331,
                                        cubepart112, cubepart212, cubepart312, cubepart122, cubepart222, cubepart322, cubepart132, cubepart232, cubepart332,
                                        cubepart113, cubepart213, cubepart313, cubepart123, cubepart223, cubepart323, cubepart133, cubepart233, cubepart333);

        
        
        return rubiksCube;
    }
}