package com.blackjack;

import java.util.ArrayList;
import java.util.List;

public class Turn implements IFTurn{
    private List<Card> currentCards;
    private List<Integer> currentValues;;
    private Integer minValue = 100; // Placeholder for first min value

    public List<Integer> getValues() {
        calculateNewValue();
        return currentValues;

    }

    public List<Card> getCards() {
        return currentCards;
    }
    public Integer getMinValue(){
        calculateNewValue();
        calculateMinValue();
        return minValue;
    }

    public void newHand() {
        currentCards = new ArrayList<>();
    }
    public void addCardToHand(Card card) {
        currentCards.add(card);
        calculateNewValue();
    }
    public void addFirstCardToHand() {
        Card card = Deck.getNewCard();
        currentCards.add(card);
        calculateNewValue();
    }

    public void calculateMinValue() {
        minValue = 100;
        for (Integer value : getValues()) {
            if (value < minValue) {
                minValue = value;
            }
        }
    }

    public Integer getBestValue() {
        Integer bestValue = null;
        for (Integer value : getValues()) {
            if (value <= 21) {
                bestValue = value;
            }
        }
        return bestValue;
    }



    public boolean checkIfBlackjack () {
        calculateNewValue();
        boolean blackJack = false;
        for (Integer value : currentValues)
            if (value.equals(21)) {
                blackJack = true;
            }
        return blackJack;
    }

    public void calculateNewValue() {
        Integer countAce = 0;
        Integer sum1 = 0;
        Integer sum2 = 0;
        Integer sum3 = 0;
        Integer sum4 = 0;
        Integer sum5 = 0;
        currentValues = new ArrayList<>();
        for (Card card : currentCards) {
            List<Integer> cardValues = new ArrayList<>();
            cardValues = Card.getValue(card);
            if (cardValues.size() == 2) {
                if (countAce.equals(0)) {
                    countAce += 1;
                    sum1 += 1;
                    sum2 += 11;
                } else if (countAce.equals(1)) {
                    countAce += 1;
                    sum1 += 1;
                    sum2 += 1;
                    sum3 += 22;                    
                } else if (countAce.equals(2)) {
                    countAce += 1;
                    sum1 += 1;
                    sum2 += 1;
                    sum3 += 1;
                    sum4 += 33;
                } else if (countAce.equals(3)) {
                    countAce += 1;
                    sum1 += 1;
                    sum2 += 1;
                    sum3 += 1;
                    sum4 += 1;
                    sum5 += 44;
                }
            } else {
                for (Integer value : cardValues) {
                    sum1 += value;
                    sum2 += value;
                    sum3 += value;
                    sum4 += value;
                    sum5 += value;
                }
            }
        }
        if (countAce == 4) {
            currentValues.add(sum1);
            currentValues.add(sum2);
            currentValues.add(sum3);
            currentValues.add(sum4);
            currentValues.add(sum5);
        } else if (countAce == 3) {
            currentValues.add(sum1);
            currentValues.add(sum2);
            currentValues.add(sum3);
            currentValues.add(sum4);
        } else if (countAce == 2) {
            currentValues.add(sum1);
            currentValues.add(sum2);
            currentValues.add(sum3);
        } else if (countAce == 1) {
            currentValues.add(sum1);
            currentValues.add(sum2);
        } else {
            currentValues.add(sum1);
        }
    }
    
}
