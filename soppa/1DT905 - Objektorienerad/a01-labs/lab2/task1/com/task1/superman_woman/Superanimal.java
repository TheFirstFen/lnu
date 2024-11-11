package task1.com.task1.superman_woman;

import java.time.LocalDateTime;
import java.util.Random;

public class Superanimal extends Superman {
    private String typeOfAnimal;
    private String PClass = "Superanimal";

    
    @Override
    public String toString() {
        LocalDateTime now = LocalDateTime.now();
        Integer currentAge = now.getYear() - getBirthYear();
        String namestring = PClass + ": The " + this.typeOfAnimal + " " + getFirstName() + " " + getLastName() +
                            ", born in " + getBirthYear() + " (turning " + currentAge +
                            " this year), "+ hatString() + getHat() + ". md5: " + getId() + "\n";
        return namestring; 
    }

    public void setAnimalType(String answer) {
        this.typeOfAnimal = answer;
    }

    
    public String rest() {
        Random random = new Random();
        Integer sleepTime = random.nextInt(10);
        long startTime = System.currentTimeMillis();
        long durationInSeconds = sleepTime * 1000;
        System.out.println("Sleeping...");
        System.out.println("Sleeping...");
        while (System.currentTimeMillis() - startTime < durationInSeconds) {
        }
        return "Slept for " + sleepTime + " seconds";
    }

}
