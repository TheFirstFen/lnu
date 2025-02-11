package org.example;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/**
 * The simple hello there test class.
 */
public class HelloThereTest {
  
  @Test
  public void testHello() {
    HelloThere helloThere = new HelloThere();
    String greeting = helloThere.hello("Bob");
    assertEquals("Hello there, Bob", greeting);
  }
}
