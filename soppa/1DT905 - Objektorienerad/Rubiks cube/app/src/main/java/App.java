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
import java.util.Scanner;

public class App extends Application {

    @Override
    public void start(Stage startStage) throws Exception {
        Parent root = FXMLLoader.load(getClass().getResource("StartPage.fxml"));

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

    public static void main(String[] args) {
        launch(args);
        Scanner scanner = new Scanner(System.in);
        //while(true){
        //    System.out.println("In what dimension whould you like to have the cube in: 2D/3D/q/Q");
        //    String choice = scanner.nextLine();
        //    if (choice.equals("2D")){
        //        RubiksCube.main(args, scanner);
        //    }
        //    else if (choice.equalsIgnoreCase("3D")){
        //        launch(args);
        //    }
        //    else if (choice.equals("q")||choice.equals("Q")){
        //        scanner.close();
        //        System.exit(0);
        //    }
        //    else{
        //        System.out.println("Input did not match, try ether 2D/3D/q/Q");
        //    }            
        //}
    }
}


