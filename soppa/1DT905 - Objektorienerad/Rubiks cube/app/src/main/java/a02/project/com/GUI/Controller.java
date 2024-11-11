package a02.project.com.GUI;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javafx.animation.PauseTransition;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.geometry.Point3D;
import javafx.scene.AmbientLight;
import javafx.scene.Group;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.PerspectiveCamera;
import javafx.scene.Scene;
import javafx.scene.SceneAntialiasing;
import javafx.scene.SubScene;
import javafx.scene.control.Button;
import javafx.scene.layout.Background;
import javafx.scene.layout.BackgroundFill;
import javafx.scene.layout.StackPane;
import javafx.scene.paint.Color;
import javafx.scene.transform.Rotate;
import javafx.scene.transform.Transform;
import javafx.stage.Stage;
import javafx.util.Duration;


public class Controller {
    @FXML
    private Button button;
    private boolean buttonPressed = true;
    private static Group RubiksCube;
    private static Group root3D;


    public static Group getRubiksCube() {
        return RubiksCube;
    }
    public static Group getRoot3d() {
        return root3D;
    }
    
    public static void setroot3d(Node groupToAdd) {
        root3D.getChildren().add(groupToAdd);
    }
    public static void setrubiks(Node groupToAdd) {
        RubiksCube.getChildren().add(groupToAdd);
    }
    public static void clearrubiks() {
        RubiksCube.getChildren().clear();
    }

    public void handleStartButtonAction(ActionEvent event) {
        Parent root2D = null;
        try {
            root2D = FXMLLoader.load(getClass().getResource("/MainPage.fxml"));
        } catch (IOException e) {
            e.printStackTrace();
        }

         if (root2D != null) {
            Stage mainStage = (Stage) ((Node) event.getSource()).getScene().getWindow();
            SubScene subScene = create3DScene();

            
            StackPane layout = new StackPane(root2D, subScene);
            


            mainStage.setTitle("Rubiks cube simulator");
            BackgroundFill backgroundFill = new BackgroundFill(Color.LIGHTBLUE, null, null);
            Background background = new Background(backgroundFill);
            layout.setBackground(background);
            mainStage.setScene(new Scene(layout, 1000, 800, true, SceneAntialiasing.BALANCED));
            mainStage.show();
        }
    }
    private SubScene create3DScene() {
        RubiksCube = GraphicCube.graphicCube();


        root3D = new Group();

        root3D.getChildren().add(RubiksCube);
        
        root3D.setTranslateX(600); 
        root3D.setTranslateY(-50);
        

        SubScene subScene = new SubScene(root3D, 1000, 400, true, SceneAntialiasing.BALANCED);
        PerspectiveCamera camera = new PerspectiveCamera();
        camera.setTranslateY(-200);
        camera.setTranslateX(100);
        camera.setTranslateZ(100);
        camera.getTransforms().add(new Rotate(-20, Rotate.X_AXIS));
        camera.getTransforms().add(new Rotate(-20, Rotate.Y_AXIS));
        subScene.setCamera(camera);

        subScene.setTranslateY(-190);

        root3D.getChildren().addAll(new AmbientLight(Color.WHITE));

        return subScene;
    }
    public static Group getFullCubeGroups() {
        return RubiksCube;
    }

    
    
    public void rButton (ActionEvent event) {
        if (!buttonPressed) {
             return;
         }
         buttonPressed = false;
         Point3D axis = new Point3D(1, 0, 0);
         List<GraphicCubePart> partsToMove =  CubeRotations.columnRotation(false, 3, axis);
         
         PauseTransition pause = new PauseTransition(Duration.seconds(0.5));
         pause.setOnFinished(e -> {
            CubePositions.fixPositionsSameColumn(false, partsToMove);
             buttonPressed = true;


            
            });
            pause.play();

    }
        public void fButton (ActionEvent event) {
        if (!buttonPressed) {
             return;
         }


         buttonPressed = false;
         Point3D axis = new Point3D(0, 0, 1);
         List<GraphicCubePart> partsToMove =  CubeRotations.sameRowRotation(false, axis);
         

         
         PauseTransition pause = new PauseTransition(Duration.seconds(0.5));
         pause.setOnFinished(e -> {
            CubePositions.fixPositionsSameRow(false, partsToMove);
             buttonPressed = true;

            });
            pause.play();
    }

    public void rPrimeButton (ActionEvent event) {
        if (!buttonPressed) {
             return;
         }
         buttonPressed = false;
         Point3D axis = new Point3D(1, 0, 0);

         List<GraphicCubePart> partsToMove =  CubeRotations.columnRotation(true, 3, axis);

         
         
         PauseTransition pause = new PauseTransition(Duration.seconds(0.5));
         pause.setOnFinished(e -> {
            CubePositions.fixPositionsSameColumn(true, partsToMove);
             buttonPressed = true;
            });
            pause.play();
    }

    public void mButton (ActionEvent event) {
        if (!buttonPressed) {
             return;
         }
         buttonPressed = false;
         Point3D axis = new Point3D(1, 0, 0);

         List<GraphicCubePart> partsToMove =  CubeRotations.columnRotation(false, 2, axis);

         
         
         PauseTransition pause = new PauseTransition(Duration.seconds(0.5));
         pause.setOnFinished(e -> {
            CubePositions.fixPositionsSameColumn(false, partsToMove);
             buttonPressed = true;
            });
            pause.play();
    }

    public void mPrimeButton (ActionEvent event) {
        if (!buttonPressed) {
             return;
         }
         buttonPressed = false;
         Point3D axis = new Point3D(1, 0, 0);

         List<GraphicCubePart> partsToMove =  CubeRotations.columnRotation(true, 2, axis);

         
         
         PauseTransition pause = new PauseTransition(Duration.seconds(0.5));
         pause.setOnFinished(e -> {
            CubePositions.fixPositionsSameColumn(true, partsToMove);
             buttonPressed = true;
            });
            pause.play();
    }

    public void lButton (ActionEvent event) {
        if (!buttonPressed) {
             return;
         }
         buttonPressed = false;
         Point3D axis = new Point3D(1, 0, 0);

         List<GraphicCubePart> partsToMove =  CubeRotations.columnRotation(true, 1, axis);

         
         
         PauseTransition pause = new PauseTransition(Duration.seconds(0.5));
         pause.setOnFinished(e -> {
            CubePositions.fixPositionsSameColumn(true, partsToMove);
             buttonPressed = true;
            });
            pause.play();
    }

    public void lPrimeButton (ActionEvent event) {
        if (!buttonPressed) {
             return;
         }
         buttonPressed = false;
         Point3D axis = new Point3D(1, 0, 0);

         List<GraphicCubePart> partsToMove =  CubeRotations.columnRotation(false, 1, axis);

         
         
         PauseTransition pause = new PauseTransition(Duration.seconds(0.5));
         pause.setOnFinished(e -> {
            CubePositions.fixPositionsSameColumn(false, partsToMove);
             buttonPressed = true;
            });
            pause.play();
    }



    public void fPrimeButton (ActionEvent event) {
        if (!buttonPressed) {
             return;
         }
         buttonPressed = false;
         Point3D axis = new Point3D(0, 0, 1);

         List<GraphicCubePart> partsToMove = CubeRotations.sameRowRotation(true, axis);

         
         
         PauseTransition pause = new PauseTransition(Duration.seconds(0.5));
         pause.setOnFinished(e -> {
            //CubePositions.fixPositionsSameRow(true, partsToMove);
             buttonPressed = true;
            });
            pause.play();
    }




        
        
        
        
        
        public void xButton (ActionEvent event) {
            if (!buttonPressed) {
                return;
            }
        buttonPressed = false;
        
        CubeRotations.wholeCubeRotation(0, 1, false, "x");
        
        PauseTransition pause = new PauseTransition(Duration.seconds(0.5));
        pause.setOnFinished(e -> {
            buttonPressed = true;
        });
        pause.play();
    }
    public void xPrimeButton (ActionEvent event) {
        if (!buttonPressed) {
            return;
        }
        buttonPressed = false;
        CubeRotations.wholeCubeRotation(0, 1, true, "x");
        PauseTransition pause = new PauseTransition(Duration.seconds(0.5));
        pause.setOnFinished(e -> {
            buttonPressed = true;
        });
        pause.play();
    }
    public void yButton (ActionEvent event) {
        if (!buttonPressed) {
            return;
        }
        buttonPressed = false;
        CubeRotations.wholeCubeRotation(1, 0, false, "y");
        PauseTransition pause = new PauseTransition(Duration.seconds(0.5));
        pause.setOnFinished(e -> {
            buttonPressed = true;
        });
        pause.play();
    }
    public void yPrimeButton (ActionEvent event) {
        if (!buttonPressed) {
            return;
        }
        buttonPressed = false;
        CubeRotations.wholeCubeRotation(1, 0, true, "y");
        PauseTransition pause = new PauseTransition(Duration.seconds(0.5));
        pause.setOnFinished(e -> {
            buttonPressed = true;
        });
        pause.play();
    }
}

