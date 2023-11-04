package org.lab5.com.sb224sc.classes;

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.PrintStream;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

class MainTest {
    private Main main;

    @Test
    void testRunWithValidConfig() {
        main = new Main();

        String simulatedUserInput = "8\n";

        InputStream inputStream = new ByteArrayInputStream(simulatedUserInput.getBytes());

        System.setIn(inputStream);
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        main.run();

        String consoleOutput = outputStream.toString();

        assertTrue(consoleOutput.contains("Welcome to "));
        assertTrue(consoleOutput.contains("Thanks for visiting "));
    }

    @AfterEach
    void tearDown() {
        System.setOut(System.out);
        System.setIn(System.in);
    }
}
