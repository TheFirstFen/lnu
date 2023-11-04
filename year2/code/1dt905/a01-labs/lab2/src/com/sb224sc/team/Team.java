package com.sb224sc.team;

import com.sb224sc.people.*;

import java.util.List;
import java.util.ArrayList;

public class Team {
    private List<Person> members = new ArrayList<>();

    public void addMember(Person newMember) {
        members.add(newMember);
    }

    public void clearMembers() {
        members.clear();
    }

    public List<Person> getMembers() {
        return members;
    }
}
