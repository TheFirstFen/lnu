package hotel2.com.mid;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

// TODO check if the queries are correct

public class Worker {

    public static boolean checkCreateWorker(Connection connection, String[] loggin) {
        String username = loggin[0];
        String email = loggin[1];
        String number = loggin[2];
        String role = loggin[3];
        String password = loggin[4];
        String hotel = loggin[5];

        try {
            if (!emailExists(connection, email)) {
                System.out.println("Email does not exist");
                createWorker(connection, username, email, number, role, password, hotel);
                return true;
            } else {
                System.out.println("Email already exists");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return false;
    }

    private static void createWorker(Connection connection, String username, String email, String number, String role,
            String password, String hotel) {
        String HashedPassword = hashPassword(password);
        try {
            String sql = "INSERT INTO worker (password, loginName, email, tel, role, hotel, status) VALUES (?, ?, ?, ?, ?, ?, ?)";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);

            preparedStatement.setString(1, HashedPassword);
            preparedStatement.setString(2, username);
            preparedStatement.setString(3, email);
            preparedStatement.setString(4, number);
            preparedStatement.setString(5, role);
            preparedStatement.setString(6, hotel);
            preparedStatement.setInt(7, 0);
            preparedStatement.executeUpdate();

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static String[][] checkALLWorkers(Connection connection, String[] search_for) {
        String search = search_for[0];
        String info = search_for[1];
        if (search.equals("Email")) {
            String[][] workerinfo = viewAllWorkersEmail(connection, info);
            return workerinfo;
        } else if (search.equals("id")) {
            String[][] workerinfo = getWorker(connection, info);
            return workerinfo;
        } else {
            String[][] workerinfo = viewAllWorkers(connection, info);
            return workerinfo;
        }
    }

    private static String[][] viewAllWorkersEmail(Connection connection, String emailSearch) {
        List<String[]> infoList = new ArrayList<>();
        String query = "SELECT * FROM worker WHERE email Like ?";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setString(1, emailSearch + "%");
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                    String userid = Integer.toString(resultSet.getInt("userid"));
                    String loginName = resultSet.getString("loginName");
                    String email = resultSet.getString("email");
                    String tel = resultSet.getString("tel");
                    String role = resultSet.getString("role");
                    String hotel = resultSet.getString("hotel");

                    String[] customerInfo = { userid, loginName, email, tel, role, hotel };
                    infoList.add(customerInfo);
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        String[][] info = new String[infoList.size()][];
        infoList.toArray(info);

        return info;
    }

    private static String[][] viewAllWorkers(Connection connection, String name) {

        String query = "SELECT * FROM worker WHERE loginName LIKE ?";
        List<String[]> infoList = new ArrayList<>();

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setString(1, name + "%");

            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                    String userid = Integer.toString(resultSet.getInt("userid"));
                    String loginName = resultSet.getString("loginName");
                    String email = resultSet.getString("email");
                    String tel = resultSet.getString("tel");
                    String role = resultSet.getString("role");
                    String hotel = resultSet.getString("hotel");

                    String[] customerInfo = { userid, loginName, email, tel, role, hotel };
                    infoList.add(customerInfo);
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        String[][] info = new String[infoList.size()][];
        infoList.toArray(info);
        return info;
    }

    private static String[][] getWorker(Connection connection, String info) {
        int userid = Integer.parseInt(info);
        List<String[]> infoList = new ArrayList<>();
        String query = "SELECT * FROM worker WHERE userid = ?";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, userid);
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                    String userids = Integer.toString(resultSet.getInt("userid"));
                    String loginName = resultSet.getString("loginName");
                    String email = resultSet.getString("email");
                    String tel = resultSet.getString("tel");
                    String role = resultSet.getString("role");
                    String hotel = resultSet.getString("hotel");

                    String[] customerInfo = { info, loginName, email, tel, role, hotel };
                    infoList.add(customerInfo);
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        String[][] infos = new String[infoList.size()][];
        infoList.toArray(infos);

        return infos;
    }

    public static boolean checkUppdateWorker(Connection connection, String[] loggin) {
        String username = loggin[0];
        String email = loggin[1];
        String number = loggin[2];
        String role = loggin[3];
        String password = loggin[4];
        String userid = loggin[5];
        String hotel = loggin[6];

        try {
            if (!emailExists(connection, email)) {
                System.out.println("Email exist");
                uppdateWorker(connection, username, number, email, password, role, userid, hotel);
                return true;
            }
            else {
                int userids = Integer.parseInt(userid);
                if (userids == emailuserid(connection, email)) {
                    uppdateWorker(connection, username, number, email, password, role, userid, hotel);
                    return true;
                }
                else {
                    return false;
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return false;
    }

    private static int emailuserid(Connection connection, String email) {
        int customerid = 0;
        String query = "SELECT userid FROM worker WHERE email = ?";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setString(1, email);
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                if (resultSet.next()) {
                    customerid = resultSet.getInt("userid");
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return customerid;
    }

    private static void uppdateWorker(Connection connection, String username, String number, String email,
            String password, String role, String userId, String hotel) {
        String HashedPassword = hashPassword(password);
        String updateQuery = "UPDATE worker SET loginName = ?, email = ?, tel = ?, role = ?, password = ?, hotel = ? WHERE userid = ?";
        try (PreparedStatement preparedStatement = connection.prepareStatement(updateQuery)) {
            preparedStatement.setString(1, username);
            preparedStatement.setString(2, email);
            preparedStatement.setString(3, number);
            preparedStatement.setString(4, role);
            preparedStatement.setString(5, HashedPassword);
            preparedStatement.setString(6, hotel);
            preparedStatement.setString(7, userId);

            preparedStatement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static boolean checkDeleteWorker(Connection connection, String userid) {
        try {
            if (workerExistst(connection, userid)) {
                int status = 1;
                deleteWorker(connection, userid, status);
                return true;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return false;
    }

    private static void deleteWorker(Connection connection, String userid, int status) {
        String deleteQuery = "update worker set status = ? WHERE userid = ?";
        try (PreparedStatement preparedStatement = connection.prepareStatement(deleteQuery)) {
            preparedStatement.setInt(1, status);
            preparedStatement.setString(2, userid);
            preparedStatement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }

    }

    private static boolean emailExists(Connection connection, String email) throws SQLException {

        String query = "SELECT Count(*) AS count FROM worker WHERE email = ?";
        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setString(1, email);

            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                if (resultSet.next()) {
                    int count = resultSet.getInt("count");
                    return count > 0;
                }
            }
        }
        return false;
    }

    private static boolean workerExistst(Connection connection, String userid) throws SQLException {
        String query = "SELECT Count(*) AS count FROM worker WHERE userid = ?";
        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setString(1, userid);
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                if (resultSet.next()) {
                    int count = resultSet.getInt("count");
                    return count > 0;
                }
            }
        }
        return false;
    }

    private static String hashPassword(String password) {
        try {
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] hash = digest.digest(password.getBytes());

            StringBuilder hexString = new StringBuilder();
            for (byte b : hash) {
                String hex = Integer.toHexString(0xff & b);
                if (hex.length() == 1)
                    hexString.append('0');
                hexString.append(hex);
            }
            return hexString.toString();

        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }
}
