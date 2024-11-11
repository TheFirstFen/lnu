package com.blackjack;


public class playerTurn extends Turn {
    public Boolean playerBlackjack = false;


    public boolean checkIfTwentyOne() {
        Boolean TwentyOne = false;
        for (Integer value : getValues()) {
            if (value.equals(21)) {
                TwentyOne = true;
            } else {
                TwentyOne = false;
            }
        }
        return TwentyOne;
    }

    public void checkIfBust(playerTurn player, bankirTurn bankir){
        if (getMinValue() > 21) {
            RoundUpdates.updateGame(player, bankir);
            System.out.println("Oh no its a bust you lose!");
            Main.exitprogram = true;
        }
    }



}
