package task2.com.task2.team;

import task1_2.com.task1_2.person.Person;

import java.util.ArrayList;
import java.util.List;

public class Team {
    private static List<Person> members = new ArrayList<>();

    public static void addPerson(Person person) {
        members.add(person);
    }

    public static void removeTeam() {
        members = new ArrayList<>();
    }

    public static List<Person> getMembers() {
        return members;
    }




}
