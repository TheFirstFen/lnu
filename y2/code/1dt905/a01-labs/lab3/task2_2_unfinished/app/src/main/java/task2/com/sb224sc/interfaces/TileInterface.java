package task2.com.sb224sc.interfaces;

import task2.com.sb224sc.classes.Robot;

public interface TileInterface {
    String getSymbol();

    boolean isAccessible();

    void onRobotEnter(Robot robot);
}
