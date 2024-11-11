package com.calculator;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class MultiplicationTest {
    @Test
    public void testMultiplication() {
        Double result = Calculator.multiplication(5.0, 2.0);
        assertEquals(Double.valueOf(10.0), result);
    }
}
