package task2.com.sb224sc.classes;

import task2.com.sb224sc.interfaces.*;

public class PlayerRobotTile implements TileInterface {

    @Override
    public String getSymbol() {
        return new String(new int[] { 0x1F916 }, 0, 1);
    }

    @Override
    public boolean isAccessible() {
        return true;
    }

    @Override
    public void onRobotEnter(Robot robot) {
        System.out.println("Should not be possible except for wolf.");
    }
}
