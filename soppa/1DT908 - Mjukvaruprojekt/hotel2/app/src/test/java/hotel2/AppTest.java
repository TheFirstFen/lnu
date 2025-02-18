/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package hotel2;

import javafx.application.Application;
import javafx.stage.Stage;
import java.sql.Connection;
import java.text.ParseException;

import hotel2.com.mid.Connector;
import hotel2.com.mid.Customer;
import hotel2.com.mid.Loggin;
import hotel2.com.mid.Worker;
import hotel2.com.mid.Room;
import hotel2.GUI.SceneManager;
import hotel2.com.mid.Booking;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AppTest {
    
}

/*
 * This Java source file was generated by the Gradle 'init' task.
 */



// public class App extends Application {
//     private static Connection connection;
//     private static SceneManager manager;
//     @Override
//     public void start(Stage startStage) throws Exception {
//         startStage.setFullScreen(true);
//         // startStage.setResizable(false);
//         SceneManager sceneManagerMain = new SceneManager(startStage);
//         manager = sceneManagerMain;
//         sceneManagerMain.switchToLoginRoot();
//     }
//     public static void main(String[] args) throws ParseException {
//         String[] loggin = new String[7];
//         loggin[0] = "Admin"; // username
//         loggin[1] = "Admin@hotel2.com"; // email
//         loggin[2] = "0700000000"; // number
//         loggin[3] = "1"; // role
//         loggin[4] = "Admin"; // password
//         loggin[5] = "1"; //userId
//         loggin[6] = "hotel2"; //hotel

//         String email = loggin[2];
//         String password = loggin[4];

//         System.out.println("Worker part test");

//         connection = Connector.Connect(email, password);
        
//         Worker.checkCreateWorker(connection, loggin);
//         Loggin.main(connection, loggin);

//         Worker.checkUppdateWorker(connection, loggin);

//         String[] workers = new String[2];
//         workers[0] = "Email";
//         workers[1] = "A";

//         System.out.println("view all workers Email");
//         String[][] result = Worker.checkALLWorkers(connection, workers);
//         if (result != null) {
//             for (String[] row : result) {
//                 for (String value : row) {
//                     System.out.print(value + "\t");
//                 }
//                 System.out.println();
//             }
//         } else {
//             System.out.println("No result or an error occurred.");
//         }

//         workers[0] = "Name";
//         System.out.println("view all workers name");
//         result = Worker.checkALLWorkers(connection, workers);
//         if (result != null) {
//             for (String[] row : result) {
//                 for (String value : row) {
//                     System.out.print(value + "\t");
//                 }
//                 System.out.println();
//             }
//         } else {
//             System.out.println("No result or an error occurred.");
//         }

//         String[] search = new String[2];
//         search[0] = "email";
//         search[1] = "t";

        
//         search[0] = "id";
//         search[1] = "2";
//         System.out.println("\nWorker id search: " + search[0] + " " + search[1]);
//         result = Worker.checkALLWorkers(connection, search);
//         if (result != null) {
//             for (String[] row : result) {
//                 for (String value : row) {
//                     System.out.print(value + "\t");
//                 }
//                 System.out.println();
//             }
//         } else {
//             System.out.println("No result or an error occurred.");
//         }


//         System.out.println("\nCustomer part test");
//         String[][] result2 = Customer.checkForAllCustomers(connection, search);
//         if (result2 != null) {
//             for (String[] row : result2) {
//                 for (String value : row) {
//                     System.out.print(value + "\t");
//                 }
//                 System.out.println();
//             }
//         } else {
//             System.out.println("No result or an error occurred.");
//         }

//         String[] customer = new String[5];
//         customer[0] = "John";
//         customer[1] = "Doe";
//         customer[2] = "test@jhon.com";
//         customer[3] = "0800000000";
//         customer[4] = "Swish";

//         Customer.checkForCreation(connection, customer);

//         String[][] result3 = Customer.checkForAllCustomers(connection, search);

//         if (result3 != null) {
//             for (String[] row : result3) {
//                 for (String value : row) {
//                     System.out.print(value + "\t");
//                 }
//                 System.out.println();
//             }
//         } else {
//             System.out.println("No result or an error occurred.");
//         }

//         System.out.println("\nLatest customer part test");
//         String[] latest = Customer.latestCustomer(connection);
//         if (latest != null) {
//             for (String row : latest) {
//                 System.out.print(row + "\t");
//             }
//             System.out.println();
//         } else {
//             System.out.println("No result or an error occurred.");
//         }

//         //Customer.checkForGetCustomer(connection, customer);


//         System.out.println("\nRoom part test");
//         String[] rooms = new String[5];
//         rooms[0] = "101";
//         rooms[1] = "4";
//         rooms[2] = "Standard";
//         rooms[3] = "100.0";
//         rooms[4] = "hotel2";

//         Room.checkCreateRoom(connection, rooms);

//         rooms[0] = "102";
//         rooms[1] = "2";

//         Room.checkCreateRoom(connection, rooms);


//         String[] search2 = new String[2];
//         search2[0] = "roomnr";
//         search2[1] = "101";
//         System.out.println("\nRoom number search: " + search2[1]);
//         String[][] result4 = Room.getRooms(connection, search2);
//         if (result4 != null) {
//             for (String[] row : result4) {
//                 for (String value : row) {
//                     System.out.print(value + "\t");
//                 }
//                 System.out.println();
//             }
//         }
//         else {
//             System.out.println("No result or an error occurred.");
//         }

//         search2[0] = "roomsize";
//         search2[1] = "4";
//         System.out.println("\nRoom size search: " + search2[1]);
//         result4 = Room.getRooms(connection, search2);
//         if (result4 != null) {
//             for (String[] row : result4) {
//                 for (String value : row) {
//                     System.out.print(value + "\t");
//                 }
//                 System.out.println();
//             }
//         }
//         else {
//             System.out.println("No result or an error occurred.");
//         }

//         String[] search3 = new String[2];
//         search3[0] = "roomtype";
//         search3[1] = "Standard";
//         System.out.println("\nRoom type search: " + search3[1]);
//         String[][] result5 = Room.getRooms(connection, search3);
//         if (result5 != null) {
//             for (String[] row : result5) {
//                 for (String value : row) {
//                     System.out.print(value + "\t");
//                 }
//                 System.out.println();
//             }
//         }
//         else {
//             System.out.println("No result or an error occurred.");
//         }

//         String[] test = new String[2];
//         test[0] = "all";
//         test[1] = "1";
//         System.out.println("All rooms: ");
//         result4 = Room.getRooms(connection, test);
        
//         if (result4 != null) {
//             for (String[] row : result4) {
//                 for (String value : row) {
//                     System.out.print(value + "\t");
//                 }
//                 System.out.println();
//             }
//         }
//         else {
//             System.out.println("No result or an error occurred.");
//         }

//         System.out.println("\nBooking part test");


//         String[] booking = new String[8];
//         booking[0] = "2024-01-01";
//         booking[1] = "2024-01-05";
//         booking[2] = "1 2";
//         booking[3] = "2";
//         booking[4] = "0";
//         booking[5] = "100.0";
//         booking[6] = "2";
//         booking[7] = "2";

//         Booking.checkCreateBooking(connection, booking);

//         String[] testBooking = new String[8];
//         testBooking[0] = "2023-12-30";
//         testBooking[1] = "2024-01-01";
//         testBooking[2] = "1";
//         testBooking[3] = "2";
//         testBooking[4] = "0";
//         testBooking[5] = "100.0";
//         testBooking[6] = "2";
//         testBooking[7] = "2";

//         Booking.checkCreateBooking(connection, testBooking);

//         testBooking[0] = "2024-01-05";
//         testBooking[1] = "2024-01-08";
//         testBooking[2] = "2";

//         Booking.checkCreateBooking(connection, testBooking);

//         testBooking[0] = "2024-01-02";
//         testBooking[1] = "2024-01-07";

//         Booking.checkCreateBooking(connection, testBooking);

//         search[0] = "startdate";
//         search[1] = "2024-01-01";
//         System.out.println("\nBooking search by startdate:" + search[1]);
//         String[][] result6 = Booking.getBookings(connection, search);

//         if (result6 != null) {
//             for (String[] row : result6) {
//                 for (String value : row) {
//                     System.out.print(value + "\t");
//                 }
//                 System.out.println();
//             }
//         }
//         else {
//             System.out.println("No result or an error occurred.");
//         }

        
//         search[0] = "enddate";
//         search[1] = "2024-01-08";
//         System.out.println("\nBooking search by enddate:" + search[1]);
//         result6 = Booking.getBookings(connection, search);

//         if (result6 != null) {
//             for (String[] row : result6) {
//                 for (String value : row) {
//                     System.out.print(value + "\t");
//                 }
//                 System.out.println();
//             }
//         }
//         else {
//             System.out.println("No result or an error occurred.");
//         }

//         search[0] = "customerid";
//         search[1] = "2";
//         System.out.println("\nBooking search by customerid:" + search[1]);
//         result6 = Booking.getBookingCustomer(connection, search);

//         if (result6 != null) {
//             for (String[] row : result6) {
//                 for (String value : row) {
//                     System.out.print(value + "\t");
//                 }
//                 System.out.println();
//             }
//         }
//         else {
//             System.out.println("No result or an error occurred.");
//         }

//         search[0] = "roomid";
//         search[1] = "2";
//         System.out.println("\nBooking search by roomid:" + search[1]);
//         result6 = Booking.getBookingRoom(connection, search);
//         if (result6 != null) {
//             for (String[] row : result6) {
//                 for (String value : row) {
//                     System.out.print(value + "\t");
//                 }
//                 System.out.println();
//             }
//         }
//         else {
//             System.out.println("No result or an error occurred.");
//         }

//         String[] checkin = new String[2];
//         checkin[0] = "2";
//         checkin[1] = "0";
//         Booking.checkIn(connection, checkin);


//         search[0] = "2024-01-01";
//         System.out.println("\nBooking checkin today:" + search[0]);
//         result6 = Booking.checkInToday(connection, search);
//         if (result6 != null) {
//             for (String[] row : result6) {
//                 for (String value : row) {
//                     System.out.print(value + "\t");
//                 }
//                 System.out.println();
//             }
//         }
//         else {
//             System.out.println("No result or an error occurred.");
//         }

//         search[0] = "2024-01-01";
//         System.out.println("\nBooking checkout today:" + search[0]);
//         result6 = Booking.checkOutToday(connection, search);
//         if (result6 != null) {
//             for (String[] row : result6) {
//                 for (String value : row) {
//                     System.out.print(value + "\t");
//                 }
//                 System.out.println();
//             }
//         }
//         else {
//             System.out.println("No result or an error occurred.");
//         }

//         search[0] = "2024-02-01";
//         search[1] = "2024-02-08";
//         System.out.println("\nEmpty rooms between startdate " + search[0] + " and enddate " + search[1]);
//         result6 = Booking.getRoomsNotBooked(connection, search);
//         if (result6 != null) {
//             for (String[] row : result6) {
//                 for (String value : row) {
//                     System.out.print(value + "\t");
//                 }
//                 System.out.println();
//             }
//         }
//         else {
//             System.out.println("No result or an error occurred.");
//         }


//         search[0] = "2024-01-01";
//         search[1] = "2024-01-08";
//         String[] emptyRoom = Booking.getAmountOfEmptyRooms(connection, search);
//         for (String amount : emptyRoom) {
//             System.out.println("Amount of empty rooms: " + amount);
//         }
        
//         String[][] emptyRooms = Booking.getEmptyRoomsPerDay(connection, search);
//         for (String[] day : emptyRooms) {
//             System.out.println("Empty roomid for each day: ");
//             for (String roomid : day) {
//                 System.out.print(roomid + " ");
//             }
//             System.out.println();
//         }

//         String[] testsearch = new String[3];
//         testsearch[0] = "2024-01-10";
//         testsearch[1] = "2024-01-12";
//         testsearch[2] = "2";
//         boolean isAvailable = Booking.isRoomAvailable(connection, testsearch);
//         System.out.println("Is room "+ testsearch[2] + " available between " + testsearch[0] + " and " + testsearch[1] + " : " + isAvailable);


//         search[0] = "customerid";
//         search[1] = "2";
//         System.out.println("\nBooking search by customerid:" + search[1]);
//         result6 = Booking.getBookingCustomer(connection, search);

//         if (result6 != null) {
//             for (String[] row : result6) {
//                 for (String value : row) {
//                     System.out.print(value + "\t");
//                 }
//                 System.out.println();
//             }
//         }
//         else {
//             System.out.println("No result or an error occurred.");
//         }

//         testsearch[0] = "2";
//         testsearch[1] = "3";
//         testsearch[2] = "1";
//         boolean updated = Booking.checkUpdateBooking(connection, testsearch);

//         System.out.println("Updated booking: " + updated);

//         search[0] = "customerid";
//         search[1] = "2";
//         System.out.println("\nBooking search by customerid:" + search[1]);
//         result6 = Booking.getBookingCustomer(connection, search);

//         if (result6 != null) {
//             for (String[] row : result6) {
//                 for (String value : row) {
//                     System.out.print(value + "\t");
//                 }
//                 System.out.println();
//             }
//         }
//         else {
//             System.out.println("No result or an error occurred.");
//         }

//         launch(args);
//         Connector.CloseConnection(connection);

//     }
//     public static Connection getConn() {
//         return connection;
//     }
//     public static SceneManager getManager() {
//         return manager;
//     }
// }

