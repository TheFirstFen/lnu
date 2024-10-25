package www.example;


import java.util.Base64;
import java.security.MessageDigest;
import java.time.LocalDateTime;

public class Person {
    private String firstName = "";
    private String lastName = "";
    private int birthYear = 0;

    public Person setPersonDetails(String fName, String lName, int YearOfBirth) {
        this.firstName = fName;
        this.lastName = lName;
        this.birthYear = YearOfBirth;
        return null;
    }

    public String toString() {
        LocalDateTime now = LocalDateTime.now();
        int age = now.getYear() - birthYear;
        return "Person: " + firstName + " " + lastName + ", born " + birthYear + " (turning " + age + " this year), md5: " + Method.md5Hashe(firstName, lastName, birthYear);
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public int getYearOfBirth() {
        return birthYear;
    }
}

class Method{
    public static String md5Hashe(String fName, String lName, int YearOfBirth){
        try {
            MessageDigest m = MessageDigest.getInstance("MD5");
            String baseText = fName + lName + YearOfBirth;
            byte[] md5Hash = m.digest(baseText.getBytes());

            // make byte[] as base64 encoded string
            String base64Str = Base64.getEncoder().encodeToString(md5Hash);
            return base64Str;
        }
        catch (Exception e) {
            return "ERROR";
        }
    }
}