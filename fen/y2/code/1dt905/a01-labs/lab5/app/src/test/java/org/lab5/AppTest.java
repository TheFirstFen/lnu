package org.lab5;

import static org.junit.jupiter.api.Assertions.assertNotNull;

import org.junit.jupiter.api.Test;
import org.lab5.com.sb224sc.classes.Main;

class AppTest {
    @Test
    void testApp() {
        Main app = new Main();

        assertNotNull(app);
    }
}
