package task3.com.sb224sc.classes;

import task3.com.sb224sc.interfaces.*;

public abstract class AbstractBlackjackPlayer extends AbstractPlayer implements IBlackjackPlayer {
    public AbstractBlackjackPlayer() {
        super();
    }

    public void clearHand() {
        hand.clear();
        score = 0;
        amountOfCardsDrawn = 0;
    }

    /**
     * A description of the entire Java function.
     *
     * @return description of return value
     */
    @Override
    public boolean wantsToSplit() {
        return false;
    }

    /**
     * Determines whether the player wants to double down.
     *
     * @return description of return value
     */
    @Override
    public boolean wantsToDoubleDown() {
        return false;
    }
}
