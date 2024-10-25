package www.example;


public class Superchild extends Superman {
    private String superSpeed = "true";

    public Superchild(String firstName, String lastName, int birthYear) {
        super(firstName, lastName, birthYear);
    }

    public String getSuperSpeed() {
        return superSpeed;
    }

    @Override
    public String toString(){
        return "superchild " + super.toString() + ", has super speed: " + superSpeed;
    }
}
