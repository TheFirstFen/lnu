package org.example;

import java.util.Scanner;
/**
 * This is the class for the C grade part of the assignment.\
 * Make sure you uncomment the corresponding test cases.
 */
public class GradeC {

  /**
   * Solution to the calculator task.
   *
   * @param input is the scanner used to read input from the user.
   */
  public void calculator(Scanner input) {
    
    System.out.print("Enter two numbers: ");
    
    double number1 = input.nextInt();
    double number2 = input.nextInt();
    input.nextLine(); // removes the empty line
    System.out.print("Choose an operation (add, subtract, multiply, division): ");
    String choice = input.nextLine();
    
    Calculator c = new Calculator();
    // checks for the correct choice
    switch (choice) {
      case "add" -> System.out.println("Addition: " + c.add(number1, number2));
      case "subtract" -> System.out.println("Subtraction: " + c.subtract(number1, number2));
      case "multiply" -> System.out.println("Multiplication: " + c.multiply(number1, number2));
      case "division" -> System.out.println("Divide: " + c.divide(number1, number2));
      default -> System.out.println("Unknown choice");
    }

    
  }

  /**
   * Solution to the 3D arrays task.
   */
  public void arrays2D() {
    ArrayAlgorithms arrayAlgorithms = new ArrayAlgorithms();
    int[][] numbersMatrix = {{ 1,  2,  3,  4,  5 },
                             { 6,  7,  8,  9, 10 },
                             { 11, 12, 13, 14, 15 },
                             { 16, 17, 18, 19, 20 },
                             { 21, 22, 23, 24, 25 } };
    int[][] transposedArray = arrayAlgorithms.transpose(numbersMatrix);
    
    System.out.println("Transposed array");
    for (int[] e : transposedArray) {
      for (int j = 0; j < e.length; j++) {
        System.out.print(" " + e[j]);
      }
      System.out.println();
    }
    
    int sum = arrayAlgorithms.sum(numbersMatrix);
    System.out.println("\nSum: " + sum);
    
    int diagonalSum = arrayAlgorithms.diagonalSum(numbersMatrix);
    System.out.println("\nDiagonal sum: " + diagonalSum);

  }

  /**
   * Solution to the genre task.
   */
  public void band() {
    Band band = new Band("ACDC", 1973);
    band.addAlbum("Back in Black", 1980);
    band.addAlbum("Highway to Hell", 1979);
    band.addAlbum("The Razors Edge", 1990);
    Album[] albums = band.getAlbums();
    for (Album e : albums) {
      System.out.println(e.getName() + " " + e.getYear());
    }
  }
}
