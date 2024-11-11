package com.task3;


import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import java.util.Scanner;


import org.junit.jupiter.api.Test;

public class GameLoopTest {
    Robot robot = new Robot();
    Wolf wolf = new Wolf();
    Home home = new Home();
    Strawberry strawberry = new Strawberry();
    Soup soup = new Soup();
    // Using mock to simulate a scanner for the method to acquire
    Scanner scanner = mock(Scanner.class);

    @Test
    public void testStartGameR4() {
        GameLoop.startGame(robot, wolf, home, strawberry, soup);
        GameLoop.setRounds(4);
        when(scanner.nextLine()).thenReturn("q");
        GameLoop.mainLoop(scanner, robot, wolf, home, strawberry, soup);
        assertEquals(0, GameLoop.getStrawberryRounds());
        assertEquals(0, GameLoop.getSoupRounds());
    }
    @Test
    public void testStartGameR0() {
        GameLoop.startGame(robot, wolf, home, strawberry, soup);
        GameLoop.setRounds(0);
        when(scanner.nextLine()).thenReturn("q");
        GameLoop.mainLoop(scanner, robot, wolf, home, strawberry, soup);
        assertTrue(strawberry.getTimeToSpawn());
        assertTrue(soup.getTimeToSpawn());
    }
    @Test
    public void testStartGameR0P5() {
        GameLoop.startGame(robot, wolf, home, strawberry, soup);
        GameLoop.setRounds(0);
        when(scanner.nextLine()).thenReturn("5");
        GameLoop.mainLoop(scanner, robot, wolf, home, strawberry, soup);
        assertTrue(strawberry.getTimeToSpawn());
        assertTrue(soup.getTimeToSpawn());
    }

}