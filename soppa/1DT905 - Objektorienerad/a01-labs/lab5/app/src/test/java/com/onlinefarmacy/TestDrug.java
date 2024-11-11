package com.onlinefarmacy;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class TestDrug {
    @Test
    public void createAndGetTest() {
        Drug testDrug = new Drug();
        testDrug.setDrug("Test", 15.0);
        assertEquals("Test", testDrug.getName());
        assertEquals(15.0, testDrug.getPrice());
    }
}
