package hotel2.GUI;

import hotel2.App;
import hotel2.com.mid.Booking;
import hotel2.com.mid.Room;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.VBox;

import java.util.Arrays;
import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.Month;
import java.time.format.DateTimeFormatter;

public class RoomController {
    @FXML TextField SearchField1;

    @FXML Label prid;
    @FXML Label psize;
    @FXML Label ptype;
    @FXML Label ppris;
    @FXML Label photel;
    @FXML Label pstatus;
    @FXML Label rnr;
    @FXML VBox CalenderBox;
    @FXML Label monthLabel;
    @FXML Button leftArrowID;
    @FXML Button rightArrowID;

    private SceneManager sceneManager;
    private int monthChanger;
    private String currMonth;

    public void setManager(SceneManager manager) {
        sceneManager = manager;
    }
    public void setupPage() {
        monthChanger = 0;
        updateCalender("First");
    }
    public void setUpSearch(String rid) {
        SearchField1.setText(rid);
        SearchForRoom();
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
        } else {
            monthChanger = 0;
        }

        GridPane calendarPane = new GridPane();

        String[] daysOfWeek = {"Mån", "Tis", "Ons", "Tors", "Fre", "Lör", "Sön"};

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
                    calendarPane.add(new DaySquare(sceneManager, 154, 63, String.valueOf(totalDaysPrevMonth), true, isCurrentDay, currentMonth.toString(), currentYear, false), col, row);
                    totalDaysPrevMonth ++;
                } else if (dayCounter <= totalDaysInMonth) {
                    calendarPane.add(new DaySquare(sceneManager, 154, 63, String.valueOf(dayCounter), false, isCurrentDay, currentMonth.toString(), currentYear, false), col, row);
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

    
    @SuppressWarnings("resource")
    public void SearchForRoom() {
        String searchWord = SearchField1.getText();
        try {
            String[][] displayBooking;
            String[] room = {"Room Number", searchWord};
            if (Room.getRooms(App.getConn(), room).length != 0) {
                String word = Room.getRooms(App.getConn(), room)[0][0];
                String[] info = {"roomid", word};
                if (Booking.getBookingRoom(App.getConn(), info) != null) {
                    displayBooking = Booking.getBookingRoom(App.getConn(), info);
                    Arrays.sort(displayBooking, (booking1, booking2) -> {
                        LocalDate startDate1 = LocalDate.parse(booking1[1], DateTimeFormatter.ISO_LOCAL_DATE);
                        LocalDate startDate2 = LocalDate.parse(booking2[1], DateTimeFormatter.ISO_LOCAL_DATE);
                        return startDate1.compareTo(startDate2);
                    });
                    String[] cRoom = Room.getRooms(App.getConn(), room)[0];
                    sceneManager.setrid(cRoom[0]);
                    prid.setText(cRoom[0]);
                    psize.setText(cRoom[2]);
                    ptype.setText(cRoom[3]);
                    ppris.setText(cRoom[4] + " kr");
                    photel.setText(cRoom[5]);
                    pstatus.setText(cRoom[6].equals("0") ? "aktivt" : "inaktivt");
                    rnr.setText(searchWord);
                    setCalender(displayBooking);
                }
            } else {
                sceneManager.ShowAlert("Saknas rum", "Rum med rumsnummer " + searchWord + " saknas.");
            }
        } catch (NumberFormatException e) {
            sceneManager.ShowAlert("Saknas rum", "Rum med rumsnummer " + searchWord + " saknas.");
        }
    }
    private void setCalender(String[][] booking) {
        sceneManager.setCurrentRoomBookings(booking);
        updateCalender("first");
    }

    public void returnButton(ActionEvent event) {
        sceneManager.switchToHomeRoot();
    }
    public void LeftArrow(ActionEvent event) {
        updateCalender("left");
    }
    public void RightArrow(ActionEvent event) {
        updateCalender("right");
    }


}
