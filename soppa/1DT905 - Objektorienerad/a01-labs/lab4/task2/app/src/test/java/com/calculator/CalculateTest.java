package com.calculator;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Arrays;

import org.junit.jupiter.api.Test;

public class CalculateTest {
    @Test
    public void testCalculate() {
        // Test 1 Addition
        Double result1 = Calculator.calculate(Arrays.asList("2.0", "+", "3.0"));
        assertEquals(Double.valueOf(5.0), result1);

        // Test 2 Subtract
        Double result2 = Calculator.calculate(Arrays.asList("5.0", "-", "2.0"));
        assertEquals(Double.valueOf(3.0), result2);

        // Test 3 Multiplication
        Double result3 = Calculator.calculate(Arrays.asList("2.0", "*", "8.0"));
        assertEquals(Double.valueOf(16.0), result3);

        // Test 4 Division
        Double result4 = Calculator.calculate(Arrays.asList("8.0", "/", "2.0"));
        assertEquals(Double.valueOf(4.0), result4);
    }
    
}
