package com.robotgame;

/**
 * Represents the home object.
 * 
 * The Home class is a subclass of the Object class in Java. It has a method to retrieve the icon of the home.
 */
public class Home extends Object {
    /**
     * Stores the emoji representation of a home icon.
     */
    final String homeIcon = "🏛";

    /**
     * Returns the value of the homeIcon field.
     * 
     * @return The emoji representation of a home icon.
     */
    public String getIcon() {
        return homeIcon;
    }
}
