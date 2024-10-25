package task2.com.sb224sc.classes;

import task2.com.sb224sc.interfaces.*;

public class WolfTile implements TileInterface {
    @Override
    public String getSymbol() {
        return new String(new int[] { 0x1F43A }, 0, 1);
    }

    @Override
    public boolean isAccessible() {
        return true;
    }

    @Override
    public void onRobotEnter(Robot robot) {
        System.out.println("Wolf Tile.");
        robot.encounterWolf();
    }
}
