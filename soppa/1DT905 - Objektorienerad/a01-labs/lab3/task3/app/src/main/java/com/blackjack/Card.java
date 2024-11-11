package com.blackjack;


import java.util.ArrayList;
import java.util.List;

public class Card {
    private String rank;
    private String suit;

    public void addRank(String rank) {
        this.rank = rank;
    }

    public void addSuit(String suit) {
        this.suit = suit;
    }

    public String getCard() {
        return rank + " of " + suit;
    }


    public static List<Integer> getValue(Card tempCard) {
        List<Integer> values = new ArrayList<>();
        String tempRank = tempCard.getCard().split(" ")[0];
        try {
            values.add(Integer.parseInt(tempRank));
        } catch (NumberFormatException e) {
            if (tempRank.equalsIgnoreCase("jack")) {
                values.add(10);
            } else if (tempRank.equalsIgnoreCase("queen")) {
                values.add(10);
            } else if (tempRank.equalsIgnoreCase("king")) {
                values.add(10);
            } else {
                values.add(14);
                values.add(1);
            }
        }
        return values;
    }
}
