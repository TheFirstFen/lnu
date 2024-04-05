package task2.com.sb224sc.classes;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Calculator {
    /**
     * Calculates the result of a mathematical expression.
     *
     * @param input the mathematical expression to be evaluated
     * @return the result of the evaluation
     */
    public static double calculate(String input) {
        String[] temp = input.split(" ");
        List<String> tokens = new ArrayList<>(Arrays.asList(temp));

        if (tokens.size() < 3) {
            System.out.println("Invalid input. Please use the format 'op1 operator op2'.");
            return Double.NaN;
        }

        while (tokens.size() != 1) {
            tokens = arrayChange(tokens);
        }

        return Double.parseDouble(tokens.get(0));
    }

    /**
     * Generates a new list of tokens by changing the elements in the input list.
     *
     * @param tokens the list of tokens to be changed
     * @return the new list of tokens with the desired changes
     */
    private static List<String> arrayChange(List<String> tokens) {
        List<String> newTokens = new ArrayList<>();

        for (int i = 0; i < tokens.size() - 2; i++) {
            if (i == 0) {
                newTokens.add("" + compute(tokens));
            } else {
                newTokens.add(tokens.get(i + 2));
            }
        }

        return newTokens;
    }

    /**
     * Computes the result of an arithmetic operation based on a list of tokens.
     *
     * @param tokens the list of tokens representing the arithmetic operation
     * @return the result of the arithmetic operation
     */
    private static double compute(List<String> tokens) {
        double op1, op2 = 0;

        try {
            op1 = Double.parseDouble(tokens.get(0));
            op2 = Double.parseDouble(tokens.get(2));
        } catch (NumberFormatException e) {
            System.out.println("Invalid input. Operands must be valid numbers.");
            return Double.NaN;
        }

        char operator = tokens.get(1).charAt(0);
        double res;

        switch (operator) {
            case '+':
                res = op1 + op2;
                break;
            case '-':
                res = op1 - op2;
                break;
            case '*':
                res = op1 * op2;
                break;
            case '/':
                if (op2 == 0) {
                    System.out.println("Division by 0 is not allowed.");
                    return Double.NaN;
                }
                res = op1 / op2;
                break;
            default:
                System.out.println("Invalid operator. Please use '+', '-', '*', or '/'.");
                return Double.NaN;
        }

        return res;
    }
}