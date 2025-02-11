package org.example;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

/**
 * Test class for ArrayAlgorithms.
 */
public class ArrayAlgorithmsTest {
  // Decomment this first as it is used in every test method
  ArrayAlgorithms arrayAlgorithms = new ArrayAlgorithms();

  @Test
  public void testAverage() {
    int[] numbers = { 1, 2, 3, 4, 5 };
    double expected = 3.0;
    double result = arrayAlgorithms.average(numbers);
    assertEquals(expected, result, 0.01);
  }

  @Test
  public void testMaxValue() {
    int[] numbers = { 1, 2, 3, 4, 5 };
    int expected = 5;
    int result = arrayAlgorithms.maxValue(numbers);
    assertEquals(expected, result);
  }

  @Test
  public void testMaxValueNegatives() {
    int[] numbers = { -1, -2, -3, -4, -5 };
    int expected = -1;
    int result = arrayAlgorithms.maxValue(numbers);
    assertEquals(expected, result);
  }

  @Test
  public void testMinIndex() {
    int[] numbers = { 5, 3, 1, 4, 2 };
    int expected = 2;
    int result = arrayAlgorithms.minIndex(numbers);
    assertEquals(expected, result);
  }

  @Test
  public void testShift() {
    int[] numbers = { 1, 2, 3, 4, 5 };
    int[] expected = { 2, 3, 4, 5, 1 };
    int[] result = arrayAlgorithms.shift(numbers);
    assertArrayEquals(expected, result);
  }

  @Test
  public void testShuffle() {
    int[] numbers = { 1, 2, 3, 4, 5 };
    int[] original = { 1, 2, 3, 4, 5 };
    int[] result = arrayAlgorithms.shuffle(numbers);
    // Assert that the array contains the same elements but in a different order
    assertEquals(original.length, result.length);
    assertTrue(containsAll(original, result));
  }

  private boolean containsAll(int[] arr1, int[] arr2) {
    for (int i = 0; i < arr1.length; i++) {
      if (!contains(arr1[i], arr2)) {
        return false;
      }
    }
    return true;
  }

  private boolean contains(int n, int[] arr) {
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] == n) {
        return true;
      }
    }
    return false;
  }
}
