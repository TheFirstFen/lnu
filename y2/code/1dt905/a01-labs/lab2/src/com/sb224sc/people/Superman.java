package com.sb224sc.people;

import java.util.Scanner;

public class Superman extends Person{
    private String canFly = "True";

    public String getAbilityToFly() {
        return canFly;
    }

    @Override
    public String toString() {
        return "Superman: " + getName() + ", born " + getBirthYear() +
                " (turning " + getAge() + " this year), md5: " + getId() +
                ", Can fly: " + getAbilityToFly();
    }

    public Superman memberCreation(Superman superman, Scanner sc) {
        try {
            System.out.print("Firstname: ");
            superman.setFirstName(sc.nextLine());
            System.out.print("Lastname: ");
            superman.setLastName(sc.nextLine());
            System.out.print("Birthyear: ");
            superman.setBirthYear(sc.nextInt());

            sc.nextLine();

            return superman;
        } catch (Exception e) {
            return null;
        }

        
    }
}
