package task1.com.task1.superman_woman;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

import task1_2.com.task1_2.person.Person;

public class Superman extends Person {
    private String PClass = "Superman";
    private Boolean hasHat = false;
    private String typeOfHat;

    @Override
    public String toString() {
        LocalDateTime now = LocalDateTime.now();
        Integer currentAge = now.getYear() - getBirthYear();
        String namestring = PClass + ": " + getFirstName() + " " + getLastName() +
                            ", born in " + getBirthYear() + " (turning " + currentAge +
                            " this year), "+ hatString() + this.typeOfHat + ". md5: " + super.getId() + "\n";
        return namestring; 
    }
    public void changeHatStatus() {
        if (this.hasHat.equals(false)) {
            this.typeOfHat = "Top hat";
            this.hasHat = true;
        } else {
            this.typeOfHat = "";
            this.hasHat = false;
        }
    }
    public void setHat(String answer) {
        if (answer.equalsIgnoreCase("true")) {
            this.hasHat = true;
        }
    }

    public void setHatType (String typeOfHat) {
        this.typeOfHat = typeOfHat;
    }

    public String getHat() {
        return this.typeOfHat;
    }

    public String changeToRandomHat() {
        ArrayList<String> hats = new ArrayList<>(Arrays.asList("Top hat", "Baseball cap", "Fedora", "Beanie", "Cowboy hat"));
        List<String> hatTypes = new ArrayList<>(hats);
        Random random = new Random();
        Integer numHat = random.nextInt(0, 5);
        this.typeOfHat = hatTypes.get(numHat);
        return hatTypes.get(numHat);

    }

    public void changeHat(String hatName) {
        this.typeOfHat = hatName;
    }

    public String hatString() {
        if (hasHat == true) {
            return "has a hat of type ";
        } else {
            return "does not have a hat on";
        }
    }
}
