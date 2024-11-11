package com.task3;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class CollisionsTest {

    @Test
    public void testCheckCollisionsWithWolf() {
        Robot robot = new Robot();
        Wolf wolf = new Wolf();
        robot.SetNewPos(2, 2);
        wolf.SetNewPos(2, 2);

        Collisions.checkCollisions(robot, wolf, new Home(), new Strawberry(), new Soup());

        assertEquals(5, robot.getEnergy());
    }

    @Test
    public void testCheckCollisionsWithStrawberry() {
        Robot robot = new Robot();
        Strawberry strawberry = new Strawberry();
        Wolf wolf = new Wolf();
        wolf.SetNewPos(0, 0);
        robot.SetNewPos(3, 3);
        strawberry.SetNewPos(3, 3);

        Collisions.checkCollisions(robot, wolf, new Home(), strawberry, new Soup());

        assertEquals(8, robot.getEnergy());
    }

    @Test
    public void testCheckCollisionsWithSoup() {
        Robot robot = new Robot();
        Soup soup = new Soup();
        Wolf wolf = new Wolf();
        wolf.SetNewPos(0, 0);
        robot.SetNewPos(4, 4);
        soup.SetNewPos(4, 4);

        Collisions.checkCollisions(robot, wolf, new Home(), new Strawberry(), soup);

        assertEquals(12, robot.getHealth());
    }

    @Test
    public void testCheckCollisionsWithHome() {
        Robot robot = new Robot();
        Home home = new Home();
        Wolf wolf = new Wolf();
        wolf.SetNewPos(0, 0);
        robot.SetNewPos(5, 5);
        home.SetNewPos(5, 5);

        Collisions.checkCollisions(robot, wolf, home, new Strawberry(), new Soup());

        assertTrue(Main.playerHome);
    }

    @Test
    public void testFightInteractionRobotWin() {
        Robot robot = new Robot();
        Wolf wolf = new Wolf();
        robot.SetNewPos(1, 1);
        wolf.SetNewPos(1, 1);

        Collisions.fightInteraction(robot, wolf, true, 5);

        assertEquals(5, wolf.getRoundToMove()); 
    }

    @Test
    public void testFightInteractionRobotLose() {
        Robot robot = new Robot();
        Wolf wolf = new Wolf();
        robot.SetNewPos(1, 1);
        wolf.SetNewPos(1, 1);

        Collisions.fightInteraction(robot, wolf, false, 5);

        assertTrue(robot.getHealth() == 5);
    }
    @Test
    public void testFightInteractionRobotDead() {
        Robot robot = new Robot();
        Wolf wolf = new Wolf();
        robot.SetNewPos(1, 1);
        wolf.SetNewPos(1, 1);

        Collisions.fightInteraction(robot, wolf, false, 10);

        assertTrue(robot.getHealth() == 0);
    }
}

