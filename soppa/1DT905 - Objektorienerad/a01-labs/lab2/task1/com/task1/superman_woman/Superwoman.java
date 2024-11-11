package task1.com.task1.superman_woman;

import java.time.LocalDateTime;
import java.util.Random;

import task1_2.com.task1_2.person.Person;

public class Superwoman extends Person {
    private String PClass = "Superwoman";
    private String weapon;

    @Override
    public String toString() {
        LocalDateTime now = LocalDateTime.now();
        Integer currentAge = now.getYear() - getBirthYear();
        String namestring = PClass + ": " + getFirstName() + " " + getLastName() +
                            ", born in " + getBirthYear() + " (turning " + currentAge +
                            " this year), has a "+ this.weapon + ". md5: " + super.getId() + "\n";
        return namestring; 
    }

    public void setWeapon(String weapon) {
        this.weapon = weapon;
    }

    public String getWeapon() {
        return this.weapon;
    }

    public Integer useWeapon() {

        Random random = new Random();
        Integer damage = random.nextInt(50);
        return damage;
    }
}
