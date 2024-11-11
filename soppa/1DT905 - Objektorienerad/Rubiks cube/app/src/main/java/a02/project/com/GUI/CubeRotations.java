package a02.project.com.GUI;

import java.util.List;
import java.util.concurrent.atomic.AtomicReference;

import javafx.animation.KeyFrame;
import javafx.animation.KeyValue;
import javafx.animation.RotateTransition;
import javafx.animation.Timeline;
import javafx.geometry.Point3D;
import javafx.scene.Group;
import javafx.scene.Node;
import javafx.scene.chart.Axis;
import javafx.scene.paint.Color;
import javafx.scene.paint.PhongMaterial;
import javafx.scene.shape.Box;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Sphere;
import javafx.scene.transform.Rotate;
import javafx.scene.transform.Transform;
import javafx.scene.transform.Translate;
import javafx.util.Duration;
import java.util.ArrayList;
import java.util.stream.Collectors;


public class CubeRotations {
    private static Integer Xrotation = 0;
    private static Integer Yrotation = 0;

    
    
    public static List<GraphicCubePart> columnRotation(Boolean isPrime, Integer column, Point3D axis) {
        
        Integer angle;
        Integer xval = 0;
        CubePartManager cubePartManager = CubePartManager.getInstance();
        if (isPrime) {
            switch (column) {
                case 1:
                    xval = 0;
                    break;
                case 2:
                    xval = 0;
                    break;
                case 3:
                    xval = 0;
                    break;
            }
            angle = 90;
        } else {
            
            switch (column) {
                case 1:
                    xval = 0;
                    break;
                case 2:
                    xval = 0;
                    break;
                case 3:
                    xval = 0;
                    break;
            }
            angle = -90;
        }
        List<GraphicCubePart> partsToMove = new ArrayList<>();

        for (int i = 0; i < 9; i++) {
            partsToMove.add(null);
        }
        for (GraphicCubePart part : cubePartManager.getCubeParts()) {
                if (part.getColumn() == column) {
                    if (part.getRow() == 3 && part.getLayer() == 1) {
                        partsToMove.set(0, part);
                    } else if (part.getRow() == 2 && part.getLayer() == 1) {
                        partsToMove.set(1, part);
                    } else if (part.getRow() == 1 && part.getLayer() == 1) {
                        partsToMove.set(2, part);
                    } else if (part.getRow() == 3 && part.getLayer() == 2) {
                        partsToMove.set(3, part);
                    } else if (part.getRow() == 2 && part.getLayer() == 2) {
                        partsToMove.set(4, part);
                    } else if (part.getRow() == 1 && part.getLayer() == 2) {
                        partsToMove.set(5, part);
                    } else if (part.getRow() == 3 && part.getLayer() == 3) {
                        partsToMove.set(6, part);
                    } else if (part.getRow() == 2 && part.getLayer() == 3) {
                        partsToMove.set(7, part);
                    } else if (part.getRow() == 1 && part.getLayer() == 3) {
                        partsToMove.set(8, part);
                    }

                    
                }
                }
                
        
        Integer i = 0;
        Integer x = 0;
        Integer y = 0;
        Integer z = 0;


            x = 50;
            y = -50;
            z = -50;
            partsToMove.get(0).getPart().getTransforms().removeIf(transform -> !(transform instanceof javafx.scene.transform.Rotate));

            partsToMove.get(0).getPart().setTranslateX(0);
            partsToMove.get(0).getPart().setTranslateZ(50);
            partsToMove.get(0).getPart().setTranslateY(50);
            Translate translateToRight = new Translate(x, y, z);
            partsToMove.get(0).getPart().getTransforms().add(translateToRight);

            x = 0;
            y = -50;
            z = -50;
            partsToMove.get(1).getPart().getTransforms().removeIf(transform -> !(transform instanceof javafx.scene.transform.Rotate));

            partsToMove.get(1).getPart().setTranslateX(0);
            partsToMove.get(1).getPart().setTranslateZ(50);
            partsToMove.get(1).getPart().setTranslateY(50);
            Translate translateToRight1 = new Translate(x, y, z);
            partsToMove.get(1).getPart().getTransforms().add(translateToRight1);

            x = 50;
            y = -50;
            z = -50;
            partsToMove.get(2).getPart().getTransforms().removeIf(transform -> !(transform instanceof javafx.scene.transform.Rotate));

            partsToMove.get(2).getPart().setTranslateX(0);
            partsToMove.get(2).getPart().setTranslateZ(50);
            partsToMove.get(2).getPart().setTranslateY(50);
            Translate translateToRight2 = new Translate(x, y, z);
            partsToMove.get(2).getPart().getTransforms().add(translateToRight2);

            x = 0;
            y = -50;
            z = -50;
            partsToMove.get(3).getPart().getTransforms().removeIf(transform -> !(transform instanceof javafx.scene.transform.Rotate));

            partsToMove.get(3).getPart().setTranslateX(0);
            partsToMove.get(3).getPart().setTranslateZ(50);
            partsToMove.get(3).getPart().setTranslateY(50);
            Translate translateToRight3 = new Translate(x, y, z);
            partsToMove.get(3).getPart().getTransforms().add(translateToRight3);


            x = 0;
            y = -50;
            z = -50;
            partsToMove.get(5).getPart().getTransforms().removeIf(transform -> !(transform instanceof javafx.scene.transform.Rotate));

            partsToMove.get(5).getPart().setTranslateX(0);
            partsToMove.get(5).getPart().setTranslateZ(50);
            partsToMove.get(5).getPart().setTranslateY(50);
            Translate translateToRight5 = new Translate(x, y, z);
            partsToMove.get(5).getPart().getTransforms().add(translateToRight5);

            x = 50;
            y = -50;
            z = -50;
            partsToMove.get(6).getPart().getTransforms().removeIf(transform -> !(transform instanceof javafx.scene.transform.Rotate));

            partsToMove.get(6).getPart().setTranslateX(0);
            partsToMove.get(6).getPart().setTranslateZ(50);
            partsToMove.get(6).getPart().setTranslateY(50);
            Translate translateToRight6 = new Translate(x, y, z);
            partsToMove.get(6).getPart().getTransforms().add(translateToRight6);

            x = 0;
            y = -50;
            z = -50;
            partsToMove.get(7).getPart().getTransforms().removeIf(transform -> !(transform instanceof javafx.scene.transform.Rotate));

            partsToMove.get(7).getPart().setTranslateX(0);
            partsToMove.get(7).getPart().setTranslateZ(50);
            partsToMove.get(7).getPart().setTranslateY(50);
            Translate translateToRight7 = new Translate(x, y, z);
            partsToMove.get(7).getPart().getTransforms().add(translateToRight7);

            x = 50;
            y = -50;
            z = -50;
            partsToMove.get(8).getPart().getTransforms().removeIf(transform -> !(transform instanceof javafx.scene.transform.Rotate));

            partsToMove.get(8).getPart().setTranslateX(0);
            partsToMove.get(8).getPart().setTranslateZ(50);
            partsToMove.get(8).getPart().setTranslateY(50);
            Translate translateToRight8 = new Translate(x, y, z);
            partsToMove.get(8).getPart().getTransforms().add(translateToRight8);

            // Set up the rotation transition
            RotateTransition rotateTransition = new RotateTransition(Duration.seconds(0.5), partsToMove.get(0).getPart());
            rotateTransition.setAxis(new Point3D(50, 0, 0)); // Rotate around the Y-axis
            rotateTransition.setByAngle(angle); // Rotate by 360 degrees
            rotateTransition.setOnFinished(event -> {

            });            
            rotateTransition.play();
            RotateTransition rotateTransition1 = new RotateTransition(Duration.seconds(0.5), partsToMove.get(1).getPart());
            rotateTransition1.setAxis(new Point3D(50, 0, 0)); // Rotate around the Y-axis
            rotateTransition1.setByAngle(angle); // Rotate by 360 degrees
            rotateTransition1.setOnFinished(event -> {

            });            
            rotateTransition1.play();
            RotateTransition rotateTransition2 = new RotateTransition(Duration.seconds(0.5), partsToMove.get(2).getPart());
            rotateTransition2.setAxis(new Point3D(50, 0, 0)); // Rotate around the Y-axis
            rotateTransition2.setByAngle(angle); // Rotate by 360 degrees
            rotateTransition2.setOnFinished(event -> {

            });          
            rotateTransition2.play();

            RotateTransition rotateTransition3 = new RotateTransition(Duration.seconds(0.5), partsToMove.get(3).getPart());
            rotateTransition3.setAxis(new Point3D(50, 0, 0)); // Rotate around the Y-axis
            rotateTransition3.setByAngle(angle); // Rotate by 360 degrees
            rotateTransition3.setOnFinished(event -> {

            });            
            rotateTransition3.play();

            RotateTransition rotateTransition4 = new RotateTransition(Duration.seconds(0.5), partsToMove.get(4).getPart());
            rotateTransition4.setAxis(new Point3D(50, 0, 0)); // Rotate around the Y-axis
            rotateTransition4.setByAngle(angle); // Rotate by 360 degrees
            rotateTransition4.setOnFinished(event -> {

            });            
            rotateTransition4.play();

            RotateTransition rotateTransition5 = new RotateTransition(Duration.seconds(0.5), partsToMove.get(5).getPart());
            rotateTransition5.setAxis(new Point3D(50, 0, 0)); // Rotate around the Y-axis
            rotateTransition5.setByAngle(angle); // Rotate by 360 degrees
            rotateTransition5.setOnFinished(event -> {

            });    
            rotateTransition5.play();

            RotateTransition rotateTransition6 = new RotateTransition(Duration.seconds(0.5), partsToMove.get(6).getPart());
            rotateTransition6.setAxis(new Point3D(50, 0, 0)); // Rotate around the Y-axis
            rotateTransition6.setByAngle(angle); // Rotate by 360 degrees
            rotateTransition6.setOnFinished(event -> {

            });            
            rotateTransition6.play();

            RotateTransition rotateTransition7 = new RotateTransition(Duration.seconds(0.5), partsToMove.get(7).getPart());
            rotateTransition7.setAxis(new Point3D(50, 0, 0)); // Rotate around the Y-axis
            rotateTransition7.setByAngle(angle); // Rotate by 360 degrees
            rotateTransition7.setOnFinished(event -> {
            });            
            rotateTransition7.play();

            RotateTransition rotateTransition8 = new RotateTransition(Duration.seconds(0.5), partsToMove.get(8).getPart());
            rotateTransition8.setAxis(new Point3D(50, 0, 0)); // Rotate around the Y-axis
            rotateTransition8.setByAngle(angle); // Rotate by 360 degrees
            rotateTransition8.setOnFinished(event -> {

            });    
            rotateTransition8.play();


            i ++;
        



        return partsToMove;
        }



    public static List<GraphicCubePart> sameRowRotation(Boolean isPrime, Point3D axis) {
        CubePartManager cubePartManager = CubePartManager.getInstance();
        Integer angle;
        if (isPrime) {
            angle = -90;
        } else {
            angle = 90;
        }
        List<GraphicCubePart> partsToMove = new ArrayList<>();
        for (int i = 0; i < 9; i++) {
            partsToMove.add(null);
        }
        for (GraphicCubePart part : cubePartManager.getCubeParts()) {
                if (part.getRow() == 3) {
                    if (part.getColumn() == 1 && part.getLayer() == 1) {
                        partsToMove.set(0, part);
                    } else if (part.getColumn() == 2 && part.getLayer() == 1) {
                        partsToMove.set(1, part);
                    } else if (part.getColumn() == 3 && part.getLayer() == 1) {
                        partsToMove.set(2, part);
                    } else if (part.getColumn() == 1 && part.getLayer() == 2) {
                        partsToMove.set(3, part);
                    } else if (part.getColumn() == 2 && part.getLayer() == 2) {
                        partsToMove.set(4, part);
                    } else if (part.getColumn() == 3 && part.getLayer() == 2) {
                        partsToMove.set(5, part);
                    } else if (part.getColumn() == 1 && part.getLayer() == 3) {
                        partsToMove.set(6, part);
                    } else if (part.getColumn() == 2 && part.getLayer() == 3) {
                        partsToMove.set(7, part);
                    } else if (part.getColumn() == 3 && part.getLayer() == 3) {
                        partsToMove.set(8, part);
                    }

                    
                }
                }
                
        
        Integer i = 0;
        Integer x = 0;
        Integer y = 0;
        Integer z = 0;



            x = 50;
            y = -50;
            z = -50;
            partsToMove.get(0).getPart().getTransforms().removeIf(transform -> !(transform instanceof javafx.scene.transform.Rotate));

            partsToMove.get(0).getPart().setTranslateX(0);
            partsToMove.get(0).getPart().setTranslateZ(50);
            partsToMove.get(0).getPart().setTranslateY(50);
            Translate translateToRight = new Translate(x, y, z);
            partsToMove.get(0).getPart().getTransforms().add(translateToRight);

            x = 0;
            y = -50;
            z = -50;
            partsToMove.get(1).getPart().getTransforms().removeIf(transform -> !(transform instanceof javafx.scene.transform.Rotate));

            partsToMove.get(1).getPart().setTranslateX(0);
            partsToMove.get(1).getPart().setTranslateZ(50);
            partsToMove.get(1).getPart().setTranslateY(50);
            Translate translateToRight1 = new Translate(x, y, z);
            partsToMove.get(1).getPart().getTransforms().add(translateToRight1);

            x = 50;
            y = -50;
            z = -50;
            partsToMove.get(2).getPart().getTransforms().removeIf(transform -> !(transform instanceof javafx.scene.transform.Rotate));

            partsToMove.get(2).getPart().setTranslateX(0);
            partsToMove.get(2).getPart().setTranslateZ(50);
            partsToMove.get(2).getPart().setTranslateY(50);
            Translate translateToRight2 = new Translate(x, y, z);
            partsToMove.get(2).getPart().getTransforms().add(translateToRight2);

            x = 0;
            y = -50;
            z = -50;
            partsToMove.get(3).getPart().getTransforms().removeIf(transform -> !(transform instanceof javafx.scene.transform.Rotate));

            partsToMove.get(3).getPart().setTranslateX(0);
            partsToMove.get(3).getPart().setTranslateZ(50);
            partsToMove.get(3).getPart().setTranslateY(50);
            Translate translateToRight3 = new Translate(x, y, z);
            partsToMove.get(3).getPart().getTransforms().add(translateToRight3);


            x = 0;
            y = -50;
            z = -50;
            partsToMove.get(5).getPart().getTransforms().removeIf(transform -> !(transform instanceof javafx.scene.transform.Rotate));

            partsToMove.get(5).getPart().setTranslateX(0);
            partsToMove.get(5).getPart().setTranslateZ(50);
            partsToMove.get(5).getPart().setTranslateY(50);
            Translate translateToRight5 = new Translate(x, y, z);
            partsToMove.get(5).getPart().getTransforms().add(translateToRight5);

            x = 50;
            y = -50;
            z = -50;
            partsToMove.get(6).getPart().getTransforms().removeIf(transform -> !(transform instanceof javafx.scene.transform.Rotate));

            partsToMove.get(6).getPart().setTranslateX(0);
            partsToMove.get(6).getPart().setTranslateZ(50);
            partsToMove.get(6).getPart().setTranslateY(50);
            Translate translateToRight6 = new Translate(x, y, z);
            partsToMove.get(6).getPart().getTransforms().add(translateToRight6);

            x = 0;
            y = -50;
            z = -50;
            partsToMove.get(7).getPart().getTransforms().removeIf(transform -> !(transform instanceof javafx.scene.transform.Rotate));

            partsToMove.get(7).getPart().setTranslateX(0);
            partsToMove.get(7).getPart().setTranslateZ(50);
            partsToMove.get(7).getPart().setTranslateY(50);
            Translate translateToRight7 = new Translate(x, y, z);
            partsToMove.get(7).getPart().getTransforms().add(translateToRight7);

            x = 50;
            y = -50;
            z = -50;
            partsToMove.get(8).getPart().getTransforms().removeIf(transform -> !(transform instanceof javafx.scene.transform.Rotate));

            partsToMove.get(8).getPart().setTranslateX(0);
            partsToMove.get(8).getPart().setTranslateZ(50);
            partsToMove.get(8).getPart().setTranslateY(50);
            Translate translateToRight8 = new Translate(x, y, z);
            partsToMove.get(8).getPart().getTransforms().add(translateToRight8);

            // Set up the rotation transition
            RotateTransition rotateTransition = new RotateTransition(Duration.seconds(0.5), partsToMove.get(0).getPart());
            rotateTransition.setAxis(new Point3D(0, 0, 1)); // Rotate around the Y-axis
            rotateTransition.setByAngle(angle); // Rotate by 360 degrees
            rotateTransition.setOnFinished(event -> {

            });            
            rotateTransition.play();
            RotateTransition rotateTransition1 = new RotateTransition(Duration.seconds(0.5), partsToMove.get(1).getPart());
            rotateTransition1.setAxis(new Point3D(0, 0, 1)); // Rotate around the Y-axis
            rotateTransition1.setByAngle(angle); // Rotate by 360 degrees
            rotateTransition1.setOnFinished(event -> {

            });            
            rotateTransition1.play();
            RotateTransition rotateTransition2 = new RotateTransition(Duration.seconds(0.5), partsToMove.get(2).getPart());
            rotateTransition2.setAxis(new Point3D(0, 0, 1)); // Rotate around the Y-axis
            rotateTransition2.setByAngle(angle); // Rotate by 360 degrees
            rotateTransition2.setOnFinished(event -> {

            });          
            rotateTransition2.play();

            RotateTransition rotateTransition3 = new RotateTransition(Duration.seconds(0.5), partsToMove.get(3).getPart());
            rotateTransition3.setAxis(new Point3D(0, 0, 1)); // Rotate around the Y-axis
            rotateTransition3.setByAngle(angle); // Rotate by 360 degrees
            rotateTransition3.setOnFinished(event -> {

            });            
            rotateTransition3.play();

            RotateTransition rotateTransition4 = new RotateTransition(Duration.seconds(0.5), partsToMove.get(4).getPart());
            rotateTransition4.setAxis(new Point3D(0, 0, 1)); // Rotate around the Y-axis
            rotateTransition4.setByAngle(angle); // Rotate by 360 degrees
            rotateTransition4.setOnFinished(event -> {

            });            
            rotateTransition4.play();

            RotateTransition rotateTransition5 = new RotateTransition(Duration.seconds(0.5), partsToMove.get(5).getPart());
            rotateTransition5.setAxis(new Point3D(0, 0, 1)); // Rotate around the Y-axis
            rotateTransition5.setByAngle(angle); // Rotate by 360 degrees
            rotateTransition5.setOnFinished(event -> {

            });    
            rotateTransition5.play();

            RotateTransition rotateTransition6 = new RotateTransition(Duration.seconds(0.5), partsToMove.get(6).getPart());
            rotateTransition6.setAxis(new Point3D(0, 0, 1)); // Rotate around the Y-axis
            rotateTransition6.setByAngle(angle); // Rotate by 360 degrees
            rotateTransition6.setOnFinished(event -> {

            });            
            rotateTransition6.play();

            RotateTransition rotateTransition7 = new RotateTransition(Duration.seconds(0.5), partsToMove.get(7).getPart());
            rotateTransition7.setAxis(new Point3D(0, 0, 1)); // Rotate around the Y-axis
            rotateTransition7.setByAngle(angle); // Rotate by 360 degrees
            rotateTransition7.setOnFinished(event -> {
            });            
            rotateTransition7.play();

            RotateTransition rotateTransition8 = new RotateTransition(Duration.seconds(0.5), partsToMove.get(8).getPart());
            rotateTransition8.setAxis(new Point3D(0, 0, 1)); // Rotate around the Y-axis
            rotateTransition8.setByAngle(angle); // Rotate by 360 degrees
            rotateTransition8.setOnFinished(event -> {

            });    
            rotateTransition8.play();


            i ++;
        



        return partsToMove;
        }
            
 
    


    public static void wholeCubeRotation(Integer Xaxis, Integer Yaxis, Boolean isPrime, String choice) {
        Group combinedGroup = new Group();
        
        Integer angle;
        if (isPrime) {
            switch (choice) {
                case "x":
                    combinedGroup.setRotate(Xrotation);
                    Xrotation += 90;
                    break;
                case "y":
                    combinedGroup.setRotate(Yrotation);
                    Yrotation += 90;
                    break;
            }
            angle = 90;
        } else {
            switch (choice) {
                case "x":
                    combinedGroup.setRotate(Xrotation);
                    Xrotation -= 90;
                    break;
                case "y":
                    combinedGroup.setRotate(Yrotation);
                    Yrotation -= 90;
                    break;
            }
            angle = -90;
        }
        List<GraphicCubePart> partsToMove = new ArrayList<>();
        for (GraphicCubePart part : CubePartManager.getInstance().getCubeParts()) {
            partsToMove.add(part);
            Group temp = part.getPart();
            combinedGroup.getChildren().add(temp);
        }

        RotateTransition rotateTransition = new RotateTransition(Duration.seconds(0.5), combinedGroup);
        rotateTransition.setAxis(new Point3D(Yaxis, Xaxis, 0));
        rotateTransition.setByAngle(angle);
        rotateTransition.setOnFinished(e -> {
            CubePositions.fixPositionWholeCube(isPrime, partsToMove, choice);
        });
        rotateTransition.play();

        
        Controller.setroot3d(combinedGroup);
        Controller.setrubiks(combinedGroup);
        
}
    }
