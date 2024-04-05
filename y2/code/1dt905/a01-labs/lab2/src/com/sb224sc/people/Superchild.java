package com.sb224sc.people;

import java.util.Scanner;

public class Superchild extends Superman {
    private String specialPower = "Heat Vision & Super Hearing";

    public String getSpecialPower() {
        return specialPower;
    }

    @Override
    public String toString() {
        return "SuperChild: " + getName() + ", born " + getBirthYear() +
                " (turning " + getAge() + " this year), md5: " + getId() +
                ", Can fly: " + getAbilityToFly() + ", Special Power: " + getSpecialPower();
    }

    public Superchild memberCreation(Superchild superchild, Scanner sc) {
        try {
            System.out.print("Firstname: ");
            superchild.setFirstName(sc.nextLine());
            System.out.print("Lastname: ");
            superchild.setLastName(sc.nextLine());
            System.out.print("Birthyear: ");
            superchild.setBirthYear(sc.nextInt());

            sc.nextLine();

            return superchild;
        } catch (Exception e) {
            return null;
        }
    }
}
