package task2;

import java.util.Scanner;

import task2.com.sb224sc.classes.*;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the calculation: ");
        String input = sc.nextLine();
        double result = Calculator.calculate(input);

        if (!Double.isNaN(result)) {
            System.out.println("\nThe sum is: " + result);
        }
        sc.close();
    }
}
