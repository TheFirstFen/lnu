package com.calculator;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
/**
 * The Calculator class provides basic calculations such as addition, subtraction,
 * multiplication, and division. It takes space-separated input strings and
 * calculates the result.
 */
public class Calculator {
    private static List<String> inputList;
    private static Boolean NaN = false;
    private static Integer tempIndex;
    private static Double sum;
    private static Boolean prevNum;
    private static Boolean prevOpe;
    private static Boolean prevDiv;

    /**
     * Main method to run the calculator program.
     *
     * @param args
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            NaN = false;
            System.out.print("Enter the calculation(q to quit): ");
            String calculationString = scanner.nextLine();
            Boolean exitProgram = menu(calculationString);
            if (exitProgram) {
                System.out.println("Exiting the program...");
                break;
            }
        }
        scanner.close();
    }


    /**
     * Provides a menu for the user to input calculations and displays the results.
     *
     * @param calculationString The user's input as a string.
     * @return True if the program should exit, false otherwise.
     */
    public static Boolean menu(String calculationString) {
        if (calculationString.equals("q")) {
            return true;
        } else {
            inputList = new ArrayList<>(Arrays.asList(calculationString.split(" ")));
            if (checkForError(inputList).equals(false)) {
                Double answer = calculate(inputList);
                System.out.println("The sum is: " + answer);
            } else {
                if (NaN.equals(true)) {
                    String answer = "NaN";
                    System.out.println("The sum is: " + answer);
                } else {
                    System.out.println("Error please input a correct calculation.");
                }
            }
            return false;
        }
    }
    /**
     * Adds two numbers and returns the result.
     *
     * @param n1 The first number to be added.
     * @param n2 The second number to be added.
     * @return The sum of n1 and n2.
     */
    public static Double addition(Double n1, Double n2) {
        Double result = n1 + n2;
        return result;
    }

    /**
     * Multiplies two numbers and returns the result.
     *
     * @param n1 The first number to be multiplied.
     * @param n2 The second number to be multiplied.
     * @return The product of n1 and n2.
     */
    public static Double multiplication(Double n1, Double n2) {
        Double result = n1 * n2;
        return result;
    }

    /**
     * Subtracts the second number from the first number and returns the result.
     *
     * @param n1 The number from which to subtract.
     * @param n2 The number to be subtracted.
     * @return The result of subtracting n2 from n1.
     */
    public static Double subtract(Double n1, Double n2) {
        Double result = n1 - n2;
        return result;
    }

    /**
     * Divides the first number by the second number and returns the result.
     *
     * @param n1 The dividend (the number to be divided).
     * @param n2 The divisor (the number by which to divide).
     * @return The result of dividing n1 by n2.
     */
    public static Double division(Double n1, Double n2) {
        Double result = n1 / n2;
        return result;
    }


    /**
     * Calculates the result of the input expression.
     *
     * @param input The list of strings representing the expression.
     * @return The result of the calculation.
     */
    public static Double calculate(List<String> input) {
        tempIndex = 0;
        sum = Double.parseDouble(input.get(tempIndex));
        for (String c : input) {
            if (c.equals("*")) {
                Double num2 = Double.parseDouble(input.get(tempIndex + 1));
                sum = multiplication(sum, num2);
            } else if (c.equals("/")) {
                Double num2 = Double.parseDouble(input.get(tempIndex + 1));
                sum = division(sum, num2);
            } else if (c.equals("+")) {
                Double num2 = Double.parseDouble(input.get(tempIndex + 1));
                sum = addition(sum, num2);
            } else if (c.equals("-")) {
                Double num2 = Double.parseDouble(input.get(tempIndex + 1));
                sum = subtract(sum, num2);
            } 
             tempIndex += 1;
        }
        return sum;
    }

    /**
     * Checks for errors in the input expression.
     *
     * @param input The list of strings representing the expression.
     * @return True if there is an error, false otherwise.
     */
    public static Boolean checkForError(List<String> input) {
        prevNum = false;
        prevOpe = true;
        prevDiv = false;
        for (String c : input) {
            try {
                Double num = Double.parseDouble(c);
                if (prevNum == true) {
                    return true;
                } else if (num == 0.0 && prevDiv) {
                    String errorMessage = "Cannot divide by zero!";
                    System.out.println(errorMessage);
                    return true;
                }
                prevNum = true;
                prevOpe = false;
                prevDiv = false;
            } catch (NumberFormatException e) {
                if (prevOpe == true && c.length() == 1) {
                    NaN = true;
                    return true;
                }
                if (c.equals("/") || c.equals("*") || c.equals("+") || c.equals("-")) {
                    if (c.equals("/")) {
                        prevDiv = true;
                    } else {
                        prevDiv = false;
                    }
                    prevNum = false;
                    prevOpe = true;
                } else {
                    return true;
                }
            }
    }
    return false;
    }
}
