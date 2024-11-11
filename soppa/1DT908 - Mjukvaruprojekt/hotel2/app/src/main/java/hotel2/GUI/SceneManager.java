package hotel2.GUI;

import javafx.application.Platform;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.layout.StackPane;
import javafx.stage.Modality;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import javafx.scene.layout.AnchorPane;

import java.time.LocalDate;

public class SceneManager {
    private Stage stage;
    private StackPane rootPane;

    private Parent loginRoot;
    private Parent homeRoot;
    private Parent handleCustomerRoot;
    private Parent createBookingRoot;
    private Parent adminRoot;
    private Parent editRoot;
    private Parent handleBookRoot;
    private Parent handleRoomRoot;
    private Scene scene;

    private HomePageController homePageController;
    private LoginController loginControlle;

    private String[] sceneLoginInfo;
    private Stage currentPopup;

    private String[] currentBookingInfo = new String[10];
    private String[] displayInfo = new String[10];
    private LocalDate[] dates = new LocalDate[2];
    private List<String[]> displayRooms = new ArrayList<>();
    private AnchorPane previewPane;
    private String[] checkInfo = new String[20];
    private String[][] CurrentRoomBookings;
    private String rid;
    private List<String> calenderDates = new ArrayList<>();

    public SceneManager(Stage stage) {
        this.stage = stage;
        this.rootPane = new StackPane();
        dates[0] = LocalDate.now();
        dates[1] = LocalDate.now().plusDays(1);
        initializeScene();
    }

    private void initializeScene() {
        scene = new Scene(rootPane);
        stage.setScene(scene);
        stage.setFullScreen(true);
    }
    public void setCalDat(String dat) {
        calenderDates.add(dat);
    }
    public void clearCalDat() {
        calenderDates.clear();
    }
    public List<String> getCalDat() {
        return calenderDates;
    }

    public void setrid(String val) {
        rid = val;
    }
    public String getrid() {
        return rid;
    }
    public void setCurrentRoomBookings(String[][] bookings) {
        CurrentRoomBookings = new String[bookings.length + 10][];
        CurrentRoomBookings = bookings;
    }
    public String[][] getCurrentRoomBookings() {
        if (CurrentRoomBookings != null) {
            if (CurrentRoomBookings.length > 0) {
                return CurrentRoomBookings;
            }
        }
        return null;
    }


    
    public String[] getCurrentCheckInfo() {
        return checkInfo;
    }


    public String[] getLoginInfo() {
        return sceneLoginInfo;
    }
    public LocalDate[] getDate() {
        return dates;
    }


    public String[] getCurrentBookingInfo() {
        return currentBookingInfo;
    }

    public void setCurrentBookingInfo(String[] currentBookingInfoi) {
        currentBookingInfo = currentBookingInfoi;
    }

    public String[] getDisplayInfo() {
        return displayInfo;
    }

    public void setDisplayInfo(String[] displayInfoi) {
        displayInfo = displayInfoi;
    }

    public List<String[]> getDisplayRooms() {
        return displayRooms;
    }

    public void setDisplayRooms(List<String[]> displayRoomsi) {
        displayRooms = displayRoomsi;
    }

    public AnchorPane getPane() {
        return previewPane;
    }

    public void setPane(AnchorPane pane) {
        previewPane = pane;
    }

    public void switchToLoginRoot() {
        Platform.runLater(() -> {
            FXMLLoader loginLoader = new FXMLLoader(getClass().getResource("/login_screen_hotel2.fxml"));
            try {
                loginRoot = loginLoader.load();
            } catch (Exception e) {
                System.err.println(e);
            }
            LoginController loginController = loginLoader.getController();
            loginController.setManager(this);
            loginControlle = loginController;
            rootPane.getChildren().clear();
            rootPane.getChildren().add(loginRoot);
            stage.setTitle("Hotel2 - Login");
            loginControlle.setFocus();
            stage.show();
        });
    }

    public void switchToCreateBookingRoot(Boolean setup) {
        Platform.runLater(() -> {
            FXMLLoader createBookingLoader = new FXMLLoader(getClass().getResource("/CreateBooking.fxml"));
            try {
                createBookingRoot = createBookingLoader.load();
            } catch (IOException e) {
                System.err.println(e);
            }
            createBookingController createBookingController1 = createBookingLoader.getController();
            createBookingController1.setManager(this);
            createBookingController1.setup(setup);
            rootPane.getChildren().clear();
            rootPane.getChildren().add(createBookingRoot);
            stage.setTitle("Hotel2 - Login");
            loginControlle.setFocus();
            stage.show();
        });
    }

    public void resetLoginPage() {
        loginControlle.reset();
    }

    public void switchToHomeRoot() {
        Platform.runLater(() -> {

            FXMLLoader homeLoader = new FXMLLoader(getClass().getResource("/main_page.fxml"));
            try {
                homeRoot = homeLoader.load();
            } catch (Exception e) {
                System.err.println(e);
            }
            HomePageController homeController = homeLoader.getController();
            homeController.setManager(this);
            homePageController = homeController;
            rootPane.getChildren().clear();
            rootPane.getChildren().add(homeRoot);
            homePageController.launch();
            stage.setTitle("Hotel2 - Home");
            stage.show();
        });
    }

    public void switchToEditProfileRoot() {
        Platform.runLater(() -> {

            FXMLLoader editLoader = new FXMLLoader(getClass().getResource("/EditProfile.fxml"));
            try {
                editRoot = editLoader.load();
            } catch (Exception e) {
                System.err.println(e);
            }
            EditProfileController editController = editLoader.getController();
            editController.setManager(this);
            rootPane.getChildren().clear();
            rootPane.getChildren().add(editRoot);
            homePageController.launch();
            stage.setTitle("Hotel2 - Edit Profile");
            stage.show();
        });
    }

    public void switchToAdminPageRoot() {
        Platform.runLater(() -> {

            FXMLLoader adminLoader = new FXMLLoader(getClass().getResource("/AdminPage.fxml"));
            try {
                adminRoot = adminLoader.load();
            } catch (Exception e) {
                System.err.println(e);
            }
            AdminController adminController = adminLoader.getController();
            adminController.setManager(this);
            rootPane.getChildren().clear();
            rootPane.getChildren().add(adminRoot);
            stage.setTitle("Hotel2 - Admin");
            stage.show();
        });
    }

    public void switchToHandleCustRoot() {
        Platform.runLater(() -> {
            FXMLLoader handleCustomerLoader = new FXMLLoader(getClass().getResource("/KundhanteringNY.fxml"));
            try {
                handleCustomerRoot = handleCustomerLoader.load();
            } catch (IOException e) {
                System.err.println(e);
            }
            CreateCustomerController handleCustomerController = handleCustomerLoader.getController();
            handleCustomerController.setManager(this);
            handleCustomerController.setupPage();

            rootPane.getChildren().clear();

            if (handleCustomerRoot != null) {
                rootPane.getChildren().add(handleCustomerRoot);
                stage.setTitle("Hotel2 - custPage");
                stage.show();
            } else {
            }
        });
    }
    public void switchToHandleBookRoot(String bid, String date) {
        Platform.runLater(() -> {
            FXMLLoader handleBookLoader = new FXMLLoader(getClass().getResource("/Bokningshantering.fxml"));
            try {
                handleBookRoot = handleBookLoader.load();
            } catch (IOException e) {
                System.err.println(e);
            }
            BookingController handleBookController = handleBookLoader.getController();
            handleBookController.setManager(this);
            handleBookController.setupPage();
            if (bid != null) {
                handleBookController.fromCalender(bid);
            }
            if (date != null) {
                handleBookController.fromMain(date);
            }

            rootPane.getChildren().clear();

            if (handleBookRoot != null) {
                rootPane.getChildren().add(handleBookRoot);
                stage.setTitle("Hotel2 - custPage");
                stage.show();
            }
        });
    }
    public void switchToHandleRoomRoot(String rid) {
        Platform.runLater(() -> {
            FXMLLoader handleRoomLoader = new FXMLLoader(getClass().getResource("/Rumshantering.fxml"));
            try {
                handleRoomRoot = handleRoomLoader.load();
            } catch (IOException e) {
                System.err.println(e);
            }
            RoomController handleRoomController = handleRoomLoader.getController();
            handleRoomController.setManager(this);
            handleRoomController.setupPage();
            if (rid != null) {
                handleRoomController.setUpSearch(rid);
            }

            rootPane.getChildren().clear();

            if (handleRoomRoot != null) {
                rootPane.getChildren().add(handleRoomRoot);
                stage.setTitle("Hotel2 - roomPage");
                stage.show();
            }
        });
    }

    public void createNewCustomerPopup() {
        try {
            Stage popupStage = new Stage();
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/createCustomerWindow.fxml"));
            Parent root = loader.load();
            CreateCustomerController controller = loader.getController();
            controller.initializePaymentChoices();
            controller.setManager(this);

            popupStage.setTitle("Skapar ny kund");
            popupStage.initModality(Modality.APPLICATION_MODAL);
            popupStage.initOwner(stage); // Set the main stage as the owner
            popupStage.setScene(new Scene(root));
            controller.setUpPopUp();
            currentPopup = popupStage;
            popupStage.showAndWait();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void editProfilePopUp() {
        try {
            Stage popupStage = new Stage();
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/EditProfile.fxml"));
            Parent root = loader.load();
            EditProfileController controller = loader.getController();
            controller.setManager(this);
            controller.init();
            popupStage.setTitle("Redigera användare");
            popupStage.initModality(Modality.APPLICATION_MODAL);
            popupStage.initOwner(stage); // Set the main stage as the owner
            popupStage.setScene(new Scene(root));
            popupStage.showAndWait();
            popupStage.setResizable(false);
            currentPopup = popupStage;
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void closeCurrentPopup() {
        if (currentPopup != null) {
            currentPopup.close();
        } else {
            System.err.println("Fel ingen popup finns");
        }
    }

    public void createNewBookingPopup() {
        try {
            Stage popupStage = new Stage();
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/PreviewPop.fxml"));
            Parent root = loader.load();
            createBookingController controller = loader.getController();
            controller.setManager(this);
            controller.createBookingButton();

            popupStage.setTitle("Förhandsgranskning av bokning");
            popupStage.initModality(Modality.APPLICATION_MODAL);
            popupStage.initOwner(stage); // Set the main stage as the owner
            popupStage.setScene(new Scene(root));
            currentPopup = popupStage;
            popupStage.showAndWait();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
    public void checkInPopup(String[] info) {
        try {
            Stage popupStage = new Stage();
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/CheckInPop.fxml"));
            Parent root = loader.load();
            HomePageController controller = loader.getController();
            controller.setManager(this);
            popupStage.setTitle("Checka in");
            popupStage.initModality(Modality.APPLICATION_MODAL);
            popupStage.initOwner(stage); // Set the main stage as the owner
            popupStage.setScene(new Scene(root));
            controller.setUpCheck(info);
            currentPopup = popupStage;
            popupStage.showAndWait();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public void checkOutPopup(String[] info) {
        try {
            Stage popupStage = new Stage();
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/CheckOutPop.fxml"));
            Parent root = loader.load();
            HomePageController controller = loader.getController();
            controller.setManager(this);
            popupStage.setTitle("Checka ut");
            popupStage.initModality(Modality.APPLICATION_MODAL);
            popupStage.initOwner(stage); // Set the main stage as the owner
            popupStage.setScene(new Scene(root));
            controller.setUpCheck(info);
            currentPopup = popupStage;
            popupStage.showAndWait();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public void createBookingCustomerPopup() {
        try {
            Stage popupStage = new Stage();
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/ChooseCustomerPopup.fxml"));
            Parent root = loader.load();
            createBookingController controller = loader.getController();
            controller.setManager(this);
            controller.setUpPopUp();

            popupStage.setTitle("För");
            popupStage.initModality(Modality.APPLICATION_MODAL);
            popupStage.initOwner(stage);
            popupStage.setScene(new Scene(root));
            currentPopup = popupStage;
            popupStage.showAndWait();
            switchToCreateBookingRoot(false);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void createBookingRoomPopup() {
        try {
            Stage popupStage = new Stage();
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/ChooseRoomPopUp.fxml"));
            Parent root = loader.load();
            createBookingController controller = loader.getController();
            controller.setManager(this);
            controller.setUpPopUpRoom();

            popupStage.setTitle("Välj rum");
            popupStage.initModality(Modality.APPLICATION_MODAL);
            popupStage.initOwner(stage); // Set the main stage as the owner
            popupStage.setScene(new Scene(root));
            currentPopup = popupStage;
            popupStage.showAndWait();
            switchToCreateBookingRoot(false);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public void ShowAlert(String title, String desc) {
        try {
            Stage popupStage = new Stage();
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/AlertBoxPop.fxml"));
            Parent root = loader.load();
            AlertController controller = loader.getController();
            controller.setManager(this);
            controller.setup(title, desc);

            popupStage.initModality(Modality.APPLICATION_MODAL);
            popupStage.initOwner(stage); // Set the main stage as the owner
            popupStage.setScene(new Scene(root));
            currentPopup = popupStage;
            popupStage.showAndWait();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public void ShowAlertChoice(String title, String desc, String id, Boolean b, Boolean d) {
        try {
            Stage popupStage = new Stage();
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/AlertBoxRoom.fxml"));
            Parent root = loader.load();
            AlertBoxChoice controller = loader.getController();
            controller.setManager(this);
            controller.setup(title, desc, id, b, d);

            popupStage.initModality(Modality.APPLICATION_MODAL);
            popupStage.initOwner(stage); // Set the main stage as the owner
            popupStage.setScene(new Scene(root));
            currentPopup = popupStage;
            popupStage.showAndWait();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public void ShowAlertChoiceB(String title, String desc, String id) {
        try {
            Stage popupStage = new Stage();
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/AlertBoxBook.fxml"));
            Parent root = loader.load();
            AlertBoxChoiceB controller = loader.getController();
            controller.setManager(this);
            controller.setup(title, desc, id);

            popupStage.initModality(Modality.APPLICATION_MODAL);
            popupStage.initOwner(stage); // Set the main stage as the owner
            popupStage.setScene(new Scene(root));
            currentPopup = popupStage;
            popupStage.showAndWait();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    public Stage getStage() {
        return stage;
    }

    public void setInfo(String[] info) {
        sceneLoginInfo = info;
    }
}