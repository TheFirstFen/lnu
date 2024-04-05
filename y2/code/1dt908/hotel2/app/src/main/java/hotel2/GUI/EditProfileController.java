package hotel2.GUI;

import hotel2.App;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import hotel2.com.mid.Worker;

public class EditProfileController {
    @FXML
    Button returnButton;
    @FXML
    AnchorPane MainAnchorpane;
    @FXML
    Label currentLogin;
    @FXML
    TextField userName;
    @FXML
    TextField userMail;

    @FXML
    PasswordField userPassword;

    private SceneManager sceneManager;

    public void setManager(SceneManager manager) {
        sceneManager = manager;
    }
    
    public void init(){
        String[] loginInfo = sceneManager.getLoginInfo();
        String userID = loginInfo[1];
    
        String[] searchInfo = {"id", userID};
        String[][] userInfo = Worker.checkALLWorkers(App.getConn(), searchInfo);
        if(userInfo != null && userInfo.length > 0) {
            userName.setText(userInfo[0][1]);
            userMail.setText(userInfo[0][2]);
        }
    }
    
    public void backButton() {
        sceneManager.switchToHomeRoot();
    }
    public void updateUser() {
        // behöver hämta id från current logged in
        String[] loginInfo = sceneManager.getLoginInfo();
        String userID = loginInfo[1];

        String[] searchInfo = {"id", userID};
        String[][] userInfo = Worker.checkALLWorkers(App.getConn(), searchInfo);
        // namn epost och lösenord
        String updatedName = userName.getText();
        String updatedMail = userMail.getText();
        String updatedPassword = userPassword.getText();
        if (updatedName.isEmpty() || updatedMail.isEmpty() || updatedPassword.isEmpty()) {
            sceneManager.ShowAlert("Error", "Please fill in all fields.");
            return; // Exit the method without attempting to update
        }
        String[] updUserInfo = {
            updatedName,
            updatedMail, userInfo[0][3],
            userInfo[0][4],
            updatedPassword,
            userID, userInfo[0][5]
        };
        boolean updated = Worker.checkUppdateWorker(App.getConn(), updUserInfo);
        if(updated) {
            sceneManager.ShowAlert("Success", "Profile edited");
        } else {
            sceneManager.ShowAlert("Fail", "Profile not edited!");
        }
    }

}
