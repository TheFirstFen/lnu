package hotel2.com.mid;

import java.util.regex.Pattern;
import java.sql.Connection;

public class RoomArrayManger {
    public boolean createNewRoom(Connection Connection, String[] roomData) {
        
        if (roomData.length != 5) {
            return false;
        }

        for (String data : roomData) {
            if (data == null || data.trim().isEmpty()) {
                return false;
            }
        }

        if (!isNumerical(roomData[0])) {
            //throw new IllegalArgumentException("Invalid roomNr");
            return false;
        }

        if (!isNumerical(roomData[1])) {
            //throw new IllegalArgumentException("Invalid roomSize");
            return false;
        }
        if (!containsOnlyLetters(roomData[2])) {
            //throw new IllegalArgumentException("Invalid roomType");
            return false;
        }
        
        return Room.checkCreateRoom(Connection, roomData);
    }

    public boolean updateExistingRoom(Connection Connection, String[] roomData) {
        
        if (roomData.length != 5) {
            return false;
        }

        for (String data : roomData) {
            if (data == null || data.trim().isEmpty()) {
                return false;
            }
        }

        if (!isNumerical(roomData[0])) {
            //throw new IllegalArgumentException("Invalid roomNr");
            return false;
        }

        if (!isNumerical(roomData[1])) {
            //throw new IllegalArgumentException("Invalid roomSize");
            return false;
        }
        if (!containsOnlyLetters(roomData[2])) {
            //throw new IllegalArgumentException("Invalid roomType");
            return false;
        }
        
        return Room.updateRoom(Connection, roomData);
    }

    public static boolean isNumerical(String input) {
        String regex = "[0-9]+";
        Pattern pattern = Pattern.compile(regex);
        return pattern.matcher(input).matches();
    }

    public boolean containsOnlyLetters(String name) {
        // Only letters are allowed in the name
        return name.matches("^[a-zA-ZéêüåäöÅÖÄøÆæ]+$");
    }
}
