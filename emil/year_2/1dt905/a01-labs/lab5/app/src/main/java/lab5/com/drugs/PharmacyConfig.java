package lab5.com.drugs;

public class PharmacyConfig {
    private String name;
    private String receiptDirectory;

    public PharmacyConfig(String name, String receiptDirectory) {
        this.name = name;
        this.receiptDirectory = receiptDirectory;
    }

    public String getName() {
        return name;
    }

    public String getReceiptDirectory() {
        return receiptDirectory;
    }
}
