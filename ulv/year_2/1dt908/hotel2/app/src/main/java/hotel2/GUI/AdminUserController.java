package hotel2.GUI;

import java.util.Arrays;

import javafx.fxml.FXML;
import javafx.geometry.Pos;
import javafx.scene.control.*;
import javafx.scene.layout.VBox;
import hotel2.com.mid.Worker;
import hotel2.App;
import javafx.scene.control.Alert.AlertType;


public class AdminUserController {
    @FXML TextField userName;
    @FXML Button resetFields;
    @FXML Button updateButton;
    @FXML Button deleteButton;
    @FXML Button createButton;
    @FXML TextField userMail;
    @FXML TextField userPhone;
    @FXML TextField userLocation;
    @FXML ChoiceBox<String> userType;
    @FXML ChoiceBox<String> searchFor;
    @FXML PasswordField userPassword;
    @FXML TextField searchUser;
    @FXML ScrollPane userList;
    @FXML Label userID;

    private SceneManager sceneManager;
    private String selectedUserID;

    @FXML
    public void initialize() {

        initializeRoomTypeChoices();
        updateButton.setDisable(true);
        deleteButton.setDisable(true);
    }

    public void setManager(SceneManager manager) {
        sceneManager = manager;
    }

    private void initializeRoomTypeChoices() {
        userType.getItems().setAll("Admin", "Worker");
        userType.setValue("Worker"); // Set default value if needed
        searchFor.getItems().setAll("Name", "Email");
        searchFor.setValue("Name");
    }

    public void handleSearchUser() {
        String search = searchFor.getSelectionModel().getSelectedItem();
        String info = searchUser.getText();
        String[] searchFor = new String[2];
        searchFor[0] = search;
        searchFor[1] = info;
        String[][] userInfo = Worker.checkALLWorkers(App.getConn(), searchFor);
        displayUsers(userInfo);
    }

    public void displayUsers(String[][] userInfo) {
        VBox buttonBox = new VBox();
        String userRole;

        for (int i = 0; i < userInfo.length; i++) {
            if (userInfo[i][4].equals("1") || userInfo[i][4].equals("Admin")) {
                userRole = "Admin"; 
            } else {
                userRole = "Worker";
            }
            Button tempButton = new Button(userInfo[i][1] + " | " + userInfo[i][2] + " | " + userRole);
            double width = userList.getWidth();
            tempButton.setPrefWidth(width - 20);
            tempButton.setPrefHeight(50);
            tempButton.getStyleClass().add("temp-button");
            tempButton.getStylesheets().add(getClass().getResource("/css/tempButton.css").toExternalForm());
            tempButton.setAlignment(Pos.BASELINE_LEFT);
            tempButton.setContentDisplay(ContentDisplay.LEFT);
            String[] selectedUser = userInfo[i];
            tempButton.setOnAction(event -> displayUserInfo(selectedUser));
            buttonBox.getChildren().add(tempButton);
        }
        userList.setContent(buttonBox);
    }

    public void displayUserInfo(String[] selectedUser) {
        updateButton.setDisable(false);
        deleteButton.setDisable(false);
        createButton.setDisable(true);
        String userRoleChoice;
        selectedUserID = selectedUser[0];
        if (selectedUser[4].equals("1") || selectedUser[4].equals("Admin")) {
            userRoleChoice = "Admin";
        } else {
            userRoleChoice = "Worker";
        }
        userType.getItems().setAll("Admin", "Worker");
        userID.setText(selectedUser[0]);
        userName.setText(selectedUser[1]);
        userMail.setText(selectedUser[2]);
        userPhone.setText(selectedUser[3]);
        userType.getSelectionModel().select(userRoleChoice);
        userLocation.setText(selectedUser[5]);

    }
    public void handleCreateUser() {
        String createUserRole;
        String createUserName = userName.getText();
        String createUserMail = userMail.getText();
        String createUserPhone = userPhone.getText();
        String createUserType = userType.getSelectionModel().getSelectedItem();
        String createUserPassword = userPassword.getText();
        String createUserLocation = userLocation.getText();
        if (createUserType.equals("Admin")) {
            createUserRole = "1";
        } else {
            createUserRole = "0";
        }
        String[] createUserInfo = {
            createUserName,
            createUserMail,
            createUserPhone,
            createUserRole,
            createUserPassword,
            createUserLocation
        };
        try {
            boolean createWorker = Worker.checkCreateWorker(App.getConn(), createUserInfo);
            if(createWorker) {
                String descString = "Användare " + createUserInfo[0] + " skapad!";
                sceneManager.ShowAlert("Godkänd", descString);
                resetFields();
            } else {
                sceneManager.ShowAlert("Nekad", "Kunde inte skapa användare");
            }
        } catch (Exception e) {
            sceneManager.ShowAlert("Nekad", "Kunde inte skapa användare");

        }

    }
    
    public void handleDeleteUser() {
        try {
            boolean deleted = Worker.checkDeleteWorker(App.getConn(), selectedUserID);
            if (deleted) {
                sceneManager.ShowAlert("Godkänd", "Användare borttagen");
            } else {
                sceneManager.ShowAlert("Nekad", "Användare ej borttagen");
            }
        } catch (Exception e) {
            sceneManager.ShowAlert("Nekad", "Användare ej borttagen");
        }

    }
    
    public void handleUpdateUser() {
        String updateUserID = userID.getText();
        String updateUserName = userName.getText();
        String updateUserMail = userMail.getText();
        String updateUserPhone = userPhone.getText();
        String updateUserType = userType.getSelectionModel().getSelectedItem();
        String updateUserPassword = userPassword.getText();
        String updateUserLocation = userLocation.getText();
        String[] updateUserInfo = {
                updateUserName,
                updateUserMail,
                updateUserPhone,
                updateUserType,
                updateUserPassword,
                updateUserID,
                updateUserLocation
        };

        try {
            boolean updatedUser = Worker.checkUppdateWorker(App.getConn(), updateUserInfo);
            if(updatedUser) {
                sceneManager.ShowAlert("Godkänd", "Användare uppdaterad");
            } else {
                sceneManager.ShowAlert("Nekad", "Kunde ej uppdatera användare");
            }
        } catch (Exception e) {
            sceneManager.ShowAlert("Nekad", "Kunde ej uppdatera användare");
        }
        

    }

    public void resetFields() {
        updateButton.setDisable(true);
        deleteButton.setDisable(true);
        createButton.setDisable(false);
        userName.setText("");
        userMail.setText("");
        userPhone.setText("");
        userType.setValue("Admin");
        userLocation.setText("");
        userList.setContent(null);
        userID.setText("");
        searchUser.setText("");
    }
}