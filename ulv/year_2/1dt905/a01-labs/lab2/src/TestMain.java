import www.example.*;

import java.util.Scanner;


public class TestMain {
    public static void main(String[] args) {


        while(true){
            Scanner scanner = new Scanner(System.in);
            System.out.println("1) Enter info on person: ");
            System.out.println("2) Enter info on superman: ");
            System.out.println("3) Enter info on superwoman: ");
            System.out.println("4) Enter info on superchild: ");
            System.out.println("q) Quit: ");

            String choice = scanner.nextLine();

            if (choice.equals("1")){
                Inputs.personinfo(scanner);
            }

            else if (choice.equals("2")){
                Inputs.sManInfo(scanner);
            }

            else if (choice.equals("3")){
                Inputs.sWomanInfo(scanner);
            }

            else if (choice.equals("4")) {
                Inputs.sChildInfo(scanner);
            }

            else if (choice.equals("q")){
                scanner.close();
                break;
            }
        }
    }
}

class Inputs{
    public static void personinfo(Scanner scanner) {
        Person person = new Person();
        System.out.println("First name of the person: ");
        String fName = scanner.nextLine();

        System.out.println("Last name of the person: ");
        String lName = scanner.nextLine();

        System.out.println("When was the person born: ");
        int YearOfBirth = scanner.nextInt();

        person.setPersonDetails(fName, lName, YearOfBirth);
        System.out.println(person.toString());
    }

    public static void sManInfo(Scanner scanner) {
        System.out.println("First name of superman: ");
        String fName = scanner.nextLine();

        System.out.println("Last name of superman: ");
        String lName = scanner.nextLine();

        System.out.println("When was superman born: ");
        int YearOfBirth = scanner.nextInt();

        Superman superman = new Superman(fName, lName, YearOfBirth);
        System.out.println(superman.toString());
    }

    public static void sWomanInfo(Scanner scanner) {
        System.out.println("First name of superwoman: ");
        String fName = scanner.nextLine();

        System.out.println("Last name of superwoman: ");
        String lName = scanner.nextLine();

        System.out.println("When was the superwoman born: ");
        int YearOfBirth = scanner.nextInt();

        Superwoman superwoman = new Superwoman(fName, lName, YearOfBirth);
        System.out.println(superwoman.toString());
    }

    public static void sChildInfo(Scanner scanner) {
        System.out.println("First name of superchild: ");
        String fName = scanner.nextLine();

        System.out.println("Last name of superchild: ");
        String lName = scanner.nextLine();

        System.out.println("When was the superchild born: ");
        int YearOfBirth = scanner.nextInt();

        Superchild superchild = new Superchild(fName, lName, YearOfBirth);
        System.out.println(superchild.toString());


    }
}