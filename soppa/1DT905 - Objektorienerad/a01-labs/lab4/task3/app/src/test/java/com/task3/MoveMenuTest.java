package com.task3;

import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import java.util.Scanner;

import org.junit.jupiter.api.Test;

public class MoveMenuTest {
    Robot robot = new Robot();
    Wolf wolf = new Wolf();
    Home home = new Home();
    Strawberry strawberry = new Strawberry();
    Soup soup = new Soup();
    // Using mock to simulate a scanner for the method to acquire
    Scanner scanner = mock(Scanner.class);

    @Test
    public void testMoveMenuInput() {
        GameLoop.startGame(robot, wolf, home, strawberry, soup);
        when(scanner.nextLine()).thenReturn("2");
        GameLoop.mainLoop(scanner, robot, wolf, home, strawberry, soup);
        assertTrue(robot.getCurrentColumn() == 1);
        when(scanner.nextLine()).thenReturn("3");
        GameLoop.mainLoop(scanner, robot, wolf, home, strawberry, soup);
        assertTrue(robot.getCurrentRow() == 1);
        when(scanner.nextLine()).thenReturn("4");
        GameLoop.mainLoop(scanner, robot, wolf, home, strawberry, soup);
        assertTrue(robot.getCurrentColumn() == 0);
        when(scanner.nextLine()).thenReturn("1");
        GameLoop.mainLoop(scanner, robot, wolf, home, strawberry, soup);
        assertTrue(robot.getCurrentRow() == 0);
    }
    @Test
    public void testMoveMenuInput5() {
        GameLoop.startGame(robot, wolf, home, strawberry, soup);
        when(scanner.nextLine()).thenReturn("5");
        GameLoop.mainLoop(scanner, robot, wolf, home, strawberry, soup);
        assertTrue(robot.getEnergy() > 5);
    }
    @Test
    public void testMoveMenuInputq() {
        GameLoop.startGame(robot, wolf, home, strawberry, soup);
        MoveMenu.check_input_choice("q", scanner, robot);
        assertTrue(Main.exitprogram);
    }

    @Test
    public void testMoveMenuInputError() {
        GameLoop.startGame(robot, wolf, home, strawberry, soup);
        when(scanner.nextLine()).thenReturn("q");
        MoveMenu.check_input_choice("x", scanner, robot);
        assertTrue(Main.exitprogram);
    }
    @Test
    public void testMoveMenuInputNoEnergy5() {
        GameLoop.startGame(robot, wolf, home, strawberry, soup);
        // Sets enrgy to 0
        while (robot.getEnergy() > 0) {
            robot.makeStep();
        }
        when(scanner.nextLine()).thenReturn("5");
        GameLoop.mainLoop(scanner, robot, wolf, home, strawberry, soup);
        assertTrue(robot.getEnergy() > 0);
    }

    @Test
    public void testMoveMenuInputNoEnergyq() {
        GameLoop.startGame(robot, wolf, home, strawberry, soup);
        // Sets enrgy to 0
        while (robot.getEnergy() > 0) {
            robot.makeStep();
        }
        MoveMenu.check_input_choice("q", scanner, robot);
        assertTrue(Main.exitprogram);
    }
    @Test
    public void testMoveMenuInputNoEnergyFalse() {
        GameLoop.startGame(robot, wolf, home, strawberry, soup);
        // Sets enrgy to 0
        while (robot.getEnergy() > 0) {
            robot.makeStep();
        }
        when(scanner.nextLine()).thenReturn("q");
        MoveMenu.check_input_choice("4", scanner, robot);
        assertTrue(Main.exitprogram);
    }
    @Test
    public void testMoveMenuInputErrorOutsideField() {
        GameLoop.startGame(robot, wolf, home, strawberry, soup);
        when(scanner.nextLine()).thenReturn("q");
        // Makes left and up imnpossible
        MoveMenu.check_input_choice("1", scanner, robot);
        assertTrue(Main.exitprogram);
        MoveMenu.check_input_choice("4", scanner, robot);
        assertTrue(Main.exitprogram);
        // Makes right impossible
        robot.SetNewPos(0, 9);
        MoveMenu.check_input_choice("2", scanner, robot);
        assertTrue(Main.exitprogram);
        // Makes down impossiple
        robot.SetNewPos(9, 0);
        MoveMenu.check_input_choice("3", scanner, robot);
        assertTrue(Main.exitprogram);
    }
}
