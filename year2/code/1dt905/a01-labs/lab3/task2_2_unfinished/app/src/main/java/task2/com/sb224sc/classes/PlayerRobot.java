package task2.com.sb224sc.classes;

import task2.com.sb224sc.interfaces.TileInterface;

public class PlayerRobot extends Robot {
    private GamePlan gamePlan;

    public PlayerRobot(int posX, int posY, int energy, int strength, GamePlan gamePlan) {
        super(posX, posY, energy, strength);
        this.gamePlan = gamePlan;
    }

    @Override
    public void move(int x, int y) {
        if (isGameOver()) {
            System.out.println("Game Over. You cannot move.");
            return;
        }

        int distance = Math.abs(x - getPosX()) + Math.abs(y - getPosY());

        if (distance == 0) {
            System.out.println("Current tile. Interperated as Pause");
            pause();
            return;
        }

        if (getEnergy() >= distance) {
            setEnergy(getEnergy() - distance);

            TileInterface targetTile = gamePlan.getTile(x, y);
            if (targetTile != null && targetTile.isAccessible()) {
                gamePlan.placeRobot(x, y);
                gamePlan.placeEmptyTile(getPosX(), getPosY());
                setPosX(x);
                setPosY(y);

                if (targetTile instanceof HomeTile) {
                    System.out.println("You reached home! You survived this round.");
                    gamePlan.print();
                    gamePlan.reset();
                } else {
                    if (targetTile instanceof StrawberryTile) {
                        eatStrawberry();
                        System.out.println("You ate a strawberry and gained 10 energy.");
                    }

                    if (targetTile instanceof WolfTile) {
                        encounterWolf();
                        if (isGameOver()) {
                            System.out.println("The wolf caught you! Game over.");
                            gamePlan.print();
                            gamePlan.reset();
                        }
                    } else {
                        gamePlan.print();
                    }
                }
            } else {
                System.out.println("The target tile is not accessible.");
            }
        } else {
            System.out.println("Not enough energy to make this move.");
        }
    }

    @Override
    public void pause() {
        if (isGameOver()) {
            System.out.println("Game over. You cannot pause.");
            return;
        }

        setEnergy(getEnergy() + 1);
        System.out.println("You paused and gained 1 energy.");
        gamePlan.print();
    }

    @Override
    public void eatStrawberry() {
        setEnergy(getEnergy() + 10);
    }

    @Override
    public void reachHome() {
        // * Handled in move()
    }

    @Override
    public void encounterWolf() {
        setEnergy(0); // * energy = 0 = Game Over!
    }

    public boolean isAtHome() {
        TileInterface curTile = gamePlan.getTile(getPosX(), getPosY());
        return curTile instanceof HomeTile;
    }

    public boolean isGameOver() {
        return getEnergy() <= 0;
    }

    public void printStats() {
        System.out.println("Position: (" + getPosX() + ", " + getPosY() + ")");
        System.out.println("Energy: " + getEnergy());
        System.out.println("Strength: " + getStrength());
    }
}
