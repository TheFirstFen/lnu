package org.example;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

public class GradeCTest {  
  @Test
  public void calculator_testAdd() {
    // Tests that the calculator add method works correctly.
    Calculator c = new Calculator();

    assertEquals(5, c.add(2.0, 3.0));
    assertEquals(0, c.add(0.0, 0.0));
    assertEquals(0, c.add(-1.0, 1.0));
    assertEquals(0, c.add(1.0, -1.0));
    assertEquals(-2, c.add(-1.0, -1.0));

  }


  @Test
  public void calculator_testSubtract() {
    // Tests that the calculator subtract method works correctly.
    Calculator c = new Calculator();
    assertEquals(-1, c.subtract(2.0, 3.0));
    assertEquals(0, c.subtract(0.0, 0.0));
    assertEquals(-2, c.subtract(-1.0, 1.0));
    assertEquals(2, c.subtract(1.0, -1.0));
    assertEquals(0, c.subtract(-1.0, -1.0));
  }


  @Test
  public void calculator_testMultiply() {
    // Tests that the calculator multiply method works correctly.
    Calculator c = new Calculator();
    assertEquals(6, c.multiply(2.0, 3.0));
    assertEquals(0, c.multiply(0.0, 0.0));
    assertEquals(-1, c.multiply(-1.0, 1.0));
    assertEquals(-1, c.multiply(1.0, -1.0));
    assertEquals(1, c.multiply(-1.0, -1.0));
  }


  @Test
  public void calculator_testDivide() {
    // Tests that the calculator divide method works correctly.
    Calculator c = new Calculator();
    assertEquals(2.0 / 3.0, c.divide(2.0, 3.0));
    assertEquals(-1.0, c.divide(-1.0, 1.0));
    assertEquals(-1.0, c.divide(1.0, -1.0));
    assertEquals(1.0, c.divide(-1.0, -1.0));
    // Tests that the calculator divide method sets the divideByZero field to true if the denominator is 0.
    c.divide(1.0, 0.0);
    assertTrue(c.isDivideByZero());
    // Tests that the calculator divide method sets the divideByZero field to false if the denominator is not 0.
    c.divide(1.0, 1.0);
    assertFalse(c.isDivideByZero());
  }
  

  @Test
  public void arrays2d_test() {
    // Tests that the arrays2D method works correctly.
    
    ArrayAlgorithms arrayAlgorithms = new ArrayAlgorithms();
    int[][] numbers = {   { 1, 2, 3 },
                          { 4, 5, 6 } };
    assertEquals(21, arrayAlgorithms.sum(numbers));
    int[][] numbers2 = {  { 1, 2, 3 },
                          { 4, 5, 6 },
                          { 7, 8, 9 } };
    int[][] transpose2 = { { 1, 4, 7 },
                           { 2, 5, 8 },
                           { 3, 6, 9 } };
    assertArrayEquals(transpose2, arrayAlgorithms.transpose(numbers2));

    // Tests that the transpose method returns the same array if the array is not square.
    assertArrayEquals(numbers, arrayAlgorithms.transpose(numbers));
    int[][] bigNumbers = {  {  1,  2,  3,  4,  5 },
                            {  6,  7,  8,  9, 10 },
                            { 11, 12, 13, 14, 15 },
                            { 16, 17, 18, 19, 20 },
                            { 21, 22, 23, 24, 25 } };
    int[][] bigTranspose = { {  1,  6, 11, 16, 21 },
                             {  2,  7, 12, 17, 22 },
                             {  3,  8, 13, 18, 23 },
                             {  4,  9, 14, 19, 24 },
                             {  5, 10, 15, 20, 25 } };
    
    assertArrayEquals(bigTranspose, arrayAlgorithms.transpose(bigNumbers));
      
    assertEquals(15, arrayAlgorithms.diagonalSum(numbers2));
    assertEquals(15, arrayAlgorithms.diagonalSum(transpose2));
    assertEquals(65, arrayAlgorithms.diagonalSum(bigNumbers));
    // Tests that the diagonalSum method returns 0 if the array is not square.
    assertEquals(0, arrayAlgorithms.diagonalSum(numbers));
    
  }


  @Test
  public void band_test() {
    // Test that the band methods work correctly.
    Band band = new Band("Pink Floyd", 1965);
    assertEquals("Pink Floyd", band.getName());
    assertEquals(1965, band.getYear());
    band.addAlbum("A Saucerful of Secrets", 1968);
    band.addAlbum("The Piper at the Gates of Dawn", 1967);
    band.addAlbum("More", 1969);
    band.addAlbum("Ummagumma", 1969);
    assertEquals(4, band.getAlbums().length);

    // check that the album artist is set to the band name
    assertEquals("Pink Floyd", band.getAlbums()[0].getArtist());

    // check that you can get the oldest album
    assertEquals("The Piper at the Gates of Dawn", band.getOldestAlbum().getTitle());
      
  }


}
