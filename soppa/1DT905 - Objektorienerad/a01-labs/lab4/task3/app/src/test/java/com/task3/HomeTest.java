package com.task3;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class HomeTest {
        Home home = new Home();

    @Test
    public void IconTest() {
        assertEquals("🏛", home.getIcon());
    }
}

