package task1_2;
import java.util.Scanner;

import task1_2.com.task1_2.person.Person;

import java.util.Random;
import java.util.ArrayList;
import java.util.List;


class Main {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in); // Creates new scanner instance
        Person person = new Person();
        while (true) {
            System.out.println("Menu:\n" +
                               "1) Get random numbers between 1 and 100\n" +
                               "2) Summarize numbers\n" +
                               "P1) Enter details on the person\n" +
                               "P2) Print details of the person\n" +
                               "q) Quit\n");
            System.out.print("Your choice: ");
            String choice = scanner.nextLine();
            if (choice.equalsIgnoreCase("q")) {
                System.out.println("Exiting the program...");
                break;
            } else {
                check_input_choice(choice, scanner, person);
            }
        }
        scanner.close(); // Close the scanner at the end of the main loop
    }

    // Method that checks so input is valid
    public static void check_input_choice(String choice, Scanner scanner, Person person) {
        if (choice.equals("1")) {
            get_random_numbers(scanner);
        } else if (choice.equals("2")) {
            get_input_numbers(scanner);
        } else if (choice.equalsIgnoreCase("P1")) {
            add_person(scanner, person);
        } else if (choice.equalsIgnoreCase("P2")) {
            print_person(person);
        } else {
            System.out.print("Incorrect input, try again: ");
            String Newchoice = scanner.nextLine();
            check_input_choice(Newchoice, scanner, person);
        }
    }

    public static void get_random_numbers(Scanner scanner) {
        System.out.print("How many numbers do you want to see? ");
        while (!scanner.hasNextInt()) {
            System.out.println("That's not an integer! Try again:");
            scanner.next();
        }
        int number = scanner.nextInt();
        scanner.nextLine();
        List<Integer> random_numbers = generate_random_numbers(number);
        for (int numbers : random_numbers) {
            System.out.print(numbers + " ");
        }
        System.out.println();
        Integer sum = summarize_numbers(random_numbers);
        System.out.println("The sum is: " + sum + "\n");
    }

    public static void get_input_numbers(Scanner scanner) {
        System.out.println("Enter the numbers, separated by space, end with newline:");
        System.out.print("> ");
        String numbers = scanner.nextLine();
        List<Integer> numberList = new ArrayList<>();
        String[] numberStr = numbers.split(" ");
        for (String n : numberStr) {
            try {
                int number = Integer.parseInt(n);
                numberList.add(number);
            } catch (NumberFormatException e) {
                System.out.println("Invalid input: " + n);
            }
        }
        Integer sum = summarize_numbers(numberList);
        System.out.println("The sum is: " + sum + "\n");
    }

    public static List<Integer> generate_random_numbers(int number) {
        List<Integer> randomNumbers = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < number; i++) {
            int randomNumber = random.nextInt(100) + 1;
            randomNumbers.add(randomNumber);
        }
        return randomNumbers;
    }

    public static Integer summarize_numbers(List<Integer> random_numbers) {
        Integer sum = 0;
        for (Integer num : random_numbers) {
            sum = sum + num;
        }
        return sum;
    }

    public static void add_person(Scanner scanner, Person person) {
        System.out.println("Enter firstname, lastname and birth year of the person.");
        System.out.print("> First name: ");
        String Fname = scanner.nextLine();
        System.out.print("> Last name: ");
        String Lname = scanner.nextLine();
        System.out.print("> Birthyear: ");
        Integer Byear = Integer.parseInt(scanner.nextLine());

        person.setFirstName(Fname);
        person.setLastName(Lname);
        person.setBirthYear(Byear);
        System.out.print("Thank you!\n");
        System.out.println(person.toString());
    }

    public static void print_person(Person person) {
        System.out.println(person.toString());
    }
}


