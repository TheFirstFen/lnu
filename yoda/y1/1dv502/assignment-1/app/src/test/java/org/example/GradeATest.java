package org.example;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class GradeATest {
    
  @Test
  public void calculator_testSqrt() {
    // Tests that the calculator sqrt method works correctly.
    Calculator c = new Calculator();

    assertEquals(2.0, c.sqrt(4.0));
    assertEquals(0.0, c.sqrt(0.0));
    assertEquals(1.0, c.sqrt(1.0));
    assertEquals(0.0, c.sqrt(-1.0));


  }

  
  @Test
  public void calculator_testSquare() {
    // Tests that the calculator square method works correctly.
    Calculator c = new Calculator();
    
    assertEquals(4.0, c.square(2.0));
    assertEquals(0.0, c.square(0.0));
    assertEquals(1.0, c.square(1.0));
    assertEquals(1.0, c.square(-1.0));
  }


  @Test
  public void calculator_testFactorial() {
    // Tests that the calculator factorial method works correctly.
    Calculator c = new Calculator();
    assertEquals(6, c.factorial(3));
    assertEquals(1, c.factorial(0));
    assertEquals(1, c.factorial(1));
    assertEquals(1, c.factorial(-1));
  }


  


  @Test
  public void arrays3d_test() {
    // Tests that the arrays3D method works correctly.
    ArrayAlgorithms arrayAlgorithms = new ArrayAlgorithms();
    int[][][] numbers = { { { 1, 2, 3 },
                            { 4, 5, 6 } },
                          { { 7, 8, 9 },
                            { 10, 11, 12 } } };
    assertEquals(78, arrayAlgorithms.sum(numbers));

    assertEquals(1, arrayAlgorithms.minValue(numbers));

    assertEquals(12, arrayAlgorithms.maxValue(numbers));
    
  }


  @Test
  public void genre_test() {
    // Test that the genre methods work correctly.
    Band band = new Band("Pink Floyd", 1965);
    
    band.addAlbum("A Saucerful of Secrets", 1968, "Psychedelic rock");
    band.addAlbum("The Piper at the Gates of Dawn", 1967, "Psychedelic rock");
    band.addAlbum("More", 1969, "Psychedelic rock");
    band.addAlbum("Ummagumma", 1969, "Progressive rock");
    band.addAlbum("Atom Heart Mother", 1970, "Progressive rock");

    assertEquals(3, band.getAlbums("Psychedelic rock").length);
    assertEquals(2, band.getAlbums("Progressive rock").length);
      
  }
}
