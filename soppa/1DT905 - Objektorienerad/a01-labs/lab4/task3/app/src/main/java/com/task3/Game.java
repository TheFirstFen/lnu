package com.task3;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;


public class Game {
    private Robot robot;
    private Wolf wolf;
    private Home home;
    private Strawberry strawberry;
    private Soup soup;
    private Integer round;

    public Game() {
        // Initialize your game objects and set initial values
        this.robot = new Robot();
        this.wolf = new Wolf();
        this.home = new Home();
        this.strawberry = new Strawberry();
        this.soup = new Soup();
        this.round = 1;
    }


    public Robot getRobot() {
        return robot;
    }

    public Wolf getWolf() {
        return wolf;
    }

    public Home getHome() {
        return home;
    }

    public Strawberry getStrawberry() {
        return strawberry;
    }

    public Soup getSoup() {
        return soup;
    }

    public Integer getRound() {
        return round;
    }

    public String toJson() {
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        return gson.toJson(this);
}
}

