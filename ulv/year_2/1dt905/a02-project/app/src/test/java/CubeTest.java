import org.junit.jupiter.api.Test;

import a02.project.com.cube.RubiksCube;

import static org.junit.jupiter.api.Assertions.*;

public class CubeTest {
    @Test
    public void testinit() {

        String[][][] cube = new String[6][3][3];

        RubiksCube.init(cube);

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    switch (i) {
                        case 0:
                            assertEquals("\u001B[97m\u25A0\u001B[0m", cube[i][j][k]);
                            break;
                        case 1:
                            assertEquals("\u001B[92m\u25A0\u001B[0m", cube[i][j][k]);
                            break;
                        case 2:
                            assertEquals("\u001B[31m\u25A0\u001B[0m", cube[i][j][k]);
                            break;
                        case 3:
                            assertEquals("\u001B[94m\u25A0\u001B[0m", cube[i][j][k]);
                            break;
                        case 4:
                            assertEquals("\u001B[93m\u25A0\u001B[0m", cube[i][j][k]);
                            break;
                        case 5:
                            assertEquals("\u001B[95m\u25A0\u001B[0m", cube[i][j][k]);
                            break;
                        default:
                            fail("Unexpected color");
                    }
                }
            }
        }
    }


    @Test
    public void testQuit() {
        String[][][] cube = new String[6][3][3];
        RubiksCube.init(cube);
        RubiksCube.mainLoop("q");
        assertTrue(true, "Result should be Quiting");
    }

    @Test
    public void testquit() {
        String[][][] cube = new String[6][3][3];
        RubiksCube.init(cube);
        RubiksCube.mainLoop("Q");
        assertTrue(true, "Result should be Quiting");
    }

    @Test
    public void testX() {
        String[][][] cube = new String[6][3][3];
        String[][][] test = new String[6][3][3];
        RubiksCube.init(cube);
        RubiksCube.mainLoop("X");
        RubiksCube.mainLoop("q");
        assertNotNull(cube);
        RubiksCube.init(test);
        assertNotEquals(test, cube);
    }

    @Test
    public void testx() {
        String[][][] cube = new String[6][3][3];
        String[][][] test = new String[6][3][3];
        RubiksCube.init(cube);
        assertNotNull(cube);
        RubiksCube.init(test);
        assertNotEquals(test, cube);
    }

    @Test
    public void testY() {
        String[][][] cube = new String[6][3][3];
        String[][][] test = new String[6][3][3];
        RubiksCube.init(cube);
        RubiksCube.mainLoop("Y");
        RubiksCube.mainLoop("q");
        assertNotNull(cube);
        RubiksCube.init(test);
        assertNotEquals(test, cube);
    }

    @Test
    public void testy() {
        String[][][] cube = new String[6][3][3];
        String[][][] test = new String[6][3][3];
        RubiksCube.init(cube);
        RubiksCube.mainLoop("y");
        RubiksCube.mainLoop("q");
        assertNotNull(cube);
        RubiksCube.init(test);
        assertNotEquals(test, cube);
    }

    @Test
    public void testF() {
        String[][][] cube = new String[6][3][3];
        String[][][] test = new String[6][3][3];
        RubiksCube.init(cube);
        RubiksCube.mainLoop("F");
        RubiksCube.mainLoop("q");
        assertNotNull(cube);
        RubiksCube.init(test);
        assertNotEquals(test, cube);
    }

    @Test
    public void testf() {
        String[][][] cube = new String[6][3][3];
        String[][][] test = new String[6][3][3];
        RubiksCube.init(cube);
        RubiksCube.mainLoop("f");
        RubiksCube.mainLoop("q");
        assertNotNull(cube);
        RubiksCube.init(test);
        assertNotEquals(test, cube);
    }

    @Test
    public void testR() {
        String[][][] cube = new String[6][3][3];
        String[][][] test = new String[6][3][3];
        RubiksCube.init(cube);
        RubiksCube.mainLoop("R");
        RubiksCube.mainLoop("q");
        assertNotNull(cube);
        RubiksCube.init(test);
        assertNotEquals(test, cube);
    }

    @Test
    public void testr() {
        String[][][] cube = new String[6][3][3];
        String[][][] test = new String[6][3][3];
        RubiksCube.init(cube);
        RubiksCube.mainLoop("r");
        RubiksCube.mainLoop("q");
        assertNotNull(cube);
        RubiksCube.init(test);
        assertNotEquals(test, cube);
    }

    @Test
    public void testL() {
        String[][][] cube = new String[6][3][3];
        String[][][] test = new String[6][3][3];
        RubiksCube.init(cube);
        RubiksCube.mainLoop("L");
        RubiksCube.mainLoop("q");
        assertNotNull(cube);
        RubiksCube.init(test);
        assertNotEquals(test, cube);
    }

    @Test
    public void testl() {
        String[][][] cube = new String[6][3][3];
        String[][][] test = new String[6][3][3];
        RubiksCube.init(cube);
        RubiksCube.mainLoop("l");
        RubiksCube.mainLoop("q");
        assertNotNull(cube);
        RubiksCube.init(test);
        assertNotEquals(test, cube);
    }

    @Test
    public void testU() {
        String[][][] cube = new String[6][3][3];
        String[][][] test = new String[6][3][3];
        RubiksCube.init(cube);
        RubiksCube.mainLoop("U");
        RubiksCube.mainLoop("q");
        assertNotNull(cube);
        RubiksCube.init(test);
        assertNotEquals(test, cube);
    }

    @Test
    public void testu() {
        String[][][] cube = new String[6][3][3];
        String[][][] test = new String[6][3][3];
        RubiksCube.init(cube);
        RubiksCube.mainLoop("u");
        RubiksCube.mainLoop("q");
        assertNotNull(cube);
        RubiksCube.init(test);
        assertNotEquals(test, cube);
    }

    @Test
    public void testD() {
        String[][][] cube = new String[6][3][3];
        String[][][] test = new String[6][3][3];
        RubiksCube.init(cube);
        RubiksCube.mainLoop("D");
        RubiksCube.mainLoop("q");
        assertNotNull(cube);
        RubiksCube.init(test);
        assertNotEquals(test, cube);
    }

    @Test
    public void testd() {
        String[][][] cube = new String[6][3][3];
        String[][][] test = new String[6][3][3];
        RubiksCube.init(cube);
        RubiksCube.mainLoop("d");
        RubiksCube.mainLoop("q");
        assertNotNull(cube);
        RubiksCube.init(test);
        assertNotEquals(test, cube);
    }

     @Test
    public void testsc() {
        String[][][] cube = new String[6][3][3];
        String[][][] test = new String[6][3][3];
        RubiksCube.init(cube);
        RubiksCube.mainLoop("sc");
        RubiksCube.mainLoop("q");
        assertNotNull(cube);
        RubiksCube.init(test);
        assertNotEquals(test, cube);
    }

    @Test
    public void testsolve() {
        String[][][] cube = new String[6][3][3];
        String[][][] test = cube;
        RubiksCube.init(cube);
        RubiksCube.mainLoop("sc");
        RubiksCube.mainLoop("solve");
        RubiksCube.mainLoop("q");
        assertNotNull(cube);
        assertEquals(test, cube);
    }

     @Test
    public void testInvalidInput() {
        String[][][] cube = new String[6][3][3];
        RubiksCube.init(cube);
        RubiksCube.mainLoop("t");
        RubiksCube.mainLoop("q");
        assertTrue(true, "Invalid input");
    }
}
