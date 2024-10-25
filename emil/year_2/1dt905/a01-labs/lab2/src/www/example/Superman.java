package www.example;

public class Superman extends Person {
    private String superStrength = "true";

    public Superman(String firstName, String lastName, int birthYear){
        setPersonDetails(firstName, lastName, birthYear);
    }

    public String superStrength(){
        return superStrength;
    }


    @Override
    public String toString(){
        return "Superman " + super.toString() + " has super strength: " + superStrength;
    }
}
