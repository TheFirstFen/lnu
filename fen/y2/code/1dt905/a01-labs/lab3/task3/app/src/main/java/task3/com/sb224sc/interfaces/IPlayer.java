package task3.com.sb224sc.interfaces;

import java.util.Scanner;

import task3.com.sb224sc.classes.*;

public interface IPlayer {
    void receiveCard(Card card);

    int getScore();

    boolean wantsToDrawCard(Scanner sc);

    void reset();
}
