public interface GameInterface {
    public static final int MAX_GUESSES = 6;

    public void init();

    public void reset();

    public boolean guess(int guess);

    public int cheat();

    public void run();
}
