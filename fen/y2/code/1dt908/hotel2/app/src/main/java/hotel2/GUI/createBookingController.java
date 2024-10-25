package hotel2.GUI;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.List;

import hotel2.App;
import hotel2.com.mid.Booking;
import hotel2.com.mid.Customer;
import hotel2.com.mid.Room;
import javafx.fxml.FXML;
import javafx.geometry.Pos;
import javafx.scene.control.Button;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.ContentDisplay;
import javafx.scene.control.DatePicker;
import javafx.scene.control.Label;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.util.StringConverter;

public class createBookingController {
    @FXML
    private DatePicker startDatePicker;
    @FXML
    private DatePicker endDatePicker;
    @FXML
    private ChoiceBox<Integer> chooseGuest;
    @FXML
    private ScrollPane roomPane;
    @FXML
    private Label prevGuest;
    @FXML
    private Label prevDate;
    @FXML
    private Label prevCRoom;
    @FXML
    private Label prevCGuest;
    @FXML
    private ScrollPane prevRoomPane;
    @FXML
    private Label prevTot;

    @FXML
    TextField SearchField1;
    @FXML
    ChoiceBox<String> SearchMethod;
    @FXML
    ChoiceBox<String> roomType;
    @FXML
    ChoiceBox<String> numGuests;
    @FXML
    private ScrollPane custPane;
    @FXML
    private AnchorPane prevPane;
    @FXML
    private AnchorPane mainAnchorP;
    @FXML
    private AnchorPane prevPopPane;

    @FXML
    private Button cButton;

    private SceneManager sceneManager;

    public void setManager(SceneManager manager) {
        sceneManager = manager;
    }

    public void setup(Boolean setup) {
        StringConverter<LocalDate> converter = new StringConverter<>() {
            @Override
            public String toString(LocalDate date) {
                return (date != null) ? date.toString() : "";
            }

            @Override
            public LocalDate fromString(String string) {
                return (string != null && !string.isEmpty()) ? LocalDate.parse(string) : null;
            }
        };
        startDatePicker.setValue(sceneManager.getDate()[0]);
        endDatePicker.setValue(sceneManager.getDate()[1]);

        String roomInfo = sceneManager.getDisplayInfo()[3];
        prevCRoom.setText(roomInfo);

        String guestInfo = sceneManager.getDisplayInfo()[4];
        chooseGuest.setValue((guestInfo != null && !guestInfo.isEmpty()) ? Integer.parseInt(guestInfo) : 0);

        startDatePicker.setConverter(converter);
        endDatePicker.setConverter(converter);
        startDatePicker.valueProperty().addListener((observable, oldValue, newValue) -> handleDateSelection());
        endDatePicker.valueProperty().addListener((observable, oldValue, newValue) -> handleDateSelection());
        chooseGuest.getSelectionModel().selectedItemProperty()
                .addListener((observable, oldValue, newValue) -> handleChoiceBoxSelection(newValue, 4));
        setup = true;
        if (setup) {
            for (int i = 1; i <= 20; i++) {
                chooseGuest.getItems().add(i);
            }
        }
        handleDateSelection();
    }

    public void setUpPopUp() {
        SearchMethod.getItems().clear();
        SearchMethod.getItems().addAll("Name", "Email");
        SearchMethod.setStyle("-fx-font-Size: 20px; -fx-background-color: #f48f0b; -fx-text-fill: #ffffff;");
        SearchMethod.setValue("Name");

        String searchFilter = SearchMethod.getSelectionModel().getSelectedItem();
        String searchWord = SearchField1.getText();
        String[] search = { searchFilter, searchWord };
        String[][] displayArray = null;
        displayArray = Customer.checkForAllCustomers(App.getConn(), search);

        VBox buttonBox = new VBox();
        for (int i = 0; i < displayArray.length; i++) {
            Button tempButton = new Button(displayArray[i][0] + " " + displayArray[i][1] + " | " + displayArray[i][3]);
            tempButton.setPrefWidth(520);
            tempButton.setPrefHeight(50);
            tempButton.getStyleClass().add("temp-button");
            tempButton.getStylesheets().add(getClass().getResource("/css/tempButton.css").toExternalForm());
            tempButton.setAlignment(Pos.BASELINE_LEFT);
            tempButton.setContentDisplay(ContentDisplay.LEFT);
            String cid = displayArray[i][2];
            tempButton.setOnAction(event -> setCustomer(cid));
            buttonBox.getChildren().add(tempButton);
        }
        custPane.setContent(buttonBox);
    }

    public void setUpPopUpRoom() {
        numGuests.getItems().clear();
        numGuests.getItems().addAll("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20");
        numGuests.setStyle("-fx-font-Size: 20px; -fx-background-color: #f48f0b; -fx-text-fill: #ffffff;");
        if (sceneManager.getDisplayInfo()[4] != null) {
            numGuests.setValue(sceneManager.getDisplayInfo()[4]);
        } else {
            numGuests.setValue("2");
        }
        
        roomType.getItems().clear();
        roomType.getItems().addAll("Alla", "Standard", "Deluxe");
        roomType.setStyle("-fx-font-Size: 20px; -fx-background-color: #f48f0b; -fx-text-fill: #ffffff;");
        roomType.setValue("Alla");
        
        String minGuests = numGuests.getValue();
        String[] search = { "Room Size", minGuests };
        String[][] displayArray = null;
        List<String[]> displayArrayView = new ArrayList<String[]>();
        displayArray = Room.getRooms(App.getConn(), search);

    numGuests.getSelectionModel().selectedItemProperty().addListener((observable, oldValue, newValue) -> {
        updateSearch(); // Call updateSearch() when numGuests changes
    });
    
    // Add listener for roomType choice box
    roomType.getSelectionModel().selectedItemProperty().addListener((observable, oldValue, newValue) -> {
        updateSearch(); // Call updateSearch() when roomType changes
    });
        
        for (int i = 0; i < displayArray.length; i++) {
            if (roomType.getValue().equals("Alla")) {
                displayArrayView.add(displayArray[i]);
            } else if (roomType.getValue().equals("Standard")) {
                if (displayArray[i][3] == "Standard") {
                    displayArrayView.add(displayArray[i]);
                }
            } else if (roomType.getValue().equals("Deluxe")) {
                if (displayArray[i][3] == "Deluxe") {
                    displayArrayView.add(displayArray[i]);
                }
            }
        }
        
        VBox buttonBox = new VBox();
        for (String[] item : displayArrayView) {
            String[] n = sceneManager.getDisplayInfo();
            String[] tempArray = { n[1], n[2], item[0] };
            if (Booking.isRoomAvailable(App.getConn(), tempArray)) {
                String t = item[3];
                if (t.equals("Standard")) {
                    t = "S";
                } else {
                    t = "D";
                }
                Button tempButton = new Button("Rumsnr: " + item[1] + " " + t + " | Antal bäddar: "
                + item[2] + " st " + " | Pris/natt: " + item[4] + " kr");
                tempButton.setPrefWidth(518);
                tempButton.setPrefHeight(50);
                tempButton.getStyleClass().add("temp-button");
                tempButton.getStylesheets().add(getClass().getResource("/css/tempButton.css").toExternalForm());
                tempButton.setAlignment(Pos.BASELINE_LEFT);
                tempButton.setContentDisplay(ContentDisplay.LEFT);
                tempButton.setOnAction(event -> setRoom(item, tempButton));
                buttonBox.getChildren().add(tempButton);
            }
        }
        
        roomPane.setContent(buttonBox);
    }

    private void updateSearch() {
        String minGuests = numGuests.getValue();
        
        String[] search = {"Room Size", minGuests};
        String[][] displayArray = null;
        List<String[]> displayArrayView = new ArrayList<String[]>();
        displayArray = Room.getRooms(App.getConn(), search);
        for (int i = 0; i < displayArray.length; i++) {
            if (roomType.getValue().equals("Alla")) {
                displayArrayView.add(displayArray[i]);
            } else if (roomType.getValue().equals("Standard")) {
                if (displayArray[i][3].equals("Standard")) {
                    displayArrayView.add(displayArray[i]);
                }
            } else if (roomType.getValue().equals("Deluxe")) {
                if (displayArray[i][3].equals("Deluxe")) {
                    displayArrayView.add(displayArray[i]);
                }
            }
        }
        
        VBox buttonBox = new VBox();
        for (String[] item : displayArrayView) {
            String[] n = sceneManager.getDisplayInfo();
            String[] tempArray = { n[1], n[2], item[0]};
            if (Booking.isRoomAvailable(App.getConn(), tempArray)) {
                String t = item[3];
                if (t.equals("Standard")) {
                    t = "S";
                } else {
                    t = "D";
                }
                Button tempButton = new Button("Rumsnr: " + item[1] + " " + t + " | Antal bäddar: "
                + item[2] + " st " + " | Pris/natt: " + item[4] + " kr");
                tempButton.setPrefWidth(518);
                tempButton.setPrefHeight(50);
                tempButton.getStyleClass().add("temp-button");
                tempButton.getStylesheets().add(getClass().getResource("/css/tempButton.css").toExternalForm());
                tempButton.setAlignment(Pos.BASELINE_LEFT);
                tempButton.setContentDisplay(ContentDisplay.LEFT);
                tempButton.setOnAction(event -> setRoom(item, tempButton));
                buttonBox.getChildren().add(tempButton);
            }
        }
        
        roomPane.setContent(buttonBox);
    }
    
    private void handleChoiceBoxSelection(Integer selectedItem, int displayInfoIndex) {
        if (selectedItem != null) {
            sceneManager.getDisplayInfo()[displayInfoIndex] = selectedItem.toString();
        } else {
            sceneManager.getDisplayInfo()[displayInfoIndex] = "";
        }
        updatePrevWindow();
    }
    
    private void handleDateSelection() {
        LocalDate startDate = startDatePicker.getValue();
        LocalDate endDate = endDatePicker.getValue();
        
        if (startDate.isAfter(endDate)) {
            endDate = startDate.plusDays(1);
            endDatePicker.setValue(endDate);
        }
        if (!startDate.isAfter(LocalDate.now().minusDays(1))) {
            startDate = LocalDate.now();
            startDatePicker.setValue(LocalDate.now());
        }

        sceneManager.getDate()[0] = startDate;
        sceneManager.getDate()[1] = endDate;

        sceneManager.getDisplayInfo()[1] = startDate.toString();
        sceneManager.getDisplayInfo()[2] = endDate.toString();
        updatePrevWindow();
    }

    private void setCustomer(String text) {
        String[] custInfo = Customer.checkForGetCustomer(App.getConn(), text);
        sceneManager.getCurrentBookingInfo()[0] = text;
        sceneManager.getDisplayInfo()[0] = custInfo[0];
        sceneManager.getDisplayInfo()[7] = custInfo[1];
        sceneManager.getDisplayInfo()[6] = text;
        sceneManager.closeCurrentPopup();

    }

    private void setRoom(String[] text, Button tempButton) {
        tempButton.setStyle("-fx-background-color: darkgrey;");
        tempButton.setOnAction(event -> unSetRoom(text, tempButton));
        sceneManager.getDisplayRooms().add(text);
    }

    private void unSetRoom(String[] text, Button tempButton) {
        tempButton.getStyleClass().add("temp-button");
        tempButton.getStylesheets().add(getClass().getResource("/css/tempButton.css").toExternalForm());
        tempButton.setOnAction(event -> setRoom(text, tempButton));
    }


    public void backButton() {
        sceneManager.switchToHomeRoot();
    }

    public void updateRooms() {
        setUpPopUpRoom();
    }

    private void updatePrevWindow() {
        boolean isMissingInfo = false;

        // Check if any display info text is null
        if (sceneManager.getDisplayInfo()[0] == null) {
            prevGuest.setTextFill(Color.RED);
            prevGuest.setText("Saknas info");
            isMissingInfo = true;
        } else {
            prevGuest.setTextFill(Color.BLACK);
            prevGuest.setText(sceneManager.getDisplayInfo()[0] + " " + sceneManager.getDisplayInfo()[7]);
        }

        if (prevDate.getText() == null) {
            prevDate.setTextFill(Color.RED);
            prevDate.setText("Saknas info");
            isMissingInfo = true;
        } else {
            prevDate.setTextFill(Color.BLACK);
            prevDate.setText(sceneManager.getDisplayInfo()[1] + " - " + sceneManager.getDisplayInfo()[2]);
        }

        if (sceneManager.getDisplayInfo()[3] == null) {
            prevCRoom.setTextFill(Color.RED);
            prevCRoom.setText("Saknas info");
            isMissingInfo = true;
        } else {
            prevCRoom.setTextFill(Color.BLACK);
            prevCRoom.setText(sceneManager.getDisplayInfo()[3]);
        }

        if (sceneManager.getDisplayInfo()[4] == null) {
            prevCGuest.setTextFill(Color.RED);
            prevCGuest.setText("Saknas info");
            isMissingInfo = true;
        } else {
            prevCGuest.setTextFill(Color.BLACK);
            prevCGuest.setText(sceneManager.getDisplayInfo()[4] + " st");
        }

        if (prevTot.getText() == null) {
            prevTot.setTextFill(Color.RED);
            prevTot.setText("Saknas info");
            isMissingInfo = true;
        } else {
            prevTot.setTextFill(Color.BLACK);
            prevTot.setText(calcPrice() + " kr");
        }

        if (isMissingInfo) {
            cButton.setDisable(true);
        } else {
            cButton.setDisable(false);
        }

        VBox buttonBox = new VBox();
        for (String[] r : sceneManager.getDisplayRooms()) {
            Button tempButton = new Button(
                    "Rumsnr: " + r[1] + " | Antal bäddar: " + r[2] + " st " + " | Pris/natt: " + r[4] + " kr");
            tempButton.setPrefWidth(387);
            tempButton.setPrefHeight(50);
            tempButton.getStyleClass().add("temp-button");
            tempButton.getStylesheets().add(getClass().getResource("/css/tempButton.css").toExternalForm());
            tempButton.setStyle("-fx-font-size: 16");
            tempButton.setAlignment(Pos.BASELINE_LEFT);
            tempButton.setContentDisplay(ContentDisplay.LEFT);
            tempButton.setDisable(true);
            buttonBox.getChildren().add(tempButton);
        }
        prevRoomPane.setContent(buttonBox);

        VBox buttonBox1 = new VBox();
        for (String[] r : sceneManager.getDisplayRooms()) {
            Button tempButton = new Button(
                    "Rumsnr: " + r[1] + " | Antal bäddar: " + r[2] + " st " + " | Pris/natt: " + r[4] + " kr");
            tempButton.setPrefWidth(512);
            tempButton.setPrefHeight(50);
            tempButton.getStyleClass().add("temp-button");
            tempButton.getStylesheets().add(getClass().getResource("/css/tempButton.css").toExternalForm());
            tempButton.setAlignment(Pos.BASELINE_LEFT);
            tempButton.setContentDisplay(ContentDisplay.LEFT);
            tempButton.setOnAction(event -> removeRoom(r, tempButton, buttonBox1));
            buttonBox1.getChildren().add(tempButton);
        }
        roomPane.setContent(buttonBox1);
        sceneManager.getDisplayInfo()[3] = Integer.toString(sceneManager.getDisplayRooms().size());
        prevCRoom.setText(sceneManager.getDisplayInfo()[3] + " st");
    }

    private void removeRoom(String[] r, Button tempButton, VBox buttonBox) {
        sceneManager.getDisplayRooms().remove(r);
        calcPrice();
        buttonBox.getChildren().remove(tempButton);
        roomPane.setContent(buttonBox);
        updatePrevWindow();
    }

    public void backButtonPop() {
        sceneManager.closeCurrentPopup();
        sceneManager.switchToCreateBookingRoot(true);
    }

    public void searchButton() {
        setUpPopUp();
    }

    public void doneButton() {
        sceneManager.closeCurrentPopup();
    }

    public void existGuest() {
        sceneManager.createBookingCustomerPopup();
    }

    public void newGuest() {
        sceneManager.createNewCustomerPopup();
        sceneManager.getDisplayInfo()[0] = Customer.latestCustomer(App.getConn())[0];
        sceneManager.getDisplayInfo()[6] = Customer.latestCustomer(App.getConn())[5];
        sceneManager.getDisplayInfo()[7] = Customer.latestCustomer(App.getConn())[1];
        updatePrevWindow();
    }

    public void chooseRoom() {
        sceneManager.createBookingRoomPopup();
    }

    public void redigeraButton() {
        mainAnchorP = sceneManager.getPane();

    }

    public void completeBooking() {
        String[] info = sceneManager.getDisplayInfo();
        String[] booking = new String[10];
        // startdate
        booking[0] = info[1];
        // end date
        booking[1] = info[2];
        // rums id
        String disp = "";
        int c = 0;
        for (String[] n : sceneManager.getDisplayRooms()) {
            if (c == 0) {
                disp = n[0];
            } else {
                disp = disp + " " + n[0];
            }
            c ++;
        }
        booking[2] = disp;
        // customer id
        booking[3] = sceneManager.getDisplayInfo()[6];
        // paid
        booking[4] = "0";
        // Price
        booking[5] = calcPrice();
        // guestcount
        booking[6] = info[4];
        // created by
        booking[7] = sceneManager.getLoginInfo()[1];
        if (Booking.checkCreateBooking(App.getConn(), booking)) {
            sceneManager.closeCurrentPopup();
            sceneManager.switchToHomeRoot();
            if (LocalDate.now() == sceneManager.getDate()[0]) {
                // TODO
                // sceneManager.checkInPopup();
            }
        } else {
            sceneManager.ShowAlert("Problem", "Bokning ej genomförd, rum upptaget dessa datum.");
        }
    }

    private String calcPrice() {
        long sum = 0;
        long amountOfNights = calculateDaysBetween(sceneManager.getDisplayInfo()[1], sceneManager.getDisplayInfo()[2]);
        for (String[] r : sceneManager.getDisplayRooms()) {
            sum += Float.parseFloat(r[4]) * amountOfNights;
        }
        sceneManager.getDisplayInfo()[5] = String.valueOf(sum);
        return String.valueOf(sum);
    }

    public static long calculateDaysBetween(String startDateString, String endDateString) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        LocalDate startDate = LocalDate.parse(startDateString, formatter);
        LocalDate endDate = LocalDate.parse(endDateString, formatter);

        long daysBetween = ChronoUnit.DAYS.between(startDate, endDate);

        return daysBetween;
    }

    public void createBookingButton() {
        mainAnchorP.getChildren().add(sceneManager.getPane());
    }

    public void createBooking() {
        if (sceneManager.getDisplayInfo()[0] != null && sceneManager.getDisplayInfo()[1] != null
                && sceneManager.getDisplayInfo()[2] != null && sceneManager.getDisplayInfo()[3] != null
                && sceneManager.getDisplayRooms().size() >= 0 && sceneManager.getDisplayInfo()[4] != null) {
            sceneManager.setPane(prevPane);
            sceneManager.createNewBookingPopup();
        } else {
            sceneManager.ShowAlert("Problem", "Info saknas för bokning");
        }
    }
}
