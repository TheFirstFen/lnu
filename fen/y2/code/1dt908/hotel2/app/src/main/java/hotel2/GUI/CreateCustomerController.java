package hotel2.GUI;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.geometry.Pos;
import javafx.scene.control.Button;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.ContentDisplay;
import javafx.scene.control.Label;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.VBox;

import java.util.ArrayList;
import java.util.List;

import hotel2.App;
import hotel2.com.mid.ClientArrayManager;
import hotel2.com.mid.Customer;

public class CreateCustomerController {
    @FXML ScrollPane custScroll;
    @FXML TextField custFirstName;
    @FXML TextField custSurName;
    @FXML TextField custMail;
    @FXML TextField custPhone;
    @FXML ChoiceBox<String> custPayment;
    @FXML TextField NEWcustFirstName;
    @FXML TextField NEWcustSurName;
    @FXML TextField NEWcustMail;
    @FXML TextField NEWcustPhone;
    @FXML ChoiceBox<String> NEWcustPayment;
    @FXML Button ButtonCreate;
    @FXML Button buttonUpdate;
    @FXML TextField SearchField1;
    @FXML ChoiceBox<String> SearchMethod;
    @FXML Label updID;
    @FXML AnchorPane MainAnchorpane;
    List<TextField> inputfields;
    private SceneManager sceneManager;

    public void setManager(SceneManager manager) {
        sceneManager = manager;
    }
    public void setupPage() {
        buttonUpdate.setDisable(true);
        SearchMethod.getItems().addAll("Name", "Email");
        SearchMethod.setStyle("-fx-font-Size: 20px; -fx-text-fill: #ffffff;");
        SearchMethod.setValue("Name");
        inputfields = new ArrayList<>();
        inputfields.add(custFirstName);
        inputfields.add(custSurName);
        inputfields.add(custMail);
        inputfields.add(custPhone);
        custFirstName.requestFocus();
        custFirstName.setOnKeyPressed(event -> handleTabTraversal(event, custSurName));
        custSurName.setOnKeyPressed(event -> handleTabTraversal(event, custMail));
        custMail.setOnKeyPressed(event -> handleTabTraversal(event, custPhone));
        custPhone.setOnKeyPressed(event -> handleTabTraversalBox(event, custPayment));
        custPayment.setOnKeyPressed(event -> handleTabTraversalToButton(event, buttonUpdate));
        buttonUpdate.setOnKeyPressed(event -> handleTabTraversal(event, custFirstName));
    }

    public void setUpPopUp() {
        NEWcustFirstName.requestFocus();
        NEWcustFirstName.setOnKeyPressed(event -> handleTabTraversal(event, NEWcustSurName));
        NEWcustSurName.setOnKeyPressed(event -> handleTabTraversal(event, NEWcustMail));
        NEWcustMail.setOnKeyPressed(event -> handleTabTraversal(event, NEWcustPhone));
        NEWcustPhone.setOnKeyPressed(event -> handleTabTraversalBox(event, NEWcustPayment));
        NEWcustPayment.setOnKeyPressed(event -> handleTabTraversalToButton(event,ButtonCreate));
        ButtonCreate.setOnKeyPressed(event -> handleTabTraversal(event, NEWcustFirstName));
    }
    private void handleTabTraversal(KeyEvent event, TextField nextField) {
        if (event.getCode() == KeyCode.TAB) {
            nextField.requestFocus();
            event.consume();
        } else if (event.getCode() == KeyCode.ENTER && nextField == NEWcustFirstName) {
            createButton();
        }
    }
    private void handleTabTraversalBox(KeyEvent event, ChoiceBox<String> box) {
        if (event.getCode() == KeyCode.TAB) {
            box.requestFocus();
            event.consume();
        }
    }
    private void handleTabTraversalToButton(KeyEvent event, Button nextField) {
        if (event.getCode() == KeyCode.TAB) {
            nextField.requestFocus();
            event.consume();
        }
    }
    
    public void SearchForCustomer() {
        String searchFilter = SearchMethod.getSelectionModel().getSelectedItem();
        String searchWord = SearchField1.getText();
        String[] search = {searchFilter, searchWord};
        String[][] displayArray = null;
        displayArray = Customer.checkForAllCustomers(App.getConn(), search);

        DisplayResults(displayArray);
    }
    private void DisplayResults(String[][] displayArray) {
        VBox buttonBox = new VBox();
        for (int i = 0; i < displayArray.length; i ++) {
            Button tempButton = new Button(displayArray[i][0] + " " + displayArray[i][1] + " | " + displayArray[i][3]);
            tempButton.setPrefWidth(700);
            tempButton.setPrefHeight(50);
            String cid = displayArray[i][2];
            tempButton.getStyleClass().add("temp-button");
            tempButton.getStylesheets().add(getClass().getResource("/css/tempButton.css").toExternalForm());
            tempButton.setAlignment(Pos.BASELINE_LEFT);
            tempButton.setContentDisplay(ContentDisplay.LEFT);
            tempButton.setOnAction(event -> Updatecust(cid));
            buttonBox.getChildren().add(tempButton);
        }
        custScroll.setContent(buttonBox);
    }

    private void Updatecust(String text) {
        buttonUpdate.setDisable(false);

        String[] custInfo = Customer.checkForGetCustomer(App.getConn(), text);
        for (TextField t : inputfields) {
            t.setDisable(false);
        }
        custPayment.setDisable(false);
        custPayment.getItems().setAll("Swish", "Card", "Paypal");
        updID.setText(text);
        custFirstName.setText(custInfo[0]);
        custSurName.setText(custInfo[1]);
        custMail.setText(custInfo[2]);
        custPhone.setText(custInfo[3]);
        custPayment.getSelectionModel().select(custInfo[4]);
    }
    public void updateCustomer() {
        String updFName = custFirstName.getText();
        String updSName = custSurName.getText();
        String updMail = custMail.getText();
        String updPhone = custPhone.getText();
        String updPayment = custPayment.getSelectionModel().getSelectedItem();
        String[] updCustInfo = {updID.getText(), updFName, updSName, updMail, updPhone, updPayment};
        boolean editClient = ClientArrayManager.editClient(App.getConn(), updCustInfo);

        if (editClient) {
            sceneManager.ShowAlert("Godkänd", "Gäst uppdaterad");
        } else {
            sceneManager.ShowAlert("Nekad", "Kunde inte uppdatera gäst");
        }

    }

    public void createNewCustomer() {
        sceneManager.createNewCustomerPopup();
    }
    public void initializePaymentChoices() {
        NEWcustPayment.getItems().setAll("Swish", "Card", "Paypal");
    }
    public void returnButton(ActionEvent event) {
        sceneManager.switchToHomeRoot();
    }

    public void createButton() {
        try {
            String newFName = NEWcustFirstName.getText();
            String newSName = NEWcustSurName.getText();
            String newMail = NEWcustMail.getText();
            String newPhone = NEWcustPhone.getText();
            String newPayment = NEWcustPayment.getSelectionModel().getSelectedItem();
            String[] newCustInfo =  {newFName, newSName, newMail, newPhone, newPayment};
            try {
                Boolean correct = ClientArrayManager.createClient(App.getConn(), newCustInfo);
                if (correct) {
                    sceneManager.ShowAlert("Gäst skapad", "Skapandet lyckades!");
                    sceneManager.closeCurrentPopup();
                } else {
                    throw new Exception("Felaktig info");
                } 
            } catch (java.sql.SQLIntegrityConstraintViolationException e) {
                sceneManager.ShowAlert("Problem vid skapande", "Gäst finns redan eller information saknas.");
            }
        } catch (Exception e) {
            sceneManager.ShowAlert("Problem vid skapande", "Gäst finns redan eller information saknas.");
    }
}
}
