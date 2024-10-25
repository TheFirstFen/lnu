package lab4.com.eu222dq;

import java.util.Scanner;

public class Calculator {

    public void main() {
        while (true) {
            Scanner scanner = new Scanner(System.in);
            System.out.println("q. Quit");
            System.out.println("Enter the equation you want to calculate, must have: space between operands and operators");
            System.out.println("Ex: 5 + 5 - 5");
            String expression = scanner.nextLine();

            if (expression.equals("q")){
                System.out.println("Quiting");
                scanner.close();
                break;                
            }
            else {
                Calculator calculator = new Calculator(expression);
                calculator.calculateAndPrint(scanner);
            }
        }
    }
    private String expression = "";

    public Calculator(String expression) {
        this.expression = expression;
    }

    public Calculator() {
    }

    /**
 * Calculates the result of a mathematical expression.
 *
 * @return The calculated result.
 * @throws IllegalArgumentException If the expression is invalid.
 */
    public double calculate() throws IllegalArgumentException {
        // Split the input expression into tokens
        String[] tokens = expression.split(" ");

        
        if (tokens.length % 2 == 0) {
            throw new IllegalArgumentException("Invalid expression");
        }

        double result = 0.0;
        
        for (int i = 0; i < tokens.length; i += 1) {
            if (i % 2 == 0) {
                try {
                    double operand = Double.parseDouble(tokens[i]);
                    if (i == 0) {
                        result = operand;
                    }
                    else {
                        String operator = tokens[i - 1];
                        switch (operator) {
                            case "+":
                                result += operand;
                                break;
                            case "-":
                                result -= operand;
                                break;
                            case "*":
                                result *= operand;
                                break;
                            case "/":
                                if (operand == 0) {
                                   throw new IllegalArgumentException("Division by zero is not allowed");
                                }
                                result /= operand;
                                break;
                            default:
                                throw new IllegalArgumentException("Invalid operator");
                        }
                    }
                    
                }
                catch (NumberFormatException e) {
                    return Double.NaN;
                }
            }
        }
        return result;
    }

    public void calculateAndPrint(Scanner scanner) {
        try {
            double result = calculate();
            System.out.println("Result: " + result);
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
