package task3.com.sb224sc.classes;

import java.util.Scanner;

public class Dealer extends AbstractBlackjackPlayer {
    public Dealer() {
        super();
    }

    /**
     * Determines if the player wants to stand based on their score.
     *
     * @return true if the player wants to stand, false otherwise.
     */
    public boolean wantsToStand() {
        return getScore() >= 17;
    }

    /**
     * Determines if the player wants to draw a card.
     *
     * @return true if the player wants to draw a card, false otherwise.
     */
    @Override
    public boolean wantsToDrawCard(Scanner sc) {
        if (getScore() < 17) {
            return true;
        }
        return false;
    }

    /**
     * Returns the value of the face-up card of the dealer.
     *
     * @return the value of the face-up card of the dealer, or 0 if the hand is
     *         empty.
     */
    public int getDealerFaceUpCardValue() {
        if (!hand.isEmpty()) {
            return hand.get(0).getValue();
        } else {
            return 0;
        }
    }

    /**
     * A description of the entire Java function.
     *
     * @return score.
     */
    public int getDealerCardValue() {
        return getScore();
    }

    /**
     * Retrieves the dealer's face-up card.
     *
     * @return the dealer's face-up card, or null if the hand is empty.
     */
    public Card getDealerFaceUpCard() {
        if (!hand.isEmpty()) {
            return hand.get(0);
        } else {
            return null;
        }
    }
}
