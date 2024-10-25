import a02.project.com.cube.RubiksCube;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.SceneAntialiasing;
import javafx.scene.layout.Background;
import javafx.scene.layout.BackgroundFill;
import javafx.scene.layout.StackPane;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

/**
 * The App class is a JavaFX application that initializes and displays a window for a Rubik's Cube simulator.
 * It extends the Application class and overrides the start method to configure and show the application window.
 */
public class App extends Application {

    /**
     * Initializes and displays the JavaFX application window.
     *
     * @param startStage The stage object representing the application window.
     * @throws Exception If an error occurs during the initialization of the window.
     */
    @Override
    public void start(Stage startStage) throws Exception {
        Parent root = FXMLLoader.load(getClass().getResource("MainPage.fxml"));

        StackPane layout = new StackPane(root);
        BackgroundFill backgroundFill = new BackgroundFill(Color.LIGHTBLUE, null, null);
        Background background = new Background(backgroundFill);
        layout.setBackground(background);
    
        Scene scene = new Scene(layout, 1000, 800, true, SceneAntialiasing.BALANCED);
    

        startStage.setResizable(false);
        startStage.setScene(scene);
        startStage.setTitle("Rubiks cube simulator");
        startStage.show();
    }

    /**
     * The main method initializes a 3D array called 'cube' with dimensions 6x3x3, 
     * and then calls the 'init' method from the 'RubiksCube' class to initialize the cube with default values. 
     * Finally, it launches the JavaFX application.
     * 
     * @param args An array of command-line arguments passed to the program.
     */
    public static void main(String[] args) {
        String[][][] cube = new String[6][3][3];
        RubiksCube.init(cube);
        launch(args);
    }
}



