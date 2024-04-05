package com.sb224sc.rubik;

import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.SubScene;
import javafx.scene.SceneAntialiasing;
import javafx.scene.PerspectiveCamera;
import javafx.scene.paint.Color;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.VBox;
import javafx.scene.canvas.*;
import javafx.scene.control.Alert;
import javafx.scene.control.TextInputDialog;
import javafx.animation.*;
import javafx.scene.text.Font;
import javafx.scene.image.Image;
import javafx.scene.text.TextAlignment;
import javafx.util.Duration;
import java.util.*;
import java.security.SecureRandom;
import javafx.geometry.Rectangle2D;
import javafx.geometry.Insets;

import javafx.scene.paint.PhongMaterial;
import javafx.scene.shape.Box;
import javafx.scene.Group;
import javafx.scene.transform.Rotate;

import com.sb224sc.rubik.model.Cube;
import com.sb224sc.rubik.model.CubeSolver;
import com.sb224sc.rubik.model.Move;

public class MainApplication extends Application {
    private SecureRandom rnd = new SecureRandom();
    private int tabSelected;
    public static boolean clickAllowed = true;
    private List<Move.Wrapper> moves = new ArrayList<>();
    Cube cube;

    private static final Rectangle2D bounds = new Rectangle2D(0, 0, 420, 740);

    // Camera
    private static double cameraX = -110;
    private static final double CAMERA_Y = -200;
    private static double cameraZ = -350;

    // Colour scheames
    private static final String TEXT_FONT = "sans-serif";
    private static final String SELECTED_TAB_COLOR = "#10F267";
    private static final String BUTTON_COLOR = "#1E6D3D";

    // Camera rotation
    private double mouseOldX;
    private double mouseOldY;
    private int rx;
    private int ry;
    private int rz;

    public static void main(String[] args) {
        launch(args);
    }

    /**
     * Starts the specified stage and initializes the Rubik's cube application.
     *
     * @param stage the stage to start the application on
     */
    @Override
    public void start(Stage stage) {
        cube = new Cube();

        PerspectiveCamera camera = new PerspectiveCamera(false);
        camera.setTranslateX(cameraX);
        camera.setTranslateY(CAMERA_Y);
        camera.setTranslateZ(cameraZ);

        // Axis are used for debugging
        Box xAxis = new Box(600, 3, 3);
        xAxis.setMaterial(new PhongMaterial(Color.RED));
        xAxis.setTranslateX(300);
        Box yAxis = new Box(3, 600, 3);
        yAxis.setMaterial(new PhongMaterial(Color.BLUE));
        yAxis.setTranslateY(300);
        Box zAxis = new Box(3, 3, 600);
        zAxis.setMaterial(new PhongMaterial(Color.GREEN));
        zAxis.setTranslateZ(300);

        StackPane controls = new StackPane();
        StackPane stackPane = new StackPane();

        SubScene scene = new SubScene(new Group(cube.getModel()), bounds.getWidth() - 10, bounds.getHeight() * 0.65,
                true, SceneAntialiasing.BALANCED);
        scene.setFocusTraversable(true);
        scene.setFill(Color.CYAN);
        scene.setCamera(camera);

        Canvas onScene = new Canvas(scene.getWidth(), scene.getHeight());
        onScene.setFocusTraversable(true);
        GraphicsContext layer = onScene.getGraphicsContext2D();
        stackPane.getChildren().addAll(scene, onScene);

        Canvas canvas = new Canvas(scene.getWidth(), bounds.getHeight() * 0.33);
        canvas.setOnMousePressed(mouse -> {
            if (!clickAllowed)
                return;

            if ((new Rectangle2D(0, 0, canvas.getWidth() / 2, 35)).contains(mouse.getX(), mouse.getY())) {
                tabSelected = 0;
            } else if ((new Rectangle2D(canvas.getWidth() / 2, 0, canvas.getWidth() / 2, 35)).contains(mouse.getX(),
                    mouse.getY())) {
                tabSelected = 1;
            }

            if (tabSelected == 0) {
                int selectedX = -1;
                int selectedY = -1;

                for (int i = 0; i < 7; i++) {
                    for (int j = 0; j < 3; j++) {
                        if ((new Rectangle2D((canvas.getWidth() - (7 * 40 + 6 * 15)) / 2 + i * (40 + 15),
                                50.0 + j * (40 + 15), 40, 40)).contains(mouse.getX(), mouse.getY())) {
                            selectedX = i;
                            selectedY = j;
                            break;
                        }
                    }
                }

                if (selectedX != -1 && selectedY != -1) {
                    if (selectedY == 0) {
                        if (selectedX == 0)
                            Move.applyMove("F", cube);
                        else if (selectedX == 1)
                            Move.applyMove("f", cube);
                        else if (selectedX == 2)
                            Move.applyMove("B", cube);
                        else if (selectedX == 3)
                            Move.applyMove("b", cube);
                        else if (selectedX == 4)
                            Move.applyMove("R", cube);
                        else if (selectedX == 5)
                            Move.applyMove("r", cube);
                        else if (selectedX == 6)
                            Move.applyMove("L", cube);
                    } else if (selectedY == 1) {
                        if (selectedX == 0)
                            Move.applyMove("l", cube);
                        else if (selectedX == 1)
                            Move.applyMove("U", cube);
                        else if (selectedX == 2)
                            Move.applyMove("u", cube);
                        else if (selectedX == 3)
                            Move.applyMove("D", cube);
                        else if (selectedX == 4)
                            Move.applyMove("d", cube);
                        else if (selectedX == 5)
                            Move.applyMove("M", cube);
                        else if (selectedX == 6)
                            Move.applyMove("m", cube);
                    } else if (selectedY == 2) {
                        if (selectedX == 0)
                            Move.applyMove("E", cube);
                        else if (selectedX == 1)
                            Move.applyMove("e", cube);
                        else if (selectedX == 2)
                            Move.applyMove("S", cube);
                        else if (selectedX == 3)
                            Move.applyMove("s", cube);
                        else if (selectedX == 4)
                            cube.rotateCubeY(1);
                        else if (selectedX == 5)
                            cube.rotateCubeY(-1);
                        else if (selectedX == 6) {
                            cube.generateCube();
                            scene.setRoot(new Group(cube.getModel()));
                            cube.getRotateX().setAngle(45);
                            cube.getRotateY().setAngle(-45);
                            cube.getRotateZ().setAngle(0);
                            camera.getTransforms().clear();
                        }
                    }
                }
            } else if (tabSelected == 1) {
                if ((new Rectangle2D(30, 60, 120, 40)).contains(mouse.getX(), mouse.getY())) {
                    moves.clear();

                    new Thread(() -> {
                        clickAllowed = false;
                        for (int i = 0; i < Cube.SCRAMBLE_MOVES; i++) {
                            moves.add(Move.randomMove(rnd, cube));
                            while (Move.animating) {
                                try {
                                    Thread.sleep(100);
                                } catch (InterruptedException ex) {
                                    ex.getMessage();
                                    Thread.currentThread().interrupt();
                                }
                            }
                        }
                        clickAllowed = true;
                    }).start();
                } else if ((new Rectangle2D(30, 120, 120, 40)).contains(mouse.getX(), mouse.getY())) {
                    if (Cube.cubeSize == 3) {
                        moves.clear();

                        do {
                            cube.solve();
                        } while (!CubeSolver.cubeIsSolved());

                        System.out.println("Solved\n");

                    } else {
                        Alert alert = new Alert(Alert.AlertType.INFORMATION);
                        alert.setTitle("Algorithm");
                        alert.setHeaderText("Solving algorithm");
                        alert.showAndWait();
                    }
                } else if ((new Rectangle2D(30, 180, 120, 40)).contains(mouse.getX(), mouse.getY())) {
                    Alert alert = new Alert(Alert.AlertType.INFORMATION);
                    alert.setTitle("Algorithm");
                    alert.setHeaderText("Solving algorithm");
                    alert.setContentText(
                            cube.solvingAlgorithm == null ? "Please solve the cube before" : cube.solvingAlgorithm);
                    alert.showAndWait();
                } else if ((new Rectangle2D(170, 60, 120, 40)).contains(mouse.getX(), mouse.getY())) {
                    String text = askInput("Enter algorithm", "Enter algorithm");
                    new Thread(() -> {
                        String strMoves = Move.parseNotation(text);
                        if (strMoves == null)
                            return;
                        clickAllowed = false;
                        for (char c : strMoves.toCharArray()) {
                            Move.applyMove(Character.toString(c), cube);
                            while (Move.animating) {
                                try {
                                    Thread.sleep(100);
                                } catch (InterruptedException ex) {
                                    ex.getMessage();
                                    Thread.currentThread().interrupt();
                                }
                            }
                        }
                        clickAllowed = true;
                    }).start();
                }

                int selected = -1;
                for (int i = 0; i < 4; i++) {
                    if ((new Rectangle2D(canvas.getWidth() - 65, 50.0 + i * (35 + 15), 35, 35)).contains(mouse.getX(),
                            mouse.getY())) {
                        selected = i;
                        break;
                    }
                }

                if (selected != -1) {
                    switch (selected) {
                        case 0:
                            Cube.defaultDuration = 240;
                            break;
                        case 1:
                            Cube.defaultDuration = 180;
                            break;
                        case 2:
                            Cube.defaultDuration = 120;
                            break;
                        case 3:
                            Cube.defaultDuration = 60;
                            break;
                        default:
                            break;
                    }
                    Cube.moveDuration = Cube.defaultDuration;
                }
            }
        });

        controls.getChildren().add(canvas);
        GraphicsContext gc = canvas.getGraphicsContext2D();

        Timeline loop = new Timeline(new KeyFrame(Duration.millis(1000.0 / 40), mouse -> update(gc, layer)));
        loop.setCycleCount(Animation.INDEFINITE);
        loop.play();

        onScene.setOnMousePressed(event -> {
            mouseOldX = event.getSceneX();
            mouseOldY = event.getSceneY();
        });

        onScene.setOnMouseDragged(event -> {
            double rotX = event.getSceneY() - mouseOldY;
            double rotY = event.getSceneX() - mouseOldX;
            this.rx -= rotX;
            this.ry += rotY;
            camera.getTransforms()
                    .addAll(new Rotate(-rotX, (Cube.cubeSize / 2.0 + 0.5 - 1) * 100 - cameraX,
                            (Cube.cubeSize / 2.0 + 0.5 - 1) * 100 - CAMERA_Y,
                            (Cube.cubeSize / 2.0 + 0.5 - 1) * 100 - cameraZ,
                            Rotate.X_AXIS),
                            new Rotate(rotY, (Cube.cubeSize / 2.0 + 0.5 - 1) * 100 - cameraX,
                                    (Cube.cubeSize / 2.0 + 0.5 - 1) * 100 - CAMERA_Y,
                                    (Cube.cubeSize / 2.0 + 0.5 - 1) * 100 - cameraZ, Rotate.Y_AXIS));
            mouseOldX = event.getSceneX();
            mouseOldY = event.getSceneY();
        });

        onScene.setOnScroll(mouse -> {
            camera.getTransforms().clear();
            if (mouse.getDeltaY() > 0) {
                cameraZ = camera.getTranslateZ() + 50;
            } else if (mouse.getDeltaY() < 0) {
                cameraZ = camera.getTranslateZ() - 50;
            }
            camera.setTranslateZ(cameraZ);
        });

        VBox layout = new VBox(stackPane, controls);
        layout.setSpacing(10);
        layout.setPadding(new Insets(5, 5, 5, 5));

        stage.setScene(new Scene(layout, bounds.getWidth(), bounds.getHeight()));
        stage.setTitle("Rubik's cube");
        stage.getIcons().add(new Image(getClass().getResourceAsStream("/icon.png")));
        stage.show();
    }

    /**
     * Updates the graphics context
     *
     * @param gc    the main graphics context
     * @param layer the graphics context for the layer
     */
    private void update(GraphicsContext gc, GraphicsContext layer) {
        layer.clearRect(0, 0, layer.getCanvas().getWidth(), layer.getCanvas().getHeight());
        layer.setFill(Color.BLACK);
        layer.fillText(String.format("Current move: %s%nMove duration: %d%nCube size: %s",
                Move.printAlgorithm(Move.currentMove), Cube.defaultDuration,
                Cube.cubeSize + "x" + Cube.cubeSize + "x" + Cube.cubeSize), 20, 20);

        double width = gc.getCanvas().getWidth();
        double height = gc.getCanvas().getHeight();

        gc.setFont(new Font(TEXT_FONT, 20));
        gc.clearRect(0, 0, width, height);
        gc.setFill(Color.web("#36B367"));
        gc.fillRect(0, 0, width, height);
        gc.setFill(tabSelected == 0 ? Color.web(SELECTED_TAB_COLOR) : Color.web("#5B956F"));
        gc.fillRect(0, 0, width / 2, 35);
        gc.setFill(Color.BLACK);
        gc.fillText("Manual input", 100, 25);
        gc.setFill(tabSelected == 1 ? Color.web(SELECTED_TAB_COLOR) : Color.web("#5B956E"));
        gc.fillRect(width / 2, 0, width / 2, 35);
        gc.setFill(Color.BLACK);
        gc.fillText("Options", 310, 25);
        gc.setFont(new Font(TEXT_FONT, 25));
        gc.setTextAlign(TextAlignment.CENTER);

        String[][] texts = new String[][] { { "F", "F'", "B", "B'", "R", "R'", "L" },
                { "L'", "U", "U'", "D", "D'", "M", "M'" },
                { "E", "E'", "S", "S'", "Y", "Y'", "Rs" } };
        String[] speeds = new String[] { "<<", "<", ">", ">>" };

        if (tabSelected == 0) {
            for (int i = 0; i < 7; i++) {
                for (int j = 0; j < 3; j++) {
                    gc.setFill(Color.web(BUTTON_COLOR));
                    double x = (width - (7 * 40 + 6 * 15)) / 2 + i * (40 + 15);
                    double y = 50.0 + j * (40 + 15);
                    gc.fillRect(x, y, 40, 40);
                    gc.setFill(Color.BLACK);
                    gc.fillText(texts[j][i], x + 40.0 / 2, y + 40.0 / 2 + 8);
                }
            }
        } else if (tabSelected == 1) {
            gc.setTextAlign(TextAlignment.LEFT);
            gc.setFill(Color.web(BUTTON_COLOR));
            gc.fillRect(30, 60, 120, 40);
            gc.fillRect(30, 120, 120, 40);
            gc.fillRect(30, 180, 120, 40);
            gc.fillRect(170, 60, 120, 40);
            gc.setFont(new Font(TEXT_FONT, 20));
            gc.setFill(Color.BLACK);
            gc.fillText("Scramble", 35, 85);
            gc.fillText("Solve", 35, 145);
            gc.fillText("Solving Alg.", 35, 205);
            gc.fillText("Input", 175, 85);
            gc.setTextAlign(TextAlignment.CENTER);

            for (int i = 0; i < 4; i++) {
                double x = width - 65;
                double y = 50.0 + i * (35 + 15);
                gc.setFill(Color.web(BUTTON_COLOR));
                gc.fillRect(x, y, 35, 35);
                gc.setFill(Color.BLACK);
                gc.fillText(speeds[i], x + 35.0 / 2, y + 35.0 / 2 + 5);
            }
        }

        if (!clickAllowed) {
            gc.save();
            gc.setGlobalAlpha(0.6);
            gc.setFill(Color.BLACK);
            gc.fillRect(0, 0, width, height);
            gc.restore();
        }
    }

    /**
     * A method to ask for user input with a dialog box.
     *
     * @param title   the title of the dialog box
     * @param message the message to be displayed in the dialog box
     * @return the input provided by the user
     */
    private static String askInput(String title, String message) {
        TextInputDialog dialog = new TextInputDialog();
        dialog.setTitle(title);
        dialog.setHeaderText(message);
        dialog.showAndWait();
        return dialog.getEditor().getText();
    }
}
