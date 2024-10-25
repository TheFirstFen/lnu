package www.example;

public class Superwoman extends Person {
    private String canFly = "true";

    public Superwoman(String firstName, String lastName, int birthYear){
        setPersonDetails(firstName, lastName, birthYear);
    }

    public String canFly(){
        return canFly;
    }


    @Override
    public String toString(){
        return "Superwoman " + super.toString() + " can fly: " + canFly;
    }
}

