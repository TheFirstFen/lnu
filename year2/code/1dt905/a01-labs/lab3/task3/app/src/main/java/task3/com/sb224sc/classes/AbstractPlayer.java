package task3.com.sb224sc.classes;

import java.util.ArrayList;
import java.util.List;

import task3.com.sb224sc.interfaces.*;

public abstract class AbstractPlayer implements IPlayer {
    protected List<Card> hand;
    protected int score;
    protected int amountOfCardsDrawn = 0;

    public AbstractPlayer() {
        hand = new ArrayList<>();
        score = 0;
    }

    /**
     * Retrieves the hand of cards.
     *
     * @return The list of cards representing the hand.
     */
    public List<Card> getHand() {
        return hand;
    }

    /**
     * A description of the entire Java function.
     *
     * @param card the card to be received.
     */
    @Override
    public void receiveCard(Card card) {
        amountOfCardsDrawn++;

        if (amountOfCardsDrawn > 2) {
            System.out.println("\nDrew Card: " + card);
        }
        hand.add(card);
        score += card.getValue();
    }

    /**
     * Calculates the score of the player's hand in a card game.
     *
     * @return the calculated score of the player's hand.
     */
    @Override
    public int getScore() {
        int calculatedScore = 0;
        boolean hasAce = false;

        for (Card card : hand) {
            calculatedScore += card.getValue();

            if (card.getRank().equals("Ace")) {
                hasAce = true;
            }
        }

        if (hasAce && calculatedScore > 21) {
            calculatedScore -= 10;
        }

        return calculatedScore;
    }

    /**
     * Resets the state of the object.
     *
     */
    @Override
    public void reset() {
        hand.clear();
        score = 0;
    }
}
