package task2.com.sb224sc.classes;

import task2.com.sb224sc.interfaces.*;

public class HomeTile implements TileInterface {

    @Override
    public String getSymbol() {
        return new String(new int[] { 0x1F3DB }, 0, 1);
    }

    @Override
    public boolean isAccessible() {
        return true;
    }

    @Override
    public void onRobotEnter(Robot robot) {
        robot.reachHome();
        System.out.println("Home Tile.");
    }
}
