package com.robotgame;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

/**
 * The Game class represents a game object that includes objects (robot, wolf, home, strawberry, soup) and the current round.
 * It provides methods to access the game objects, the current round, and to convert the game object to JSON format.
 */
public class Game {
    private Robot robot;
    private Wolf wolf;
    private Home home;
    private Strawberry strawberry;
    private Soup soup;
    private Integer round;

    /**
     * Constructs a new Game object and initializes the game objects and the current round.
     */
    public Game() {
        this.robot = new Robot();
        this.wolf = new Wolf();
        this.home = new Home();
        this.strawberry = new Strawberry();
        this.soup = new Soup();
        this.round = 1;
    }

    /**
     * Returns the Robot object.
     *
     * @return the Robot object
     */
    public Robot getRobot() {
        return robot;
    }

    /**
     * Returns the Wolf object.
     *
     * @return the Wolf object
     */
    public Wolf getWolf() {
        return wolf;
    }

    /**
     * Returns the Home object.
     *
     * @return the Home object
     */
    public Home getHome() {
        return home;
    }

    /**
     * Returns the Strawberry object.
     *
     * @return the Strawberry object
     */
    public Strawberry getStrawberry() {
        return strawberry;
    }

    /**
     * Returns the Soup object.
     *
     * @return the Soup object
     */
    public Soup getSoup() {
        return soup;
    }

    /**
     * Returns the current round as an Integer.
     *
     * @return the current round
     */
    public Integer getRound() {
        return round;
    }

    /**
     * Converts the Game object to JSON format.
     *
     * @return the Game object in JSON format
     */
    public String toJson() {
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        return gson.toJson(this);
    }
}

