package hotel2.GUI;

import javafx.fxml.FXML;
import javafx.scene.control.Label;

public class AlertController {
    private SceneManager sceneManager;

    @FXML Label titleLabel;
    @FXML Label descriptionLabel;

    public void setManager(SceneManager manager) {
        sceneManager = manager;
    }

    public void setup(String title, String desc) {
        titleLabel.setText(title);
        descriptionLabel.setText(desc);
    }

    public void doneButton() {
        sceneManager.closeCurrentPopup();
    }
}
