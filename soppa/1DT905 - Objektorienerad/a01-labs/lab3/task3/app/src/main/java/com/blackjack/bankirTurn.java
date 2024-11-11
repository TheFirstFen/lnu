package com.blackjack;


public class bankirTurn extends Turn {
    public static Boolean bust = false;
    public static Boolean timeToStop = false;
    public Boolean bankirBlackJack = false;


    public void bankirLoop(playerTurn player, bankirTurn bankir) {
        addFirstCardToHand();
        if (checkIfBlackjack()) {
            bankirBlackJack = true;
        }
        while (bust.equals(false) || timeToStop.equals(false)) {
            if (checkIfBlackjack()) {
                break;
            } else if (getMinValue() > 21) {
                bust = true;
                break;
            }
            checkIfStop();
            if (timeToStop) {
                break;
            }
            addFirstCardToHand();
        }
        CheckWinner.checkWinner(player, bankir);

    }

    public void checkIfStop() {
        if (getMinValue() >= 17) {
            timeToStop = true;
        }
    }


}
