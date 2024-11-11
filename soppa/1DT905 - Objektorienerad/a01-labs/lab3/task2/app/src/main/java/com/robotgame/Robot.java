package com.robotgame;

import java.util.Random;

/**
 * Represents a robot character.
 * Extends the Characters class and has fields for energy and health, as well as a robot icon.
 * Provides methods to retrieve the robot's icon, energy, and health, as well as methods to pick up strawberries and soup to increase energy and health respectively.
 * Also has methods to set the robot's health after taking damage, rest to randomly increase energy, and make a step to decrease energy.
 */
public class Robot extends Characters {
    private Integer energy = 5;
    private Integer health = 10;
    final String robotIcon = "🤖";

    /**
     * Returns the robot's icon.
     * @return The robot's icon.
     */
    public String getIcon() {
        return robotIcon;
    }

    /**
     * Returns the robot's energy.
     * @return The robot's energy.
     */
    public Integer getEnergy() {
        return energy;
    }
    
    /**
     * Increases the robot's energy by 3.
     */
    public void strawberryPickup() {
        energy += 3;
    }

    /**
     * Returns the robot's health.
     * @return The robot's health.
     */
    public Integer getHealth() {
        return health;
    }

    /**
     * Increases the robot's health by 2.
     */
    public void soupPickup() {
        health += 2;
    }

    /**
     * Decreases the robot's health by the specified amount.
     * @param damage The amount of damage to be taken.
     */
    public void setHealth(Integer damage) {
        health = health - damage;
    }

    /**
     * Randomly increases the robot's energy and returns the amount rested.
     * @return The amount of energy rested.
     */
    public Integer rest() {
        Random random = new Random();
        Integer restedEnergy = random.nextInt(1, 6);
        energy += restedEnergy;
        return restedEnergy;
    }

    /**
     * Decreases the robot's energy by 1.
     */
    public void makeStep() {
        energy -= 1;
    }
}
