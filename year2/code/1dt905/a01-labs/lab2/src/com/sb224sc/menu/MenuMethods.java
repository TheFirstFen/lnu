package com.sb224sc.menu;

import com.sb224sc.people.*;
import com.sb224sc.team.*;

import java.util.List;
import java.util.Scanner;

public class MenuMethods {
    public void predefinedAdd(Team team) {
        Person p1 = new Person();
        Superman p2 = new Superman();
        Superwoman p3 = new Superwoman();
        Superchild p4 = new Superchild();
        Person p5 = new Person();

        p1.setAllDetails("Clark", "Kent", 2000);
        p2.setAllDetails("Kal EL", "Kent", 1985);
        p3.setAllDetails("Lois", "Kent", 1990);
        p4.setAllDetails("Jon", "Kent", 2015);
        p5.setAllDetails("Lois", "Lane", 1990);

        team.addMember(p1);
        team.addMember(p2);
        team.addMember(p3);
        team.addMember(p4);
        team.addMember(p5);

        System.out.println("Five predefined members were added to the team.");
    }

    public void printTeamMembers(Team team) {
        List<Person> teamMembers = team.getMembers();
        if (teamMembers.isEmpty()) {
            System.out.println("There are currently no team members.");
        } else {
            System.out.println("Team members:");
            for (Person member : teamMembers) {
                if (member != null) {
                    System.out.println(member.toString());
                } else {
                    System.out.println("Null");
                }
            }
        }
    }

    public void createPersonlizedMember(Team team, Scanner sc) {
        System.out.println("Type of member:");
        System.out.println("1) Person");
        System.out.println("2) Superman");
        System.out.println("3) Superwoman");
        System.out.println("4) Superchild");

        try {
            System.out.print("Your choice > ");
            String choice = sc.nextLine();

            switch (choice) {
                case "1":
                    Person person = new Person();
                    
                    person.memberCreation(person, sc);

                    team.addMember(person);
                    break;
                
                case "2":
                    Superman superman = new Superman();
                    
                    superman.memberCreation(superman, sc);

                    team.addMember(superman);
                    break;
                
                case "3":
                    Superwoman superwoman = new Superwoman();
                    
                    superwoman.memberCreation(superwoman, sc);

                    team.addMember(superwoman);
                    break;

                case "4":
                    Superchild superchild = new Superchild();
                    
                    superchild.memberCreation(superchild, sc);

                    team.addMember(superchild);
                    break;

                default:
                    System.out.println("Invalid input. Returning to menu.");
                    break;
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
