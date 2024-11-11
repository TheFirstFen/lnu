package com.calculator;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class AdditionTest {
    @Test
    public void testAddition() {
        Double result = Calculator.addition(5.0, 1.2);
        assertEquals(Double.valueOf(6.2), result);
    }
}
