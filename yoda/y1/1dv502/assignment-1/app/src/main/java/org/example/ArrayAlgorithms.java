package org.example;

import java.util.Random;

/**
 * ArrayAlgorithms class providing various array manipulation methods.
 */
public class ArrayAlgorithms {

  /**
   * Calculates the average of an array of integers.
   *
   * @param numbers the array of integers
   * @return the average of the numbers
   */
  public final double average(final int[] numbers) {
    int total = 0;
    for (int i : numbers) {
      total += i;
    }
    return total / (double) numbers.length;
  }

  /**
   * Finds the maximum value in an array of integers.
   *
   * @param numbers the array of integers
   * @return the maximum value
   */
  public final int maxValue(final int[] numbers) {
    int currMax = numbers[0];

    for (int i = 1; i < numbers.length; i++) {
      if (numbers[i] > currMax) {
        currMax = numbers[i];
      }
    }
    return currMax;
  }

  /**
   * Finds the maximum value in a 3D array of integers.
   *
   * @param numbers the 3D array of integers
   * @return the maximum value
   */
  public final int maxValue(final int[][][] numbers) {
    int biggestValue = numbers[0][0][0];
    for (int i = 1; i < numbers.length; i++) {
      for (int[] number : numbers[i]) {
        for (int k = 0; k < number.length; k++) {
          if (number[k] > biggestValue) {
            biggestValue = number[k];
          }
        }
      }
    }
    return biggestValue;
  }

  /**
   * Finds the index of the minimum value in an array of integers.
   *
   * @param numbers the array of integers
   * @return the index of the minimum value
   */
  public final int minIndex(final int[] numbers) {
    int smallestIndex = 0;

    for (int i = 1; i < numbers.length; i++) {
      if (numbers[smallestIndex] > numbers[i]) {
        smallestIndex = i;
      }
    }
    return smallestIndex;
  }

  /**
   * Shifts the elements of an array to the right by one position.
   *
   * @param numbers the array of integers
   * @return the shifted array
   */
  public final int[] shift(final int[] numbers) {
    int currValue = numbers[0];

    for (int i = numbers.length - 1; i > 0; i--) {
      // swaps the elements
      int temp = numbers[i];
      numbers[i] = currValue;
      currValue = temp;
    }
    // element 0 will not have
    numbers[0] = currValue;

    return numbers;
  }

  /**
   * Shuffles the elements of an array randomly.
   *
   * @param numbers the array of integers
   * @return the shuffled array
   */
  public final int[] shuffle(final int[] numbers) {
    Random random = new Random();

    for (int i = 0; i < numbers.length; i++) {
      int randomIndex = random.nextInt(numbers.length);
      int temp = numbers[i];
      numbers[i] = numbers[randomIndex];
      numbers[randomIndex] = temp;
    }

    return numbers;
  }

  /**
   * Calculates the sum of a 2D array of integers.
   *
   * @param numbers the 2D array of integers
   * @return the sum of the numbers
   */
  public final int sum(final int[][] numbers) {
    int total = 0;
    for (int[] number : numbers) {
      for (int j = 0; j < number.length; j++) {
        total += number[j];
      }
    }
    return total;
  }

  /**
   * Calculates the sum of a 3D array of integers.
   *
   * @param numbers the 3D array of integers
   * @return the sum of the numbers
   */
  public final int sum(final int[][][] numbers) {
    int total = 0;
    for (int[][] number : numbers) {
      for (int[] number1 : number) {
        for (int k = 0; k < number1.length; k++) {
          total += number1[k];
        }
      }
    }
    return total;
  }
  

  /**
   * Transposes a 2D array of integers.
   *
   * @param numbers the 2D array of integers
   * @return the transposed array
   */
  public final int[][] transpose(final int[][] numbers) {
    if (!isSquare(numbers)) {
      return numbers;
    }
    int[][] transposedArray = new int[numbers[0].length][numbers.length];

    for (int i = 0; i < numbers.length; i++) {
      for (int j = 0; j < numbers[0].length; j++) {
        transposedArray[j][i] += numbers[i][j];
      }
    }


    return transposedArray;
  }

  /**
   * Calculates the sum of the diagonal elements of a 2D array of integers.
   *
   * @param numbers the 2D array of integers
   * @return the sum of the diagonal elements
   */
  public final int diagonalSum(final int[][] numbers) {
    if (!isSquare(numbers)) {
      return 0;
    }

    int sum = 0;
    for (int i = 0; i < numbers.length; i++) {
      sum += numbers[i][i];
    }
    return sum;
  }

  /**
   * Checks if a 2D array is square (i.e., has the same number of rows and columns).
   *
   * @param array the 2D array to check
   * @return true if the array is square, false otherwise
   */
  private boolean isSquare(final int[][] array) {
    int arrayLength1D = array.length;

    for (int i = 0; i < arrayLength1D; i++) {
      if (array[i].length != arrayLength1D) {
        return false;
      }
    }
    return true;
  }


  /**
   * Finds the minimum value in a 3D array of integers.
   *
   * @param numbers the 3D array of integers
   * @return the minimum value
   */
  public final int minValue(final int[][][] numbers) {
    int smallestValue = numbers[0][0][0];
    for (int i = 1; i < numbers.length; i++) {
      for (int[] number : numbers[i]) {
        for (int k = 0; k < number.length; k++) {
          if (number[k] < smallestValue) {
            smallestValue = number[k];
          }
        }
      }
    }
    return smallestValue;
  }


}
