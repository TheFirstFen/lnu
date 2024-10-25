package www.example;

import java.util.ArrayList;
import java.util.List;

public class Team {
    private List<Person> members;

    public Team() {
        members = new ArrayList<>();
    }

    public void addPerson(Person person) {
        members.add(person);
    }

    public void removePersons() {
        members.clear();
    }

    public List<Person> getMembers() {
        return members;
    }
    
}
