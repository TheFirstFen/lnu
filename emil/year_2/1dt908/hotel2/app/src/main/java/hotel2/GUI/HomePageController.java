package hotel2.GUI;

import javafx.animation.RotateTransition;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.geometry.Pos;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.ComboBox;
import javafx.scene.control.ContentDisplay;
import javafx.scene.control.Label;
import javafx.scene.control.ScrollPane;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.VBox;

import java.time.Month;
import java.time.DayOfWeek;
import java.time.LocalDate;

import java.util.ArrayList;
import javafx.util.Duration;

import hotel2.App;
import hotel2.com.mid.Booking;
import hotel2.com.mid.Customer;
import hotel2.com.mid.Room;


public class HomePageController {
    @FXML Button newButton;
    @FXML ScrollPane CheckinPane;
    @FXML ScrollPane CheckoutPane;
    @FXML AnchorPane MainAnchorpane;
    @FXML VBox CalenderBox;
    @FXML Label monthLabel;
    @FXML private ComboBox<String> settingsBox;
    @FXML Label LoggedinName;
    @FXML ImageView settingsIcon;
    @FXML Button leftArrowID;
    @FXML Button rightArrowID;

    // Check in/out properties
    @FXML Label checkGuest;
    @FXML Label checkDate;
    @FXML Label checkRoom;
    @FXML Label checkGuestCount;
    @FXML Label checkTot;
    @FXML Label checkPaid;
    @FXML CheckBox checkBoxPay;

    private SceneManager sceneManager;
    private int monthChanger;
    private String currMonth;
    private Boolean isRotated = false;

    private String[] booking;
    public void setManager(SceneManager manager) {
        sceneManager = manager;
    }

    
    public void launch() {
        monthChanger = 0;

        updateCalender("First");
        settingsBox.getItems().clear();
        settingsIcon.setImage(new Image("/settingsicon.png"));
        settingsBox.getItems().add("Ändra profil");
        settingsBox.getItems().add("Adminpanel");
        settingsBox.getItems().add("Logga ut");
        
        
        settingsBox.setOnAction(event -> handleSettingsBoxSelection());
        settingsBox.setOnMouseClicked(event -> settingClicked());
        MainAnchorpane.setStyle("-fx-background-color: rgba(255, 255, 255, 0.8);");
        LoggedinName.setText("Inloggad som: " + sceneManager.getLoginInfo()[0]);

        String[] inInfo = {LocalDate.now().toString()};
        String[][] checkInToday = new String[100][10];
        String[] outInfo = {LocalDate.now().toString()};
        String[][] checkOutToday = new String[100][10];
        try {
            checkInToday = Booking.checkInToday(App.getConn(), inInfo);
            VBox buttonBox = new VBox();
            for (int i = 0; i < checkInToday.length; i++) {
                String[] guest = Customer.checkForGetCustomer(App.getConn(), checkInToday[i][4]);
                String in = checkInToday[i][3];
                String[] rids = in.split("[,\\s]+");
                String dispRoom = "";
                for (int j = 0; j < rids.length; j++) {
                    String[] room = {"Room ID", rids[j]};
                    dispRoom = dispRoom + " " + Room.getRooms(App.getConn(), room)[0][1];
                }
                Button tempButton = new Button("Rumsnr: " + dispRoom + " | " + guest[0] + " " + guest[1] + " | Betald: " + (checkInToday[i][5].equals("1") ? "Ja" : "Nej"));
                tempButton.setPrefWidth(348);
                tempButton.setPrefHeight(25);
                tempButton.getStyleClass().add("temp-button");
                tempButton.getStylesheets().add(getClass().getResource("/css/CheckButtons.css").toExternalForm()); 
                tempButton.setAlignment(Pos.BASELINE_LEFT);
                tempButton.setContentDisplay(ContentDisplay.LEFT);
                String[] info = checkInToday[i];
                tempButton.setOnAction(event -> checkInButtonInfo(info));
                buttonBox.getChildren().add(tempButton);
            }
            CheckinPane.setContent(buttonBox);
            
            checkOutToday = Booking.checkOutToday(App.getConn(), outInfo);
            buttonBox = new VBox();
            for (int i = 0; i < checkOutToday.length; i++) {
                String[] guest = Customer.checkForGetCustomer(App.getConn(), checkOutToday[i][4]);
                String out = checkOutToday[i][3];
                String[] rids = out.split("[,\\s]+");
                String dispRoom = "";
                for (int j = 0; j < rids.length; j++) {
                    String[] room = {"Room ID", rids[j]};
                    dispRoom = dispRoom + " " + Room.getRooms(App.getConn(), room)[0][1];
                }
                Button tempButton = new Button("Rumsnr:" + dispRoom + " | " + guest[0] + " " + guest[1] + " | Betald: " + (checkOutToday[i][5].equals("1") ? "Ja" : "Nej"));
                tempButton.setPrefWidth(348);
                tempButton.setPrefHeight(25);
                tempButton.getStyleClass().add("temp-button");
                tempButton.getStylesheets().add(getClass().getResource("/css/CheckButtons.css").toExternalForm()); 
                tempButton.setAlignment(Pos.BASELINE_LEFT);
                tempButton.setContentDisplay(ContentDisplay.LEFT);
                String[] info = checkOutToday[i];
                tempButton.setOnAction(event -> checkOutButtonInfo(info));
                buttonBox.getChildren().add(tempButton);
            }
            CheckoutPane.setContent(buttonBox);
        } catch(Exception e) {
        }



    }

    public void updateCalender(String arrow) {
        if (monthChanger == 59) {
            rightArrowID.setDisable(true);
        } else {
            rightArrowID.setDisable(false);
        }
        if (monthChanger == -23) {
            leftArrowID.setDisable(true);
        } else {
            leftArrowID.setDisable(false);
        }
        CalenderBox.getChildren().clear();
        if (arrow.equals("left")) {
            monthChanger--;
        } else if (arrow.equals("right")) {
            monthChanger++;
        }

        GridPane calendarPane = new GridPane();

        // Days of the week
        String[] daysOfWeek = {"Mån", "Tis", "Ons", "Tors", "Fre", "Lör", "Sön"};

        // Adding the days of the week to the calendar
        for (int i = 0; i < daysOfWeek.length; i++) {
            calendarPane.add(new DaySquare(sceneManager, 154, 40, daysOfWeek[i], false, false, null, null, true), i, 0);
        }

        LocalDate currentDate = LocalDate.now();

        LocalDate newYearMonth = currentDate.plusMonths(monthChanger);
        LocalDate prevYearMonth = currentDate.plusMonths(monthChanger - 1);

        int currentYear = newYearMonth.getYear();
        Month currentMonth = newYearMonth.getMonth();

        Month prevMonth = prevYearMonth.getMonth();

        int totalDaysPrevMonth = getDaysInMonth(prevMonth.toString(), currentYear);
        int totalDaysInMonth = getDaysInMonth(currentMonth.toString(), currentYear);

        // Calculate the day of the week for the first day of the current month
        LocalDate firstDayOfMonth = LocalDate.of(currentYear, currentMonth, 1);
        DayOfWeek startDayOfWeek = firstDayOfMonth.getDayOfWeek();
        int count = -2;
        int startingColumn = startDayOfWeek.getValue();
        int dayCounter = 1;
        
        for (int row = 1; row < 6; row++) {
            for (int col = 0; col < 7; col++) {
                if (row == 1 && col < startingColumn) {
                    count ++;
                }
            }
        }
        totalDaysPrevMonth -= count;
        for (int row = 1; row < 7; row++) {
            for (int col = 0; col < 7; col++) {
                boolean isCurrentDay = (dayCounter == LocalDate.now().getDayOfMonth() && monthChanger == 0);
                if (row == 1 && col < startingColumn - 1) {
                    calendarPane.add(new DaySquare(sceneManager, 154, 63, String.valueOf(totalDaysPrevMonth), true, isCurrentDay, currentMonth.toString(), currentYear, true), col, row);
                    totalDaysPrevMonth ++;
                } else if (dayCounter <= totalDaysInMonth) {
                    calendarPane.add(new DaySquare(sceneManager, 154, 63, String.valueOf(dayCounter), false, isCurrentDay, currentMonth.toString(), currentYear, true), col, row);
                    dayCounter++;
                }
            }
        }

        CalenderBox.getChildren().add(calendarPane);

        monthLabel.setText(currMonth + " " + currentYear);
    }
    private int getDaysInMonth(String inpMonth, int year) {
        String month = inpMonth.toLowerCase();
        switch (month) {
            case "january":
                currMonth = "Januari";
                return 31;
            case "february":
                currMonth = "Februari";
                if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
                    return 29;
                } else {
                    return 28;
                }
            case "march":
                currMonth = "Mars";
                return 31;
            case "april":
                currMonth = "April";
                return 30;
            case "may":
                currMonth = "Maj";
                return 31;
            case "june":
                currMonth = "Juni";
                return 30;
            case "july":
                currMonth = "Juli";
                return 31;
            case "august":
                currMonth = "Augusti";
                return 31;
            case "september":
                currMonth = "September";
                return 30;
            case "october":
                currMonth = "Oktober";
                return 31;
            case "november":
                currMonth = "November";
                return 30;
            case "december":
                currMonth = "December";
                return 31;
            default:
                return 0;
        }
    }

    private void handleSettingsBoxSelection() {
        String selectedOption = settingsBox.getValue();

        if ("Ändra profil".equals(selectedOption)) {
            sceneManager.editProfilePopUp();
        } else if ("Adminpanel".equals(selectedOption)) {
            if (sceneManager.getLoginInfo()[2].equals("1")) {
                sceneManager.switchToAdminPageRoot();
            } else {
                sceneManager.ShowAlert("Ej tillgång", "Användare saknar adminpriviligier.");
            }
        } else if ("Logga ut".equals(selectedOption)) {
            sceneManager.resetLoginPage();
            sceneManager.switchToLoginRoot();
        }
    }
    public void customerHandlingButton() {
        sceneManager.switchToHandleCustRoot();
    }
    public void LeftArrow(ActionEvent event) {
        updateCalender("left");
    }
    public void RightArrow(ActionEvent event) {
        updateCalender("right");
    }
    public void ManageBooking(ActionEvent event) {
        sceneManager.switchToHandleBookRoot(null, null);
    }
    public void ResetPage(ActionEvent event) {
        monthChanger = 0;
        updateCalender("Reset");
    }

    public void NewBooking(ActionEvent event) {
        sceneManager.setCurrentBookingInfo(new String[10]);
        sceneManager.setDisplayInfo(new String[10]);
        sceneManager.setDisplayRooms(new ArrayList<>());
        sceneManager.getDate()[0] = LocalDate.now();
        sceneManager.getDate()[1] = LocalDate.now().plusDays(1);
        sceneManager.switchToCreateBookingRoot(true);
    }
    public void roomHandling(ActionEvent event) {
        sceneManager.switchToHandleRoomRoot(null);
    }
    public void checkOutButtonInfo(String[] info) {
        sceneManager.checkOutPopup(info);
    }
    public void checkInButtonInfo(String[] info) {
        sceneManager.checkInPopup(info);
    }
    public void checkOutButton() {
        if (checkBoxPay.isSelected()) {
            String[] info = {booking[0], "1"};
            Booking.checkOut(App.getConn(), info);
        } else {
            String[] info = {booking[0], "0"};
            Booking.checkOut(App.getConn(), info);
        }
        sceneManager.closeCurrentPopup();
        sceneManager.switchToHomeRoot();
    }
    public void checkInButton() {
        if (checkBoxPay.isSelected()) {
            String[] info = {booking[0], "1"};
            Booking.checkIn(App.getConn(), info);
        } else {
            String[] info = {booking[0], "0"};
            Booking.checkIn(App.getConn(), info);
        }
        sceneManager.closeCurrentPopup();
        sceneManager.switchToHomeRoot();
    }
    public void setUpCheck(String[] info) {
        String[] guest = Customer.checkForGetCustomer(App.getConn(), info[4]);
        checkGuest.setText("Gäst: " + guest[0] + " " + guest[1]);
        checkDate.setText("Datum: " + info[1] + " - " + info[2]);
        String out = info[3];
        String[] rids = out.split("[,\\s]+");
        String dispRoom = "";
        for (int j = 0; j < rids.length; j++) {
            String[] room = {"Room ID", rids[j]};
            dispRoom = dispRoom + " " + Room.getRooms(App.getConn(), room)[0][1];
        }
        checkRoom.setText("Rumsnr: " + dispRoom);
        checkGuestCount.setText("Antal gäster: " + info[7]);
        checkTot.setText("Totalpris: " + info[6]);
        checkPaid.setText("Betald: " + (info[5].equals("1") ? "Ja" : "Nej") + " | " + guest[4]);
        if (info[5].equals("1")) {
            checkBoxPay.setSelected(true);
            checkBoxPay.setDisable(true);
        } else {
            checkBoxPay.setSelected(false);
        }
        booking = info;
    }

    public void backButtonCheckIn() {
        sceneManager.closeCurrentPopup();
    }
    public void backButtonCheckOut() {
        sceneManager.closeCurrentPopup();
    }
    public void settingClicked() {
        int angle;
        if (isRotated) {
            angle = -45;
            isRotated = false;
        } else {
            angle = 45;
            isRotated = true;
        }
        RotateTransition rotateTransition = new RotateTransition();
        rotateTransition.setNode(settingsIcon);
        rotateTransition.setDuration(Duration.seconds(0.2));
        rotateTransition.setByAngle(angle);

        rotateTransition.play();
    }
}