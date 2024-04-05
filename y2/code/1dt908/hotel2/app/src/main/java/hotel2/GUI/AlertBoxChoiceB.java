package hotel2.GUI;

import javafx.fxml.FXML;
import javafx.scene.control.Label;

public class AlertBoxChoiceB {
    private SceneManager sceneManager;

    @FXML Label titleLabel;
    @FXML Label descriptionLabel;
    private String id;

    public void setManager(SceneManager manager) {
        sceneManager = manager;
    }

    public void setup(String title, String desc, String i) {
        id = i;
        titleLabel.setText(title);
        descriptionLabel.setText(desc);
    }
    public void moveOnButton() {
        sceneManager.closeCurrentPopup();
        sceneManager.switchToHandleRoomRoot(id);
    }
    public void closeAlertButton() {
        sceneManager.closeCurrentPopup();
    }
}
