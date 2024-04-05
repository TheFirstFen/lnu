package task3;

import task3.com.sb224sc.classes.*;

public class App {
    /**
     * The main method is the entry point of the Java program.
     *
     * @param args the command line arguments passed to the program.
     */
    public static void main(String[] args) {
        Deck deck = new Deck();
        DrawCard drawCard = new DrawCard(deck);

        Player player = new Player(drawCard);
        Dealer dealer = new Dealer();

        BlackJackGame game = new BlackJackGame(player, dealer, deck);
        game.play();
    }
}
