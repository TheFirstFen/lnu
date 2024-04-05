package task2.com.sb224sc.classes;

import task2.com.sb224sc.interfaces.*;

public class EmptyTile implements TileInterface {

    @Override
    public String getSymbol() {
        // TODO: Fix gamePlan size so it is not uneven
        // return new String(new int[] { 0x25A1 }, 0, 1);
        return ".";
    }

    @Override
    public boolean isAccessible() {
        return true;
    }

    @Override
    public void onRobotEnter(Robot robot) {
        System.out.println("Tile is empty.");
    }
}
