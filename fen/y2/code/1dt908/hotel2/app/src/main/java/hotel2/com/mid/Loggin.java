package hotel2.com.mid;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Loggin {
    public static String[] main(Connection connection, String[] loggin) {
        String email = loggin[0];
        String password = loggin[1];

        System.out.println("Welcome to Hotel2 loggin");
        String[] info = new String[3];
        
        if (isValidUser(connection, email, password, info)) {
            System.out.println("Login successful");
            info[0] = "1";
        } else {
            System.out.println("Wrong login info");
            info[0] = "0";
        }
        return info;
    }
    
    private static boolean isValidUser(Connection connection, String email, String password, String[] info) {
        String hashedPassword = hashPassword(password);

        // after userid put in ", role"
        String query = "SELECT * FROM worker WHERE loginName = ? AND password = ? AND status = ?";
        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setString(1, email);
            preparedStatement.setString(2, hashedPassword);
            preparedStatement.setInt(3, 0);

            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                if (resultSet.next()) {
                    info[1] = Integer.toString(resultSet.getInt("userid"));
                    info[2] = resultSet.getString("role");
                    return true;
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return false;
    }

    private static String hashPassword(String password) {
        try {MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] hash = digest.digest(password.getBytes());

            StringBuilder hexString = new StringBuilder();
            for (byte b : hash) {
                String hex = Integer.toHexString(0xff & b);
                if (hex.length() == 1) hexString.append('0');
                    hexString.append(hex);
            }
            return hexString.toString();
        
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }
}
