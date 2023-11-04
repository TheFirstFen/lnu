package task3.com.sb224sc.classes.menu;

import org.junit.jupiter.api.*;

import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.Scanner;

import static org.junit.jupiter.api.Assertions.*;

class MenuTest {
    private Menu menu;

    @BeforeEach
    void setUp() {
        menu = new Menu();
    }

    @Test
    void testPrintMenuOptions() {
        InputStream originalIn = System.in;
        System.setIn(new ByteArrayInputStream("1\n".getBytes()));
        try {
            menu.printMenuOptions();
            Scanner sc = new Scanner(System.in);
            assertEquals(1, sc.nextInt());
            sc.close();
        } finally {
            System.setIn(originalIn);
        }
    }

    @Test
    void testGetIntInputWithInvalidInputThenValidInput() {
        InputStream originalIn = System.in;
        System.setIn(new ByteArrayInputStream("invalid\n42\n".getBytes()));
        try {
            Scanner sc = new Scanner(System.in);
            int input = menu.getIntInput(sc);
            assertEquals(42, input);
        } finally {
            System.setIn(originalIn);
        }
    }

    @Test
    void testGetIntInputWithValidInput() {
        InputStream originalIn = System.in;
        System.setIn(new ByteArrayInputStream("42\n".getBytes()));
        try {
            Scanner sc = new Scanner(System.in);
            int input = menu.getIntInput(sc);
            assertEquals(42, input);
        } finally {
            System.setIn(originalIn);
        }
    }

    @Test
    void testMenuLoopWithInvalidInputThenValidInput() {
        InputStream originalIn = System.in;
        System.setIn(new ByteArrayInputStream("invalid\n1\n2\n3\n4\n5\n6\n7\n8\n".getBytes()));
        try {
            assertDoesNotThrow(() -> menu.menuLoop());
        } finally {
            System.setIn(originalIn);
        }
    }

    @Test
    void testMenuLoopWithValidInput() {
        InputStream originalIn = System.in;
        System.setIn(new ByteArrayInputStream("1\n2\n2\n3\n1\n2\n2\n4\n1\n5\n6\n7\n8\n".getBytes()));
        try {
            assertDoesNotThrow(() -> menu.menuLoop());
        } finally {
            System.setIn(originalIn);
        }
    }
}
