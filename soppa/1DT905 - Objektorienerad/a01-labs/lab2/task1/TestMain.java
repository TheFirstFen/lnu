package task1;

import java.util.Scanner;

import task1.com.task1.superman_woman.Superman;
import task1.com.task1.superman_woman.Superwoman;
import task1.com.task1.superman_woman.Superanimal;

public class TestMain {
    private static boolean exitprogram = false;

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in); // Creates new scanner instance
        while (true) {
            System.out.println("Menu:\n" +
                               "1) Superman menu\n" +
                               "2) Superwoman menu\n" +
                               "3) Superanimal menu\n" +
                               "q) Quit\n");
            System.out.print("Your choice: ");
            String choice = scanner.nextLine();
            if (choice.equalsIgnoreCase("q")) {
                System.out.println("Exiting the program...");
                break;
            } else {
                check_input_choice(choice, scanner);
            }
            if (exitprogram) {
                System.out.println("Exiting the program...");
                break;
        }
        }
        scanner.close(); 
    }

    public static void check_input_choice(String choice, Scanner scanner) {
        if (choice.equals("1")) {
            menuSuperman(scanner);
        } else if (choice.equals("2")) {
            menuSuperwoman(scanner);
        } else if (choice.equalsIgnoreCase("3")) {
            menuSuperanimal(scanner);
        } else if (choice.equalsIgnoreCase("q")) {
            exitprogram = true;
        } else {
            System.out.print("Incorrect input, try again: ");
            String Newchoice = scanner.nextLine();
            check_input_choice(Newchoice, scanner);
        }
    }

    
    // Testing superman creation and methods
    public static void menuSuperman(Scanner scanner) {
        Superman superman = new Superman();
        while (true) {
            System.out.println("Menu:\n" +
                       "1) Create new superman\n" +
                       "2) Change to random hat\n" +
                       "3) Change to hat of your choice\n" +
                       "4) Printdetails\n" +
                       "5) Add/remove hat\n" +
                       "q) Quit\n");
            System.out.print("Your choice: ");
            String choice = scanner.nextLine();
            if (choice.equalsIgnoreCase("q")) {
                System.out.println("Exiting the program...");
                break;
            } else {
                input_superman(choice, scanner, superman);
            }
        }
    }

    public static void input_superman (String choice, Scanner scanner, Superman superman) {
        if (choice.equals("1")) {
            addSuperman(scanner, superman);
        } else if (choice.equals("2")) {
            String randomHat = ((Superman) superman).changeToRandomHat();
            System.out.println("Changed hat to a " + randomHat);
        } else if (choice.equalsIgnoreCase("3")) {
            System.out.println("What hat should he have? ");
            String newHat = scanner.nextLine();
            ((Superman) superman).changeHat(newHat);
        } else if (choice.equalsIgnoreCase("4")) {
            System.out.println(((Superman) superman).toString());
        } else if (choice.equalsIgnoreCase("5")) {
            ((Superman) superman).changeHatStatus();
            System.out.println("Changed hat status");
        } else { 
            System.out.print("Incorrect input, try again: ");
            String Newchoice = scanner.nextLine();
            input_superman(Newchoice, scanner, superman);
        }
    }

    // Testing superwoman creation and methods
    public static void menuSuperwoman(Scanner scanner) {
        Superwoman superwoman = new Superwoman();
        while (true) {
            System.out.println("Menu:\n" +
                       "1) Create new superwoman\n" +
                       "2) Use weapon\n" +
                       "3) Change weapon\n" +
                       "4) Print details\n" +
                       "q) Quit\n");
            System.out.print("Your choice: ");
            String choice = scanner.nextLine();
            if (choice.equalsIgnoreCase("q")) {
                System.out.println("Exiting the program...");
                break;
            } else {
                input_superwoman(choice, scanner, superwoman);
            }
        }
    }

    public static void input_superwoman (String choice, Scanner scanner, Superwoman superwoman) {
        if (choice.equals("1")) {
            addSuperwoman(scanner, superwoman);
        } else if (choice.equals("2")) {
            Integer damage = ((Superwoman) superwoman).useWeapon();
            System.out.println(((Superwoman) superwoman).getWeapon() + " was used, " + damage + " damage was made!");
        } else if (choice.equalsIgnoreCase("3")) {
            System.out.println("What weapon should she have? ");
            String newWeapon = scanner.nextLine();
            ((Superwoman) superwoman).setWeapon(newWeapon);
        } else if (choice.equalsIgnoreCase("4")) {
            System.out.println(((Superwoman) superwoman).toString());
        } else {
            System.out.print("Incorrect input, try again: ");
            String Newchoice = scanner.nextLine();
            input_superwoman(Newchoice, scanner, superwoman);
        }
    }



    // Testing superwoman creation and methods
    public static void menuSuperanimal(Scanner scanner) {
        Superanimal superanimal = new Superanimal();
        while (true) {
            System.out.println("Menu:\n" +
                       "1) Create new superanimal\n" +
                       "2) Rest\n" +
                       "3) Change type of animal\n" +
                       "4) Print details\n" +
                       "5) Remove/add hat\n" +
                       "q) Quit\n");
            System.out.print("Your choice: ");
            String choice = scanner.nextLine();
            if (choice.equalsIgnoreCase("q")) {
                System.out.println("Exiting the program...");
                break;
            } else {
                input_superanimal(choice, scanner, superanimal);
            }
        }
    }

    public static void input_superanimal (String choice, Scanner scanner, Superanimal superanimal) {
        if (choice.equals("1")) {
            addSuperanimal(scanner, superanimal);
        } else if (choice.equals("2")) {
            System.out.println(((Superanimal) superanimal).rest());
        } else if (choice.equalsIgnoreCase("3")) {
            System.out.println("What type of animal should it be? ");
            String newAnimal = scanner.nextLine();
            ((Superanimal) superanimal).setAnimalType(newAnimal);
        } else if (choice.equalsIgnoreCase("4")) {
            System.out.println(((Superanimal) superanimal).toString());
        } else if (choice.equalsIgnoreCase("5")) {
            ((Superman) superanimal).changeHatStatus();
            System.out.println("Changed hat status");
        } else {
            System.out.print("Incorrect input, try again: ");
            String Newchoice = scanner.nextLine();
            input_superanimal(Newchoice, scanner, superanimal);
        }
    }



    public static void addSuperman(Scanner scanner, Superman superman) {

        System.out.println("Enter firstname, lastname and birth year of the person.");
        System.out.print("> First name: ");
        String Fname = scanner.nextLine();
        System.out.print("> Last name: ");
        String Lname = scanner.nextLine();
        System.out.print("> Birthyear: ");
        Integer Byear = Integer.parseInt(scanner.nextLine());
        System.out.print("> Has a hat? (true/false): ");
        String hasHat = scanner.nextLine();
        System.out.print("> If it has a hat, what hat does it have?(If no, leave blank): ");
        String typeHat = scanner.nextLine();


        superman.setFirstName(Fname);
        superman.setLastName(Lname);
        superman.setBirthYear(Byear);
        ((Superman) superman).setHat(hasHat);
        ((Superman) superman).setHatType(typeHat);

        
        System.out.print("Thank you!\n");
        System.out.println(((Superman) superman).toString());

    }

    public static void addSuperwoman(Scanner scanner, Superwoman superwoman) {
        System.out.println("Enter firstname, lastname and birth year of the person.");
        System.out.print("> First name: ");
        String Fname = scanner.nextLine();
        System.out.print("> Last name: ");
        String Lname = scanner.nextLine();
        System.out.print("> Birthyear: ");
        Integer Byear = Integer.parseInt(scanner.nextLine());
        System.out.print("> What weapon does she have? ");
        String weapon = scanner.nextLine();


        superwoman.setFirstName(Fname);
        superwoman.setLastName(Lname);
        superwoman.setBirthYear(Byear);
        ((Superwoman) superwoman).setWeapon(weapon);

        
        System.out.print("Thank you!\n");
        System.out.println(((Superwoman) superwoman).toString());
    }

    public static void addSuperanimal(Scanner scanner, Superanimal superanimal) {
        System.out.println("Enter firstname, lastname and birth year of the person.");
        System.out.print("> First name: ");
        String Fname = scanner.nextLine();
        System.out.print("> Last name: ");
        String Lname = scanner.nextLine();
        System.out.print("> Birthyear: ");
        Integer Byear = Integer.parseInt(scanner.nextLine());
        System.out.print("> What type of animal is it? ");
        String animalType = scanner.nextLine();
        System.out.print("> Has a hat? (true/false): ");
        String hasHat = scanner.nextLine();
        System.out.print("> If it has a hat, what hat does it have?(If no, leave blank): ");
        String typeHat = scanner.nextLine();

        superanimal.setFirstName(Fname);
        superanimal.setLastName(Lname);
        superanimal.setBirthYear(Byear);
        ((Superanimal) superanimal).setAnimalType(animalType);
        ((Superman) superanimal).setHat(hasHat);
        ((Superman) superanimal).setHatType(typeHat);

        
        System.out.print("Thank you!\n");
        System.out.println(((Superanimal) superanimal).toString());
    }
    
}
