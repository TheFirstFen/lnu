package a02.project.com.GUI;

import java.io.IOException;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.stage.Stage;

public class Controller {
@FXML
private Button button;

public void handleStartButtonAction(ActionEvent event) {
    Parent newNode = null;
    try {
        newNode = FXMLLoader.load(getClass().getResource("/MainPage.fxml"));
    } catch (IOException e) {
        e.printStackTrace();
    }

     if (newNode != null) {
        Scene scene = new Scene(newNode);
        Stage stage = (Stage) ((Node) event.getSource()).getScene().getWindow();
        stage.setScene(scene);
        stage.show();
    }
}
}
