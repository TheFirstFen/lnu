package a02.project.com.GUI;

import javafx.scene.shape.Rectangle;
import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.VBox;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.paint.Color;
import javafx.util.Duration;

import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import a02.project.com.cube.RubiksCube;

import java.util.ArrayList;


/**
 * The `Controller` class is a JavaFX controller class that handles the user interface and logic for a Rubik's Cube application.
 * It initializes the cube, updates the colors of the cube's faces, handles user input, and controls the timer for solving the cube.
 *
 * Fields:
 * - `Cube11` to `Cube69`: Rectangles representing the individual cubes of the Rubik's Cube.
 * - `inputField`: TextField for user input.
 * - `timer`: Label for displaying the elapsed time.
 * - `recentTime`: Label for displaying the most recent time.
 * - `bestTime`: Label for displaying the best time.
 * - `besttime`: Double variable for storing the best time.
 * - `isInit`: Boolean variable to check if the cube has been initialized.
 * - `cube3d`: 3D array of Rectangle objects representing the Rubik's Cube.
 * - `timeline`: Timeline object for controlling the timer.
 * - `seconds`: Double variable for storing the elapsed time in seconds.
 * - `test`: VBox object representing the user interface.
 */
public class Controller { 
    @FXML private Rectangle Cube11;
    @FXML private Rectangle Cube12;
    @FXML private Rectangle Cube13;
    @FXML private Rectangle Cube14;
    @FXML private Rectangle Cube15;
    @FXML private Rectangle Cube16;
    @FXML private Rectangle Cube17;
    @FXML private Rectangle Cube18;
    @FXML private Rectangle Cube19;
    @FXML private Rectangle Cube21;
    @FXML private Rectangle Cube22;
    @FXML private Rectangle Cube23;
    @FXML private Rectangle Cube24;
    @FXML private Rectangle Cube25;
    @FXML private Rectangle Cube26;
    @FXML private Rectangle Cube27;
    @FXML private Rectangle Cube28;
    @FXML private Rectangle Cube29;
    @FXML private Rectangle Cube31;
    @FXML private Rectangle Cube32;
    @FXML private Rectangle Cube33;
    @FXML private Rectangle Cube34;
    @FXML private Rectangle Cube35;
    @FXML private Rectangle Cube36;
    @FXML private Rectangle Cube37;
    @FXML private Rectangle Cube38;
    @FXML private Rectangle Cube39;
    @FXML private Rectangle Cube41;
    @FXML private Rectangle Cube42;
    @FXML private Rectangle Cube43;
    @FXML private Rectangle Cube44;
    @FXML private Rectangle Cube45;
    @FXML private Rectangle Cube46;
    @FXML private Rectangle Cube47;
    @FXML private Rectangle Cube48;
    @FXML private Rectangle Cube49;
    @FXML private Rectangle Cube51;
    @FXML private Rectangle Cube52;
    @FXML private Rectangle Cube53;
    @FXML private Rectangle Cube54;
    @FXML private Rectangle Cube55;
    @FXML private Rectangle Cube56;
    @FXML private Rectangle Cube57;
    @FXML private Rectangle Cube58;
    @FXML private Rectangle Cube59;
    @FXML private Rectangle Cube61;
    @FXML private Rectangle Cube62;
    @FXML private Rectangle Cube63;
    @FXML private Rectangle Cube64;
    @FXML private Rectangle Cube65;
    @FXML private Rectangle Cube66;
    @FXML private Rectangle Cube67;
    @FXML private Rectangle Cube68;
    @FXML private Rectangle Cube69;
    @FXML private TextField inputField;
    @FXML private Label timer;
    @FXML private Label recentTime;
    @FXML private Label bestTime;
    private static Double besttime = 0.0;
    private Boolean isInit = false;
    private static Rectangle [][][] cube3d;
    private static Timeline timeline;
    private Double seconds;
    @FXML public static VBox test;


    
    /**
     * Initializes a 3D array of Rectangle objects and assigns them to the corresponding rectangles in the JavaFX scene.
     * 
     * Inputs: None
     * 
     * Outputs: None
     */
    public void initializeCube() {
        List<Rectangle> parts = new ArrayList<>();
        parts.add(Cube11);
        parts.add(Cube12);
        parts.add(Cube13);
        parts.add(Cube14);
        parts.add(Cube15);
        parts.add(Cube16);
        parts.add(Cube17);
        parts.add(Cube18);
        parts.add(Cube19);
        parts.add(Cube21);
        parts.add(Cube22);
        parts.add(Cube23);
        parts.add(Cube24);
        parts.add(Cube25);
        parts.add(Cube26);
        parts.add(Cube27);
        parts.add(Cube28);
        parts.add(Cube29);
        parts.add(Cube31);
        parts.add(Cube32);
        parts.add(Cube33);
        parts.add(Cube34);
        parts.add(Cube35);
        parts.add(Cube36);
        parts.add(Cube37);
        parts.add(Cube38);
        parts.add(Cube39);
        parts.add(Cube41);
        parts.add(Cube42);
        parts.add(Cube43);
        parts.add(Cube44);
        parts.add(Cube45);
        parts.add(Cube46);
        parts.add(Cube47);
        parts.add(Cube48);
        parts.add(Cube49);
        parts.add(Cube61);
        parts.add(Cube62);
        parts.add(Cube63);
        parts.add(Cube64);
        parts.add(Cube65);
        parts.add(Cube66);
        parts.add(Cube67);
        parts.add(Cube68);
        parts.add(Cube69);
        parts.add(Cube51);
        parts.add(Cube52);
        parts.add(Cube53);
        parts.add(Cube54);
        parts.add(Cube55);
        parts.add(Cube56);
        parts.add(Cube57);
        parts.add(Cube58);
        parts.add(Cube59);
        cube3d = new Rectangle [6][3][3];
        Integer index = 0;
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    cube3d[i][j][k] = parts.get(index);
                    index ++;
                }
            }
        }
        isInit = true;
    }

    /**
     * Updates the colors of the rectangles in a Rubik's Cube based on the provided 3D array representation of the cube.
     *
     * @param newCube a 3D array representing the colors of the Rubik's Cube.
     */
    public static void changeFaces(String[][][] newCube) {
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    Color color = getColor(newCube[i][j][k]);
                    cube3d[i][j][k].setFill(color);
                }
            }
        }
    }

    /**
     * Maps a given color string to a corresponding JavaFX Color object.
     *
     * @param color The color string to be mapped to a Color object.
     * @return The corresponding Color object for the given color string.
     */
    private static Color getColor(String color) {
        switch (color) {
            case "\033[97m\u25A0\033[0m":
                return Color.WHITE;
            case "\033[92m\u25A0\033[0m":
                return Color.web("#1fff68");
            case "\033[31m\u25A0\033[0m":
                return Color.web("#ff1f1f");
            case "\033[94m\u25A0\033[0m":
                return Color.DODGERBLUE;
            case "\033[93m\u25A0\033[0m":
                return Color.web("#e7ff1f");
            case "\033[95m\u25A0\033[0m":
                return Color.web("#ff8e1f");
        }
        return Color.BLACK;
    }

    /**
     * Takes user input from a text field, checks if it is a valid input, and performs corresponding actions based on the input.
     * 
     * @param event The event triggered by the user's action.
     */
    public void performInput(ActionEvent event){
        String input = inputField.getText();
        if (checkInputString(input)) {
            String[] algo = input.split(" ");
            for (String a : algo) {
                switch (a) {
                    case "r":
                        rButton(event);
                        break;
                    case "r'":
                        rPrimeButton(event);
                        break;
                    case "m":
                        mButton(event);
                        break;
                    case "m'":
                        mPrimeButton(event);
                        break;
                    case "l":
                        lButton(event);
                        break;
                    case "l'":
                        lPrimeButton(event);
                        break;
                    case "f":
                        fButton(event);
                        break;
                    case "f'":
                        fPrimeButton(event);
                        break;
                    case "u":
                        uButton(event);
                        break;
                    case "u'":
                        uPrimeButton(event);
                        break;
                    case "d":
                        dButton(event);
                        break;
                    case "d'":
                        dPrimeButton(event);
                        break;
                    case "x":
                        xButton(event);
                        break;
                    case "x'":
                        xPrimeButton(event);
                        break;
                    case "y":
                        yButton(event);
                        break;
                    case "y'":
                        yPrimeButton(event);
                        break;
                    default:
                        Alert alert = new Alert(AlertType.ERROR);
                        alert.setTitle("Invalid Input");
                        alert.setHeaderText(null);
                        alert.setContentText("Please provide a valid input separated by whitespace!");
                        alert.showAndWait(); 
                        break;
                    }
                
                }
            } else {
                Alert alert = new Alert(AlertType.ERROR);
                alert.setTitle("Invalid Input");
                alert.setHeaderText(null);
                alert.setContentText("Please provide a valid input separated by whitespace!");
                alert.showAndWait(); 
        }
    
    }
    /**
     * Checks if a given input string is valid according to give instructions.
     *
     * @param input The input string to be checked for validity.
     * @return True if the input string is valid, false otherwise.
     */
    public static boolean checkInputString(String input) {
        if (!input.matches("^[udfrlmxyUDFRLMXY\\s']+$")) {
            return false;
        }

        Pattern pattern = Pattern.compile("^[udfrlmxyUDFRLMXY\\s']*");
        Matcher matcher = pattern.matcher(input);

        return matcher.matches();
    }

    
    /**
     * Initializes the Rubik's Cube, generates a random scramble sequence of 80 moves, and updates the colors of the cube's faces accordingly.
     *
     * @param event The event triggered by clicking the scramble button.
     */
    public void scrambleButton(ActionEvent event) {
        if (!isInit) {
            initializeCube();
        }
        String[][][] newCube = RubiksCube.mainLoop("sc");
        changeFaces(newCube);
    }
    /**
     * Calls the mainLoop("solve") method from the RubiksCube class to solve the cube.
     * Finally, it updates the faces of the cube with the solved configuration.
     * 
     * @param event The event object representing the button click.
     */
    public void solveButton(ActionEvent event) {
        if (!isInit) {
            initializeCube();
        }
        String[][][] newCube = RubiksCube.mainLoop("solve");
        changeFaces(newCube);
    }
    /**
     * Handles the event when a key is pressed.
     * If the pressed key is the space key, it checks if a timeline is currently running.
     * If a timeline is running, it stops the timer and resets it.
     * If a timeline is not running, it starts the timer.
     *
     * @param key The key event object that represents the key press event.
     */
    public void keyPressed(KeyEvent key) {
        if (key.getCode().equals(KeyCode.SPACE)) {
            if (timeline != null) {
                stopTimer();
                reset();
            } else {
                start(null);
            }
        }
    }
    /**
     * Starts a timer when a button is clicked. Initializes a timeline and updates a label with the elapsed time.
     * 
     * @param eventt The event object representing the button click.
     */
    public void start(ActionEvent eventt) {
        if (timeline == null) {
            seconds = 0.0;

            timeline = new Timeline(new KeyFrame(Duration.millis(10), event -> {
                seconds += 0.01;
                timer.setText(String.format("%.2f", seconds));
            }));

            timeline.setCycleCount(Timeline.INDEFINITE);

            timeline.play();
        }
    }
    /**
     * Resets the timer in the Rubik's Cube application.
     */
    public void reset() {
        timeline.stop();
        timeline = null;
        seconds = 0.0;
        timer.setText("0,00");
    }

    /**
     * Stops the timer, updates the best time if the current time is better, and displays the recent time.
     */
    public void stopTimer() {
        if (timeline != null) {
            if (seconds < besttime || besttime == 0.0){
                besttime = seconds;
                bestTime.setText(String.format("%.2f", seconds));
            }
            recentTime.setText(String.format("%.2f", seconds));
            timeline.stop();
            timeline = null;
        }
    }
    /**
     * Starts or stops a timer based on its current state.
     * If the timer is already running, it will be stopped and reset.
     * If the timer is not running, it will be started.
     *
     * @param event The event object representing the button click.
     */
    public void startTButton(ActionEvent event) {
        if (timeline != null) {
            stopTimer();
            reset();
        } else {
            start(null);
        }  
    }
    /**
     * Resets the best time record to 0.0 and updates the corresponding label on the user interface.
     * 
     * @param event The event object representing the button click.
     */
    public void resetRecordButton(ActionEvent event) {
        besttime = 0.0;
        bestTime.setText("0,00");
    }
    /**
     * Handles the action event when the "r" button is clicked.
     *
     * @param event The event object representing the button click.
     */
    public void rButton (ActionEvent event) {
        if (!isInit) {
            initializeCube();
        }
        String [][][] newCube = RubiksCube.mainLoop("R");
        changeFaces(newCube);
    }
    /**
     * Handles the action event when the "r'" button is clicked.
     *
     * @param event The event object representing the button click.
     */
    public void rPrimeButton (ActionEvent event) {
        if (!isInit) {
            initializeCube();
        }
        String [][][] newCube = RubiksCube.mainLoop("r");
        changeFaces(newCube);
    }
    /**
     * Handles the action event when the "m" button is clicked.
     *
     * @param event The event object representing the button click.
     */
    public void mButton (ActionEvent event) {
        if (!isInit) {
            initializeCube();
        }
        String [][][] newCube = RubiksCube.mainLoop("r");
        newCube = RubiksCube.mainLoop("L");
        newCube = RubiksCube.mainLoop("Y");
        changeFaces(newCube);
    }
    /**
     * Handles the action event when the "m'" button is clicked.
     *
     * @param event The event object representing the button click.
     */
    public void mPrimeButton (ActionEvent event) {
        if (!isInit) {
            initializeCube();
        }
        String [][][] newCube = RubiksCube.mainLoop("R");
        newCube = RubiksCube.mainLoop("l");
        newCube = RubiksCube.mainLoop("y");
        changeFaces(newCube);
    }
    /**
     * Handles the action event when the "l" button is clicked.
     *
     * @param event The event object representing the button click.
     */
    public void lButton (ActionEvent event) {
        if (!isInit) {
            initializeCube();
        }
        String [][][] newCube = RubiksCube.mainLoop("L");
        changeFaces(newCube);
    }
    /**
     * Handles the action event when the "l'" button is clicked.
     *
     * @param event The event object representing the button click.
     */
    public void lPrimeButton (ActionEvent event) {
        if (!isInit) {
            initializeCube();
        }
        String [][][] newCube = RubiksCube.mainLoop("l");
        changeFaces(newCube);
    }
    
    /**
     * Handles the action event when the "f" button is clicked.
     *
     * @param event The event object representing the button click.
     */
    public void fButton (ActionEvent event) {
        if (!isInit) {
            initializeCube();
        }
        String [][][] newCube = RubiksCube.mainLoop("F");
        changeFaces(newCube);
    }
    
    /**
     * Handles the action event when the "f'" button is clicked.
     *
     * @param event The event object representing the button click.
     */
    public void fPrimeButton (ActionEvent event) {
        if (!isInit) {
            initializeCube();
        }
        String [][][] newCube = RubiksCube.mainLoop("f");
        changeFaces(newCube);
    }
    /**
     * Handles the action event when the "d" button is clicked.
     *
     * @param event The event object representing the button click.
     */
    public void dButton (ActionEvent event) {
        if (!isInit) {
            initializeCube();
        }
        String [][][] newCube = RubiksCube.mainLoop("D");
        changeFaces(newCube);
    }
    
    /**
     * Handles the action event when the "d'" button is clicked.
     *
     * @param event The event object representing the button click.
     */
    public void dPrimeButton (ActionEvent event) {
        if (!isInit) {
            initializeCube();
        }
        String [][][] newCube = RubiksCube.mainLoop("d");
        changeFaces(newCube);
    }
    /**
     * Handles the action event when the "u" button is clicked.
     *
     * @param event The event object representing the button click.
     */
    public void uButton (ActionEvent event) {
        if (!isInit) {
            initializeCube();
        }
        String [][][] newCube = RubiksCube.mainLoop("U");
        changeFaces(newCube);
    }
    
    /**
     * Handles the action event when the "u'" button is clicked.
     *
     * @param event The event object representing the button click.
     */
    public void uPrimeButton (ActionEvent event) {
        if (!isInit) {
            initializeCube();
        }
        String [][][] newCube = RubiksCube.mainLoop("u");
        changeFaces(newCube);
    }
    
    /**
     * Handles the action event when the "x" button is clicked.
     *
     * @param event The event object representing the button click.
     */
    public void xButton (ActionEvent event) {
        if (!isInit) {
            initializeCube();
        }
        String [][][] newCube = RubiksCube.mainLoop("X");
        changeFaces(newCube);
    }
    /**
     * Handles the action event when the "x'" button is clicked.
     *
     * @param event The event object representing the button click.
     */
    public void xPrimeButton(ActionEvent event) {
        if (!isInit) {
            initializeCube();
        }
        String[][][] newCube = RubiksCube.mainLoop("x");
        changeFaces(newCube);
    }
    /**
     * Handles the action event when the "y" button is clicked.
     * 
     * @param event The event object representing the button click.
     */
    public void yButton(ActionEvent event) {
        if (!isInit) {
            initializeCube();
        }
        String[][][] newCube = RubiksCube.mainLoop("Y");
        changeFaces(newCube);
    }
    /**
     * Handles the action event when the "y'" button is clicked.
     *
     * @param event The event object representing the button click.
     */
    public void yPrimeButton(ActionEvent event) {
        if (!isInit) {
            initializeCube();
        }
        String[][][] newCube = RubiksCube.mainLoop("y");
        changeFaces(newCube);
    }

}

