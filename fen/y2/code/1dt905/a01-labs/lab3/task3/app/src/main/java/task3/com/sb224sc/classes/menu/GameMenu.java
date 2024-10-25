package task3.com.sb224sc.classes.menu;

import task3.com.sb224sc.classes.*;

public class GameMenu {
    /**
     * Prints the dealer's face-up card and known hand value, as well as the
     * player's cards and score.
     *
     * @param player the player object representing the current player.
     * @param dealer the dealer object representing the game dealer.
     */
    public static void gameBoardPlayerTurn(Player player, Dealer dealer) {
        System.out.println("\nDealer's face-up card: " + dealer.getDealerFaceUpCard());
        System.out.println("Dealer's known hand value: " + dealer.getDealerFaceUpCardValue());

        System.out.print("\nPlayer's cards: ");
        for (Card card : player.getHand()) {
            System.out.print(card + ", ");
        }
        System.out.println("\nPlayer's score: " + player.getScore());
    }

    /**
     * Deals the cards for the dealer's turn in the game board.
     *
     * @param player          the player object.
     * @param dealer          the dealer object.
     * @param printDealerHand true if the dealer's hand should be printed, false
     *                        otherwise.
     */
    public static void gameBoardDealerTurn(Player player, Dealer dealer, boolean printDealerHand) {
        if (printDealerHand) {
            System.out.print("\nDealer's cards: ");
            for (Card card : dealer.getHand()) {
                System.out.print(card + ", ");
            }
            System.out.println("\nDealer's score: " + dealer.getScore());
        }

        System.out.print("\nPlayer's cards: ");
        for (Card card : player.getHand()) {
            System.out.print(card + ", ");
        }
        System.out.println("\nPlayer's score: " + player.getScore());
    }

    /**
     * Draws a line to indicate turn over.
     *
     */
    public static void turnEnd() {
        System.out.println("\n" + "-----------------------------------------------");
    }
}