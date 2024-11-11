package com.calculator;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SubtractTest {
    @Test
    public void testSubtract() {
        Double result = Calculator.subtract(5.0, 1.2);
        assertEquals(Double.valueOf(3.8), result);
    }
}
