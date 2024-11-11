package task3.com.task3.helpers;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;


public class Deck {
    private static String[] ranks = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"};
    private static String[] suits = {"Hearts", "Diamonds", "Clubs", "Spades"};
    public static List<String> deck = new ArrayList<>();

    public static void createDeck() {

        for (String suit : suits) {
            for (String rank : ranks) {
                Card card = new Card();
                card.addRank(rank);
                card.addSuit(suit);
                deck.add(card.getCard());
            }
        } 
        
    }
    public static void shuffleDeck() {
        Collections.shuffle(deck);
    }

    public static void printDeck() {
        for (String card : deck) {
            System.out.println(card);
        }
    }

    public static String getFirst() {
        return deck.get(0);
    }
    public static String getLast() {
        Integer amountOfCards = deck.size();
        return deck.get(amountOfCards - 1);
    }
    public static String removeAndShow() {
        Random random = new Random();
        int randomNumber = random.nextInt(deck.size()) + 1;
        String tempCard = deck.get(randomNumber);
        deck.remove(randomNumber);
        return tempCard;
    }
    public static List<String> givePokerHand() {
    List<String> pokerHand = new ArrayList<>();
    Random randoms = new Random();
    for (int i = 0; i < 5; i++) {
        int randomNumber = randoms.nextInt(deck.size());
        pokerHand.add(deck.get(randomNumber));
        deck.remove(randomNumber);
    }
    return pokerHand;
    }

    public static List<Integer> twoCardDeal() {
    List<Integer> handValue = new ArrayList<>();
    Integer sum1 = 0;
    Integer sum2 = 0;
    Integer sum3 = 0;
    Integer countAce = 0;
    Random random = new Random();
    System.out.println("-----------------------------------------------");
    System.out.println("Your cards are: ");
    for (int i = 0; i < 2; i++) {
        Integer card = 0;
        int randomNumber = random.nextInt(deck.size());
        List<Integer> values = Card.getValue(deck.get(randomNumber));
        System.out.println(deck.get(randomNumber));
        if (values.size() == 2) {
            countAce += 1;
            sum1 += 14;
            sum2 += 1;
            sum3 = 15;
        } else {
            for (Integer value : values) {
                card = value;
                sum1 += card;
                sum2 += card;
            }
        }
        deck.remove(randomNumber);
    }
    if (countAce == 2) {
        handValue.add(sum1);
        handValue.add(sum2);
        handValue.add(sum3);
        return handValue;
    } else if (countAce == 1) {
        handValue.add(sum1);
        handValue.add(sum2);
        return handValue;
    } else {
        handValue.add(sum1);
        return handValue;
    }
    }
}

