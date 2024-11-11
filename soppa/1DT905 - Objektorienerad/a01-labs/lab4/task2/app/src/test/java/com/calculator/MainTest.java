package com.calculator;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.PrintStream;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class MainTest {
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private final ByteArrayInputStream inContent = new ByteArrayInputStream(new byte[0]);
    private final PrintStream originalOut = System.out;
    private final InputStream originalIn = System.in;

    @BeforeEach
    public void setUpStreams() {
        System.setOut(new PrintStream(outContent));
        System.setIn(inContent);
    }

    @AfterEach
    public void restoreStreams() {
        System.setOut(originalOut);
        System.setIn(originalIn);
    }

    @Test
    public void testMainWithExit() {
        ByteArrayInputStream testInput = new ByteArrayInputStream("q\n".getBytes());
        System.setIn(testInput);

        Calculator.main(new String[0]);

        assertEquals("Enter the calculation(q to quit): Exiting the program...\n", outContent.toString());
    }

    @Test
    public void testMainWithCalculation() {
        ByteArrayInputStream testInput = new ByteArrayInputStream("2 + 2\nq\n".getBytes());
        System.setIn(testInput);

        Calculator.main(new String[0]);

        assertEquals("Enter the calculation(q to quit): The sum is: 4.0\nEnter the calculation(q to quit): Exiting the program...\n", outContent.toString());
    }
}
