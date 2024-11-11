package com.blackjack;

import java.util.List;

public interface IFTurn {
    List<Integer> getValues();
    List<Card> getCards();
    Integer getMinValue();
    void newHand();
    void addCardToHand(Card card);
    void addFirstCardToHand();
    void calculateMinValue();
    boolean checkIfBlackjack();
    void calculateNewValue();
}