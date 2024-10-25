package task2;

import java.util.Scanner;

import task2.com.sb224sc.classes.*;

// import com.google.gson.Gson;
// import com.google.gson.GsonBuilder;

public class App {
    public static void main(String[] args) {
        GamePlan gamePlan = new GamePlan(10, 10);
        PlayerRobot robot = new PlayerRobot(0, 0, 10, 2, gamePlan);
        Wolf wolf = new Wolf(0, 0, gamePlan);
        gamePlan.placeRandomStrawberries(3);
        gamePlan.placeHome(9, 9);
        gamePlan.placeRobot(robot.getPosX(), robot.getPosY());
        gamePlan.placeRandomWolf(wolf.getPosX(), wolf.getPosY(), wolf, robot);

        Scanner sc = new Scanner(System.in);
        boolean gameOver = false;

        while (!gameOver) {
            gamePlan.print();
            robot.printStats();

            System.out.println("Choose an action: \n1 Move\n2 Pause");
            try {
                String choice = sc.nextLine(); // ! Exception "java.util.NoSuchElementException: No line found"

                if (choice.equals("1")) {
                    System.out.println("Enter X and Y coordinates to move:");
                    int x = sc.nextInt();
                    sc.nextLine();
                    int y = sc.nextInt();
                    sc.nextLine();
                    robot.move(x, y);

                    if (robot.isAtHome()) {
                        System.out.println("You reached home! You survived this round.");
                        gameOver = true;
                    }

                    if (robot.getPosX() == wolf.getPosX() && robot.getPosY() == wolf.getPosY()) {
                        robot.encounterWolf();
                        if (robot.isGameOver()) {
                            System.out.println("The wolf caught you! Game over.");
                            gameOver = true;
                        }
                    }
                } else if (choice.equals("2")) {
                    robot.pause();
                } else {
                    System.out.println("Invalid choice. Please choose 1 or 2.");
                }
            } catch (Exception e) {
                System.out.println(e);
                break;
            }

            sc.close();

            // Gson gson = new GsonBuilder().setPrettyPrinting().create();
            // String gamePlanJSON = gson.toJson(gamePlan);
            // String robotJson = gson.toJson(robot);
            // System.out.println("Game Plan JSON:");
            // System.out.println(gamePlanJSON);
            // System.out.println("Robot JSON:");
            // System.out.println(robotJson);
        }
    }
}
