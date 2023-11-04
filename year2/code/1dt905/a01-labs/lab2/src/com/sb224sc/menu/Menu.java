package com.sb224sc.menu;

import com.sb224sc.team.*;

import java.util.Scanner;

public class Menu {
    MenuMethods menuMethods = new MenuMethods();

    public void menuLoop() {
        Team team = new Team();
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\nMenu: ");
            System.out.println("1) Add 5 pre-defined persons (all Person types should be added) to the team");
            System.out.println("2) Print the team and its members");
            System.out.println("3) Remove all from the team");
            System.out.println("4) Create a new Person/Superman/Superwoman/Superchild and add to the team");
            System.out.println("\nqQ) Exit.");

            System.out.print("\nYour choice: ");

            if (sc.hasNextLine()) {
                String input = sc.nextLine();

                try {
                    if (input.equals("q") || input.equals("Q")) {
                        System.out.println("Exiting...");
                        sc.close();
                        System.exit(0);
                    } else if (Integer.parseInt(input) == 1) {
                        menuMethods.predefinedAdd(team);
                    } else if (Integer.parseInt(input) == 2) {
                        menuMethods.printTeamMembers(team);
                    } else if (Integer.parseInt(input) == 3) {
                        team.clearMembers();
                        System.out.println("Team cleared of members.");
                    } else if (Integer.parseInt(input) == 4) {
                        menuMethods.createPersonlizedMember(team, sc);
                    } else {
                        System.out.println("Please input an appropriate value.");
                    }
                } catch (Exception e) {
                    System.out.println(e);
                }
            } else {
                break;
            }
            
        }
    }
}
