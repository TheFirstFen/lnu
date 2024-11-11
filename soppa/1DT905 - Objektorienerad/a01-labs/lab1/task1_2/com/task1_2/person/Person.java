package task1_2.com.task1_2.person;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;
import java.time.LocalDateTime;

public class Person {
    // Set default values
    private String firstName = "First name";
    private String lastName = "Last name";
    private Integer birthYear = 2000;

    // Set and get functions, so i can use private properties
    public void setFirstName (String name){
        this.firstName = name;
    }

    public void setLastName (String name){
        this.lastName = name;
    }

    public void setBirthYear (Integer year){
        this.birthYear = year;
    }
    
    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public Integer getBirthYear() {
        return birthYear;
    }

    // Calculates the md5 hash
    public String getId () {
        String base64Str = "";
        try {
            MessageDigest msg = MessageDigest.getInstance("MD5");
            String baseText = this.firstName + this.lastName + this.birthYear;
            byte[] md5Hash = msg.digest(baseText.getBytes());
            base64Str = Base64.getEncoder().encodeToString(md5Hash);
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        return base64Str;
    }

    // Prints the person to string
    public String toString () {
        LocalDateTime now = LocalDateTime.now();
        Integer currentAge = now.getYear() - this.birthYear;
        String namestring = "Person: " + this.firstName + " " + this.lastName +
                            ", born in " + this.birthYear + " (turning " + currentAge +
                            " this year), md5: " + getId() + "\n";
        return namestring;
    }
}