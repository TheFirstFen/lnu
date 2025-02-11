package org.example;

import java.util.Scanner;

/**
 * This is the class for the A grade part of the assignment.\
 * Make sure you uncomment the corresponding test cases.
 */
public class GradeA {

  /**
   * Solution to the calculator task.
   *
   * @param input is the scanner used to read input from the user.
   */
  public void calculator(Scanner input) {
    double n1;
    double n2 = 0;

    String[] choicesSimple = {"sqrt", "factorial", "square"};
    String[] choicesMultipleInputs = {"add", "subtraction", "division",
                                      "multiplication"};
                                      
    
    System.out.print("Input a number: ");
    n1 = input.nextDouble();

    // takes the next input value, trims it of spaces if the line is empty
    // we have one number else we have two numbers and need to convert the next number to a double
    String line = input.nextLine().trim();
    boolean hasTwoValues = !line.isEmpty();

    if (hasTwoValues){
      n2 = Double.parseDouble(line);
    }

    if (hasTwoValues) {
      System.out.print("\nChoose one of the following operations: ( ");
      showChoices(choicesMultipleInputs);
      System.out.print(" )\n");
    } else {
      System.out.println("\nChoose one of the following operations ( ");
      showChoices(choicesSimple);
      System.out.print(" )\n");
    }
    String choice = input.nextLine();
    
    Calculator c = new Calculator();
    System.out.println();

    if (hasTwoValues) {
      // regular switch statement just formatter wanted it this way
      switch (choice) {
        case "add" -> System.out.println("Addition: " + c.add(n1, n2));
        case "subtract" -> System.out.println("Subtraction: " + c.subtract(n1, n2));
        case "multiply" -> System.out.println("Multiplication: " + c.multiply(n1, n2));
        case "division" -> System.out.println("Divide: " + c.divide(n1, n2));
        default -> System.out.println("Unknown choice");
      }
    } else {
      switch (choice) {
        case "sqrt" -> System.out.println("Square root: " + c.sqrt(n1));
        case "factorial" -> {
            int number1 = (int) n1;
            System.out.println("Factorial: " + c.factorial(number1));
            }
        case "square" -> System.out.println("Square: " + c.square(n1));
        default -> System.out.println("Unknown choice");
      }
    }

  }

  // method to show the possible choices
  private void showChoices(String[] choices) {
    for (String e : choices) {
      System.out.print(e + " ");
    }
  }


  /**
   * Solution to the 3D arrays task.
   */
  public void arrays3D() {
    ArrayAlgorithms arrayAlgorithms = new ArrayAlgorithms();
    int[][][] matrix = { { { 1, 2, 3 }, { 4, 5, 6 } }, 
                         { { 7, 8, 9 }, { 10, 11, 12 } } };
    int sum = arrayAlgorithms.sum(matrix);
    int minValue = arrayAlgorithms.minValue(matrix);
    int maxValue = arrayAlgorithms.maxValue(matrix);

    System.out.println("Sum: " + sum);
    System.out.println("Min value: " + minValue);
    System.out.println("Max value: " + maxValue);
  }

  /**
   * Solution to the genre task.
   */
  public void genre() {
    Band band = new Band("ACDC", 1973);
    band.addAlbum("Back in Black", 1980, "Rock");
    band.addAlbum("Highway to Hell", 1979, "Rock");
    band.addAlbum("The Razors Edge", 1990, "Rock");
    Album[] albums = band.getAlbums();
    System.out.println("The following albums are made by: " + band.getName());
    for (Album e : albums) {
      System.out.println(e.getTitle() + " " + e.getYear() +  " " + e.getGenre());
    }
  }
}
