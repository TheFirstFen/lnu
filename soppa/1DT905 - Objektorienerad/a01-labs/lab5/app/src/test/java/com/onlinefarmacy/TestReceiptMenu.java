package com.onlinefarmacy;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.Scanner;

public class TestReceiptMenu {
    private Scanner scanner;
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;

    @BeforeEach
    public void setUp() {
        System.setOut(new PrintStream(outContent));
        scanner = mock(Scanner.class);
    }

    @AfterEach
    public void tearDown() {
        System.setOut(originalOut);
    }

    @Test
    public void testShowReceipt() {
        Receipt testReceipt = new Receipt();
        testReceipt.setDateTime();
        testReceipt.setDrugName("Test Drug");
        ReceiptStorage.storeReceipt(testReceipt);

        when(scanner.nextLine()).thenReturn("1");
        ReceiptMenu.showChoices();
        ReceiptMenu.showReceipt("1", scanner);
        assertTrue(outContent.toString().contains(testReceipt.getDateTime()));
        assertTrue(outContent.toString().contains(testReceipt.getDrugName()));
    }
    @Test
    public void testShowReceiptFalseInputText() {
        Receipt testReceipt = new Receipt();
        testReceipt.setDateTime();
        testReceipt.setDrugName("Test Drug");
        ReceiptStorage.storeReceipt(testReceipt);
        when(scanner.nextLine()).thenReturn("1");
        ReceiptMenu.showChoices();
        ReceiptMenu.showReceipt("f", scanner);
        assertTrue(outContent.toString().contains(testReceipt.getDateTime()));
        assertTrue(outContent.toString().contains(testReceipt.getDrugName()));
    }

    @Test
    public void testRemoveReceipt() {
        InitializeDrugs.setDrugs();
        InitializeReceipts.setReceipts();
        when(scanner.nextLine()).thenReturn("y");
        ReceiptMenu.removeReceipt("1", scanner);
        assertTrue(outContent.toString().contains("Receipt was removed!"));
    }
    @Test
    public void testInputRemoveFalseInput() {
        InitializeDrugs.setDrugs();
        InitializeReceipts.setReceipts();
        when(scanner.nextLine()).thenReturn("y");
        ReceiptMenu.incorrectInputRemove("f", scanner, "1");
        assertTrue(outContent.toString().contains("Receipt was removed!"));
    }

    @Test
    public void testUpdateReceiptDrug() {
        InitializeDrugs.setDrugs();
        InitializeReceipts.setReceipts();
        when(scanner.nextLine()).thenReturn("1");
        ReceiptMenu.updateReceipt("1", scanner);
        assertEquals("Alvedon", ReceiptStorage.getStoredReceipts().get(0).getDrugName());
    }
    @Test
    public void testIncorrectUpdateFalseInput() {
        InitializeDrugs.setDrugs();
        InitializeReceipts.setReceipts();
        when(scanner.nextLine()).thenReturn("q");
        ReceiptMenu.incorrectInputUpdate("f", scanner, "1");
        assertFalse(outContent.toString().contains("Receipt was updated"));
    }

    @Test
    public void testUpdateReceiptQuantity() {
        Receipt testReceipt = new Receipt();
        testReceipt.setDateTime();
        testReceipt.setDrugName("Test Drug");
        testReceipt.setAPrice(50.0);
        testReceipt.setAmount(2);
        ReceiptStorage.storeReceipt(testReceipt);

        when(scanner.nextLine()).thenReturn("2");
        ReceiptMenu.updateReceipt("1", scanner);
        assertEquals(2, testReceipt.getAmount());
    }
    @Test
    public void testDrugChoiceInput() {
        assertEquals(0, ReceiptMenu.check_input_choice_drug("1", scanner));
        assertEquals(1, ReceiptMenu.check_input_choice_drug("2", scanner));
        assertEquals(2, ReceiptMenu.check_input_choice_drug("3", scanner));
        assertEquals(3, ReceiptMenu.check_input_choice_drug("4", scanner));
        assertEquals(4, ReceiptMenu.check_input_choice_drug("5", scanner));
        when(scanner.nextLine()).thenReturn("1");
        assertEquals(0, ReceiptMenu.check_input_choice_drug("f", scanner));
    }
}

