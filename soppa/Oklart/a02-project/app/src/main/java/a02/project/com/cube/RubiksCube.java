package a02.project.com.cube;

public class RubiksCube {
    public static void main(String[] args) {
        String[][][] colorMatrix = new String[6][3][3];

        char[] colorLetters = { 'R', 'G', 'B', 'W', 'Y', 'O' };

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    colorMatrix[i][j][k] = String.valueOf(colorLetters[i]);
                }
            }
        }

        print2DCube(colorMatrix);
        print3DCube(colorMatrix);

        rotateCube(colorMatrix, "clockwise");

        print2DCube(colorMatrix);
        print3DCube(colorMatrix);
    }

    private static void print2DCube(String[][][] cube) {
        for (int i = 0; i < 3; i++) {
            System.out.print("       ");
            for (int j = 0; j < 3; j++) {
                System.out.print(cube[1][i][j] + " ");
            }
            System.out.println();
        }
        
        // Print the left, front, right, and back faces
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(cube[4][i][j] + " ");
            }
            System.out.print(" ");
            for (int j = 0; j < 3; j++) {
                System.out.print(cube[0][i][j] + " ");
            }
            System.out.print(" ");
            for (int j = 0; j < 3; j++) {
                System.out.print(cube[2][i][j] + " ");
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
                System.out.print(cube[3][i][j] + " ");
            }
            System.out.println();
        }
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

    private static void rotateCube(String[][][] cube, String direction) {
        if (direction.equals("clockwise")) {
            String[][][] temp = new String[6][3][3];

            for (int i = 0; i < 6; i++) {
                for (int j = 0; j < 3; j++) {
                    for (int k = 0; k < 3; k++) {
                        temp[i][j][k] = cube[i][j][k];
                    }
                }
            }
            for (int i = 0; i < 6; i++) {
                cube[i][0][0] = temp[(i + 4) % 6][0][0];
                cube[i][0][1] = temp[(i + 4) % 6][0][1];
                cube[i][0][2] = temp[(i + 4) % 6][0][2];
                cube[i][1][0] = temp[(i + 4) % 6][1][0];
                cube[i][1][2] = temp[(i + 4) % 6][1][2];
                cube[i][2][0] = temp[(i + 4) % 6][2][0];
                cube[i][2][1] = temp[(i + 4) % 6][2][1];
                cube[i][2][2] = temp[(i + 4) % 6][2][2];
            }
        }
    }
}
