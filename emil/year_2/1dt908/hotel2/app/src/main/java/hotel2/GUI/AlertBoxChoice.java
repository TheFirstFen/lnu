package hotel2.GUI;

import hotel2.App;
import hotel2.com.mid.Booking;
import javafx.fxml.FXML;
import javafx.scene.control.Label;

public class AlertBoxChoice {
    private SceneManager sceneManager;

    @FXML Label titleLabel;
    @FXML Label descriptionLabel;
    private String id;
    private Boolean fromM;
    private Boolean delb;

    public void setManager(SceneManager manager) {
        sceneManager = manager;
    }

    public void setup(String title, String desc, String i, Boolean fromMain, Boolean delBook) {
        id = i;
        fromM = fromMain;
        delb = delBook;
        titleLabel.setText(title);
        descriptionLabel.setText(desc);
    }
    public void moveOnButton() {
        if (fromM) {
            sceneManager.switchToHandleBookRoot(null, id);
        } else if (delb) {
            String[] i = {id};
            if (Booking.cancelBooking(App.getConn(), i)) {
                sceneManager.closeCurrentPopup();
                sceneManager.ShowAlert("Radering lyckades", "Bokning " + id + " är borttagen.");
                sceneManager.switchToHandleBookRoot(null, null);
            } else {
                sceneManager.ShowAlert("Radering misslyckades", "Bokning " + id + " är inte borttagen.");
            }
        } else {
            sceneManager.switchToHandleBookRoot(id, null);
        }
        sceneManager.closeCurrentPopup();
    }

    public void closeAlertButton() {
        sceneManager.closeCurrentPopup();
    }
}
