package com.sb224sc.rubik.model;

import javafx.scene.paint.Color;

import java.util.*;
import java.util.stream.Collectors;
import com.sb224sc.rubik.MainApplication;

@SuppressWarnings("java:S106")
public class CubeSolver {
    private Cube cube;

    private static final String T_RIGHT = "drdRDFDf";
    private static final String T_LEFT = "DLDldfdF";
    private static final String INVERT_CORNERS = "rBRDrdbDR"; // dLDFdflFD
    private static final String TURN_CORNERS = "fUFRUrDRurfuFd"; // rDRFDfUFdfrdRu
    private static final String TURN_CORNERS_FROM_LEFT = "dBDLBlFLbldbDf"; // rDRFDfUFdfrdRu
    private static final String TURN_BOTTOM_EDGES = "mDMDDmDM";
    private static final String TRIANGLE_LEFT = "LDlDLDDl";
    private static final String TRIANGLE_RIGHT = "rdRdrddR";

    private static ArrayList<Boolean> isSolved = new ArrayList<>();

    public CubeSolver(Cube cube) {
        this.cube = cube;
    }

    /**
     * Solves the Rubik's Cube puzzle by generating a sequence of moves.
     *
     * @return A string representing the sequence of moves to solve the Rubik's
     *         Cube.
     */
    public String solve() {
        Move.animation = false;
        List<String> solution = new ArrayList<>();

        // Make corners
        for (int i = 0; i < 4; i++) {
            makeCorner(solution);
            if (i != 3) {
                turnCubeY(solution, 1);
            }
        }
        turnCubeY(solution, 1);

        // Make edges
        for (int i = 0; i < 4; i++) {
            makeEdge(solution);
            if (i != 3) {
                turnCubeY(solution, 1);
            }
        }

        // Make Ts
        for (int i = 0; i < 4; i++) {
            makeRightT(solution);
            makeLeftT(solution);
            if (i != 4) {
                turnCubeY(solution, 1);
            }
        }

        // Make bottom corners
        makeBottomCorners(solution);
        turnCubeY(solution, 1);
        turnCubeY(solution, 1);
        makeBottomCorners(solution);
        if (!(cube.findCubeByPos(0, 2, 0).isInCorrectPlace(cube) &&
                cube.findCubeByPos(2, 2, 0).isInCorrectPlace(cube) &&
                cube.findCubeByPos(0, 2, 2).isInCorrectPlace(cube) &&
                cube.findCubeByPos(2, 2, 2).isInCorrectPlace(cube))) {
            turnCubeY(solution, 1);
            turnCubeY(solution, 1);
            makeBottomCorners(solution);
        }

        // Turn bottom edges
        turnBottomEdges(solution);
        turnBottomEdges(solution);

        // Make bottom edges
        makeBottomEdges(solution);
        makeBottomEdges(solution);

        if (solution.isEmpty())
            return null;

        // ------------ Reset -----------------
        StringBuilder builder = new StringBuilder();
        for (String s : solution) {
            for (char c : s.toCharArray()) {
                builder.append(Character.toString(c));
            }
        }
        String sol = clean(builder.toString());
        String opposite = reverse(sol);

        makeMove(opposite, new ArrayList<>());
        Move.animation = true;

        if (sol.length() == 0)
            return null;

        MainApplication.clickAllowed = false;
        new Thread(() -> {
            for (int i = 0; i < sol.length(); i++) {
                char c = sol.charAt(i);
                makeMove(Character.toString(c), new ArrayList<>());
                while (Move.animating) {
                    try {
                        Thread.sleep(100);
                    } catch (InterruptedException ex) {
                        ex.getMessage();
                        Thread.currentThread().interrupt();
                    }
                }
            }
            MainApplication.clickAllowed = true;
        }).start();

        return sol;
    }

    /**
     * Cleans the input string by applying specific rules.
     *
     * @param sol the input string to be cleaned
     * @return the cleaned string
     */
    private String clean(String sol) {
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < sol.length(); i++) {
            char c = sol.charAt(i);
            if (i < sol.length() - 1) {
                char next = sol.charAt(i + 1);
                if (c == next && Character.isLowerCase(c)) {
                    builder.append(Character.toUpperCase(c) + "" + Character.toUpperCase(c));
                    i++;
                    continue;
                } else if (((Character.isUpperCase(c) && Character.isLowerCase(next))
                        || (Character.isUpperCase(next) && Character.isLowerCase(c)))
                        && Character.toUpperCase(c) == Character.toUpperCase(next)) {
                    i++;
                    continue;
                }
            }
            if (i < sol.length() - 4 && (c == sol.charAt(i + 1) && c == sol.charAt(i + 2) && c == sol.charAt(i + 3))) {
                i += 3;
                continue;

            }
            if (i < sol.length() - 3 && (c == sol.charAt(i + 1) && c == sol.charAt(i + 2))) {
                builder.append(Character.isUpperCase(c) ? Character.toLowerCase(c) : Character.toUpperCase(c));
                i += 2;
                continue;

            }
            builder.append(Character.toString(c));
        }

        String output = builder.toString();
        StringBuilder builder2 = new StringBuilder();
        for (int i = 0; i < output.length(); i++) {
            if (Character.toUpperCase(output.charAt(i)) != 'Y') {
                builder2.append(Character.toString(output.charAt(i)));
            }
        }

        boolean only = true;
        for (char c : output.toCharArray()) {
            if (Character.toUpperCase(c) != 'Y') {
                only = false;
                break;
            }
        }

        return only ? builder2.toString() : output;
    }

    /**
     * Turn the cube along the Y-axis.
     *
     * @param solution  the list to store the solution
     * @param direction the direction to rotate the cube (positive for clockwise,
     *                  negative for counterclockwise)
     */
    private void turnCubeY(List<String> solution, int direction) {
        cube.rotateCubeY(direction);
        solution.add(direction > 0 ? "Y" : "y");
    }

    /**
     * Reverses the input string and converts each character to the opposite case.
     *
     * @param in the input string to be reversed
     * @return the reversed string with opposite case characters
     */
    private static String reverse(String in) {
        StringBuilder builder = new StringBuilder();
        for (int i = in.length() - 1; i >= 0; i--) {
            String ch = Character.toString(in.charAt(i));
            builder.append(Move.CAPS.contains(ch) ? ch.toLowerCase() : ch.toUpperCase());
        }
        return builder.toString();
    }

    /**
     * Executes a move in the Rubik's Cube given an algorithm.
     *
     * @param algorithm the algorithm to execute
     * @param sol       the list of moves performed
     */
    private void makeMove(String algorithm, List<String> sol) {
        sol.add(algorithm);
        for (char c : algorithm.toCharArray()) {
            if (Character.toUpperCase(c) == 'Y') {
                cube.rotateCubeY(Character.isUpperCase(c) ? 1 : -1);
            } else {
                Move.applyMove(Character.toString(c), cube);
            }
        }
    }

    /**
     * Makes a triangle on the Rubik's Cube by performing a series of moves.
     *
     * @param solution the list to store the moves of the solution
     */
    private void makeTriangle(List<String> solution) {
        Color front = cube.findCubeByViewCoords(1, 2, 0).getFaceSystem().getFrontFace();
        if (front == cube.getFaces().getLeftFace()) {
            makeMove(TRIANGLE_RIGHT, solution);
            turnCubeY(solution, 1);
            makeMove(TRIANGLE_LEFT, solution);
        } else if (front == cube.getFaces().getRightFace()) {
            makeMove(TRIANGLE_LEFT, solution);
            turnCubeY(solution, -1);
            makeMove(TRIANGLE_RIGHT, solution);
        } else {
            makeMove(TRIANGLE_RIGHT, solution);
            turnCubeY(solution, 1);
            makeMove(TRIANGLE_LEFT, solution);
            makeTriangle(solution);
        }
    }

    /**
     * Makes the bottom edges of the cube.
     *
     * @param solution the list to store the solution steps
     */
    private void makeBottomEdges(List<String> solution) {
        if (!cube.findCubeByViewCoords(0, 2, 1).isInCorrectPlace(cube)
                && !cube.findCubeByViewCoords(1, 2, 0).isInCorrectPlace(cube)
                && !cube.findCubeByViewCoords(2, 2, 1).isInCorrectPlace(cube)) {
            makeTriangle(solution);
        } else if (!cube.findCubeByViewCoords(1, 2, 0).isInCorrectPlace(cube)
                && !cube.findCubeByViewCoords(2, 2, 1).isInCorrectPlace(cube)
                && !cube.findCubeByViewCoords(1, 2, 2).isInCorrectPlace(cube)) {
            turnCubeY(solution, 1);
            makeTriangle(solution);
        } else if (!cube.findCubeByViewCoords(2, 2, 1).isInCorrectPlace(cube)
                && !cube.findCubeByViewCoords(1, 2, 2).isInCorrectPlace(cube)
                && !cube.findCubeByViewCoords(0, 2, 1).isInCorrectPlace(cube)) {
            turnCubeY(solution, 1);
            turnCubeY(solution, 1);
            makeTriangle(solution);
        } else if (!cube.findCubeByViewCoords(1, 2, 2).isInCorrectPlace(cube)
                && !cube.findCubeByViewCoords(0, 2, 1).isInCorrectPlace(cube)
                && !cube.findCubeByViewCoords(1, 2, 0).isInCorrectPlace(cube)) {
            turnCubeY(solution, -1);
            makeTriangle(solution);
        } else {
            isSolved.add(true);
        }
    }

    /**
     * Turns the bottom edges of the cube if they are not correctly positioned.
     * 
     * If the bottom edges are not correctly positioned, this function makes the
     * necessary moves to position them correctly.
     *
     * @param solution the list to store the moves made
     */
    private void turnBottomEdges(List<String> solution) {
        /*
         * 1 2 0
         * 0 2 1 2 2 1
         * 1 2 2
         */

        if (cube.findCubeByViewCoords(1, 2, 0).getFaceSystem().getBottomFace() != cube.getFaces().getBottomFace()
                && cube.findCubeByViewCoords(0, 2, 1).getFaceSystem().getBottomFace() != cube.getFaces()
                        .getBottomFace()) {
            makeMove(TURN_BOTTOM_EDGES, solution);
        } else if (cube.findCubeByViewCoords(1, 2, 0).getFaceSystem().getBottomFace() != cube.getFaces().getBottomFace()
                && cube.findCubeByViewCoords(2, 2, 1).getFaceSystem().getBottomFace() != cube.getFaces()
                        .getBottomFace()) {
            turnCubeY(solution, 1);
            makeMove(TURN_BOTTOM_EDGES, solution);
        } else if (cube.findCubeByViewCoords(2, 2, 1).getFaceSystem().getBottomFace() != cube.getFaces().getBottomFace()
                && cube.findCubeByViewCoords(1, 2, 2).getFaceSystem().getBottomFace() != cube.getFaces()
                        .getBottomFace()) {
            turnCubeY(solution, 1);
            turnCubeY(solution, 1);
            makeMove(TURN_BOTTOM_EDGES, solution);
        } else if (cube.findCubeByViewCoords(1, 2, 2).getFaceSystem().getBottomFace() != cube.getFaces().getBottomFace()
                && cube.findCubeByViewCoords(0, 2, 1).getFaceSystem().getBottomFace() != cube.getFaces()
                        .getBottomFace()) {
            turnCubeY(solution, -1);
            makeMove(TURN_BOTTOM_EDGES, solution);
        } else if ((cube.findCubeByViewCoords(1, 2, 0).getFaceSystem().getBottomFace() != cube.getFaces()
                .getBottomFace()
                && cube.findCubeByViewCoords(1, 2, 2).getFaceSystem().getBottomFace() != cube.getFaces()
                        .getBottomFace())
                ||
                (cube.findCubeByViewCoords(0, 2, 1).getFaceSystem().getBottomFace() != cube.getFaces()
                        .getBottomFace()
                        && cube.findCubeByViewCoords(2, 2, 1).getFaceSystem().getBottomFace() != cube.getFaces()
                                .getBottomFace())) {
            makeMove(TRIANGLE_LEFT, solution);
            turnCubeY(solution, -1);
            makeMove(TRIANGLE_RIGHT, solution);
            turnCubeY(solution, 1);
            turnBottomEdges(solution);
        } else {
            isSolved.add(true);
        }
    }

    /**
     * Returns a list of common colors between two InnerCube pieces.
     *
     * @param piece1 the first InnerCube piece
     * @param piece2 the second InnerCube piece
     * @return a list of common colors between the two pieces
     */
    private List<Color> getCommonColors(InnerCube piece1, InnerCube piece2) {
        List<Color> colors1 = piece1.getVisibleColors();
        colors1.remove(cube.getFaces().getBottomFace());
        List<Color> colors2 = piece2.getVisibleColors();
        colors2.remove(cube.getFaces().getBottomFace());
        return colors1.stream().filter(colors2::contains).collect(Collectors.toList());
    }

    /**
     * Makes the bottom corners of the cube match the adjacent faces.
     *
     * @param solution the list of moves to solve the cube
     */
    private void makeBottomCorners(List<String> solution) {
        InnerCube piece1 = this.cube.findCubeByViewCoords(0, 2, 0);
        InnerCube piece2 = this.cube.findCubeByViewCoords(2, 2, 0);
        List<Color> sames = getCommonColors(piece1, piece2);
        Color same = null;
        if (sames.size() > 0) {
            same = sames.get(0);
            if (cube.getFaces().getRightFace().equals(same)) {
                makeMove("D", solution);
                turnCubeY(solution, 1);
            } else if (cube.getFaces().getBackFace().equals(same)) {
                makeMove("DD", solution);
                turnCubeY(solution, 1);
                turnCubeY(solution, 1);
            } else if (cube.getFaces().getLeftFace().equals(same)) {
                makeMove("d", solution);
                turnCubeY(solution, -1);
            }
        } else {
            turnCubeY(solution, 1);
            makeMove(INVERT_CORNERS, solution);
            turnCubeY(solution, -1);
            makeBottomCorners(solution);
            return;
        }
        if (piece1.hasColor(cube.getFaces().getRightFace())) {
            makeMove(INVERT_CORNERS, solution);
        }
        if (piece1.getFaceSystem().getFrontFace() == same && piece2.getFaceSystem().getFrontFace() == same) {
            // Ok!
            isSolved.add(true);
        } else if (piece1.getFaceSystem().getBottomFace() == same && piece2.getFaceSystem().getBottomFace() == same) {
            makeMove(TURN_CORNERS, solution);
        } else if (piece1.getFaceSystem().getLeftFace() == same && piece2.getFaceSystem().getRightFace() == same) {
            makeMove(TURN_CORNERS_FROM_LEFT, solution);
        } else {
            turnCubeY(solution, 1);
            makeMove(TURN_CORNERS, solution);
            makeMove(TURN_CORNERS, solution);
            turnCubeY(solution, -1);
            makeBottomCorners(solution);
        }
    }

    /**
     * Makes a right turn on the Rubik's Cube by manipulating the cube's state to
     * solve the cube.
     *
     * @param solution a list of moves that represents the solution to the cube
     */
    private void makeRightT(List<String> solution) {
        InnerCube piece = this.cube.findCubesByColor(cube.getFaces().getFrontFace(), cube.getFaces().getRightFace())
                .get(0);
        if (piece.isInCorrectPlace(cube)) {
            isSolved.add(true);
            return;
        }
        if (piece.getViewCoords(cube).getY() == 1) {
            if (piece.getViewCoords(cube).getX() == 0 && piece.getViewCoords(cube).getZ() == 0) {
                makeMove(T_LEFT, solution);
                makeRightT(solution);
            } else if (piece.getViewCoords(cube).getX() == 2 && piece.getViewCoords(cube).getZ() == 0) {
                makeMove(T_RIGHT, solution);
                makeRightT(solution);
            } else if (piece.getViewCoords(cube).getX() == 0 && piece.getViewCoords(cube).getZ() == 2) {
                turnCubeY(solution, -1);
                makeMove(T_LEFT, solution);
                turnCubeY(solution, 1);
                makeRightT(solution);
            } else if (piece.getViewCoords(cube).getX() == 2 && piece.getViewCoords(cube).getZ() == 2) {
                turnCubeY(solution, 1);
                makeMove(T_RIGHT, solution);
                turnCubeY(solution, -1);
                makeRightT(solution);
            }
        } else if (piece.getViewCoords(cube).getY() == 2) {
            if (piece.getViewCoords(cube).getX() == 2 && piece.getViewCoords(cube).getZ() == 1) {
                makeMove("d", solution);
            } else if (piece.getViewCoords(cube).getX() == 1 && piece.getViewCoords(cube).getZ() == 2) {
                makeMove("dd", solution);
            } else if (piece.getViewCoords(cube).getX() == 0 && piece.getViewCoords(cube).getZ() == 1) {
                makeMove("D", solution);
            }
            if (piece.getFaceSystem().getFrontFace().equals(cube.getFaces().getFrontFace())) {
                makeMove(T_RIGHT, solution);
            } else {
                makeMove("D", solution);
                turnCubeY(solution, 1);
                makeMove(T_LEFT, solution);
                turnCubeY(solution, -1);
            }
        }
    }

    /**
     * Generates the function comment for the given function body.
     *
     * @param solution the list of solutions
     */
    private void makeLeftT(List<String> solution) {
        InnerCube piece = this.cube.findCubesByColor(cube.getFaces().getFrontFace(), cube.getFaces().getLeftFace())
                .get(0);
        if (piece.isInCorrectPlace(cube)) {
            isSolved.add(true);
            return;
        }
        if (piece.getViewCoords(cube).getY() == 1) {
            if (piece.getViewCoords(cube).getX() == 0 && piece.getViewCoords(cube).getZ() == 0) {
                makeMove(T_LEFT, solution);
                makeLeftT(solution);
            } else if (piece.getViewCoords(cube).getX() == 2 && piece.getViewCoords(cube).getZ() == 0) {
                makeMove(T_RIGHT, solution);
                makeLeftT(solution);
            } else if (piece.getViewCoords(cube).getX() == 0 && piece.getViewCoords(cube).getZ() == 2) {
                turnCubeY(solution, -1);
                makeMove(T_LEFT, solution);
                turnCubeY(solution, 1);
                makeLeftT(solution);
            } else if (piece.getViewCoords(cube).getX() == 2 && piece.getViewCoords(cube).getZ() == 2) {
                turnCubeY(solution, 1);
                makeMove(T_RIGHT, solution);
                turnCubeY(solution, -1);
                makeLeftT(solution);
            }
        } else if (piece.getViewCoords(cube).getY() == 2) {
            if (piece.getViewCoords(cube).getX() == 2 && piece.getViewCoords(cube).getZ() == 1) {
                makeMove("d", solution);
            } else if (piece.getViewCoords(cube).getX() == 1 && piece.getViewCoords(cube).getZ() == 2) {
                makeMove("dd", solution);
            } else if (piece.getViewCoords(cube).getX() == 0 && piece.getViewCoords(cube).getZ() == 1) {
                makeMove("D", solution);
            }
            if (piece.getFaceSystem().getFrontFace().equals(cube.getFaces().getFrontFace())) {
                makeMove(T_LEFT, solution);
            } else {
                makeMove("d", solution);
                turnCubeY(solution, -1);
                makeMove(T_RIGHT, solution);
                turnCubeY(solution, 1);
            }
        }
    }

    /**
     * Generates the function comment for the given function body in a markdown code
     * block with the correct language syntax.
     *
     * @param solution the list of strings representing the solution
     */
    private void makeEdge(List<String> solution) {
        InnerCube piece = this.cube.findCubesByColor(cube.getFaces().getFrontFace(), cube.getFaces().getTopFace())
                .get(0);
        if (piece.isInCorrectPlace(cube)) {
            isSolved.add(true);
            return;
        }
        boolean down = false;
        String add = null;
        if (piece.getViewCoords(cube).getY() == 0) {
            down = true;
            if (piece.getViewCoords(cube).getX() == 1 && piece.getViewCoords(cube).getZ() == 0) {
                makeMove("MdmD", solution);
            } else if (piece.getViewCoords(cube).getX() == 0 && piece.getViewCoords(cube).getZ() == 1) {
                makeMove("sDS", solution);
            } else if (piece.getViewCoords(cube).getX() == 2 && piece.getViewCoords(cube).getZ() == 1) {
                makeMove("Sds", solution);
            } else if (piece.getViewCoords(cube).getX() == 1 && piece.getViewCoords(cube).getZ() == 2) {
                makeMove("mDMD", solution);
            }
        } else if (piece.getViewCoords(cube).getY() == 1) {
            if (piece.getViewCoords(cube).getX() == 0 && piece.getViewCoords(cube).getZ() == 0) {
                makeMove("E", solution);
                add = "e";
            } else if (piece.getViewCoords(cube).getX() == 0 && piece.getViewCoords(cube).getZ() == 2) {
                makeMove("EE", solution);
                add = "ee";
            } else if (piece.getViewCoords(cube).getX() == 2 && piece.getViewCoords(cube).getZ() == 2) {
                makeMove("e", solution);
                add = "E";
            }
        } else if (piece.getViewCoords(cube).getY() == 2) {
            down = true;
            if (piece.getViewCoords(cube).getX() == 0 && piece.getViewCoords(cube).getZ() == 1) {
                makeMove("D", solution);
            } else if (piece.getViewCoords(cube).getX() == 2 && piece.getViewCoords(cube).getZ() == 1) {
                makeMove("d", solution);
            } else if (piece.getViewCoords(cube).getX() == 1 && piece.getViewCoords(cube).getZ() == 2) {
                makeMove("DD", solution);
            }
        }

        if (down) {
            if (piece.getFaceSystem().getFrontFace().equals(cube.getFaces().getTopFace())) {
                makeMove("dMDm", solution);
            } else if (piece.getFaceSystem().getBottomFace().equals(cube.getFaces().getTopFace())) {
                makeMove("FEEffEEF", solution);
            }
        } else {
            if (piece.getFaceSystem().getRightFace().equals(cube.getFaces().getTopFace())) {
                makeMove("EFef", solution);
            } else if (piece.getFaceSystem().getFrontFace().equals(cube.getFaces().getTopFace())) {
                makeMove("EEfEFE", solution);
            }
        }

        // Adjust top face
        if (add != null) {
            makeMove(add, solution);
        }
    }

    /**
     * Makes a corner in the cube by performing a series of moves.
     *
     * @param solution the list to store the moves performed
     */
    private void makeCorner(List<String> solution) {
        InnerCube piece = this.cube.findCubesByColor(cube.getFaces().getFrontFace(), cube.getFaces().getTopFace(),
                cube.getFaces().getLeftFace()).get(0);
        if (piece.isInCorrectPlace(cube)) {
            isSolved.add(true);
            return;
        }
        if (piece.getViewCoords(cube).getY() == 0) {
            if (piece.getViewCoords(cube).getX() == 0 && piece.getViewCoords(cube).getZ() == 2) {
                makeMove("BDb", solution);
            } else if (piece.getViewCoords(cube).getX() == 2 && piece.getViewCoords(cube).getZ() == 2) {
                makeMove("bddB", solution);
            } else if (piece.getViewCoords(cube).getX() == 2 && piece.getViewCoords(cube).getZ() == 0) {
                makeMove("rdR", solution);
            } else if (piece.getViewCoords(cube).getX() == 0 && piece.getViewCoords(cube).getZ() == 0) {
                makeMove("LDld", solution);
            }
        } else if (piece.getViewCoords(cube).getY() == 2) {
            if (piece.getViewCoords(cube).getX() == 0 && piece.getViewCoords(cube).getZ() == 2) {
                makeMove("D", solution);
            } else if (piece.getViewCoords(cube).getX() == 2 && piece.getViewCoords(cube).getZ() == 2) {
                makeMove("DD", solution);
            } else if (piece.getViewCoords(cube).getX() == 2 && piece.getViewCoords(cube).getZ() == 0) {
                makeMove("d", solution);
            }
        }
        if (piece.getFaceSystem().getFrontFace().equals(cube.getFaces().getTopFace())) {
            makeMove("DLdl", solution);
        } else if (piece.getFaceSystem().getBottomFace().equals(cube.getFaces().getTopFace())) {
            makeMove("LDDlddfDF", solution);
        } else if (piece.getFaceSystem().getLeftFace().equals(cube.getFaces().getTopFace())) {
            makeMove("dfDF", solution);
        }
    }

    /**
     * Checks if the cube is solved.
     *
     * @return true if the cube is solved, false otherwise
     */
    public static boolean cubeIsSolved() {
        for (boolean value : isSolved) {
            if (!value) {
                return false;
            }
        }
        return true;
    }
}
