import www.example.*;

import java.util.Scanner;
import java.util.List;


public class Main {
    public static void main(String[] args) {
        Team team = new Team();
        Person person = new Person();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Menu:");
            System.out.println("1) Add 5 pre-defined persons to the team");
            System.out.println("2) Print the team and its members");
            System.out.println("3) Remove all from the team");
            System.out.println("4) Add a new person/superman/superwoman/superchild to the team");
            System.out.println("anything else ) Quit/exit");
            System.out.print("Enter your choice: ");

            String choice = scanner.nextLine();
        
            if (choice.equals("1")) {
                addPredefinedPersons(team, person);
            }
            else if (choice.equals("2")) {
                printTeamMembers(team);
            }

            else if (choice.equals("3")){
                team.removePersons();
                System.out.println("All team members where removed");
            }

            else if (choice.equals("4")) {
                System.out.println("1) add a new person");
                System.out.println("2) add a new superman");
                System.out.println("3) add a new superwoman");
                System.out.println("4) Add a new superchild");
                System.out.println("Anything else) goes back to main menu");

                String pick = scanner.nextLine();
                
                
                if (pick.equals("1")) {
                    addCostumePerson(team, scanner);
                }

                else if (pick.equals("2")) {
                    addCostumeSuperman(scanner, team);
                }

                else if (pick.equals("3")) {
                    addCostumeSuperwoman(scanner, team);
                }

                else if (pick.equals("4")) {
                    addCostumeSuperchild(scanner, team);
                }
                else{
                    System.out.println("goes back to main menu");
                }
                
            }

            else {
                scanner.close();
                break;
            }
        }
    }

    public static void addPredefinedPersons(Team team, Person person) {
        Person person1 = new Person();
        person1.setPersonDetails("n1", "m1", 2000);
        team.addPerson(person1);
        Person person2 = new Person();
        person2.setPersonDetails("n2", "m3", 2001);
        team.addPerson(person2);
        Person person3 = new Person();
        person3.setPersonDetails("n3", "m3", 2002);
        team.addPerson(person3);
        Person person4 = new Person();
        person4.setPersonDetails("n4", "m4", 2003);
        team.addPerson(person4);
        Person person5 = new Person();
        person5.setPersonDetails("n5", "m5", 2004);
        team.addPerson(person5);
        System.out.println("5 predefinde people added to the team.");
    }

    public static void printTeamMembers(Team team) {
        List<Person> members = team.getMembers();
        if (members.isEmpty()) {
            System.out.println("Team is empty");
        }
        else {
            System.out.println("Team members: ");
            for (Person person : members) {
                System.out.println(person.toString());
            }
        }
    }

    private static void addCostumePerson(Team team, Scanner scanner) {
        System.out.println("Enter the first name of the person: ");
        String fName = scanner.nextLine();
        System.out.println("Enter last name of the person: ");
        String lName = scanner.nextLine();
        System.out.println("Enter the year the person is born: ");
        int YearOfBirth = scanner.nextInt();
        scanner.nextLine();

        Person newPerson = new Person();
        newPerson.setPersonDetails(fName, lName, YearOfBirth);
        team.addPerson(newPerson);
        System.out.println(fName + " " + lName + " Added to team");

    }

    public static void addCostumeSuperman(Scanner scanner, Team team) {
        System.out.println("First name of superman: ");
        String fName = scanner.nextLine();

        System.out.println("Last name of superman: ");
        String lName = scanner.nextLine();

        System.out.println("When was superman born: ");
        int YearOfBirth = scanner.nextInt();
        scanner.nextLine();

        Superman superman = new Superman(fName, lName, YearOfBirth);
        team.addPerson(superman);
        System.out.println(fName + " " + lName + " Added to team");
    }

    public static void addCostumeSuperwoman(Scanner scanner, Team team) {
        System.out.println("First name of superwoman: ");
        String fName = scanner.nextLine();

        System.out.println("Last name of superwoman: ");
        String lName = scanner.nextLine();

        System.out.println("When was the superwoman born: ");
        int YearOfBirth = scanner.nextInt();
        scanner.nextLine();

        Superwoman superwoman = new Superwoman(fName, lName, YearOfBirth);
        team.addPerson(superwoman);
        System.out.println(fName + " " + lName + " Added to team");
    }

    public static void addCostumeSuperchild(Scanner scanner, Team team) {
        System.out.println("First name of superchild: ");
        String fName = scanner.nextLine();

        System.out.println("Last name of superchild: ");
        String lName = scanner.nextLine();

        System.out.println("When was the superchild born: ");
        int YearOfBirth = scanner.nextInt();
        scanner.nextLine();

        Superchild superchild = new Superchild(fName, lName, YearOfBirth);
        team.addPerson(superchild);
        System.out.println(fName + " " + lName + " Added to team");
    }

}
