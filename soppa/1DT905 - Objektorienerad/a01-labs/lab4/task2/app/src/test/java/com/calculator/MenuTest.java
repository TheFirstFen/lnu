package com.calculator;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;


import org.junit.jupiter.api.Test;

public class MenuTest {
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;

    
    public void setUpStreams() {
        System.setOut(new PrintStream(outContent));
    }
    
    public void restoreStreams() {
        System.setOut(originalOut);
    }
    @Test
    public void exitTest() {
        Boolean result = Calculator.menu("q");
        assertTrue(result);
    }
    @Test
    public void correctInput() {
        Boolean result = Calculator.menu("1 + 1");
        assertFalse(result);
    }
    @Test
    public void NaNInput() {
        System.setOut(new PrintStream(outContent));
        Calculator.menu("1 + y");
        assertEquals("The sum is: NaN\n", outContent.toString());
        System.setOut(originalOut);

    }
    @Test
    public void falseInput() {
        System.setOut(new PrintStream(outContent));
        Calculator.menu("1 +1");
        assertEquals("Error please input a correct calculation.\n", outContent.toString());
        System.setOut(originalOut);
    }
}
