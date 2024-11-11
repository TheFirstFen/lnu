package com.task3;

import java.util.Random;

public class Robot extends Characters {
    private Integer energy = 5;
    private Integer health = 10;
    final String robotIcon = "🤖";


    public String getIcon() {
        return robotIcon;
    }

    public Integer getEnergy() {
        return energy;
    }
    
    public void strawberryPickup() {
        energy += 3;
    }

    public Integer getHealth() {
        return health;
    }

    public void soupPickup() {
        health += 2;
    }
    public void setHealth(Integer damage) {
        health = health - damage;
    }

    public Integer rest() {
        Random random = new Random();
        Integer restedEnergy = random.nextInt(1, 6);
        energy += restedEnergy;
        return restedEnergy;
    }

    public void makeStep() {
        energy -= 1;
    }
}
