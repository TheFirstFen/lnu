package hotel2.GUI;

import java.io.IOException;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.control.Button;
import javafx.scene.layout.AnchorPane;

public class AdminController {
    @FXML Button returnButton;
    @FXML AnchorPane MainAnchorpane;
    @FXML AnchorPane SecondaryAnchorpane;

    private SceneManager sceneManager;

    public void setManager(SceneManager manager) {
        sceneManager = manager;
    }

    @FXML
    public void backButton() {
        sceneManager.switchToHomeRoot();
    }

    @FXML
    public void manageRoomButton() {

        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/AdminPageManageRoom.fxml"));
            AnchorPane page = loader.load();
            AdminRoomController roomController = loader.getController();
            roomController.setManager(sceneManager);
            SecondaryAnchorpane.getChildren().setAll(page);
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
    @FXML
    public void initialize() {

        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/AdminPageManageRoom.fxml"));
            AnchorPane page = loader.load();
            AdminRoomController roomController = loader.getController();
            roomController.setManager(sceneManager);
            SecondaryAnchorpane.getChildren().setAll(page);
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    @FXML
    public void manageUsersButton() {
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/AdminPageManageUser.fxml"));
            AnchorPane page = loader.load();
            AdminUserController userController = loader.getController();
            userController.setManager(sceneManager);
            SecondaryAnchorpane.getChildren().setAll(page);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
