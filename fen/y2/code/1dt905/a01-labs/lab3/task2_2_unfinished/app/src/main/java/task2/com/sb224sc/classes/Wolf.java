package task2.com.sb224sc.classes;

public class Wolf extends Robot {
    private GamePlan gamePlan;

    public Wolf(int posX, int posY, GamePlan gamePlan) {
        super(posX, posY, 0, 0);
        this.gamePlan = gamePlan;
    }

    @Override
    public void move(int x, int y) {

    }

    @Override
    public void pause() {

    }

    @Override
    public void eatStrawberry() {
        pause(); // * Pause for one full turn.
    }

    @Override
    public void reachHome() {

    }

    @Override
    public void encounterWolf() {
        // * Not possible
    }
}
