package com.onlinefarmacy;

import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.Scanner;

import org.junit.jupiter.api.Test;

public class TestMenu {
    private Scanner scanner;
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;

    @Test
    public void testMenuWithUserInput() {
        scanner = mock(Scanner.class);
        when(scanner.nextLine()).thenReturn("q");
        String recDirectory = "ExportsTest";
        Menu.menu(scanner, recDirectory);
        assertTrue(Main.exitprogram);
    }
    @Test
    public void testInput1() {
        System.setOut(new PrintStream(outContent));
        scanner = mock(Scanner.class);
        when(scanner.nextLine()).thenReturn("1");
        String recDirectory = "ExportsTest";
        InitializeDrugs.setDrugs();
        InitializeReceipts.setReceipts();
        Menu.menu(scanner, recDirectory);
        System.out.println(outContent.toString());
        assertTrue(outContent.toString().contains("1000"));
        assertTrue(outContent.toString().contains("1001"));
        assertTrue(outContent.toString().contains("1002"));
        assertTrue(outContent.toString().contains("1003"));
        assertTrue(outContent.toString().contains("1004"));
        System.setOut(originalOut);
    }
    @Test
    public void testInput2() {
        System.setOut(new PrintStream(outContent));
        scanner = mock(Scanner.class);
        when(scanner.nextLine()).thenReturn("1");
        String recDirectory = "ExportsTest";
        InitializeDrugs.setDrugs();
        InitializeReceipts.setReceipts();
        Menu.check_input_choice("2", scanner, recDirectory);
        assertTrue(outContent.toString().contains("1000"));
        System.setOut(originalOut);
    }
    @Test
    public void testInput3() {
        System.setOut(new PrintStream(outContent));
        scanner = mock(Scanner.class);
        when(scanner.nextLine()).thenReturn("1");
        String recDirectory = "ExportsTest";
        InitializeDrugs.setDrugs();
        InitializeReceipts.setReceipts();
        Menu.check_input_choice("3", scanner, recDirectory);
        assertTrue(outContent.toString().contains("Alvedon"));
        System.setOut(originalOut);
    }
    @Test
    public void testInput4() {
        System.setOut(new PrintStream(outContent));
        scanner = mock(Scanner.class);
        when(scanner.nextLine()).thenReturn("2");
        String recDirectory = "ExportsTest";
        InitializeDrugs.setDrugs();
        InitializeReceipts.setReceipts();
        Menu.check_input_choice("4", scanner, recDirectory);
        ReceiptMenu.showReceipt("2", scanner);
        assertTrue(outContent.toString().contains(": 2"));
        System.setOut(originalOut);
    }
    @Test
    public void testInput6() {
        System.setOut(new PrintStream(outContent));
        scanner = mock(Scanner.class);
        when(scanner.nextLine()).thenReturn("q");
        String recDirectory = "ExportsTest";
        InitializeDrugs.setDrugs();
        InitializeReceipts.setReceipts();
        Menu.check_input_choice("6", scanner, recDirectory);
        assertTrue(outContent.toString().contains("Files saved to "));
        assertTrue(outContent.toString().contains("JsonExports"));
        System.setOut(originalOut);
    }
    @Test
    public void testInput7() {
        System.setOut(new PrintStream(outContent));
        scanner = mock(Scanner.class);
        when(scanner.nextLine()).thenReturn("q");
        String recDirectory = "ExportsTest";
        InitializeDrugs.setDrugs();
        InitializeReceipts.setReceipts();
        Menu.check_input_choice("7", scanner, recDirectory);
        assertTrue(outContent.toString().contains("Files saved to "));
        assertTrue(outContent.toString().contains("CSVExports"));
        System.setOut(originalOut);
    }
    @Test
    public void testInputq() {
        scanner = mock(Scanner.class);
        String recDirectory = "ExportsTest";
        Menu.check_input_choice("q", scanner, recDirectory);
        assertTrue(Main.exitprogram);
    }
    @Test
    public void testInputFalse() {
        scanner = mock(Scanner.class);
        when(scanner.nextLine()).thenReturn("q");
        String recDirectory = "ExportsTest";
        Menu.check_input_choice("f", scanner, recDirectory);
        assertTrue(Main.exitprogram);
    }
}


