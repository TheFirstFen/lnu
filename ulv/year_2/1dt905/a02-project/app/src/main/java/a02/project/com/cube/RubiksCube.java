package a02.project.com.cube;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * The `RubiksCube` class represents a Rubik's Cube and provides methods to initialize, manipulate, and solve the cube.
 * It uses a 3-dimensional array to store the colors of the cube's squares and provides methods to rotate different parts of the cube.
 *
 * Fields:
 * - fullCube: A 3-dimensional array representing the Rubik's Cube.
 * - savedMoves: A list to store the moves made on the Rubik's Cube.
 *
 */
public class RubiksCube {
    private static String[][][] fullCube;
    private static List<String> savedMoves = new ArrayList<>();
    /**
     * Initializes the Rubik's cube with different colored squares.
     * 
     * @param cube a 3-dimensional array representing the Rubik's cube
     */
    public static void init(String[][][] cube) {

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
                    cube[i][j][k] = String.valueOf(colorLetters[i]);
                }
            }
        }
        fullCube = cube;
    }

    /**
     * Performs different operations on a Rubik's Cube based on the user's choice.
     *
     * @param choice The choice made by the user to perform a specific operation on the Rubik's Cube.
     * @return The updated Rubik's Cube after performing the operation based on the choice.
     */
    public static String[][][] mainLoop(String choice) {
        //print2DCube(fullCube);

        if (choice.equals("X")){
            rotateCubeToRight(fullCube);
            savedMoves.add(choice);
        }
        else if (choice.equals("x")){
            rotateCubeToLeft(fullCube);
            savedMoves.add(choice);
        }
        else if (choice.equals("Y")){
            rotateCubeFrontfaceUp(fullCube);
            savedMoves.add(choice);
        }
        else if (choice.equals("y")){
            rotateCubeFrontfaceDown(fullCube);
            savedMoves.add(choice);
        }
        else if (choice.equals("F")){
            rotateCubefaceClockwise(fullCube);
            savedMoves.add(choice);
            printIfCubeIsSolved(fullCube);
        }
        else if (choice.equals("f")){
            rotateCubefaceCounterClockwise(fullCube);
            savedMoves.add(choice);
            printIfCubeIsSolved(fullCube);
        }
        else if (choice.equals("R")){
            rotateRightSideClockwise(fullCube);
            savedMoves.add(choice);
            printIfCubeIsSolved(fullCube);
        }
        else if (choice.equals("r")){
            rotaterightSideCounterClockwise(fullCube);
            savedMoves.add(choice);
            printIfCubeIsSolved(fullCube);
        }
        else if (choice.equals("L")){
            rotateLeftSideDown(fullCube);
            savedMoves.add(choice);
            printIfCubeIsSolved(fullCube);
        }
        else if (choice.equals("l")){
            rotateLeftSideUp(fullCube);
            savedMoves.add(choice);
            printIfCubeIsSolved(fullCube);
        }
        else if (choice.equals("U")){
            rotateTopClockwise(fullCube);
            savedMoves.add(choice);
            printIfCubeIsSolved(fullCube);
        }
        else if (choice.equals("u")){
            rotateTopCounterClockwise(fullCube);
            savedMoves.add(choice);
            printIfCubeIsSolved(fullCube);
        }
        else if (choice.equals("D")){
            rotateBottomClockwise(fullCube);
            savedMoves.add(choice);
            printIfCubeIsSolved(fullCube);
        }
        else if (choice.equals("d")){
            rotateBottomCounterClockwise(fullCube);
            savedMoves.add(choice);
            printIfCubeIsSolved(fullCube);
        }
        else if (choice.equals("q")||choice.equals("Q")){
            System.out.println("Quitting");
        }
        else if (choice.equals("show")){
            for(String input : savedMoves){
                System.out.println(input);
            }
        }
        else if (choice.equals("solve")){
            solveCube(savedMoves, fullCube);
            savedMoves.clear();
        }
        else if (choice.equals("sc")){
            scrambleCube(fullCube, savedMoves);
        }
        else {
            System.out.println("Invalid input");
        }
        // print2DCube(fullCube);
        return fullCube;
    }

    //private static void print2DCube(String[][][] cube) {
    //    for (int i = 0; i < 3; i++) {
    //        System.out.print("       ");
    //        for (int j = 0; j < 3; j++) {
    //            System.out.print(cube[0][i][j] + " ");
    //        }
    //        System.out.println();
    //    }
    //    
    //    // Print the left, front, right, and back faces
    //    for (int i = 0; i < 3; i++) {
    //        for (int j = 0; j < 3; j++) {
    //            System.out.print(cube[1][i][j] + " ");
    //        }
    //        System.out.print(" ");
    //        for (int j = 0; j < 3; j++) {
    //            System.out.print(cube[2][i][j] + " ");
    //        }
    //        System.out.print(" ");
    //        for (int j = 0; j < 3; j++) {
    //            System.out.print(cube[3][i][j] + " ");
    //        }
    //        System.out.print(" ");
    //        for (int j = 0; j < 3; j++) {
    //            System.out.print(cube[5][i][j] + " ");
    //        }
    //        System.out.println();
    //    }
//
    //    // Print the bottom face
    //    for (int i = 0; i < 3; i++) {
    //        System.out.print("       ");
    //        for (int j = 0; j < 3; j++) {
    //            System.out.print(cube[4][i][j] + " ");
    //        }
    //        System.out.println();
    //    }
    //    System.out.println();
    //}

    /**
     * Rotates a face of a Rubik's Cube clockwise by swapping the colors of the individual squares.
     *
     * @param cube a 3D array representing the Rubik's Cube with colors assigned to each square
     */
    private static void rotateCubefaceClockwise(String[][][] cube) {
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

    /**
     * Rotates a face of a Rubik's Cube counter-clockwise.
     *
     * @param cube a 3D array representing the Rubik's Cube
     */
    private static void rotateCubefaceCounterClockwise(String[][][] cube) {
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

    /**
     * Rotates a Rubik's Cube to the right by rearranging the colors of its faces.
     *
     * @param cube The Rubik's Cube represented as a 3-dimensional array of strings.
     */
    private static void rotateCubeToRight(String[][][] cube) {
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

    /**
     * Rotates a Rubik's Cube to the left by rearranging the colors of the cube's faces.
     *
     * @param cube a 3D array representing the Rubik's Cube with 6 faces and 3x3 squares on each face.
     */
    private static void rotateCubeToLeft(String[][][] cube) {
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

    /**
     * Rotates the front face of a Rubik's Cube represented by a 3D array of strings in a clockwise direction.
     *
     * @param cube The 3D array representing the Rubik's Cube.
     */
    public static void rotateCubeFrontfaceUp(String[][][] cube) {
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

    /**
     * Rotates the front face of a Rubik's Cube down, along with the adjacent faces, in a clockwise direction.
     *
     * @param cube a 3D array representing the Rubik's Cube
     */
    public static void rotateCubeFrontfaceDown(String[][][] cube) {
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

        // Move face 2 to be face 4
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

    /**
     * Rotates the right side of a Rubik's Cube clockwise.
     *
     * @param cube a 3D array representing the Rubik's Cube
     */
    public static void rotateRightSideClockwise(String[][][] cube) {
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

        // Move part of face 4 to part of face 2
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

    /**
     * This method rotates the right side of a Rubik's Cube counterclockwise.
     * It takes a 3D array representing the cube as input and modifies it accordingly.
     *
     * @param cube a 3D array representing the Rubik's Cube
     */
    public static void rotaterightSideCounterClockwise(String[][][] cube) {
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

    /**
     * Rotates the left side of a Rubik's Cube upwards, along with the adjacent sides.
     *
     * @param cube a 3D array representing the Rubik's Cube
     */
    public static void rotateLeftSideUp(String[][][] cube) {
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

    /**
     * Rotates the left side of a Rubik's Cube down by rearranging the colors of the cube's faces.
     *
     * @param cube a 3D array representing the Rubik's Cube with colors assigned to each face.
     */
    public static void rotateLeftSideDown(String[][][] cube) {
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

    /**
     * Rotates the top face of a Rubik's Cube clockwise, along with the adjacent faces.
     *
     * @param cube a 3D array representing the Rubik's Cube
     */
    public static void rotateTopClockwise(String[][][] cube) {
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

    /**
     * Rotates the top face of a Rubik's Cube counter-clockwise, along with the adjacent faces.
     * 
     * @param cube a 3D array representing the Rubik's Cube, with each element representing a colored square on the cube.
     */
    public static void rotateTopCounterClockwise(String[][][] cube) {
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

    /**
     * Rotates the bottom face of a Rubik's Cube clockwise, along with the adjacent faces.
     *
     * @param cube a 3D array representing the Rubik's Cube
     */
    public static void rotateBottomClockwise(String[][][] cube) {

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

    /**
     * Rotates the bottom face of a Rubik's Cube counter-clockwise, along with the adjacent faces.
     *
     * @param cube The Rubik's Cube represented as a 3D array of strings.
     */
    public static void rotateBottomCounterClockwise(String[][][] cube) {
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


    /**
     * Reverses the effect of the moves stored in the 'savedMoves' list on the Rubik's Cube.
     * 
     * @param savedMoves A list of moves that have been performed on the Rubik's Cube.
     * @param cube A 3-dimensional array representing the Rubik's Cube.
     */
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

    /**
     * Randomly scrambles the Rubik's cube by making 80 random moves.
     *
     * @param cube The 3D array representing the Rubik's cube.
     * @param savedMoves A list to store the moves made during the scrambling process.
     */
    public static void scrambleCube(String[][][] cube, List<String> savedMoves) {
        String[] moves = { "X", "x", "Y", "y", "F", "f", "R", "r", "L", "l", "U", "u", "D", "d" };
        Random rand = new Random();

        int numMoves = 80;
        for (int i = 0; i < numMoves; i++) {
            int randomMoveIndex = rand.nextInt(moves.length);
            String move = moves[randomMoveIndex];
            makeMove(cube, move, savedMoves);
        }
    }

    /**
     * Makes a move on the Rubik's Cube by rotating the cube's faces or sides based on the given move.
     * It updates the cube's state and adds the move to the list of saved moves.
     *
     * @param cube        The 3D array representing the Rubik's Cube.
     * @param move        The move to be made on the cube.
     * @param savedMoves  The list to store the moves made on the cube.
     */
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
        else {
            rotateBottomCounterClockwise(cube);
            savedMoves.add(move);
        }
    }


    /**
     * Checks if the Rubik's Cube is solved and prints a congratulatory message if it is.
     *
     * @param cube The Rubik's Cube represented as a 3D array.
     */
    public static void printIfCubeIsSolved(String[][][] cube) {
        if (checkIfSolved(cube)){
            System.out.println("Congratulation the cube is now solved");
        }
    }

    /**
     * Checks if a Rubik's Cube is solved by comparing the color of each sticker on each face of the cube
     * with the color of the sticker in the top-left corner of that face.
     *
     * @param cube a 3D array representing the Rubik's Cube, where each element represents the color of a sticker on the cube
     * @return true if the Rubik's Cube is solved (all stickers have the same color on each face), false otherwise
     */
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
