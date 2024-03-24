package hotel2.com.mid;

import java.util.regex.Pattern;
import java.sql.Connection;

public class WorkerArrayManager {

    // Method to create a worker
    public static boolean createValidWorker(Connection Connection, String[] workerData) {

        // Checks for null or ""
        for (String data : workerData) {
            if (data == null || data.trim().isEmpty()) {
                System.out.println("Invalid client data");
                return false;
            }
        }

        if (!isValidEmail(workerData[1])) {
            System.out.println("Invalid Email");
            //throw new IllegalArgumentException("Invalid Email");
            return false;
        }
        if (!isValidPhoneNumber(workerData[2])) {
            System.out.println("Invalid phone number");
            //throw new IllegalArgumentException("Invalid phone number);
            return false;
        }

        // Create a new worker
        return Worker.checkCreateWorker(Connection, workerData);
    }
    
    
    public static boolean editValidWorker(Connection Connection, String[] workerData) {

        // Checks for null or ""
        for (String data : workerData) {
            if (data == null || data.trim().isEmpty()) {
                return false;
            }
        }

        // Validate email, phone number, and name
        if (!isValidEmail(workerData[1])) {
            //throw new IllegalArgumentException("Invalid Email");
            return false;
        }
        if (!isValidPhoneNumber(workerData[2])) {
            //throw new IllegalArgumentException("Invalid phone number);
            return false;
        }
        

        // Update a worker
        return Worker.checkUppdateWorker(Connection, workerData);
    }

    public static boolean isValidEmail(String email) {
        // Basic email pattern check
        String emailRegex = "^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$";
        return Pattern.matches(emailRegex, email);
    }

    public static boolean isValidPhoneNumber(String phoneNumber) {
        // Basic phone number check: allowing digits and optional dashes or spaces
        return phoneNumber.matches("^[0-9-\\s]+$");
    }
}

    

