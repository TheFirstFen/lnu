package com.blackjack;

import java.util.Scanner;


public class Main {
    public static Boolean exitprogram = false;

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in); // Intialize scanner
        playerTurn player = new playerTurn();
        bankirTurn bankir = new bankirTurn();

        while (true) {
            RoundUpdates.updateGame (player, bankir);
            if (checkPlayerBlackJack(player) && RoundUpdates.getRound() == 0) {
                System.out.println("BLACKJACK!!!");
                ((playerTurn) player).playerBlackjack = true;
                bankir.bankirLoop(player, bankir);
            } else {
                Menu.startMenu(scanner, player, bankir);
            }
            if (exitprogram) {
                System.out.println("Exiting the program...");
                break;
            }
        }
        scanner.close();
    }

    private static boolean checkPlayerBlackJack(playerTurn player){
        if (((playerTurn) player).checkIfBlackjack()) {
            return true;
        }
        return false;
    }
}
