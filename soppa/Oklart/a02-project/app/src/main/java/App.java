import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class App extends Application {

    @Override
    public void start(Stage mainStage) throws Exception {
        Parent root = FXMLLoader.load(getClass().getResource("NewStartPage.fxml"));
        mainStage.setTitle("FXML Viewer");
        mainStage.setScene(new Scene(root, 300, 275));
        mainStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}