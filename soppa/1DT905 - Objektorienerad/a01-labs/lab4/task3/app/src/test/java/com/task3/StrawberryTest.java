package com.task3;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class StrawberryTest {
    Strawberry strawberry = new Strawberry();

    @Test
    public void IconTest() {
        assertEquals("🍓", strawberry.getIcon());
    }
}
