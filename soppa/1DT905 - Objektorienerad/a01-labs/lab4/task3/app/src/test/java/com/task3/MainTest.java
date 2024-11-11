package com.task3;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class MainTest {
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;

    @BeforeEach
    public void setUpStreams() {
        System.setOut(new PrintStream(outContent));
    }

    @AfterEach
    public void restoreStreams() {
        System.setOut(originalOut);
    }

    @Test
    public void RobotWonTest() {
        ByteArrayInputStream testInput = new ByteArrayInputStream("2\n".getBytes());
        System.setIn(testInput);
        Main.playerHome = true;
        Main.exitprogram = false;
        Main.main(new String[0]);
        // Splits the output to each lines so i only compare the last line
        String[] lines = outContent.toString().split("\n");
        String Lastline = lines[lines.length - 1];
        assertEquals("You won! The robot is home", Lastline);
    }
    @Test
    public void exitTest() {
        ByteArrayInputStream testInput = new ByteArrayInputStream("q\n".getBytes());
        System.setIn(testInput);
        Main.main(new String[0]);
        assertTrue(Main.exitprogram);
    }
}