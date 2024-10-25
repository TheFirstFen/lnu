package hotel2.com.mid;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

import java.util.ArrayList;

// TODO Check if the queries are correct

public class Customer {

    public static boolean checkForUppdate(Connection connection, String[] customer) {
        int customerid = Integer.parseInt(customer[0]);
        String fName = customer[1];
        String lName = customer[2];
        String email = customer[3];
        String number = customer[4];
        String payMethod = customer[5];

        try{
            if (!emailExists(connection, email)) {
                updateCustomer(connection, customerid, fName, lName, number, email, payMethod);
                return true;
            }
            else {
                if (customerid == emailCustomerid(connection, email)) {
                    updateCustomer(connection, customerid, fName, lName, number, email, payMethod);
                    return true;
                }
                else {
                    return false;
                }
            }
        }catch (SQLException e){
            e.printStackTrace();
        }
        return false;
    }

    private static void updateCustomer(Connection connection, int customerid, String fname, String lName, String number, String email, String payMethod) throws SQLException {
        try {
            String updatequery = "UPDATE customer SET fName = ?, lName = ?, tel = ?, email = ?, paymentmethod = ? WHERE customerid = ?";
            try (PreparedStatement preparedStatement = connection.prepareStatement(updatequery)) {
                preparedStatement.setString(1, fname);
                preparedStatement.setString(2, lName);
                preparedStatement.setString(3, number);
                preparedStatement.setString(4, email);
                preparedStatement.setString(5, payMethod);
                preparedStatement.setInt(6, customerid);
                preparedStatement.executeUpdate();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static boolean checkForCreation(Connection connection, String[] customer) {
        String fName = customer[0];
        String lName = customer[1];
        String email = customer[2];
        String number = customer[3];
        String payMethod = customer[4];
        try {
            if (!emailExists(connection, email)) {
                System.out.println("Email does not exist");
                create(connection, fName, lName, number, email, payMethod);
                return true;
            }
            else {
                System.out.println("Email already exists");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return false;
    }

    private static void create(Connection connection, String fName, String lName, String number, String email, String payMethod) throws SQLException {
        try {
            String insertquery = "INSERT INTO customer (fName, lName, tel, email, paymentmethod) VALUES (?, ?, ?, ?, ?)";
            try (PreparedStatement preparedStatement = connection.prepareStatement(insertquery)) {
                preparedStatement.setString(1, fName);
                preparedStatement.setString(2, lName);
                preparedStatement.setString(3, number);
                preparedStatement.setString(4, email);
                preparedStatement.setString(5, payMethod);

                preparedStatement.executeUpdate();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }  
    }

    public static String[][] checkForAllCustomers(Connection connection, String[] search_for) {
        String search = search_for[0];
        String info = search_for[1];
        if (search.equals("Email")) {
            String[][] customerinfo = getCustomerEmail(connection, info);
            return customerinfo;
        }
        else{
            String[][] customerinfo = getCustomerName(connection, info);
            return customerinfo;
        }
        //String[][] customerinfo = viewAllCustomer(connection);
        //return customerinfo;
    }

    private static String[][] viewAllCustomer(Connection connection) {
        String query = "SELECT * FROM customer";
        List<String[]> infoList = new ArrayList<>();

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                // Assuming you want to retrieve the first name and last name
                    String firstName = resultSet.getString("fName");
                    String lastName = resultSet.getString("lName");
                    String customeremail = resultSet.getString("email");
                    String customerid = Integer.toString(resultSet.getInt("customerid"));
                // Add the retrieved data to the result list
                    String[] customerInfo = {firstName, lastName, customerid, customeremail};
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

    private static String[][] getCustomerEmail(Connection connection, String email) {
        List<String[]> infoList = new ArrayList<>();
        String query = "SELECT * FROM customer WHERE email Like ?";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setString(1, email + "%");
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                
                    String firstName = resultSet.getString("fName");
                    String lastName = resultSet.getString("lName");
                    String customeremail = resultSet.getString("email");
                    String customerid = Integer.toString(resultSet.getInt("customerid"));
                
                    String[] customerInfo = {firstName, lastName, customerid, customeremail};
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

    private static String[][] getCustomerName(Connection connection, String name) {
        String[] result = name.split(" ");
        String fName = result[0];
        String lName = (result.length > 1) ?  result [1] : result[0];
    
        String query = "SELECT * FROM customer WHERE fName LIKE ? OR lName LIKE ?";
        List<String[]> infoList = new ArrayList<>();
    
        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setString(1, fName + "%");
            preparedStatement.setString(2, lName + "%");
    
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                    // Assuming you want to retrieve the first name and last name
                    String firstName = resultSet.getString("fName");
                    String lastName = resultSet.getString("lName");
                    String customeremail = resultSet.getString("email");
                    String customerid = Integer.toString(resultSet.getInt("customerid"));
    
                    // Add the retrieved data to the result list
                    String[] customerInfo = {firstName, lastName, customerid, customeremail};
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

    public static String[] checkForGetCustomer(Connection connection, String userid) {
        int customerid = Integer.parseInt(userid);

        String[] customerinfo = getcustomer(connection, customerid);
        return customerinfo;
    }

    private static String[] getcustomer(Connection connection, int userid) {
        String[] info = new String[5];
        String query = "SELECT * FROM customer WHERE customerid = ?";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query, userid)) {
            preparedStatement.setInt(1, userid);
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                
                    String firstName = resultSet.getString("fName");
                    String lastName = resultSet.getString("lName");
                    String email = resultSet.getString("email");
                    String phone = resultSet.getString("tel");
                    String payment = resultSet.getString("paymentmethod");
                
                    String[] customerInfo = {firstName, lastName, email, phone, payment};
                    info = customerInfo;
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return info;
    }

    public static String[] latestCustomer(Connection connection) {
        String[] info = new String[6];
        String query = "SELECT * FROM customer ORDER BY customerid DESC LIMIT 1";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)){
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                    String firstName = resultSet.getString("fName");
                    String lastName = resultSet.getString("lName");
                    String email = resultSet.getString("email");
                    String phone = resultSet.getString("tel");
                    String payment = resultSet.getString("paymentmethod");
                    String id = Integer.toString(resultSet.getInt("customerid"));
                
                    String[] customerInfo = {firstName, lastName, email, phone, payment, id};
                    info = customerInfo;
                }
            }
            
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return info;
    }

    private static boolean emailExists(Connection connection, String email) throws SQLException {

        String query = "SELECT Count(*) AS count FROM customer WHERE email = ?";
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

    private static int emailCustomerid(Connection connection, String email) {
        int customerid = 0;
        String query = "SELECT customerid FROM customer WHERE email = ?";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setString(1, email);
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                if (resultSet.next()) {
                    customerid = resultSet.getInt("customerid");
                }
            }
        }
        catch (SQLException e) {
            e.printStackTrace();
        }
        return customerid;
    }
}