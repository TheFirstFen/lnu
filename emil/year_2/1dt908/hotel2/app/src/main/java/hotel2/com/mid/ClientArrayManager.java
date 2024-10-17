package hotel2.com.mid;


import java.util.regex.Pattern;
import java.sql.Connection;


public class ClientArrayManager {

    public static boolean createClient(Connection Connection, String[] clientData) {

        // Checks for null or ""
        for (String data : clientData) {
            if (data == null || data.trim().isEmpty()) {
                System.out.println("Invalid client data");
                return false;
            }
        } 

        // Validate email, phone number, and name
        if (!isValidEmail(clientData[2])) {
            System.out.println("Invalid Email");
            //throw new IllegalArgumentException("Invalid Email");
            return false;
        }
        if (!isValidPhoneNumber(clientData[3])) {
            System.out.println("Invalid phone number");
            //throw new IllegalArgumentException("Invalid phone number);
            return false;
        }
        if (!containsOnlyLetters(clientData[0])) {
            System.out.println("Invalid First name");
            //throw new IllegalArgumentException("Invalid First name");
            return false;
        }
        if (!containsOnlyLetters(clientData[1])) {
            System.out.println("Invalid Last name");
            //throw new IllegalArgumentException("Invalid Last name");
            return false;
        }
 
        // Create a new customer
        return Customer.checkForCreation(Connection, clientData);
    }
     
    
    public static boolean editClient(Connection Connection, String[] clientData) {
        if (clientData.length != 6) {
            throw new IllegalArgumentException("Invalid client data");
        }
 
        // Checks for null or ""
        for (String data : clientData) {
            if (data == null || data.trim().isEmpty()) {
                return false;
            }
        }
 
        // Validate email, phone number, and name
        if (!isValidEmail(clientData[3])) {
            //throw new IllegalArgumentException("Invalid Email");
            return false;
        }
        if (!isValidPhoneNumber(clientData[4])) {
            //throw new IllegalArgumentException("Invalid phone number);
            return false;
        }
        if (!containsOnlyLetters(clientData[1])) {
            //throw new IllegalArgumentException("Invalid First name");
            return false;
        }
        if (!containsOnlyLetters(clientData[2])) {
            //throw new IllegalArgumentException("Invalid Last name");
            return false;
        }

        // Update a customer
        return Customer.checkForUppdate(Connection, clientData);
    }
 
    public static boolean isValidEmail(String email) {
        // Email pattern check
        String emailRegex = "^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$";
        return Pattern.matches(emailRegex, email);
    }

    public static boolean isValidPhoneNumber(String phoneNumber) {
        // Basic phone number check: allowing digits and optional dashes or spaces
        return phoneNumber.matches("^[0-9-\\s]+$");
    }
 
    public static boolean containsOnlyLetters(String name) {
        // Only letters and "-" are allowed in the name
        return name.matches("^[a-zA-ZéêüåäöÅÖÄøÆæ-]+$");
    }
}
   
 