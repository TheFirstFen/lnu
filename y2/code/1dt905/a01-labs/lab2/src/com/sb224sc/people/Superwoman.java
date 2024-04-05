package com.sb224sc.people;

import java.util.Scanner;

public class Superwoman extends Person {
    private String SuperStrength = "True";

    public String hasSuperStrength() {
        return SuperStrength;
    }

    @Override
    public String toString() {
        return "Superwoman: " + getName() + ", born " + getBirthYear() +
                " (turning " + getAge() + " this year), md5: " + getId() +
                ", Has super strength: " + hasSuperStrength();
    }

    public Superwoman memberCreation(Superwoman superwoman, Scanner sc) {
        try {
            System.out.print("Firstname: ");
            superwoman.setFirstName(sc.nextLine());
            System.out.print("Lastname: ");
            superwoman.setLastName(sc.nextLine());
            System.out.print("Birthyear: ");
            superwoman.setBirthYear(sc.nextInt());

            sc.nextLine();
            
            return superwoman;
        } catch (Exception e) {
            return null;
        }
    }
}
