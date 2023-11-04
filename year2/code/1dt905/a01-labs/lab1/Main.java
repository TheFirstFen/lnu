import java.util.Scanner;
import java.util.Random;
import java.security.MessageDigest;
import java.util.Base64;
import java.time.LocalDateTime;

public class Main {
    public static void main(String[] args) throws Exception {
        Menu menu = new Menu();

        menu.menuLoop();
    }
}

class Menu {
    public void menuLoop() {
        Person person = new Person();

        while (true) {
            System.out.println("Main: ");
            System.out.println("1) Get random numbers between 1 and 100");
            System.out.println("2) Summarize numbers");
            System.out.println("P1) Enter details on the person");
            System.out.println("P2) Print details on the person");
            System.out.println("qQ) Quit");

            System.out.print("\nYour choice: ");

            Random rnd = new Random();
            Scanner sc = new Scanner(System.in);
            String input = sc.nextLine();

            if (input.equals("1")) {
                Methods.randomNumbers(sc, rnd);
            } else if (input.equals("2")) {
                Methods.summarizeNumbers(sc);
            } else if (input.equals("P1")) {
                Methods.addPerson(sc, person);
            } else if (input.equals("P2")) {
                Methods.printPerson(person);
            } else if (input.equals("q") || input.equals("Q")) {
                System.out.println("Goodbye!");
                sc.close();
                break;
            } else {
                System.out.println("Please input an appropriate value.");
            }
        }
    }
}

class Person {

    private String firstName = "";
    private String lastName = "";
    private int birthYear = 0;

    public Person setFirstName(String fName) {
        firstName = fName;
        return null;
    }

    public Person setLastName(String lName) {
        lastName = lName;
        return null;
    }

    public Person setBirthYear(int yearOfBirth) {
        birthYear = yearOfBirth;
        return null;
    }

    public String getId() {
        String output = md5Hash(lastName, firstName, birthYear);
        return output;
    }

    public String toString() {
        LocalDateTime now = LocalDateTime.now();
        String output = "Person: " + firstName + " " + lastName + ", born " + birthYear + " (turning " + (now.getYear() - birthYear) + " this year), md5: " + getId();
        
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
}

class Methods {
    public static void randomNumbers(Scanner sc, Random rnd) {
        System.out.print("How many random numbers do you want to see? ");
            
        int amount = sc.nextInt();
        int num = 0;
        int sum = 0;
        
        for (int i = 0; i < amount; i++) {
            num = rnd.nextInt(100);
            System.out.print(num + " ");
            sum += num;
        }
        
        System.out.println("\nThe sum is: " + sum + "\n");
    }

    public static void summarizeNumbers(Scanner sc) {
        System.out.println("Enter the numbers, separated by space, end with newline:");
        System.out.print("> ");
        String nums = sc.nextLine();
        
        String[] numsAsString = nums.split(" ");

        int amount = 0;
        int sum = 0;

        for (String numStr : numsAsString) {
            int num = Integer.parseInt(numStr);
            sum += num;
            amount++;
        }

        System.out.println("You entered " + amount + " numbers.");
        System.out.println("The sum is: " + sum + "\n");
    }

    public static Person addPerson(Scanner sc, Person person) {
        System.out.println("Enter firstname, lastname and birth year of the person.");
        System.out.print("> First name: ");
        person.setFirstName(sc.nextLine());

        System.out.print("> Last Name: ");
        person.setLastName(sc.nextLine());

        System.out.print("> Birth year: ");
        person.setBirthYear(sc.nextInt());

        System.out.println("Thank you!");
        System.out.println(person.toString() + "\n");

        return person;
    }

    public static void printPerson(Person person) {
        System.out.println(person.toString() + "\n");
    }
}