package hotel2.GUI;

import hotel2.App;
import hotel2.com.mid.Booking;
import hotel2.com.mid.Customer;
import hotel2.com.mid.Room;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.geometry.Pos;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.ContentDisplay;
import javafx.scene.control.Label;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.VBox;
import javafx.scene.text.Font;

import java.util.List;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Arrays;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class BookingController {
    @FXML ScrollPane bookScroll;
    @FXML ScrollPane roomPane;
    @FXML TextField SearchField1;
    @FXML ChoiceBox<String> SearchMethod;
    @FXML TextField custFirstName;
    @FXML CheckBox payCheck;
    @FXML ChoiceBox<String> guestCount;
    @FXML Label updID;
    @FXML Label roomCount;
    @FXML Label totPris;
    @FXML AnchorPane MainAnchorpane;
    @FXML Button updbut;
    @FXML Button delbut;

    private SceneManager sceneManager;

    public void setManager(SceneManager manager) {
        sceneManager = manager;
    }
    public void setupPage() {
        SearchMethod.getItems().addAll("Boknings-id", "Gästnamn", "Rumsnummer", "Datum(yyyy-mm-dd)");
        guestCount.getItems().addAll("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20");
        SearchMethod.setStyle("-fx-font-Size: 20px; -fx-text-fill: #ffffff;");
        SearchMethod.setValue("Boknings-id");
        updbut.setDisable(true);
        delbut.setDisable(true);
    }
    
    public void fromCalender(String bid) {
        SearchField1.setText(bid);
        SearchForBooking();
        String[] i = {bid};
        Updatebooking(Booking.getBookingid(App.getConn(), i));
    }
    public void fromMain(String searchWord) {
        SearchField1.setText(searchWord);
        SearchMethod.setValue("Datum(yyyy-mm-dd)");
        SearchForBooking();
    }
    @SuppressWarnings("resource")
    public void SearchForBooking() {
        String searchFilter = SearchMethod.getSelectionModel().getSelectedItem();
        String searchWord = SearchField1.getText();
        if (searchFilter == "Gästnamn") {
            String[] search = {searchFilter, searchWord};
            String[][] displayArray = null;
            try {
                displayArray = Customer.checkForAllCustomers(App.getConn(), search);
                if (displayArray.length > 0 || displayArray != null) {
                    List<String[]> displayBooking = new ArrayList<>();
                    for (int i = 0; i < displayArray.length; i++) {
                        String cid = displayArray[i][2];
                        String[] nsearch = {"customerid", cid};
                        String[][] info = Booking.getBookingCustomer(App.getConn(), nsearch);
                        for (int j = 0; j < info.length; j++) {
                            displayBooking.add(info[j]);
                        }
                        DisplayResultsList(displayBooking);
                    }
                }   
            } catch (Exception e) {
                sceneManager.ShowAlert("Saknas bokning", "Gäst med namn som liknar " + searchWord + " saknar bokningar eller är ej registrerade.");
            }
        } else if (searchFilter.equals("Boknings-id")) {
            try {
                List<String[]> displayBooking = new ArrayList<>();
                String[] info = {searchWord};
                String[][] i = Booking.getBookingid(App.getConn(), info);
                if (i.length > 0) {
                    displayBooking.add(i[0]);
                    DisplayResultsList(displayBooking);
                } else {
                    sceneManager.ShowAlert("Saknas bokning", "Bokning med boknings-id " + searchWord + " saknas.");
                }
            } catch (NumberFormatException e) {
                sceneManager.ShowAlert("Saknas bokning", "Bokning med boknings-id " + searchWord + " saknas.");
            }
        } else if (searchFilter.equals("Datum(yyyy-mm-dd)")) {
            try {
                String[] info = {searchWord};
                // TODO Hitta rätt metod
                String[][] i = Booking.getBookingSingleDate(App.getConn(), info);
                
                if (i.length > 0) {
                    DisplayResultsArray(i);
                } else {
                    sceneManager.ShowAlert("Saknas bokningar", "Finns inga bokningar för datumet " + searchWord + ".");
                }
            } catch (NumberFormatException e) {
                sceneManager.ShowAlert("Saknas bokningar", "Finns inga bokningar för datumet " + searchWord + ".");
            }
         } else {
            try {
                String[][] displayBooking;
                String[] room = {"Room Number", searchWord};
                if (Room.getRooms(App.getConn(), room).length != 0) {
                    String word = Room.getRooms(App.getConn(), room)[0][0];
                    String[] info = {"roomid", word};
                    displayBooking = Booking.getBookingRoom(App.getConn(), info);
                    Arrays.sort(displayBooking, (booking1, booking2) -> {
                        LocalDate startDate1 = LocalDate.parse(booking1[1], DateTimeFormatter.ISO_LOCAL_DATE);
                        LocalDate startDate2 = LocalDate.parse(booking2[1], DateTimeFormatter.ISO_LOCAL_DATE);
                        return startDate1.compareTo(startDate2);
                    });
                    DisplayResultsArray(displayBooking);
                } else {
                    sceneManager.ShowAlert("Saknas rum", "Rum med rumsnummer " + searchWord + " saknas.");
                }
            } catch (NumberFormatException e) {
                sceneManager.ShowAlert("Saknas rum", "Rum med rumsnummer " + searchWord + " saknas.");
            }
        }
        
    }
    private void DisplayResultsArray(String[][] disp) {
        VBox buttonBox = new VBox();
        for (int i = 0; i < disp.length; i++) {
            String[] d = disp[i];
            Button tempButton = new Button("Gästnamn: " + Customer.checkForGetCustomer(App.getConn(), d[4])[0] + " " + Customer.checkForGetCustomer(App.getConn(), d[4])[1] + " | Boknings-id: " + d[0] + " | Datum: " + d[1] + " - " + d[2]);
            tempButton.setPrefWidth(713);
            tempButton.setPrefHeight(50);
            String[][] cid = {d};
            tempButton.getStyleClass().add("temp-button");
            tempButton.getStylesheets().add(getClass().getResource("/css/tempButton.css").toExternalForm());
            tempButton.setAlignment(Pos.BASELINE_LEFT);
            tempButton.setContentDisplay(ContentDisplay.LEFT);
            tempButton.setOnAction(event -> Updatebooking(cid));
            buttonBox.getChildren().add(tempButton);
        }
        bookScroll.setContent(buttonBox);
    }

    private void DisplayResultsList(List<String[]> disp) {
        VBox buttonBox = new VBox();
        for (String[] d : disp) {
            Button tempButton = new Button("Gästnamn: " + Customer.checkForGetCustomer(App.getConn(), d[4])[0] + " " + Customer.checkForGetCustomer(App.getConn(), d[4])[1] + " | Boknings-id: " + d[0] + " | Datum: " + d[1] + " - " + d[2]);
            tempButton.setPrefWidth(713);
            tempButton.setPrefHeight(50);
            String[][] cid = {d};
            tempButton.getStyleClass().add("temp-button");
            tempButton.getStylesheets().add(getClass().getResource("/css/tempButton.css").toExternalForm());
            tempButton.setAlignment(Pos.BASELINE_LEFT);
            tempButton.setContentDisplay(ContentDisplay.LEFT);
            tempButton.setOnAction(event -> Updatebooking(cid));
            buttonBox.getChildren().add(tempButton);
        }
        bookScroll.setContent(buttonBox);
    }

    private void Updatebooking(String[][] book) {
        updbut.setDisable(false);
        delbut.setDisable(false);
        String[] bookInfo = book[0];
        
        updID.setText(bookInfo[0]);
        guestCount.setValue(bookInfo[7]);
        try {
            String rid = Booking.getRoomIdsForBooking(App.getConn(), bookInfo[0]);
            // TODO splitvariant
            String[] split = rid.split("[,\\s]+");
            VBox buttonBox = new VBox();
            for (int i = 0; i < split.length; i++) {
                String[] search = {"Room ID", split[i]};
                String[][] roominfo = Room.getRooms(App.getConn(), search);
                String[] r = roominfo[0];
                Button tempButton = new Button("Rumsnr: " + r[1] + " | Antal bäddar: " + r[2] + " st " + " | Pris/natt: " + r[4] + " kr");
                tempButton.setPrefWidth(347);
                tempButton.setPrefHeight(30);
                tempButton.getStyleClass().add("temp-button");
                tempButton.getStylesheets().add(getClass().getResource("/css/CheckButtons.css").toExternalForm());
                tempButton.setAlignment(Pos.BASELINE_LEFT);
                tempButton.setContentDisplay(ContentDisplay.LEFT);
                tempButton.setFont(Font.font(10));
                tempButton.setOnAction(event -> showRoomInfo(r));
                buttonBox.getChildren().add(tempButton);
            }
            roomPane.setContent(buttonBox);
            int l = split.length;
            roomCount.setText(String.valueOf(l));
            if (bookInfo[5].equals("1")) {
                payCheck.setSelected(true);
                payCheck.setDisable(true);
            }
            totPris.setText(bookInfo[6] + " kr");


        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void showRoomInfo(String[] rInfo) {
        sceneManager.ShowAlertChoiceB("Är du säker?", "Vill du visa mer info om rum " + rInfo[1] + " ?", rInfo[1]);
    }
    public void updateButton() {
        String p;
        if (payCheck.isSelected()) {
            p = "1";
        } else {
            p = "0";
        }
        String[] info = {updID.getText(), guestCount.getValue(), p};
        boolean updated = Booking.checkUpdateBooking(App.getConn(), info);
        if (updated) {
            sceneManager.ShowAlert("Godkänd", "Bokning uppdaterad");;
        } else {
            sceneManager.ShowAlert("Nekad", "Kunde ej uppdatera bokning");
        }
    }

    public void returnButton(ActionEvent event) {
        sceneManager.switchToHomeRoot();
    }

    public void createNewBooking() {
        sceneManager.switchToCreateBookingRoot(true);
    }
    public void deleteButton() {
        String i = updID.getText();
        sceneManager.ShowAlertChoice("Vill du ta bort bokning?", "Är du säker på att du vill ta bort bokning med boknings-id " + i + "?", i, false, true);
    }
}
