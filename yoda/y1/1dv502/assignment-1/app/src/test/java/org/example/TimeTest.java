package org.example;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/**
 * Test class for Time.
 */
public class TimeTest {
  
  @Test
  public void testToSeconds() {
    Time time = new Time();
    int h = 1;
    int m = 30;
    int s = 45;
    int expected = 5445;
    int result = time.toSeconds(h, m, s);
    assertEquals(expected, result);
  }

}
