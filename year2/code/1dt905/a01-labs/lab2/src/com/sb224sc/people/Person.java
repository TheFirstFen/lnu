package com.sb224sc.people;

import java.security.MessageDigest;
import java.time.LocalDateTime;
import java.util.Base64;
import java.util.Scanner;

public class Person {
    private String firstName = "";
    private String lastName = "";
    private int birthYear = 0;

    public Person setAllDetails(String fName, String lName, int yearOfBirth) {
        firstName = fName;
        lastName = lName;
        birthYear = yearOfBirth;
        return null;
    }

    public Person setFirstName(String fName) {
        firstName = fName;
        return null;
    }

    public Person setLastName(String lName) {
        lastName = lName;
        return null;
    }

    public String getName() {
        return firstName + " " + lastName;
    }

    public Person setBirthYear(int yearOfBirth) {
        birthYear = yearOfBirth;
        return null;
    }

    public int getBirthYear() {
        return birthYear;
    }

    public int getAge() {
        LocalDateTime now = LocalDateTime.now();

        return now.getYear() - birthYear;
    }

    public String getId() {
        String output = md5Hash(lastName, firstName, birthYear);
        return output;
    }

    public String toString() {
        String output = "Person: " + getName() + ", born " + getBirthYear() +
                        " (turning " + getAge() + " this year), md5: " + getId();
        
        return output;
    }

    public String md5Hash(String fName, String lName, int dateOfBirth) {
        try {
            MessageDigest m = MessageDigest.getInstance("MD5");
            String baseText = fName + lName + dateOfBirth;
            byte[] md5Hash = m.digest(baseText.getBytes());
            String base64Str = Base64.getEncoder().encodeToString(md5Hash);

            return base64Str;
        } catch (Exception e) {
            System.out.println(e);

            return "Error";
        }
    }

    public Person memberCreation(Person person, Scanner sc) {
        try {
            System.out.print("Firstname: ");
            person.setFirstName(sc.nextLine());
            System.out.print("Lastname: ");
            person.setLastName(sc.nextLine());
            System.out.print("Birthyear: ");
            person.setBirthYear(sc.nextInt());

            sc.nextLine();

            return person;
        } catch (Exception e) {
            System.out.println(e);
            return null;
        }
    }
}
