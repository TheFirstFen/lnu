package hotel2.GUI;

import hotel2.App;
import hotel2.com.mid.Loggin;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;

public class LoginController {
    @FXML private TextField usernameInField;
    @FXML private TextField passwordInField;
    @FXML private Button loginBbutton;
    private String[] logininfo;
    private SceneManager sceneManager;
    public void setManager(SceneManager manager) {
        sceneManager = manager;
    }

    public void setFocus() {
        usernameInField.requestFocus();
        usernameInField.setOnKeyPressed(event -> handleTabTraversal(event, passwordInField));
        passwordInField.setOnKeyPressed(event -> handleTabTraversalToButton(event, loginBbutton));
        loginBbutton.setOnKeyPressed(event -> handleTabTraversal(event, usernameInField));
        loginBbutton.setOnKeyPressed(event -> handleEnterOnLogin(event));
    }
    private void handleTabTraversal(KeyEvent event, TextField nextField) {
        if (event.getCode() == KeyCode.TAB) {
            nextField.requestFocus();
            event.consume();
        }
    }
    private void handleTabTraversalToButton(KeyEvent event, Button nextField) {
        if (event.getCode() == KeyCode.TAB) {
            nextField.requestFocus();
            event.consume();
        }
    }
    private void handleEnterOnLogin(KeyEvent event) {
        if (event.getCode() == KeyCode.ENTER) {
            loginButton(null);
            event.consume();
        }
    }

    public void reset() {
        usernameInField.clear();
        passwordInField.clear();
    }
    public void loginButton(ActionEvent event) {
        logininfo = new String[3];
        String[] info = {usernameInField.getText(), passwordInField.getText()};
        logininfo = Loggin.main(App.getConn(), info);
        if (logininfo[0] == "1") {
            logininfo[0] = usernameInField.getText();
            sceneManager.setInfo(logininfo);
            sceneManager.switchToHomeRoot();
        } else {
            sceneManager.ShowAlert("Felaktig information", "Uppgifterna matchar ej någon användare, var snäll fyll i korrekta uppgifter.");
        }
    }
    public void closeProgram() {
        System.exit(0);
    }
}
