package task2.com.sb224sc.classes;

import task2.com.sb224sc.interfaces.TileInterface;

public class StrawberryTile implements TileInterface {

    @Override
    public String getSymbol() {
        return new String(new int[] { 0x1F353 }, 0, 1);
    }

    @Override
    public boolean isAccessible() {
        return true;
    }

    @Override
    public void onRobotEnter(Robot robot) {
        robot.eatStrawberry();
        System.out.println("Strawberry Tile.");
    }

}
