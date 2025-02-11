package org.example;

/**
 * Calculator class with the following operations. Addition, subtraction
 * multiplication, division, square root, square and factorial
 */
public class Calculator {
  private boolean isZero;

  /**
   * Addition.
   *
   * @param n1 the first number
   * @param n2 the second number
   * @return the sum of n1 and n2
   */
  public double add(double n1, double n2) {
    return n1 + n2;
  }

  /**
   * Subtraction.
   *
   * @param n1 the first number
   * @param n2 the second number
   * @return the difference between n1 and n2
   */
  public double subtract(double n1, double n2) {
    return n1 - n2;
  }

  /**
   * Multiplication.
   *
   * @param n1 the first number
   * @param n2 the second number
   * @return the product of n1 and n2
   */
  public double multiply(double n1, double n2) {
    return n1 * n2;
  }

  /**
   * Checks if the last division operation was by zero.
   *
   * @return true if the last division was by zero, false otherwise
   */
  public boolean isDivideByZero() {
    return isZero;
  }

  /**
   * Division.
   *
   * @param n1 the numerator
   * @param n2 the denominator
   * @return the quotient of n1 and n2, or 0 if n2 is zero
   */
  public double divide(double n1, double n2) {
    if (n2 != 0) {
      isZero = false;
      return n1 / n2;
    }
    isZero = true;
    return 0;
  }

  /**
   * Square root for n >= 0.
   *
   * @param n1 the number
   * @return the square root of n1, or 0 if n1 is negative
   */
  public double sqrt(double n1) {
    if (!validNumber(n1)) {
      return 0.0;
    }
    return Math.sqrt(n1);
  }

  private boolean validNumber(double n1) {
    return n1 >= 0;
  }

  /**
   * The square of a number n².
   *
   * @param n1 the number
   * @return the square of n1
   */
  public double square(double n1) {
    return n1 * n1;
  }

  /**
   * Factorial.
   *
   * @param n1 the number
   * @return the factorial of n1
   */
  public int factorial(int n1) {
    if (n1 <= 1) {
      return 1;
    }
    int total = 1; // lowest value there can be
    for (int i = 1; i <= n1; i++) {
      total *= i;
    }
    return total;
  }
}
