package com.onlinefarmacy;

public class InitializeDrugs {
    private static Drug alvedon;
    private static Drug ipren;
    private static Drug desloratadine;
    private static Drug brikanyl;
    private static Drug morifin;

    public static void setDrugs() {
        alvedon = new Drug();
        ipren = new Drug();
        desloratadine = new Drug();
        brikanyl = new Drug();
        morifin = new Drug();
        alvedon.setDrug("Alvedon", 20.0);
        ipren.setDrug("Ipren", 35.0);
        desloratadine.setDrug("Desloratadine", 50.0);
        brikanyl.setDrug("Brikanyl", 55.0);
        morifin.setDrug("Morifin", 80.0);
        ReceiptHandling.setDrugNamesList(alvedon, ipren, desloratadine, brikanyl, morifin);
        ReceiptHandling.setDrugPriceList(alvedon, ipren, desloratadine, brikanyl, morifin);
    }

    public static Drug getAlvedon() {
        return alvedon;
    }
    public static Drug getIpren() {
        return ipren;
    }
    public static Drug getDesloratadine() {
        return desloratadine;
    }
    public static Drug getBrikanyl() {
        return brikanyl;
    }
    public static Drug getMorifin() {
        return morifin;
    }
}
