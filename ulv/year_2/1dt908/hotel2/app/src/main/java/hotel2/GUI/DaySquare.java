package hotel2.GUI;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.Month;
import java.util.Calendar;
import java.util.Date;

import hotel2.App;
import hotel2.com.mid.Booking;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Line;
import javafx.scene.shape.Rectangle;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import java.time.LocalDate;


public class DaySquare extends StackPane {
    private Label label;
    private Label emptyRoomsLabel;
    private Label checkInLabel;
    private Label checkOutLabel;
    
    private String bid;
    private SceneManager sceneManager;


    @SuppressWarnings("resource")
    public DaySquare(SceneManager manager, double width, double height, String text, Boolean isPrevious, Boolean isCurrentDay, String month, Integer year, Boolean mainPage) {
        sceneManager = manager;
        Rectangle border = new Rectangle(width, height);
        Circle circle = new Circle();
            
            label = new Label(text);
            try {
                Integer.parseInt(label.getText());
                label.setTranslateX(-60);
                label.setTranslateY(-20);
            } catch (NumberFormatException e) {
                // Continue if its a weekday
            }
            label.setFont(Font.font("Arial", FontWeight.BOLD, 12));
            border.setStroke(Color.BLACK);
        if (mainPage) {
            emptyRoomsLabel = new Label();
            checkInLabel = new Label();
            checkOutLabel = new Label();
            Line line = new Line();
            Button dayButton = new Button();
            dayButton.setPrefHeight(height);
            dayButton.setPrefWidth(width);
            dayButton.setOpacity(0);
            
            border.setFill(null);
            if (isPrevious) {
                border.setFill(Color.GRAY);
            } else if (month != null){
                border.setFill(Color.WHITE);
                if (text.length() == 1) {
                    text = "0" + text;
                }
                String dateString = year + "-" + convertToNumeric(month) + "-" + text;
                if (LocalDate.parse(dateString).equals(LocalDate.now())) {
                    circle.setRadius(10); // Set the radius
                    circle.setStroke(Color.BLACK); // Set the stroke color
                    circle.setStrokeWidth(3);
                    circle.setFill(Color.TRANSPARENT); 
                    circle.setTranslateX(-60);
                    circle.setTranslateY(-20);
                }
                dayButton.setOnAction(event -> showBookingsDate(dateString));
                if (isAfterToday(dateString)) {
                    String[] date = {dateString, dateString};
                    String[] date1 = {dateString};
                    line.setStroke(Color.BLACK);
                    line.setStartX(20);
                    line.setEndX(-20);
                    line.setStartY(-40);
                    line.setEndY(-10);
                    line.setTranslateY(-10);
                    line.setOpacity(1);
                    emptyRoomsLabel.setText("Lediga rum: " + Booking.getAmountOfEmptyRooms(App.getConn(), date)[0]);
                    Integer checkInAmount = -1;
                    Integer checkOutAmount = -1;
                    try {
                        checkInAmount = Booking.checkInToday(App.getConn(), date1).length;
                        checkOutAmount = Booking.checkOutToday(App.getConn(), date1).length;
                    } catch (ParseException e) {
                        e.printStackTrace();
                    }
                    checkInLabel.setText("In: " + checkInAmount.toString());
                    checkOutLabel.setText("Ut: " + checkOutAmount.toString());
                    checkInLabel.setTranslateX(-20);
                    checkInLabel.setTranslateY(-15);
                    checkOutLabel.setTranslateX(20);
                    emptyRoomsLabel.setTranslateY(20);
                    emptyRoomsLabel.setStyle("-fx-font-family: Arial; -fx-font-weight: bold; -fx-font-size: 12;");
                    if (Integer.parseInt(Booking.getAmountOfEmptyRooms(App.getConn(), date)[0]) <= 5) {
                        emptyRoomsLabel.setStyle("-fx-text-fill: red;-fx-font-family: Arial; -fx-font-weight: bold; -fx-font-size: 12;");
                    } else if (Integer.parseInt(Booking.getAmountOfEmptyRooms(App.getConn(), date)[0]) <= 15) {
                        emptyRoomsLabel.setStyle("-fx-text-fill: orange;-fx-font-family: Arial; -fx-font-weight: bold; -fx-font-size: 12;");
                    } else {
                        emptyRoomsLabel.setStyle("-fx-text-fill: green;-fx-font-family: Arial; -fx-font-weight: bold; -fx-font-size: 12;");
                    }
                }
            }
            
            checkInLabel.setFont(Font.font("Arial", FontWeight.BOLD, 12));
            checkOutLabel.setFont(Font.font("Arial", FontWeight.BOLD, 12));
            
            getChildren().addAll(border, label, emptyRoomsLabel, circle, checkInLabel, checkOutLabel, line, dayButton);
        } else {
            if (text.length() == 1) {
                text = "0" + text;
            }
            if (isPrevious) {
                border.setFill(Color.GRAY);
                getChildren().addAll(border, label);
            } else if (month != null){
                border.setFill(Color.WHITE);
            
                String dateString = year + "-" + convertToNumeric(month) + "-" + text;
                if (LocalDate.parse(dateString).equals(LocalDate.now())) {
                    circle.setRadius(10); // Set the radius
                    circle.setStroke(Color.BLACK); // Set the stroke color
                    circle.setStrokeWidth(3);
                    circle.setFill(Color.TRANSPARENT); 
                    circle.setTranslateX(-60);
                    circle.setTranslateY(-20);
                }
                
                if (!dateString.equals("2024-02-30") && !dateString.equals("2024-02-31")) {
                    LocalDate targetDate = LocalDate.parse(dateString);

                    Button dispButton1 = new Button();
                    Button dispButton2 = new Button();
                    Button dispButton3 = new Button();
                    Line line = new Line();
                    line.setStroke(Color.BLACK);
                    line.setStartX(40);
                    line.setEndX(-40);
                    line.setStartY(-20);
                    line.setEndY(20);
                    line.setOpacity(0);
                    dispButton1.setPrefHeight(0);
                    dispButton1.setPrefWidth(0);
                    dispButton2.setPrefHeight(0);   
                    dispButton2.setPrefWidth(0); 
                    dispButton3.setPrefHeight(0);   
                    dispButton3.setPrefWidth(0); 
                    dispButton1.setStyle("-fx-background-color: rgba(255, 255, 255, 0);");            
                    dispButton2.setStyle("-fx-background-color: rgba(255, 255, 255, 0);");            
                    dispButton3.setStyle("-fx-background-color: rgba(255, 255, 255, 0);");            
                    dispButton1.setFont(Font.font("Arial", FontWeight.BOLD, 16));
                    dispButton2.setFont(Font.font("Arial", FontWeight.BOLD, 16));
                    dispButton3.setFont(Font.font("Arial", FontWeight.BOLD, 16));
                    if (sceneManager.getCurrentRoomBookings() != null) {
                        String[][] booking = sceneManager.getCurrentRoomBookings();
                        for (int i = 0; i < booking.length; i++) {
                            if (booking[i][1].equals(dateString)) {
                                dispButton1.setText((booking[i][0]));
                                dispButton1.setTranslateY(15);
                                dispButton1.setTranslateX(15);
                                dispButton1.setPrefHeight(25);
                                dispButton1.setPrefWidth(50);
                                dispButton1.setStyle("-fx-background-color: rgba(255, 255, 255, 1);");
                                String[] cB = booking[i];
                                dispButton1.setOnAction(event -> showBooking(cB));
                                line.setOpacity(1);
                            } else if (booking[i][2].equals(dateString)) {
                                dispButton2.setText((booking[i][0]));
                                dispButton2.setTranslateY(-15);
                                dispButton2.setTranslateX(-15);
                                dispButton2.setPrefHeight(25);   
                                dispButton2.setPrefWidth(50); 
                                dispButton2.setStyle("-fx-background-color: rgba(255, 255, 255, 1);"); 
                                String[] cB = booking[i];
                                dispButton2.setOnAction(event -> showBooking(cB));
                                line.setOpacity(1);
                            } else if (targetDate.isAfter(LocalDate.parse(booking[i][1])) && targetDate.isBefore(LocalDate.parse(booking[i][2]))) {
                                dispButton3.setText((booking[i][0]));
                                dispButton3.setPrefHeight(50);
                                dispButton3.setPrefWidth(75);
                                dispButton3.setStyle("-fx-background-color: rgba(255, 255, 255, 1);"); 
                                String[] cB = booking[i];
                                dispButton3.setOnAction(event -> showBooking(cB));
                            }
                        } 
                    }
                    getChildren().addAll(border, label, circle, dispButton1, dispButton2, dispButton3, line);
                }
            }
        }
    }
    @SuppressWarnings("resource")
    private void showBookingsDate(String dateString) {
        String[] info = {dateString};
        if (Booking.getBookingSingleDate(App.getConn(), info).length > 0) {
            sceneManager.ShowAlertChoice("Är du säker?", "Vill du visa bokningar för " + dateString + "?", dateString, true, false);
        } else {
            sceneManager.ShowAlert("Saknas bokningar", "Finns inga bokningar för datumet " + dateString + ".");
        }
    }

    private void showBooking(String[] book) {
        bid = book[0];
        sceneManager.ShowAlertChoice("Är du säker?", "Vill du visa mer info om bokning " + book[0] + " ?", bid, false, false);
    }

    public void setText(String text) {
        label.setText(text);
    }

    public static String convertToNumeric(String monthName) {
        monthName = monthName.toUpperCase();

        try {
            Month month = Month.valueOf(monthName);

            int monthValue = month.getValue();

            String monthString = String.format("%02d", monthValue);

            return monthString;
        } catch (IllegalArgumentException e) {
            return null;
        }
    }
    public static boolean isAfterToday(String dateString) {
        try {
            // Parse the input date string
            Date date = new SimpleDateFormat("yyyy-MM-dd").parse(dateString);

            // Get today's date
            Calendar today = Calendar.getInstance();
            today.set(Calendar.HOUR_OF_DAY, 0);
            today.set(Calendar.MINUTE, 0);
            today.set(Calendar.SECOND, 0);
            today.set(Calendar.MILLISECOND, 0);

            // Create a calendar object for the parsed date
            Calendar parsedDate = Calendar.getInstance();
            parsedDate.setTime(date);

            // Set the time components (hours, minutes, seconds, milliseconds) of parsedDate to zero for accurate comparison
            parsedDate.set(Calendar.HOUR_OF_DAY, 0);
            parsedDate.set(Calendar.MINUTE, 0);
            parsedDate.set(Calendar.SECOND, 0);
            parsedDate.set(Calendar.MILLISECOND, 0);

            // Compare the parsed date with today's date
            return !parsedDate.before(today);
        } catch (ParseException e) {
            // Handle parsing errors
            e.printStackTrace();
            return false;
        }
    }
}


