package com.onlinefarmacy;

import static org.junit.jupiter.api.Assertions.assertNotNull;

import org.junit.jupiter.api.Test;

public class TestInitializeDrugs {

    @Test
    public void testCreation() {
        InitializeDrugs.setDrugs();
        assertNotNull(InitializeDrugs.getAlvedon());
        assertNotNull(InitializeDrugs.getIpren());
        assertNotNull(InitializeDrugs.getDesloratadine());
        assertNotNull(InitializeDrugs.getBrikanyl());
        assertNotNull(InitializeDrugs.getMorifin());
    }


}
