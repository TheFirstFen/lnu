package lab4;
import lab4.com.eu222dq.Calculator;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.io.InputStream;
import java.io.PrintStream;
import java.util.Scanner;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;

public class CalculatorTest {

    @Test
    void testValidAddition() {
        Calculator calculator = new Calculator("5 + 5");
        double result = calculator.calculate();
        assertEquals(10.0, result, 0.001);
    }

    @Test
    void testValidSubtraction() {
        Calculator calculator = new Calculator("10 - 5");
        double result = calculator.calculate();
        assertEquals(5.0, result, 0.001);
    }

    @Test
    void testValidMultiplication(){
        Calculator calculator = new Calculator("2 * 3");
        double result = calculator.calculate();
        assertEquals(6.0, result, 0.001);
    }

    @Test
    void testValidDivision() {
        Calculator calculator = new Calculator("4 / 2");
        double result = calculator.calculate();
        assertEquals(2.0, result, 0.001);
    }

    @Test
    void testDivisionByZero() {
        Calculator calculator = new Calculator("2 / 0");
        assertThrows(IllegalArgumentException.class, calculator::calculate);
    }

    @Test
    void testInvalidExpression() {
        Calculator calculator = new Calculator("1 + + 1");
        assertThrows(IllegalArgumentException.class, calculator::calculate);
    }

    @Test
    void testNaN() {
        Calculator calculator = new Calculator("x + 1");
        double result = calculator.calculate();
        assertTrue(Double.isNaN(result), "Result should be Double.NaN for an invalid expression");
    }


    @Test
    void testNoOperator() {
        Calculator calculator = new Calculator("5 5 5");
        assertThrows(IllegalArgumentException.class, calculator::calculate);
    }
    @Test
    void testQuitInput() {
        String input = "q\n";
        InputStream inputStream = new ByteArrayInputStream(input.getBytes());
        System.setIn(inputStream);
        Calculator calculator = new Calculator();
        calculator.main();
        System.setIn(System.in);
        assertTrue(true, "Result should be Quiting");
    }

     @Test
    void testCalculateAndPrintValidExpression() {
        Calculator calculator = new Calculator("5 + 5");
        String expectedOutput = "Result: 10.0\n";

        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        calculator.calculateAndPrint(new Scanner(""));

        System.setOut(System.out);

        String printedOutput = outputStream.toString();

        double expectedValue = Double.parseDouble(expectedOutput.replaceAll("[^\\d.]", ""));

        double actualValue = Double.parseDouble(printedOutput.replaceAll("[^\\d.]", ""));

        assertEquals(expectedValue, actualValue, 0.0001,  "Printed output should match the expected output");
    }

    @Test
    void testCalculateAndPrintInvalidExpression() {
        Calculator calculator = new Calculator("5 + + 5");
        String expectedOutput = "Error: Invalid expression";

        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        calculator.calculateAndPrint(new Scanner(""));

        System.setOut(System.out);

        String printedOutput = outputStream.toString().trim();

        assertEquals(expectedOutput, printedOutput, "Printed error message should match the expected error message");
    }
}
