package task3.com.sb224sc.classes;

import java.util.Scanner;

import task3.com.sb224sc.classes.menu.GameMenu;

public class BlackJackGame {
    private Player player;
    private Dealer dealer;
    private Deck deck;
    Scanner sc = new Scanner(System.in);

    public BlackJackGame(Player player, Dealer dealer, Deck deck) {
        this.player = player;
        this.dealer = dealer;
        this.deck = deck;
    }

    /**
     * Plays a game of blackjack.
     */
    public void play() {
        boolean quit = false;

        shuffleDeck(deck);

        while (!quit) {
            player.receiveCard(deck.drawCard());
            dealer.receiveCard(deck.drawCard());
            player.receiveCard(deck.drawCard());
            dealer.receiveCard(deck.drawCard());

            while (player.getScore() < 21) {
                GameMenu.gameBoardPlayerTurn(player, dealer);
                if (player.wantsToDrawCard(sc)) {
                    player.receiveCard(deck.drawCard());
                } else {
                    break;
                }
                GameMenu.turnEnd();
            }

            while (dealer.wantsToDrawCard(sc) && dealer.getScore() < 17) {
                GameMenu.gameBoardDealerTurn(player, dealer, true);
                dealer.receiveCard(deck.drawCard());
                GameMenu.turnEnd();
            }

            endOfTurn(quit);
        }
    }

    private void endOfTurn(boolean quit) {
        printHandsAndValues();
        determineWinner();
        checkDeckSize();
        GameMenu.turnEnd();

        if (oneMoreHand(sc)) {
            player.clearHand();
            dealer.clearHand();
        } else {
            quit = true;
            System.out.println("Thanks for playing!");
            System.exit(0);
        }
    }

    private boolean oneMoreHand(Scanner sc) {
        System.out.println("Wanna play one more hand? (y/n)");
        if (sc.nextLine().equals("y")) {
            return true;
        } else {
            return false;
        }
    }

    /**
     * Prints the dealer's and player's hands and scores.
     */
    private void printHandsAndValues() {
        System.out.print("\nDealer's cards: ");
        for (Card card : dealer.getHand()) {
            System.out.print(card + ", ");
        }
        System.out.println("\nDealer's score: " + dealer.getScore());

        System.out.print("\nPlayer's cards: ");
        for (Card card : player.getHand()) {
            System.out.print(card + ", ");
        }
        System.out.println("\nPlayer's score: " + player.getScore());
    }

    /**
     * Determines the winner of the game based on the player's and dealer's scores.
     *
     */
    private void determineWinner() {
        int playerScore = player.getScore();
        int dealerScore = dealer.getScore();

        if (playerScore == dealerScore) {
            System.out.println("\nIt's a tie!");
        } else if (playerScore > 21 && dealerScore <= 21 || (dealerScore <= 21 && dealerScore > playerScore)) {
            System.out.println("\nDealer wins!");
            gotBlackJack(playerScore, dealerScore);
        } else if (dealerScore > 21 || playerScore > dealerScore) {
            System.out.println("\nPlayer wins!");
            gotBlackJack(playerScore, dealerScore);
        }
    }

    /**
     * A function that is called when a player or dealer gets a blackjack.
     *
     * @param playerScore the score of the player.
     * @param dealerScore the score of the dealer.
     */
    private void gotBlackJack(int playerScore, int dealerScore) {
        if (playerScore == 21 || dealerScore == 21) {
            String message = " Blackjack! ";
            int messageLength = message.length();

            StringBuilder topBorder = new StringBuilder("+");
            for (int i = 0; i < messageLength + 2; i++) {
                topBorder.append("-");
            }
            topBorder.append("+");

            String middleLine = "| " + message + " |";

            System.out.println("\n" + topBorder);
            System.out.println(middleLine);
            System.out.println(topBorder);
        }
    }

    private void shuffleDeck(Deck deck) {
        for (int i = 0; i < 5; i++) {
            deck.shuffle();
        }
    }

    /**
     * Checks the size of the deck and replaces it with a new one if necessary.
     */
    private void checkDeckSize() {
        if (deck.getRemainingAmountOfCards() < 52 / 2) {
            System.out.println("Replacing the deck with a new one and shuffling it.");
            deck = new Deck();
            shuffleDeck(deck);
        }
    }
}
