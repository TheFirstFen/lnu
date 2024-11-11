package com.onlinefarmacy;


import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import java.util.Scanner;

import org.junit.jupiter.api.Test;

public class TestCreateMenu {

    @Test
    public void testCreateReceiptMenu1() {
        InitializeDrugs.setDrugs();
        InitializeReceipts.setReceipts();
        Scanner scanner = mock(Scanner.class);
        when(scanner.nextLine()).thenReturn("1");
        CreateReceiptMenu.createReceiptMenu(scanner);
        assertEquals("Alvedon", ReceiptStorage.getStoredReceipts().get(5).getDrugName());
        assertEquals(1, ReceiptStorage.getStoredReceipts().get(5).getAmount());
    }
    @Test
    public void testCreateReceiptMenu2() {
        Scanner scanner = mock(Scanner.class);
        when(scanner.nextLine()).thenReturn("2");
        CreateReceiptMenu.check_input_choice("2", scanner);
        assertEquals("Ipren", ReceiptStorage.getStoredReceipts().get(6).getDrugName());
        assertEquals(2, ReceiptStorage.getStoredReceipts().get(6).getAmount());
    }
    @Test
    public void testCreateReceiptMenu3() {
        Scanner scanner = mock(Scanner.class);
        when(scanner.nextLine()).thenReturn("3");
        CreateReceiptMenu.check_input_choice("3", scanner);
        assertEquals("Desloratadine", ReceiptStorage.getStoredReceipts().get(7).getDrugName());
        assertEquals(3, ReceiptStorage.getStoredReceipts().get(7).getAmount());
    }
    @Test
    public void testCreateReceiptMenu4() {
        Scanner scanner = mock(Scanner.class);
        when(scanner.nextLine()).thenReturn("4");
        CreateReceiptMenu.check_input_choice("4", scanner);
        assertEquals("Brikanyl", ReceiptStorage.getStoredReceipts().get(8).getDrugName());
        assertEquals(4, ReceiptStorage.getStoredReceipts().get(8).getAmount());
    }
    @Test
    public void testCreateReceiptMenu5() {
        Scanner scanner = mock(Scanner.class);
        when(scanner.nextLine()).thenReturn("5");
        CreateReceiptMenu.check_input_choice("5", scanner);
        assertEquals("Morifin", ReceiptStorage.getStoredReceipts().get(9).getDrugName());
        assertEquals(5, ReceiptStorage.getStoredReceipts().get(9).getAmount());
    }
    @Test
    public void testCreateReceiptMenuFalse() {
        Scanner scanner = mock(Scanner.class);
        when(scanner.nextLine()).thenReturn("5");
        CreateReceiptMenu.check_input_choice("g", scanner);
        assertEquals("Morifin", ReceiptStorage.getStoredReceipts().get(9).getDrugName());
        assertEquals(5, ReceiptStorage.getStoredReceipts().get(9).getAmount());
    }
}

