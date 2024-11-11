package com.task3;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SoupTest {
    Soup soup = new Soup();

    @Test
    public void IconTest() {
        assertEquals("🍜", soup.getIcon());
    }
}
