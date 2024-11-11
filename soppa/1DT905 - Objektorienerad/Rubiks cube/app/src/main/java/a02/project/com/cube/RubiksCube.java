package a02.project.com.cube;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class RubiksCube {
    public static void main(String[] args, Scanner scanner) {
        List<String> savedMoves = new ArrayList<>();

        String[][][] colorMatrix = new String[6][3][3];


        String square = "\u25A0";

        String W = "\033[97m" + square + "\033[0m";
        String G = "\033[92m" + square + "\033[0m";
        String R = "\033[31m" + square + "\033[0m";
        String B = "\033[94m" + square + "\033[0m";
        String Y = "\033[93m" + square + "\033[0m";
        String O = "\033[95m" + square + "\033[0m";
        


        String[] colorLetters = { W, G, R, B, Y, O }; 

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    colorMatrix[i][j][k] = String.valueOf(colorLetters[i]);
                }
            }
        }
        print2DCube(colorMatrix);
        while(true){
            System.out.println("What would you like to do?");

            String choice = scanner.nextLine();

            if (choice.equals("X")){
                rotateCubeToRight(colorMatrix);
                savedMoves.add(choice);
            }
            else if (choice.equals("x")){
                rotateCubeToLeft(colorMatrix);
                savedMoves.add(choice);
            }
            else if (choice.equals("Y")){
                rotateCubeFrontfaceUp(colorMatrix);
                savedMoves.add(choice);
            }
            else if (choice.equals("y")){
                rotateCubeFrontfaceDown(colorMatrix);
                savedMoves.add(choice);
            }
            else if (choice.equals("F")){
                rotateCubefaceClockwise(colorMatrix);
                savedMoves.add(choice);
                printIfCubeIsSolved(colorMatrix);
            }
            else if (choice.equals("f")){
                rotateCubefaceCounterClockwise(colorMatrix);
                savedMoves.add(choice);
                printIfCubeIsSolved(colorMatrix);
            }
            else if (choice.equals("R")){
                rotateRightSideClockwise(colorMatrix);
                savedMoves.add(choice);
                printIfCubeIsSolved(colorMatrix);
            }
            else if (choice.equals("r")){
                rotaterightSideCounterClockwise(colorMatrix);
                savedMoves.add(choice);
                printIfCubeIsSolved(colorMatrix);
            }
            else if (choice.equals("L")){
                rotateLeftSideDown(colorMatrix);
                savedMoves.add(choice);
                printIfCubeIsSolved(colorMatrix);
            }
            else if (choice.equals("l")){
                rotateLeftSideUp(colorMatrix);
                savedMoves.add(choice);
                printIfCubeIsSolved(colorMatrix);
            }
            else if (choice.equals("U")){
                rotateTopClockwise(colorMatrix);
                savedMoves.add(choice);
                printIfCubeIsSolved(colorMatrix);
            }
            else if (choice.equals("u")){
                rotateTopCounterClockwise(colorMatrix);
                savedMoves.add(choice);
                printIfCubeIsSolved(colorMatrix);
            }
            else if (choice.equals("D")){
                rotateBottomClockwise(colorMatrix);
                savedMoves.add(choice);
                printIfCubeIsSolved(colorMatrix);
            }
            else if (choice.equals("d")){
                rotateBottomCounterClockwise(colorMatrix);
                savedMoves.add(choice);
                printIfCubeIsSolved(colorMatrix);
            }
            else if (choice.equals("p3")){
                print3DCube(colorMatrix);
            }
            else if (choice.equals("q")||choice.equals("Q")){
                break;
            }
            else if (choice.equals("show")){
                for(String input : savedMoves){
                    System.out.println(input);
                }
            }
            else if (choice.equals("Solve")){
                solveCube(savedMoves, colorMatrix);
                savedMoves.clear();
            }
            else if (choice.equals("sc")){
                scrambleCube(colorMatrix, savedMoves);
            }
            else {
                System.out.println("Invalid input");
            }
            print2DCube(colorMatrix);
        }
    }

    private static void print2DCube(String[][][] cube) {
        for (int i = 0; i < 3; i++) {
            System.out.print("       ");
            for (int j = 0; j < 3; j++) {
                System.out.print(cube[0][i][j] + " ");
            }
            System.out.println();
        }
        
        // Print the left, front, right, and back faces
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(cube[1][i][j] + " ");
            }
            System.out.print(" ");
            for (int j = 0; j < 3; j++) {
                System.out.print(cube[2][i][j] + " ");
            }
            System.out.print(" ");
            for (int j = 0; j < 3; j++) {
                System.out.print(cube[3][i][j] + " ");
            }
            System.out.print(" ");
            for (int j = 0; j < 3; j++) {
                System.out.print(cube[5][i][j] + " ");
            }
            System.out.println();
        }

        // Print the bottom face
        for (int i = 0; i < 3; i++) {
            System.out.print("       ");
            for (int j = 0; j < 3; j++) {
                System.out.print(cube[4][i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    private static void print3DCube(String[][][] cube) {
        for (int i = 0; i < 6; i++) {
            System.out.println("Face " + i + ":");
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    System.out.print(cube[i][j][k] + " ");
                }
                System.out.println();
            }
        }
        System.out.println();
    }

    private static void rotateCubefaceClockwise(String[][][] cube) {
        System.out.println("Rotate frontface clockwise");
        String[][][] temp = new String[6][3][3];

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    temp[i][j][k] = cube[i][j][k];
                }
            }
        }
            
        // From face 1 to face 0
        cube[0][2][2] = temp[1][0][2]; 
        cube[0][2][1] = temp[1][1][2];
        cube[0][2][0] = temp[1][2][2];

        // From face 0 to face 3
        cube[3][0][0] = temp[0][2][0];
        cube[3][1][0] = temp[0][2][1];
        cube[3][2][0] = temp[0][2][2];

        // From face 3 to face 4
        cube[4][0][2] = temp[3][0][0];
        cube[4][0][1] = temp[3][1][0];
        cube[4][0][0] = temp[3][2][0];

        // From face 4 to face 1
        cube[1][0][2] = temp[4][0][0];
        cube[1][1][2] = temp[4][0][1];
        cube[1][2][2] = temp[4][0][2];

        // Face 2 rotate clockwise
        cube[2][0][0] = temp[2][2][0];
        cube[2][0][1] = temp[2][1][0];
        cube[2][0][2] = temp[2][0][0];
        cube[2][1][0] = temp[2][2][1];
        cube[2][1][2] = temp[2][0][1];
        cube[2][2][0] = temp[2][2][2];
        cube[2][2][1] = temp[2][1][2];
        cube[2][2][2] = temp[2][0][2];
    }

    private static void rotateCubefaceCounterClockwise(String[][][] cube) {
        System.out.println("Rotate frontface counterclockwise");
        String[][][] temp = new String[6][3][3];

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    temp[i][j][k] = cube[i][j][k];
                }
            }
        }

        // From face 0 to face 1
        cube[1][2][2] = temp[0][2][0]; 
        cube[1][1][2] = temp[0][2][1];
        cube[1][0][2] = temp[0][2][2];

        // From face 3 to face 0
        cube[0][2][0] = temp[3][0][0]; 
        cube[0][2][1] = temp[3][1][0];
        cube[0][2][2] = temp[3][2][0];

        // From face 4 to face 3
        cube[3][0][0] = temp[4][0][2]; 
        cube[3][1][0] = temp[4][0][1];
        cube[3][2][0] = temp[4][0][0];

        // From face 1 to face 4
        cube[4][0][0] = temp[1][0][2]; 
        cube[4][0][1] = temp[1][1][2];
        cube[4][0][2] = temp[1][2][2];

        // Face 2 rotate counterclockwise 
        cube[2][0][0] = temp[2][0][2]; 
        cube[2][0][1] = temp[2][1][2];
        cube[2][0][2] = temp[2][2][2];
        cube[2][1][0] = temp[2][0][1]; 
        cube[2][1][2] = temp[2][2][1];
        cube[2][2][0] = temp[2][0][0];
        cube[2][2][1] = temp[2][1][0]; 
        cube[2][2][2] = temp[2][2][0];
    }

    private static void rotateCubeToRight(String[][][] cube) {
        System.out.println("Rotate cube to right");
        String[][][] temp = new String[6][3][3];

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    temp[i][j][k] = cube[i][j][k];
                }
            }
        }

        // Rotate Face 0 counterclockwise
        cube[0][0][0] = temp[0][0][2]; 
        cube[0][0][1] = temp[0][1][2];
        cube[0][0][2] = temp[0][2][2];
        cube[0][1][0] = temp[0][0][1]; 
        cube[0][1][2] = temp[0][2][1];
        cube[0][2][0] = temp[0][0][0];
        cube[0][2][1] = temp[0][1][0]; 
        cube[0][2][2] = temp[0][2][0];

        // Move face 1 to be face 2
        cube[2][0][0] = temp[1][0][0]; 
        cube[2][0][1] = temp[1][0][1];
        cube[2][0][2] = temp[1][0][2];
        cube[2][1][0] = temp[1][1][0]; 
        cube[2][1][1] = temp[1][1][1];
        cube[2][1][2] = temp[1][1][2];
        cube[2][2][0] = temp[1][2][0];
        cube[2][2][1] = temp[1][2][1]; 
        cube[2][2][2] = temp[1][2][2];

        // Move face 2 to be face 3
        cube[3][0][0] = temp[2][0][0]; 
        cube[3][0][1] = temp[2][0][1];
        cube[3][0][2] = temp[2][0][2];
        cube[3][1][0] = temp[2][1][0]; 
        cube[3][1][1] = temp[2][1][1];
        cube[3][1][2] = temp[2][1][2];
        cube[3][2][0] = temp[2][2][0];
        cube[3][2][1] = temp[2][2][1]; 
        cube[3][2][2] = temp[2][2][2];

        // Move face 3 to be face 5
        cube[5][0][0] = temp[3][0][0]; 
        cube[5][0][1] = temp[3][0][1];
        cube[5][0][2] = temp[3][0][2];
        cube[5][1][0] = temp[3][1][0]; 
        cube[5][1][1] = temp[3][1][1];
        cube[5][1][2] = temp[3][1][2];
        cube[5][2][0] = temp[3][2][0];
        cube[5][2][1] = temp[3][2][1]; 
        cube[5][2][2] = temp[3][2][2];

        // Move face 5 to face 1
        cube[1][0][0] = temp[5][0][0]; 
        cube[1][0][1] = temp[5][0][1];
        cube[1][0][2] = temp[5][0][2];
        cube[1][1][0] = temp[5][1][0]; 
        cube[1][1][1] = temp[5][1][1];
        cube[1][1][2] = temp[5][1][2];
        cube[1][2][0] = temp[5][2][0];
        cube[1][2][1] = temp[5][2][1]; 
        cube[1][2][2] = temp[5][2][2];

        // Rotate face 4 clockwise
        cube[4][0][0] = temp[4][2][0];
        cube[4][0][1] = temp[4][1][0];
        cube[4][0][2] = temp[4][0][0];
        cube[4][1][0] = temp[4][2][1];
        cube[4][1][2] = temp[4][0][1];
        cube[4][2][0] = temp[4][2][2];
        cube[4][2][1] = temp[4][1][2];
        cube[4][2][2] = temp[4][0][2];
    }

    private static void rotateCubeToLeft(String[][][] cube) {
        System.out.println("Rotate cube to left");
        String[][][] temp = new String[6][3][3];

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    temp[i][j][k] = cube[i][j][k];
                }
            }
        }

        // Rotate face 0 clockwise
        cube[0][0][0] = temp[0][2][0];
        cube[0][0][1] = temp[0][1][0];
        cube[0][0][2] = temp[0][0][0];
        cube[0][1][0] = temp[0][2][1];
        cube[0][1][2] = temp[0][0][1];
        cube[0][2][0] = temp[0][2][2];
        cube[0][2][1] = temp[0][1][2];
        cube[0][2][2] = temp[0][0][2];

        // Move face 1 to be face 5
        cube[5][0][0] = temp[1][0][0]; 
        cube[5][0][1] = temp[1][0][1];
        cube[5][0][2] = temp[1][0][2];
        cube[5][1][0] = temp[1][1][0]; 
        cube[5][1][1] = temp[1][1][1];
        cube[5][1][2] = temp[1][1][2];
        cube[5][2][0] = temp[1][2][0];
        cube[5][2][1] = temp[1][2][1]; 
        cube[5][2][2] = temp[1][2][2];

        // Move face 2 to be face 1
        cube[1][0][0] = temp[2][0][0]; 
        cube[1][0][1] = temp[2][0][1];
        cube[1][0][2] = temp[2][0][2];
        cube[1][1][0] = temp[2][1][0]; 
        cube[1][1][1] = temp[2][1][1];
        cube[1][1][2] = temp[2][1][2];
        cube[1][2][0] = temp[2][2][0];
        cube[1][2][1] = temp[2][2][1]; 
        cube[1][2][2] = temp[2][2][2];

        // Move face 3 to be face 2
        cube[2][0][0] = temp[3][0][0]; 
        cube[2][0][1] = temp[3][0][1];
        cube[2][0][2] = temp[3][0][2];
        cube[2][1][0] = temp[3][1][0]; 
        cube[2][1][1] = temp[3][1][1];
        cube[2][1][2] = temp[3][1][2];
        cube[2][2][0] = temp[3][2][0];
        cube[2][2][1] = temp[3][2][1]; 
        cube[2][2][2] = temp[3][2][2];

        // Move face 5 to be face 3
        cube[3][0][0] = temp[5][0][0]; 
        cube[3][0][1] = temp[5][0][1];
        cube[3][0][2] = temp[5][0][2];
        cube[3][1][0] = temp[5][1][0]; 
        cube[3][1][1] = temp[5][1][1];
        cube[3][1][2] = temp[5][1][2];
        cube[3][2][0] = temp[5][2][0];
        cube[3][2][1] = temp[5][2][1]; 
        cube[3][2][2] = temp[5][2][2];

        // Rotate face 4 counterclockwise 
        cube[4][0][0] = temp[4][0][2]; 
        cube[4][0][1] = temp[4][1][2];
        cube[4][0][2] = temp[4][2][2];
        cube[4][1][0] = temp[4][0][1]; 
        cube[4][1][2] = temp[4][2][1];
        cube[4][2][0] = temp[4][0][0];
        cube[4][2][1] = temp[4][1][0]; 
        cube[4][2][2] = temp[4][2][0];
    }

    public static void rotateCubeFrontfaceUp(String[][][] cube) {
        System.out.println("Rotate cubeface up");
        String[][][] temp = new String[6][3][3];

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    temp[i][j][k] = cube[i][j][k];
                }
            }
        }

        // Move face 0 to be face 5
        cube[5][2][2] = temp[0][0][0];
        cube[5][2][1] = temp[0][0][1];
        cube[5][2][0] = temp[0][0][2];
        cube[5][1][2] = temp[0][1][0];
        cube[5][1][1] = temp[0][1][1];
        cube[5][1][0] = temp[0][1][2];
        cube[5][0][2] = temp[0][2][0];
        cube[5][0][1] = temp[0][2][1];
        cube[5][0][0] = temp[0][2][2];

        // Move face 2 to be face 0
        cube[0][0][0] = temp[2][0][0];
        cube[0][0][1] = temp[2][0][1];
        cube[0][0][2] = temp[2][0][2];
        cube[0][1][0] = temp[2][1][0];
        cube[0][1][1] = temp[2][1][1];
        cube[0][1][2] = temp[2][1][2];
        cube[0][2][0] = temp[2][2][0];
        cube[0][2][1] = temp[2][2][1];
        cube[0][2][2] = temp[2][2][2];


        // Move face 4 to be face 2
        cube[2][0][0] = temp[4][0][0];
        cube[2][0][1] = temp[4][0][1];
        cube[2][0][2] = temp[4][0][2];
        cube[2][1][0] = temp[4][1][0];
        cube[2][1][1] = temp[4][1][1];
        cube[2][1][2] = temp[4][1][2];
        cube[2][2][0] = temp[4][2][0];
        cube[2][2][1] = temp[4][2][1];
        cube[2][2][2] = temp[4][2][2];

        // Move face 5 to be face 4
        cube[4][2][2] = temp[5][0][0];
        cube[4][2][1] = temp[5][0][1];
        cube[4][2][0] = temp[5][0][2];
        cube[4][1][2] = temp[5][1][0];
        cube[4][1][1] = temp[5][1][1];
        cube[4][1][0] = temp[5][1][2];
        cube[4][0][2] = temp[5][2][0];
        cube[4][0][1] = temp[5][2][1];
        cube[4][0][0] = temp[5][2][2];

        // Rotate face 1 counterclockwise
        cube[1][0][0] = temp[1][0][2];
        cube[1][0][1] = temp[1][1][2];
        cube[1][0][2] = temp[1][2][2];
        cube[1][1][0] = temp[1][0][1];
        cube[1][1][2] = temp[1][2][1];
        cube[1][2][0] = temp[1][0][0];
        cube[1][2][1] = temp[1][1][0];
        cube[1][2][2] = temp[1][2][0];

        // Rotate face 3 clockise
        cube[3][0][0] = temp[3][2][0];
        cube[3][0][1] = temp[3][1][0];
        cube[3][0][2] = temp[3][0][0];
        cube[3][1][0] = temp[3][2][1];
        cube[3][1][2] = temp[3][0][1];
        cube[3][2][0] = temp[3][2][2];
        cube[3][2][1] = temp[3][1][2];
        cube[3][2][2] = temp[3][0][2];
    }

    public static void rotateCubeFrontfaceDown(String[][][] cube) {
        System.out.println("Rotate cubeface down");
        String[][][] temp = new String[6][3][3];

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    temp[i][j][k] = cube[i][j][k];
                }
            }
        }

        // Move face 5 to be face 0
        cube[0][2][2] = temp[5][0][0];
        cube[0][2][1] = temp[5][0][1];
        cube[0][2][0] = temp[5][0][2];
        cube[0][1][2] = temp[5][1][0];
        cube[0][1][1] = temp[5][1][1];
        cube[0][1][0] = temp[5][1][2];
        cube[0][0][2] = temp[5][2][0];
        cube[0][0][1] = temp[5][2][1];
        cube[0][0][0] = temp[5][2][2];

        // Move face 0 to be face 2
        cube[2][0][0] = temp[0][0][0];
        cube[2][0][1] = temp[0][0][1];
        cube[2][0][2] = temp[0][0][2];
        cube[2][1][0] = temp[0][1][0];
        cube[2][1][1] = temp[0][1][1];
        cube[2][1][2] = temp[0][1][2];
        cube[2][2][0] = temp[0][2][0];
        cube[2][2][1] = temp[0][2][1];
        cube[2][2][2] = temp[0][2][2];

        // Move fave 2 to be face 4
        cube[4][0][0] = temp[2][0][0];
        cube[4][0][1] = temp[2][0][1];
        cube[4][0][2] = temp[2][0][2];
        cube[4][1][0] = temp[2][1][0];
        cube[4][1][1] = temp[2][1][1];
        cube[4][1][2] = temp[2][1][2];
        cube[4][2][0] = temp[2][2][0];
        cube[4][2][1] = temp[2][2][1];
        cube[4][2][2] = temp[2][2][2];

        // Move face 4 to be face 5
        cube[5][0][0] = temp[4][2][2];
        cube[5][0][1] = temp[4][2][1];
        cube[5][0][2] = temp[4][2][0];
        cube[5][1][0] = temp[4][1][2];
        cube[5][1][1] = temp[4][1][1];
        cube[5][1][2] = temp[4][1][0];
        cube[5][2][0] = temp[4][0][2];
        cube[5][2][1] = temp[4][0][1];
        cube[5][2][2] = temp[4][0][0];

        // Rotate face 1 clockwise
        cube[1][0][0] = temp[1][2][0];
        cube[1][0][1] = temp[1][1][0];
        cube[1][0][2] = temp[1][0][0];
        cube[1][1][0] = temp[1][2][1];
        cube[1][1][2] = temp[1][0][1];
        cube[1][2][0] = temp[1][2][2];
        cube[1][2][1] = temp[1][1][2];
        cube[1][2][2] = temp[1][0][2];


        // Rotate face 3 counterclockwise
        cube[3][0][0] = temp[3][0][2];
        cube[3][0][1] = temp[3][1][2];
        cube[3][0][2] = temp[3][2][2];
        cube[3][1][0] = temp[3][0][1];
        cube[3][1][2] = temp[3][2][1];
        cube[3][2][0] = temp[3][0][0];
        cube[3][2][1] = temp[3][1][0];
        cube[3][2][2] = temp[3][2][0];
    }

    public static void rotateRightSideClockwise(String[][][] cube) {
        System.out.println("Rotate right side clockwise");
        String[][][] temp = new String[6][3][3];

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    temp[i][j][k] = cube[i][j][k];
                }
            }
        }

        // Rotate face 3 clockwise
        cube[3][0][0] = temp[3][2][0];
        cube[3][0][1] = temp[3][1][0];
        cube[3][0][2] = temp[3][0][0];
        cube[3][1][0] = temp[3][2][1];
        cube[3][1][2] = temp[3][0][1];
        cube[3][2][0] = temp[3][2][2];
        cube[3][2][1] = temp[3][1][2];
        cube[3][2][2] = temp[3][0][2];

        // Move part of face 2 to part of face 0
        cube[0][0][2] = temp[2][0][2];
        cube[0][1][2] = temp[2][1][2];
        cube[0][2][2] = temp[2][2][2];

        // Move part of face 4 to parf of face 2
        cube[2][0][2] = temp[4][0][2];
        cube[2][1][2] = temp[4][1][2];
        cube[2][2][2] = temp[4][2][2];

        // Move part of face 0 to part of face 5
        cube[5][2][0] = temp[0][0][2];
        cube[5][1][0] = temp[0][1][2];
        cube[5][0][0] = temp[0][2][2];

        // Move part of face 5 to part of face 4
        cube[4][2][2] = temp[5][0][0];
        cube[4][1][2] = temp[5][1][0];
        cube[4][0][2] = temp[5][2][0];
    }

    public static void rotaterightSideCounterClockwise(String[][][] cube) {
        System.out.println("Rotate right side counterclockwise");
        String[][][] temp = new String[6][3][3];

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    temp[i][j][k] = cube[i][j][k];
                }
            }
        }

        // Rotate face 3 counterclockwise
        cube[3][0][0] = temp[3][0][2];
        cube[3][0][1] = temp[3][1][2];
        cube[3][0][2] = temp[3][2][2];
        cube[3][1][0] = temp[3][0][1];
        cube[3][1][2] = temp[3][2][1];
        cube[3][2][0] = temp[3][0][0];
        cube[3][2][1] = temp[3][1][0];
        cube[3][2][2] = temp[3][2][0];

        // Move part of face 0 to part of face 2
        cube[2][0][2] = temp[0][0][2];
        cube[2][1][2] = temp[0][1][2];
        cube[2][2][2] = temp[0][2][2];

        // Move part of face 2 to part of face 4
        cube[4][0][2] = temp[2][0][2];
        cube[4][1][2] = temp[2][1][2];
        cube[4][2][2] = temp[2][2][2];

        // Move part of face 4 to part of face 5
        cube[5][2][0] = temp[4][0][2];
        cube[5][1][0] = temp[4][1][2];
        cube[5][0][0] = temp[4][2][2];

        // Move part of face 5 to part of face 0
        cube[0][2][2] = temp[5][0][0];
        cube[0][1][2] = temp[5][1][0];
        cube[0][0][2] = temp[5][2][0];
    }

    public static void rotateLeftSideUp(String[][][] cube) {
        System.out.println("Rotate left side up");
        String[][][] temp = new String[6][3][3];

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    temp[i][j][k] = cube[i][j][k];
                }
            }
        }

        // Rotate face 1 counterclockwise
        cube[1][0][0] = temp[1][0][2];
        cube[1][0][1] = temp[1][1][2];
        cube[1][0][2] = temp[1][2][2];
        cube[1][1][0] = temp[1][0][1];
        cube[1][1][2] = temp[1][2][1];
        cube[1][2][0] = temp[1][0][0];
        cube[1][2][1] = temp[1][1][0];
        cube[1][2][2] = temp[1][2][0];

        // Move part of face 2 to part of face 0
        cube[0][0][0] = temp[2][0][0];
        cube[0][1][0] = temp[2][1][0];
        cube[0][2][0] = temp[2][2][0];

        // Move part of face 4 to part of face 2
        cube[2][0][0] = temp[4][0][0];
        cube[2][1][0] = temp[4][1][0];
        cube[2][2][0] = temp[4][2][0];

        // Move part of face 0 to part of face 5
        cube[5][0][2] = temp[0][2][0];
        cube[5][1][2] = temp[0][1][0];
        cube[5][2][2] = temp[0][0][0];

        // Move part of face 5 to part of face 4
        cube[4][0][0] = temp[5][2][2];
        cube[4][1][0] = temp[5][1][2];
        cube[4][2][0] = temp[5][0][2];
    }

    public static void rotateLeftSideDown(String[][][] cube) {
        System.out.println("Rotate left side down");
        String[][][] temp = new String[6][3][3];

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    temp[i][j][k] = cube[i][j][k];
                }
            }
        }

        // Rotate face 1 clockwise
        cube[1][0][0] = temp[1][2][0];
        cube[1][0][1] = temp[1][1][0];
        cube[1][0][2] = temp[1][0][0];
        cube[1][1][0] = temp[1][2][1];
        cube[1][1][2] = temp[1][0][1];
        cube[1][2][0] = temp[1][2][2];
        cube[1][2][1] = temp[1][1][2];
        cube[1][2][2] = temp[1][0][2];

        // Move part of face 0 to part of face 2
        cube[2][0][0] = temp[0][0][0];
        cube[2][1][0] = temp[0][1][0];
        cube[2][2][0] = temp[0][2][0];

        // Move part of face 2 to part of face 4
        cube[4][0][0] = temp[2][0][0];
        cube[4][1][0] = temp[2][1][0];
        cube[4][2][0] = temp[2][2][0];

        // Move part of face 4 to part of face 5
        cube[5][2][2] = temp[4][0][0];
        cube[5][1][2] = temp[4][1][0];
        cube[5][0][2] = temp[4][2][0];

        // Move part of face 5 to part of face 0
        cube[0][0][0] = temp[5][2][2];
        cube[0][1][0] = temp[5][1][2];
        cube[0][2][0] = temp[5][0][2];
    }

    public static void rotateTopClockwise(String[][][] cube) {
        System.out.println("Rotate top clockwise");
        String[][][] temp = new String[6][3][3];

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    temp[i][j][k] = cube[i][j][k];
                }
            }
        }

        // Rotate face 0 clockwise
        cube[0][0][0] = temp[0][2][0];
        cube[0][0][1] = temp[0][1][0];
        cube[0][0][2] = temp[0][0][0];
        cube[0][1][0] = temp[0][2][1];
        cube[0][1][2] = temp[0][0][1];
        cube[0][2][0] = temp[0][2][2];
        cube[0][2][1] = temp[0][1][2];
        cube[0][2][2] = temp[0][0][2];

        // Move part of face 2 to part of face 1
        cube[1][0][0] = temp[2][0][0];
        cube[1][0][1] = temp[2][0][1];
        cube[1][0][2] = temp[2][0][2];

        // Move part of face 3 to face 2
        cube[2][0][0] = temp[3][0][0];
        cube[2][0][1] = temp[3][0][1];
        cube[2][0][2] = temp[3][0][2];

        // Move part of face 5 to face 3
        cube[3][0][0] = temp[5][0][0];
        cube[3][0][1] = temp[5][0][1];
        cube[3][0][2] = temp[5][0][2];

        // Move part of face 1 to face 5
        cube[5][0][0] = temp[1][0][0];
        cube[5][0][1] = temp[1][0][1];
        cube[5][0][2] = temp[1][0][2];
    }

    public static void rotateTopCounterClockwise(String[][][] cube) {
        System.out.println("Rotate top counterclockwise");
        String[][][] temp = new String[6][3][3];

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    temp[i][j][k] = cube[i][j][k];
                }
            }
        }

        // Rotate face 0 counterclockwise
        cube[0][0][0] = temp[0][0][2];
        cube[0][0][1] = temp[0][1][2];
        cube[0][0][2] = temp[0][2][2];
        cube[0][1][0] = temp[0][0][1];
        cube[0][1][2] = temp[0][2][1];
        cube[0][2][0] = temp[0][0][0];
        cube[0][2][1] = temp[0][1][0];
        cube[0][2][2] = temp[0][2][0];

        // Move part of face 1 to part of face 2
        cube[2][0][0] = temp[1][0][0];
        cube[2][0][1] = temp[1][0][1];
        cube[2][0][2] = temp[1][0][2];

        // Move part of face 2 to part of face 3
        cube[3][0][0] = temp[2][0][0];
        cube[3][0][1] = temp[2][0][1];
        cube[3][0][2] = temp[2][0][2]; 

        // Move part of face 3 to part of face 5
        cube[5][0][0] = temp[3][0][0];
        cube[5][0][1] = temp[3][0][1];
        cube[5][0][2] = temp[3][0][2];

        // Move part of face 5 to part of face 1
        cube[1][0][0] = temp[5][0][0];
        cube[1][0][1] = temp[5][0][1];
        cube[1][0][2] = temp[5][0][2];
    }

    public static void rotateBottomClockwise(String[][][] cube) {
        System.out.println("Rotate bottom clockwise");
        String[][][] temp = new String[6][3][3];

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    temp[i][j][k] = cube[i][j][k];
                }
            }
        }

        // rotate face 4 clockwise
        cube[4][0][0] = temp[4][2][0];
        cube[4][0][1] = temp[4][1][0];
        cube[4][0][2] = temp[4][0][0];
        cube[4][1][0] = temp[4][2][1];
        cube[4][1][2] = temp[4][0][1];
        cube[4][2][0] = temp[4][2][2];
        cube[4][2][1] = temp[4][1][2];
        cube[4][2][2] = temp[4][0][2];

        // Move part of face 1 to part of face 2
        cube[2][2][0] = temp[1][2][0];
        cube[2][2][1] = temp[1][2][1];
        cube[2][2][2] = temp[1][2][2];

        // Move part of face 2 to part of face 3
        cube[3][2][0] = temp[2][2][0];
        cube[3][2][1] = temp[2][2][1];
        cube[3][2][2] = temp[2][2][2];

        // Move part of face 3 to part of face 5
        cube[5][2][0] = temp[3][2][0];
        cube[5][2][1] = temp[3][2][1];
        cube[5][2][2] = temp[3][2][2];

        // Move part of face 5 to part of face 1
        cube[1][2][0] = temp[5][2][0];
        cube[1][2][1] = temp[5][2][1];
        cube[1][2][2] = temp[5][2][2];
    }

    public static void rotateBottomCounterClockwise(String[][][] cube) {
        System.out.println("Rotate bottom counterclockwise");
        String[][][] temp = new String[6][3][3];

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    temp[i][j][k] = cube[i][j][k];
                }
            }
        }

        // Rotate face 4 counterclockwise
        cube[4][0][0] = temp[4][0][2];
        cube[4][0][1] = temp[4][1][2];
        cube[4][0][2] = temp[4][2][2];
        cube[4][1][0] = temp[4][0][1];
        cube[4][1][2] = temp[4][2][1];
        cube[4][2][0] = temp[4][0][0];
        cube[4][2][1] = temp[4][1][0];
        cube[4][2][2] = temp[4][2][0];

        // Move part of face 2 to part of face 1
        cube[1][2][0] = temp[2][2][0];
        cube[1][2][1] = temp[2][2][1];
        cube[1][2][2] = temp[2][2][2];

        // Move part of face 3 to part of face 2
        cube[2][2][0] = temp[3][2][0];
        cube[2][2][1] = temp[3][2][1];
        cube[2][2][2] = temp[3][2][2];

        // Move part of face 5 to part of face 3
        cube[3][2][0] = temp[5][2][0];
        cube[3][2][1] = temp[5][2][1];
        cube[3][2][2] = temp[5][2][2];

        // Move part of face 1 to part of face 5
        cube[5][2][0] = temp[1][2][0];
        cube[5][2][1] = temp[1][2][1];
        cube[5][2][2] = temp[1][2][2];
    }


    public static void solveCube(List<String> savedMoves, String[][][] cube) {
        for (int i = savedMoves.size() - 1; i >= 0; i--){
            String moveToRevers = savedMoves.get(i);
            if (moveToRevers.equals("x")){
                rotateCubeToRight(cube);
            }
            else if (moveToRevers.equals("X")){
                rotateCubeToLeft(cube);
            }
            else if (moveToRevers.equals("y")){
                rotateCubeFrontfaceUp(cube);
            }
            else if (moveToRevers.equals("Y")){
                rotateCubeFrontfaceDown(cube);
            }
            else if (moveToRevers.equals("f")){
                rotateCubefaceClockwise(cube);
            }
            else if (moveToRevers.equals("F")){
                rotateCubefaceCounterClockwise(cube);
            }
            else if (moveToRevers.equals("r")){
                rotateRightSideClockwise(cube);
            }
            else if (moveToRevers.equals("R")){
                rotaterightSideCounterClockwise(cube);
            }
            else if (moveToRevers.equals("l")){
                rotateLeftSideDown(cube);
            }
            else if (moveToRevers.equals("L")){
                rotateLeftSideUp(cube);
            }
            else if (moveToRevers.equals("u")){
                rotateTopClockwise(cube);
            }
            else if (moveToRevers.equals("U")){
                rotateTopCounterClockwise(cube);
            }
            else if (moveToRevers.equals("d")){
                rotateBottomClockwise(cube);
            }
            else if (moveToRevers.equals("D")){
                rotateBottomCounterClockwise(cube);
            }
        }
    }

    public static void scrambleCube(String[][][] cube, List<String> savedMoves) {
        String[] moves = { "X", "x", "Y", "y", "F", "f", "R", "r", "L", "l", "U", "u", "D", "d" };
        Random rand = new Random();

        int numMoves = 40;

        for (int i = 0; i < numMoves; i++) {
            int randomMoveIndex = rand.nextInt(moves.length);
            String move = moves[randomMoveIndex];
            makeMove(cube, move, savedMoves);
        }
    }

    public static void makeMove(String[][][] cube, String move, List<String> savedMoves) {
        if (move.equals("X")){
            rotateCubeToRight(cube);
            savedMoves.add(move);
        }
        else if (move.equals("x")){
            rotateCubeToLeft(cube);
            savedMoves.add(move);
        }
        else if (move.equals("Y")){
            rotateCubeFrontfaceUp(cube);
            savedMoves.add(move);
        }
        else if (move.equals("y")){
            rotateCubeFrontfaceDown(cube);
            savedMoves.add(move);
        }
        else if (move.equals("F")){
            rotateCubefaceClockwise(cube);
            savedMoves.add(move);
        }
        else if (move.equals("f")){
            rotateCubefaceCounterClockwise(cube);
            savedMoves.add(move);
        }
        else if (move.equals("R")){
            rotateRightSideClockwise(cube);
            savedMoves.add(move);
        }
        else if (move.equals("r")){
            rotaterightSideCounterClockwise(cube);
            savedMoves.add(move);
        }
        else if (move.equals("L")){
            rotateLeftSideDown(cube);
            savedMoves.add(move);
        }
        else if (move.equals("l")){
            rotateLeftSideUp(cube);
            savedMoves.add(move);
        }
        else if (move.equals("U")){
            rotateTopClockwise(cube);
            savedMoves.add(move);
        }
        else if (move.equals("u")){
            rotateTopCounterClockwise(cube);
            savedMoves.add(move);
        }
        else if (move.equals("D")){
            rotateBottomClockwise(cube);
            savedMoves.add(move);
        }
        else if (move.equals("d")){
            rotateBottomCounterClockwise(cube);
            savedMoves.add(move);
        }
    }


    public static void printIfCubeIsSolved(String[][][] cube) {
        if (checkIfSolved(cube)){
            System.out.println("Congratulation the cube is now solved");
        }
    }

    public static boolean checkIfSolved(String[][][] cube) {
        for(int i = 0; i < 6; i++) {
            String referenceColor = cube[i][0][0];
            for(int j = 0; j < 3; j++){
                for(int k = 0; k < 3; k++){
                    if (!cube[i][j][k].equals(referenceColor)){
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
