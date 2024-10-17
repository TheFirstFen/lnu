package hotel2.GUI;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import hotel2.App;
import hotel2.com.mid.Room;

import javafx.fxml.FXML;
import javafx.geometry.Pos;
import javafx.scene.control.Button;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.ContentDisplay;
import javafx.scene.control.Label;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;

public class AdminRoomController {
    @FXML TextField roomNumber;
    @FXML Button updateButton;
    @FXML Button deleteButton;
    @FXML Button createButton;
    @FXML Button resetFields;
    @FXML TextField roomSize;
    @FXML TextField roomPrice;
    @FXML ChoiceBox<String> roomType;
    @FXML ChoiceBox<String> searchType;
    @FXML TextField roomLocation;
    @FXML TextField searchRoom;
    @FXML ScrollPane roomList;
    @FXML Label roomID;
    List<TextField> inputfields;

    private String[] selectedRoomForDelete;
    private SceneManager sceneManager;

    public void setManager(SceneManager manager) {
        sceneManager = manager;
    }

    @FXML
    public void initialize() {
        initializeRoomTypeChoices();
        updateButton.setDisable(true);
        deleteButton.setDisable(true);
        inputfields = new ArrayList<>();
        inputfields.add(roomNumber);
        inputfields.add(roomSize);
        inputfields.add(roomPrice);
        inputfields.add(roomLocation);

    }

    private void initializeRoomTypeChoices() {
        roomType.getItems().setAll("Standard", "Deluxe", "Suite");
        searchType.getItems().setAll("Room Number", "Room Size", "Room Type", "Room ID");
        roomType.setValue("Standard"); // Set default value if needed
        searchType.setValue("Room Number");
    }

    public void searchRooms() {
        String search = searchType.getSelectionModel().getSelectedItem();
        String info = searchRoom.getText();
        String[] searchFor = new String[2];
        searchFor[0] = search;
        searchFor[1] = info;

        String[][] roomInfo = Room.getRooms(App.getConn(), searchFor);
        displayRooms(roomInfo);
    }

    public void displayRooms(String[][] roomInfo) {
        VBox buttonBox = new VBox();
        for (int i = 0; i < roomInfo.length; i++) {
            Button tempButton = new Button(roomInfo[i][1] + " | " + roomInfo[i][2] + " | " + roomInfo[i][3] + " | " + roomInfo[i][4]);
            double width = roomList.getWidth();
            tempButton.setPrefWidth(width - 20);
            tempButton.setPrefHeight(50);
            tempButton.getStyleClass().add("temp-button");
            tempButton.getStylesheets().add(getClass().getResource("/css/tempButton.css").toExternalForm());
            tempButton.setAlignment(Pos.BASELINE_LEFT);
            tempButton.setContentDisplay(ContentDisplay.LEFT);
            selectedRoomForDelete = roomInfo[i];
            String[] selectedRoom = roomInfo[i];
            tempButton.setOnAction(event -> displayRoomInfo(selectedRoom));
            buttonBox.getChildren().add(tempButton);
        }
        roomList.setContent(buttonBox);
    }

    public void displayRoomInfo(String[] selectedRoom) {
        createButton.setDisable(true);
        updateButton.setDisable(false);
        deleteButton.setDisable(false);
        roomType.getItems().setAll("Standard", "Suite", "Deluxe");
        roomID.setText(selectedRoom[0]);
        roomNumber.setText(selectedRoom[1]);
        roomSize.setText(selectedRoom[2]);
        roomType.getSelectionModel().select((selectedRoom[3]));
        roomPrice.setText(selectedRoom[4]);
        roomLocation.setText(selectedRoom[5]);

    }

    public String[] getRoom(String[][] roominfo, String rid) {
        for (String[] room : roominfo) {
            if (room.length > 0 && room[0].equals(rid)) {
                return room; // Return the entire room array
            }
        }
        return null;
    }
    

    public void handleCreateRoom() {
        String createRoomNumber = roomNumber.getText();
        String createRoomSize = roomSize.getText();
        String createRoomType = roomType.getSelectionModel().getSelectedItem();
        String createRoomPrice = roomPrice.getText();
        String createRoomLocation = roomLocation.getText();
        String[] createRoomInfo = {
            createRoomNumber,
            createRoomSize,
            createRoomType,
            createRoomPrice,
            createRoomLocation
        };

        try {
            boolean createdRoom = Room.checkCreateRoom(App.getConn(), createRoomInfo);
            if(createdRoom) {
                String descString = "Rum nr " + createRoomInfo[0] + " skapat!";
                sceneManager.ShowAlert("Godkänd", descString);
                resetFields();
            } else {
                sceneManager.ShowAlert("Nekad", "Rum ej skapat");
            }
        } catch (Exception e) {
            sceneManager.ShowAlert("Nekad", "Rum ej skapat");
        }
    }

    public void handleDeleteRoom() {
        try {
            boolean deleted = Room.deleteRoom(App.getConn(), selectedRoomForDelete);

            if (deleted) {
                sceneManager.ShowAlert("Godkänd", "Rum borttaget");
            } else {
                sceneManager.ShowAlert("Nekad", "Rum ej borttaget");
            }
        } catch (Exception e) {
            sceneManager.ShowAlert("Nekad", "Rum ej borttaget");

        }

    }

    public void handleUpdateRoom() {
        String updateRoomID = roomID.getText();
        String updatedRoomNumber = roomNumber.getText();
        String updatedRoomSize = roomSize.getText();
        String updatedRoomType = roomType.getSelectionModel().getSelectedItem();
        String updatedRoomPrice = roomPrice.getText();
        String updatedRoomLocation = roomLocation.getText();
        String[] updateRoomInfo = {
            updateRoomID,
            updatedRoomNumber,
            updatedRoomSize,
            updatedRoomType,
            updatedRoomPrice,
            updatedRoomLocation,
        };
        try {
            boolean updatedRoom = Room.updateRoom(App.getConn(), updateRoomInfo);
            if(updatedRoom) {
                sceneManager.ShowAlert("Godkänd", "Rum uppdaterat");
            } else {
                sceneManager.ShowAlert("Nekad", "Rum ej uppdaterat");
            }
        } catch (Exception e) {
            sceneManager.ShowAlert("Nekad", "Rum ej uppdaterat");

        }


    }

    public void resetFields() {
        updateButton.setDisable(true);
        deleteButton.setDisable(true);
        createButton.setDisable(false);
        roomNumber.setText("");
        roomSize.setText("");
        roomPrice.setText("");
        roomType.setValue("Standard");
        roomLocation.setText("");
        roomList.setContent(null);
        roomID.setText("");
        searchRoom.setText("");
    }
}
