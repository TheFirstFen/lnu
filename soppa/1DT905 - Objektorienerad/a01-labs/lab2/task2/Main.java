package task2;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import task1_2.com.task1_2.person.Person;
import task1.com.task1.superman_woman.Superman;
import task1.com.task1.superman_woman.Superwoman;
import task1.com.task1.superman_woman.Superanimal;
import task2.com.task2.team.Team;

public class Main {
    private static Boolean exitprogram = false;
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in); // Creates new scanner instance
        while (true) {
            System.out.println("Menu:\n" +
                               "1) Add 5 pre-defined persons (all Person types should be added) to the team\n" +
                               "2) Print the team and its members\n" +
                               "3) Remove all from the team\n" +
                               "4) Create a new Person/Superman/Superwoman/Superanimal and add to the team\n" +
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
            addPreDefTeam();
        } else if (choice.equals("2")) {
            printTeam();
        } else if (choice.equalsIgnoreCase("3")) {
            removeTeam();
        } else if (choice.equalsIgnoreCase("4")) {
            addMenu(scanner);
        } else if (choice.equalsIgnoreCase("q")) {
            exitprogram = true;
        } else {
            System.out.print("Incorrect input, try again: ");
            String Newchoice = scanner.nextLine();
            check_input_choice(Newchoice, scanner);
        }
    }

    public static void addPreDefTeam() {
        Person pre1 = new Person();
        Superman pre2 = new Superman();
        Superman pre3 = new Superman();
        Superwoman pre4 = new Superwoman();
        Superanimal pre5 = new Superanimal();

        pre1.setFirstName("Kalle");
        pre1.setLastName("Anka");
        pre1.setBirthYear(1970);
        Team.addPerson(pre1);

        pre2.setFirstName("James");
        pre2.setLastName("Allen");
        pre2.setBirthYear(2000);
        ((Superman) pre2).setHat("true");
        ((Superman) pre2).setHatType("baseball cap");
        Team.addPerson(pre2);

        pre3.setFirstName("Reece");
        pre3.setLastName("Anderson");
        pre3.setBirthYear(1992);
        ((Superman) pre3).setHat("false");
        ((Superman) pre3).setHatType("");
        Team.addPerson(pre3);

        pre4.setFirstName("Hanna");
        pre4.setLastName("Kerr");
        pre4.setBirthYear(1982);
        ((Superwoman) pre4).setWeapon("gun");
        Team.addPerson(pre4);

        pre5.setFirstName("Simba");
        pre5.setLastName("Simpson");
        pre5.setBirthYear(2013);
        ((Superanimal) pre5).setAnimalType("cheetah");
        ((Superman) pre5).setHat("true");
        ((Superman) pre5).setHatType("party hat");
        Team.addPerson(pre5);

        System.out.println("A pre-defined team of 5 members has been created");
    }

    public static void printTeam() {
        List <Person> tempTeam = new ArrayList<>();
        tempTeam = Team.getMembers();
        for (Person person : tempTeam) {
            System.out.print(person);
        }

    }

    public static void removeTeam() {
        System.out.println("Removed all team members!");
        Team.removeTeam();
    }

    public static void addMenu(Scanner scanner) {
        while (true) {
            System.out.println("Choose what type of person to add:\n" +
                       "1) New superman\n" +
                       "2) New superwoman\n" +
                       "3) New superanimal\n" +
                       "q) Quit\n");
            System.out.print("Your choice: ");
            String choice = scanner.nextLine();
            if (choice.equalsIgnoreCase("q")) {
                System.out.println("Exiting the program...");
                break;
            } else {
                inputAddMenu(choice, scanner);
            }
            if (exitprogram.equals(true)) {
                break;
            }
        }
    }

    public static void inputAddMenu (String choice, Scanner scanner) {
        if (choice.equals("1")) {
            addSuperman(scanner);
        } else if (choice.equals("2")) {
            addSuperwoman(scanner);
        } else if (choice.equals("3")) {
            addSuperanimal(scanner);
        } else if (choice.equalsIgnoreCase("q")) {
            exitprogram = true;
        } else {
            System.out.print("Incorrect input, try again: ");
            String Newchoice = scanner.nextLine();
            inputAddMenu(Newchoice, scanner);
        }
    }


    public static void addSuperman(Scanner scanner) {
        Superman superman = new Superman();
        System.out.println("Enter firstname, lastname and birth year of the person.");
        System.out.print("> First name: ");
        String Fname = scanner.nextLine();
        System.out.print("> Last name: ");
        String Lname = scanner.nextLine();
        Integer Byear = null;
        boolean validInput = false;
        System.out.print("> Birthyear: ");
        while (!validInput) {
            try {
                Byear = Integer.parseInt(scanner.nextLine());
                validInput = true;
            } catch (NumberFormatException e) {
                System.out.print("Please enter a valid integer for birth year: ");
            }
        }
        
        System.out.print("> Has a hat? (true/false): ");
        String hasHat = null;
        validInput = false;
        
        while (!validInput) {
            hasHat = scanner.nextLine().toLowerCase(); 
            
            if (hasHat.equals("true") || hasHat.equals("false")) {
                validInput = true; 
            } else {
                System.out.print("Please enter 'true' or 'false': ");
            }
        }

        System.out.print("> If it has a hat, what hat does it have?(If no, leave blank): ");
        String typeHat = scanner.nextLine();


        superman.setFirstName(Fname);
        superman.setLastName(Lname);
        superman.setBirthYear(Byear);
        ((Superman) superman).setHat(hasHat);
        ((Superman) superman).setHatType(typeHat);

        
        System.out.print("Thank you!\n");
        System.out.println(((Superman) superman).toString());
        Team.addPerson(superman);

    }

    public static void addSuperwoman(Scanner scanner) {
        Superwoman superwoman = new Superwoman();
        System.out.println("Enter firstname, lastname and birth year of the person.");
        System.out.print("> First name: ");
        String Fname = scanner.nextLine();
        System.out.print("> Last name: ");
        String Lname = scanner.nextLine();
        Integer Byear = null;
        boolean validInput = false;
        System.out.print("> Birthyear: ");
        while (!validInput) {
            try {
                Byear = Integer.parseInt(scanner.nextLine());
                validInput = true;
            } catch (NumberFormatException e) {
                System.out.print("Please enter a valid integer for birth year: ");
            }
        }
        
        System.out.print("> What weapon does she have? ");
        String weapon = scanner.nextLine();


        superwoman.setFirstName(Fname);
        superwoman.setLastName(Lname);
        superwoman.setBirthYear(Byear);
        ((Superwoman) superwoman).setWeapon(weapon);

        
        System.out.print("Thank you!\n");
        System.out.println(((Superwoman) superwoman).toString());
        Team.addPerson(superwoman);
    }

    public static void addSuperanimal(Scanner scanner) {
        Superanimal superanimal = new Superanimal();
        System.out.println("Enter firstname, lastname and birth year of the person.");
        System.out.print("> First name: ");
        String Fname = scanner.nextLine();
        System.out.print("> Last name: ");
        String Lname = scanner.nextLine();
        
        Integer Byear = null;
        boolean validInput = false;
        System.out.print("> Birthyear: ");
        while (!validInput) {
            try {
                Byear = Integer.parseInt(scanner.nextLine());
                validInput = true;
            } catch (NumberFormatException e) {
                System.out.print("Please enter a valid integer for birth year: ");
            }
        }
        
        System.out.print("> What type of animal is it? ");
        String animalType = scanner.nextLine();

        System.out.print("> Has a hat? (true/false): ");
        String hasHat = null;
        validInput = false;
        
        while (!validInput) {
            hasHat = scanner.nextLine().toLowerCase(); 
            
            if (hasHat.equals("true") || hasHat.equals("false")) {
                validInput = true; 
            } else {
                System.out.print("Please enter 'true' or 'false': ");
            }
        }

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
        Team.addPerson(superanimal);
    }

}
