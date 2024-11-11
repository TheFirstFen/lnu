package com.task3;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;


import org.junit.jupiter.api.Test;

public class GamefieldTest {
    Robot robot = new Robot();
    Wolf wolf = new Wolf();
    Home home = new Home();
    Strawberry strawberry = new Strawberry();
    Soup soup = new Soup();
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;


    @Test
    public void initializeTest() {
        GameField.initializeField();
        char[][] board = GameField.getBoard();
        
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                assertEquals('-', board[i][j]);
            }
        }
    }
    
    @Test
    public void setStartPosRobotTest() {
        GameField.setStartPosRobot(robot);
        assertEquals(0, robot.getCurrentRow());
        assertEquals(0, robot.getCurrentColumn());
    }
    @Test
    public void setPosHomeTest() {
        GameField.setPosHome(home);
        assertEquals(9, home.getCurrentRow());
        assertEquals(9, home.getCurrentColumn());
    }
    @Test
    public void CheckWolfStartPosInInterval() {
        GameField.setStartPosWolf(wolf);
        assertTrue(wolf.getCurrentRow() >= 3 && wolf.getCurrentRow() <= 9);
        assertTrue(wolf.getCurrentColumn() >= 3 && wolf.getCurrentColumn() <= 9);
    }
    @Test
    public void CheckStrawberryStartPosInInterval() {
        GameField.setPosStrawberry(strawberry, soup, 4, 4);
        assertTrue(strawberry.getCurrentRow() == 4 && strawberry.getCurrentRow() == 4);
        assertTrue(strawberry.getCurrentColumn() == 4 && strawberry.getCurrentColumn() == 4);
    }
    @Test
    public void CheckSoupStartPosInInterval() {
        GameField.setPosSoup(soup, strawberry, 3, 3);
        assertTrue(soup.getCurrentRow() == 3 && soup.getCurrentRow() == 3);
        assertTrue(soup.getCurrentColumn() == 3 && soup.getCurrentColumn() == 3);
    }

    @Test
    public void testRemoveStrawberry() {
        strawberry.SetNewPos(-1, -1);    
        GameField.removeStrawberry(strawberry);
        int newRow = strawberry.getCurrentRow();
        int newColumn = strawberry.getCurrentColumn();
        assertTrue(newRow >= 0 && newRow <= 7);
        assertTrue(newColumn >= 0 && newColumn <= 7);
    }
    @Test
    public void testRemoveSoup() {
        soup.SetNewPos(-1, -1);    
        GameField.removeSoup(soup);
        Integer newRow = soup.getCurrentRow();
        Integer newColumn = soup.getCurrentColumn();
        assertTrue(newRow >= 0 && newRow <= 7);
        assertTrue(newColumn >= 0 && newColumn <= 7);
    }

    @Test
    public void updateGameFieldTest() {
        System.setOut(new PrintStream(outContent));
        robot.SetNewPos(0, 1);
        wolf.SetNewPos(0, 2);
        home.SetNewPos(0, 3);
        soup.SetNewPos(0, 4);
        strawberry.SetNewPos(0, 5);
        GameField.initializeField();
        GameField.updateGameField(robot, wolf, home, strawberry, soup);
        assertEquals("- 🤖🐺🏛🍜🍓- - - - \n" +
                     "- - - - - - - - - - \n" +
                     "- - - - - - - - - - \n" +
                     "- - - - - - - - - - \n" +
                     "- - - - - - - - - - \n" +
                     "- - - - - - - - - - \n" +
                     "- - - - - - - - - - \n" +
                     "- - - - - - - - - - \n" +
                     "- - - - - - - - - - \n" +
                     "- - - - - - - - - - \n" +
                     "********************\n", outContent.toString());
            System.setOut(originalOut);

    }
    @Test
    public void updateGameFieldTimeToSpawnFalseTest() {
        System.setOut(new PrintStream(outContent));
        robot.SetNewPos(0, 1);
        wolf.SetNewPos(0, 2);
        home.SetNewPos(0, 3);
        soup.SetNewPos(0, 4);
        strawberry.SetNewPos(0, 5);
        strawberry.setTimeToSpawn(false);
        soup.setTimeToSpawn(false);
        GameField.initializeField();
        GameField.updateGameField(robot, wolf, home, strawberry, soup);
        assertEquals("- 🤖🐺🏛- - - - - - \n" +
                     "- - - - - - - - - - \n" +
                     "- - - - - - - - - - \n" +
                     "- - - - - - - - - - \n" +
                     "- - - - - - - - - - \n" +
                     "- - - - - - - - - - \n" +
                     "- - - - - - - - - - \n" +
                     "- - - - - - - - - - \n" +
                     "- - - - - - - - - - \n" +
                     "- - - - - - - - - - \n" +
                     "********************\n", outContent.toString());
            System.setOut(originalOut);

    }
    @Test
    public void updateGameFieldTimeToRemoveTest() {
        robot.SetNewPos(0, 1);
        wolf.SetNewPos(0, 2);
        home.SetNewPos(0, 3);
        soup.SetNewPos(0, 4);
        strawberry.SetNewPos(0, 5);
        strawberry.setTimeToSpawn(false);
        soup.setTimeToSpawn(false);
        strawberry.setTimeToremove(true);
        soup.setTimeToremove(true);
        GameField.initializeField();
        GameField.updateGameField(robot, wolf, home, strawberry, soup);
        GameField.updateGameField(robot, wolf, home, strawberry, soup);
        assertFalse(strawberry.getTimeToRemove());
        assertFalse(soup.getTimeToRemove());

    }
    @Test
    public void testSamePosStraw() {
        Soup soup3 = new Soup();
        Strawberry strawberry3 = new Strawberry();
        soup3.SetNewPos(4, 4);
        GameField.setPosStrawberry(strawberry3, soup3, 4, 4);
        assertFalse(strawberry.getCurrentColumn() == 4 || strawberry.getCurrentRow() == 4);
    }
    @Test
    public void testSamePosSoup() {
        Soup soup2 = new Soup();
        Strawberry strawberry2 = new Strawberry();
        strawberry2.SetNewPos(3, 3);
        GameField.setPosSoup(soup2, strawberry2, 3, 3);
        assertFalse(soup.getCurrentColumn() == 3 || soup.getCurrentRow() == 3);
    }
}
