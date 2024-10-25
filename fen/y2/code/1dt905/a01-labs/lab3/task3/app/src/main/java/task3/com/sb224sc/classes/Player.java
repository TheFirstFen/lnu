package task3.com.sb224sc.classes;

import java.util.Scanner;

public class Player extends AbstractBlackjackPlayer {
    private DrawCard cardDrawer;

    public Player(DrawCard drawCard) {
        this.cardDrawer = drawCard;
    }

    /**
     * Determines whether the user wants to draw a card.
     *
     * @return true if the user wants to draw a card, false otherwise.
     */
    @Override
    public boolean wantsToDrawCard(Scanner sc) {
        System.out.print("\nDo you want to draw a card? (y/n): ");
        String choice = sc.nextLine().toLowerCase();
        if (choice.equals("cheat")) {
            System.out.println("Top card's value: " + cardDrawer.cheat().getValue());
            System.out.print("\nDo you want to draw that card? (y/n): ");
            choice = sc.nextLine().toLowerCase();
        }

        if (choice.equals("y")) {
            return true;
        } else if (choice.equals("q")) {
            System.exit(0);
            return false;
        } else {
            return false;
        }
    }

    /**
     * A description of the entire Java function.
     *
     * @return description of return value.
     */
    @Override
    public boolean wantsToDoubleDown() {
        // Implement logic for the player' decision to double down, if needed.
        return false;
    }

    /**
     * A description of the entire Java function.
     *
     * @return description of return value.
     */
    @Override
    public boolean wantsToSplit() {
        // Implement logic for the players decision to split, if needed.
        return false;
    }

    /**
     * Retrieves the value of the player's card.
     *
     * @return the value of the player's card.
     */
    public int getPlayerCardValue() {
        return getScore();
    }
}