package task3.com.task3.helpers;

import java.util.ArrayList;
import java.util.List;

public class Card {
    private static String rank;
    private static String suit;

    public void addRank(String rank) {
        Card.rank = rank;
    }

    public void addSuit(String suit) {
        Card.suit = suit;
    }

    public String getCard() {
        return rank + " of " + suit;
    }


    public static List<Integer> getValue(String tempCard) {
        List<Integer> values = new ArrayList<>();
        String tempRank = tempCard.split(" ")[0];
        try {
            values.add(Integer.parseInt(tempRank));
        } catch (NumberFormatException e) {
            if (tempRank.equalsIgnoreCase("jack")) {
                values.add(11);
            } else if (tempRank.equalsIgnoreCase("queen")) {
                values.add(12);
            } else if (tempRank.equalsIgnoreCase("king")) {
                values.add(13);
            } else {
                values.add(14);
                values.add(1);
            }
        }
        return values;
    }
}
