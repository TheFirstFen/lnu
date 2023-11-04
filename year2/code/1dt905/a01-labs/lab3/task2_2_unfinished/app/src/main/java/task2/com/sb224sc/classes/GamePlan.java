package task2.com.sb224sc.classes;

import java.util.Random;

import task2.com.sb224sc.interfaces.*;

// TODO: Add checking if Tile to place is empty before placing

public class GamePlan {
    private TileInterface[][] tiles;
    private int sizeX;
    private int sizeY;

    public GamePlan(int sizeX, int sizeY) {
        this.sizeX = sizeX;
        this.sizeY = sizeY;
        tiles = new TileInterface[sizeX][sizeY];

        for (int x = 0; x < sizeX; x++) {
            for (int y = 0; y < sizeY; y++) {
                tiles[x][y] = new EmptyTile();
            }
        }
    }

    public void placeEmptyTile(int x, int y) {
        tiles[x][y] = new EmptyTile();
    }

    public void reset() {
        for (int x = 0; x < sizeX; x++) {
            for (int y = 0; y < sizeY; y++) {
                tiles[x][y] = new EmptyTile();
            }
        }
    }

    public TileInterface getTile(int x, int y) {
        if (x >= 0 && x < sizeX && y >= 0 && y < sizeY) {
            return tiles[x][y];
        } else {
            return null;
        }
    }

    public int getSizeX() {
        return sizeX;
    }

    public int getSizeY() {
        return sizeY;
    }

    public void placeStrawberry(int x, int y) {
        tiles[x][y] = new StrawberryTile();
    }

    public void placeRandomStrawberries(int amount) {
        Random rnd = new Random();
        for (int i = 0; i < amount; i++) {
            int x = rnd.nextInt(sizeX);
            int y = rnd.nextInt(sizeY);
            placeStrawberry(x, y);
        }
    }

    public void placeHome(int x, int y) {
        tiles[x][y] = new HomeTile();
    }

    public void placeRobot(int x, int y) {
        tiles[x][y] = new PlayerRobotTile();
    }

    public void placeWolf(int x, int y) {
        tiles[x][y] = new WolfTile();
    }

    public void placeRandomWolf(int x, int y, Wolf wolf, PlayerRobot robot) {
        Random rnd = new Random();
        TileInterface curTile = getTile(x, y);

        while (curTile instanceof PlayerRobotTile) {
            x = rnd.nextInt(sizeX);
            y = rnd.nextInt(sizeY);
            curTile = getTile(x, y);
        }
        placeWolf(x, y);
        wolf.setPosX(x);
        wolf.setPosY(y);
    }

    public void print() {

        for (int y = 0; y < sizeY; y++) {
            for (int x = 0; x < sizeX; x++) {
                System.out.print(tiles[x][y].getSymbol() + " ");
            }
            System.out.println();
        }
    }
}
