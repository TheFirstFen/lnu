package com.calculator;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class DivisionTest {
    @Test
    public void TestDivision() {
        Double result = Calculator.division(5.0, 2.0);
        assertEquals(Double.valueOf(2.5), result);
    }
}
