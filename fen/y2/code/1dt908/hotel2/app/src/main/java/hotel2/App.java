package hotel2;

import javafx.application.Application;
import javafx.stage.Stage;
import java.sql.Connection;
import java.text.ParseException;

import hotel2.com.mid.Connector;
import hotel2.GUI.SceneManager;

public class App extends Application {
    private static Connection connection;
    private static SceneManager manager;

    @Override
    public void start(Stage startStage) throws Exception {
        startStage.setFullScreen(true);
        SceneManager sceneManagerMain = new SceneManager(startStage);
        manager = sceneManagerMain;
        sceneManagerMain.switchToLoginRoot();
    }

    public static void main(String[] args) throws ParseException {
        connection = Connector.Connect();
        launch(args);
        Connector.CloseConnection(connection);

    }

    public static Connection getConn() {
        return connection;
    }

    public static SceneManager getManager() {
        return manager;
    }
}
