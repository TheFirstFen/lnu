package task2.com.sb224sc.classes;

public abstract class Robot {
    private int posX;
    private int posY;
    private int energy;
    private int strength;

    public Robot(int posX, int posY, int energy, int strength) {
        this.posX = posX;
        this.posY = posY;
        this.energy = energy;
        this.strength = strength;
    }

    public abstract void move(int x, int y);

    public abstract void pause();

    public abstract void eatStrawberry();

    public abstract void reachHome();

    public abstract void encounterWolf();

    public int getPosX() {
        return posX;
    }

    public void setPosX(int posX) {
        this.posX = posX;
    }

    public int getPosY() {
        return posY;
    }

    public void setPosY(int posY) {
        this.posY = posY;
    }

    public int getEnergy() {
        return energy;
    }

    public void setEnergy(int energy) {
        this.energy = energy;
    }

    public int getStrength() {
        return strength;
    }

    public void setStrength(int strength) {
        this.strength = strength;
    }
}
