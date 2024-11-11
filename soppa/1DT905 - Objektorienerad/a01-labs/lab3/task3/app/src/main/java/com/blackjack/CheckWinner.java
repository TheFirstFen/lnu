package com.blackjack;

public class CheckWinner {

    public static void checkWinner(playerTurn player, bankirTurn bankir) {
        RoundUpdates.updateGame(player, bankir);
        if (player.playerBlackjack && bankir.bankirBlackJack) {
            System.out.println("Double BLACKJACK!! Its a tie!");
        } else if (player.playerBlackjack) {
            System.out.println("Congratulations you have won by blackjack!");
        } else if (bankir.bankirBlackJack) {
            System.out.println("Oh no you lost! The bankir got a blackjack");
        } else if (bankirTurn.bust) {
            System.out.println("Congratulations you have won!! The bankir busted");
        } else if (bankirTurn.timeToStop) {
            if (((bankirTurn) bankir).getBestValue() < ((playerTurn) player).getBestValue()) {
                System.out.println("Congratulations you have won!");
            } else if (((bankirTurn) bankir).getBestValue() > ((playerTurn) player).getBestValue()) {
                System.out.println("Oh no you lost!");
            } else {
                System.out.println("Its a tie!");
            }
        }
        Main.exitprogram = true;

    }
}
