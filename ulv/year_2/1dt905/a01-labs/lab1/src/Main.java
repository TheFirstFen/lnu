import java.util.Scanner;
import java.util.Random;
import java.util.Base64;
import java.security.MessageDigest;
import java.time.LocalDateTime;

public class Main {
    public static void main(String[] args){

        Menu menu = new Menu();
        menu.menuLoop();
 
    }
}

class Menu {
    public void menuLoop(){
        
        Person person = new Person();
        while(true) {
            Random random = new Random();
            Scanner scanner = new Scanner(System.in);

            System.out.println("Menu: ");
            System.out.println("1) Get random numbers between 1 and 100");
            System.out.println("2) Summarize numbers");
            System.out.println("p1 Enter details on person: ");
            System.out.println("p2 Show info on person");
            System.out.println("q) quit");
            System.out.print("\nYour choice: ");
            String choice = scanner.nextLine();
            System.out.println("\nYour choice: "+choice);

            if (choice.equals("1")){
                Method.randomNumber(scanner, random);
            }
            else if (choice.equals("2")){
                Method.sumNumber(scanner);
            }
            else if (choice.equals("p1")){
                Method.enterInfo(scanner, person);
            }
            else if (choice.equals("p2")){
                Method.showInfo(person);
            }
            else if (choice.equals("q")){
                scanner.close();
                break;
            }
            else {
                System.out.println("Wrong input!");
            } 
           
        }
    }
}

class Person{
    private String firstName = "";
    private String lastName = "";
    private int birthYear = 0;

    public Person setPersonDetails(String fName, String lName, int YearOfBirth) {
        firstName = fName;
        lastName = lName;
        birthYear = YearOfBirth;
        return null;
    }

    public String toString() {
        LocalDateTime now = LocalDateTime.now();
        int age = now.getYear() - birthYear;
        return "Person: " + firstName + " " + lastName + ", born " + birthYear + " (turning " + age + " this year), md5: " + Method.md5Hashe(firstName, lastName, birthYear);
    }
}


class Method{
    public static void randomNumber(Scanner scanner, Random random){
        System.out.print("How many random numbers do you want to see? ");
        int number = scanner.nextInt();
        int s = 0;
        for(int i=0; i<number; i++){
            int x = random.nextInt(100);
            System.out.print(x+" ");
            s += x;
            }
        System.out.print("\nSum: "+s);
    }
    

    public static void sumNumber(Scanner scanner){
        System.out.println("Enter the numbers, separated by space, end with newline:");
        String input = scanner.nextLine();

        String[] numbers = input.split(" ");
        int num = numbers.length;
        int s = 0;
        for(String numberStr : numbers){
            int number = Integer.parseInt(numberStr);
            s = s + number;
        }
        System.out.println("You entered" + num + "numbers");
        System.out.println("The sum is: " + s);
    }


    public static void enterInfo(Scanner scanner, Person person) {
        System.out.println("Enter firstname, lastname and birth year of the person.");
        System.out.print("First name:");
        String fName = scanner.nextLine();
        System.out.print("Last name: ");
        String lName = scanner.nextLine();
        System.out.print("Birth year: ");
        int YearOfBirth = scanner.nextInt();

        person.setPersonDetails(fName, lName, YearOfBirth);
        
        LocalDateTime now = LocalDateTime.now();
        int age = now.getYear() - YearOfBirth;

        String md5 = md5Hashe(fName, lName, YearOfBirth);
        System.out.println(fName + " " + lName + " born " + YearOfBirth + " (turning " + (age + 1) + " this year) md5: " + md5);
    }


    public static void showInfo(Person person){
        System.out.println(person.toString());    
    }


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
