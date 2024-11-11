package com.calculator;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;

import org.junit.jupiter.api.Test;

public class CheckErrorTest {
    @Test
    // Checks if two numbers have been inputed after each other
    public void DoubleNumTest() {
        Boolean result = Calculator.checkForError(Arrays.asList("2.0", "+", "3.0", "5.0"));
        assertEquals(Boolean.valueOf(true), result);
    }
    @Test
    public void DoubleOperatorTest() {
        Boolean result = Calculator.checkForError(Arrays.asList("2.0", "+", "+", "5.0"));
        assertEquals(Boolean.valueOf(true), result);
    }
    @Test
    public void DivideByZeroTest() {
        Boolean result = Calculator.checkForError(Arrays.asList("2", "/", "0"));
        assertTrue(result);
    }
    @Test
    public void NotANumberTest() {
        Boolean result = Calculator.checkForError(Arrays.asList("2", "/", "y"));
        assertTrue(result); 
    }
    @Test
    public void NoErrorTest() {
        Boolean result = Calculator.checkForError(Arrays.asList("2", "/", "1"));
        assertEquals(Boolean.valueOf(false), result);
    }
    @Test
    public void failTest() {
        Boolean result = Calculator.checkForError(Arrays.asList("1", "k", "7"));
        assertEquals(Boolean.valueOf(true), result);
    }
    @Test
    public void LaterDivByZeroTest() {
        Boolean result = Calculator.checkForError(Arrays.asList("5", "+", "0", "/", "0"));
        assertEquals(Boolean.valueOf(true), result);
    }
    @Test
    public void tempTest() {
        Boolean result = Calculator.checkForError(Arrays.asList("5", "+", "5" ,"*", "*"));
        assertEquals(Boolean.valueOf(true), result);
    }
}

