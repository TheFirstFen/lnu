package task2.com.sb224sc.classes;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.AfterAll;

public class CalculatorTest {
    private final static Calculator calculator = new Calculator();

    @Test
    public void testAddition() {
        assertEquals(4.0, Calculator.calculate("2 + 2"), 0.001);
    }

    @Test
    public void testSubtraction() {
        assertEquals(2.0, Calculator.calculate("4 - 2"), 0.001);
    }

    @Test
    public void testMultiplication() {
        assertEquals(6.0, Calculator.calculate("2 * 3"), 0.001);
    }

    @Test
    public void testDivision() {
        assertEquals(2.0, Calculator.calculate("6 / 3"), 0.001);
    }

    @Test
    public void testInvalidInput() {
        assertEquals(Double.NaN, Calculator.calculate("2 +"), 0.001);
    }

    @Test
    public void testDivisionByZero() {
        assertEquals(Double.NaN, Calculator.calculate("4 / 0"), 0.001);
    }

    @Test
    public void testInvalidOperator() {
        assertEquals(Double.NaN, Calculator.calculate("4 % 2"), 0.001);
    }

    @Test
    public void testComplexExpression() {
        assertEquals(8.0, Calculator.calculate("2 + 2 * 2"), 0.001);
    }

    @Test
    public void testExpressionWithSpaces() {
        assertEquals(4.0, Calculator.calculate("2 + 2"), 0.001);
    }

    @Test
    public void testExpressionWithMixedSpaces() {
        assertEquals(4.0, Calculator.calculate("2 + 2 / 1"), 0.001);
    }

    @Test
    public void testInvalidOperand() {
        assertEquals(Double.NaN, Calculator.calculate("2 + a"), 0.001);
    }

    @AfterAll
    public static void tearDown() {
        calculator.toString();
    }
}
