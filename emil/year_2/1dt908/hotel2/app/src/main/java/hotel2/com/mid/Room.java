package hotel2.com.mid;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

import java.util.ArrayList;

public class Room {
    public static boolean checkCreateRoom(Connection connection, String[] room) {
        int roomnr = Integer.parseInt(room[0]);
        int roomsize = Integer.parseInt(room[1]);
        String roomtype = room[2];
        float price = Float.parseFloat(room[3]);
        String hotel = room[4];

        try {
            if (!roomnrExists(connection, roomnr)) {
                createRoom(connection, roomnr, roomsize, roomtype, price, hotel);
                return true;
            } else {
                return false;
            }
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }

    private static void createRoom(Connection connection, int roomnr, int roomsize, String roomtype, float price,
            String hotel) throws SQLException {
        String query = "insert into room (roomnr, roomsize, roomtype, price, hotel, status) values (?, ?, ?, ?, ?, ?)";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, roomnr);
            preparedStatement.setInt(2, roomsize);
            preparedStatement.setString(3, roomtype);
            preparedStatement.setFloat(4, price);
            preparedStatement.setString(5, hotel);
            preparedStatement.setInt(6, 0);
            preparedStatement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static String[][] getRooms(Connection connection, String[] search_for) {
        String search = search_for[0];
        String info = search_for[1];
        if (info.equals("")) {
            String[][] roominfo = getAllRooms(connection);
            return roominfo;
        } else if (search.equals("Room Number")) {
            String[][] roominfo = getRoomNr(connection, info);
            return roominfo;
        } else if (search.equals("Room Size")) {
            String[][] roominfo = getRoomSize(connection, info);
            return roominfo;
        } else if (search.equals("Room Type")) {
            String[][] roominfo = getRoomType(connection, info);
            return roominfo;
        } else if (search.equals("Room ID")) {
            String[][] roominfo = getRoomId(connection, info);
            return roominfo;
        } else {
            System.out.println("Wrong search word");
            return null;
        }
    }

    private static String[][] getRoomNr(Connection connection, String info) {

        int roomnr = Integer.parseInt(info);
        List<String[]> infoList = new ArrayList<>();
        String query = "SELECT * FROM room WHERE roomnr = ? and status = 0";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, roomnr);
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {

                    String roomid = Integer.toString(resultSet.getInt("roomid"));
                    String size = resultSet.getString("roomsize");
                    String type = resultSet.getString("roomtype");
                    String price = Float.toString(resultSet.getFloat("price"));
                    String hotel = resultSet.getString("hotel");
                    String status = Integer.toString(resultSet.getInt("status"));
                    String[] roominformation = { roomid, info, size, type, price, hotel, status };
                    infoList.add(roominformation);
                }
            }
        } catch (Exception e) {
            return null;
        }
        String[][] roominfo = new String[infoList.size()][];
        infoList.toArray(roominfo);

        return roominfo;
    }

    private static String[][] getRoomSize(Connection connection, String info) {
        int roomsize = Integer.parseInt(info);
        List<String[]> infoList = new ArrayList<>();
        String query = "SELECT * FROM room WHERE roomsize <= ? and status = 0";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, roomsize);
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {

                    String roomnr = Integer.toString(resultSet.getInt("roomnr"));
                    String type = resultSet.getString("roomtype");
                    String roomSize = resultSet.getString("roomsize");
                    String roomid = Integer.toString(resultSet.getInt("roomid"));
                    String price = Float.toString(resultSet.getFloat("price"));
                    String hotel = resultSet.getString("hotel");
                    String status = Integer.toString(resultSet.getInt("status"));

                    String[] roominformation = { roomid, roomnr, roomSize, type, price, hotel, status };
                    infoList.add(roominformation);
                }
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
        String[][] roominfo = new String[infoList.size()][];
        infoList.toArray(roominfo);

        return roominfo;
    }

    private static String[][] getRoomType(Connection connection, String info) {
        String roomtype = info;
        List<String[]> infoList = new ArrayList<>();
        String query = "SELECT * FROM room WHERE roomtype = ? and status = 0";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setString(1, roomtype);
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {

                    String roomnr = Integer.toString(resultSet.getInt("roomnr"));
                    String size = resultSet.getString("roomsize");
                    String roomid = Integer.toString(resultSet.getInt("roomid"));
                    String price = Float.toString(resultSet.getFloat("price"));
                    String hotel = resultSet.getString("hotel");
                    String status = Integer.toString(resultSet.getInt("status"));

                    String[] roominformation = { roomid, roomnr, size, info, price, hotel, status };
                    infoList.add(roominformation);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        String[][] roominfo = new String[infoList.size()][];
        infoList.toArray(roominfo);

        return roominfo;
    }

    private static String[][] getRoomId(Connection connection, String info) {
        int roomid = Integer.parseInt(info);
        List<String[]> infoList = new ArrayList<>();
        String query = "SELECT * FROM room WHERE roomid = ? and status = 0";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, roomid);
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {

                    String roomnr = Integer.toString(resultSet.getInt("roomnr"));
                    String size = resultSet.getString("roomsize");
                    String type = resultSet.getString("roomtype");
                    String price = Float.toString(resultSet.getFloat("price"));
                    String hotel = resultSet.getString("hotel");
                    String status = Integer.toString(resultSet.getInt("status"));

                    String[] roominformation = { info, roomnr, size, type, price, hotel, status };
                    infoList.add(roominformation);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        String[][] roominfo = new String[infoList.size()][];
        infoList.toArray(roominfo);

        return roominfo;

    }

    public static boolean updateRoom(Connection connection, String[] room) {
        int roomid = Integer.parseInt(room[0]);
        int roomnr = Integer.parseInt(room[1]);
        int roomsize = Integer.parseInt(room[2]);
        String roomtype = room[3];
        float price = Float.parseFloat(room[4]);
        String hotel = room[5];

        try {
            if (roomExists(connection, roomid)) {
                updateRoom(connection, roomid, roomnr, roomsize, roomtype, price, hotel);
                return true;
            } else {
                return false;
            }
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }

    private static String[][] getAllRooms(Connection connection) {
        List<String[]> infoList = new ArrayList<>();
        String query = "SELECT * FROM room WHERE status = 0";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                    String roomid = Integer.toString(resultSet.getInt("roomid"));
                    String roomnr = Integer.toString(resultSet.getInt("roomnr"));
                    String size = resultSet.getString("roomsize");
                    String type = resultSet.getString("roomtype");
                    String price = Float.toString(resultSet.getFloat("price"));
                    String hotel = resultSet.getString("hotel");
                    String status = Integer.toString(resultSet.getInt("status"));

                    String[] roominformation = { roomid, roomnr, size, type, price, hotel, status };
                    infoList.add(roominformation);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        String[][] roominfo = new String[infoList.size()][];
        infoList.toArray(roominfo);

        return roominfo;
    }

    public static String[][] getAllRoomsAdmin(Connection connection) {
        List<String[]> infoList = new ArrayList<>();
        String query = "SELECT * FROM room";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                    String roomid = Integer.toString(resultSet.getInt("roomid"));
                    String roomnr = Integer.toString(resultSet.getInt("roomnr"));
                    String size = resultSet.getString("roomsize");
                    String type = resultSet.getString("roomtype");
                    String price = Float.toString(resultSet.getFloat("price"));
                    String hotel = resultSet.getString("hotel");
                    String status = Integer.toString(resultSet.getInt("status"));

                    String[] roominformation = { roomid, roomnr, size, type, price, hotel, status };
                    infoList.add(roominformation);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        String[][] roominfo = new String[infoList.size()][];
        infoList.toArray(roominfo);

        return roominfo;
    }

    private static void updateRoom(Connection connection, int roomid, int roomnr, int roomsize, String roomtype,
            float price, String hotel) throws SQLException {
        try {
            String query = "UPDATE room SET roomnr = ?, roomsize = ?, roomtype = ?, price = ?, hotel = ? WHERE roomid = ?";
            try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
                preparedStatement.setInt(1, roomnr);
                preparedStatement.setInt(2, roomsize);
                preparedStatement.setString(3, roomtype);
                preparedStatement.setFloat(4, price);
                preparedStatement.setString(5, hotel);
                preparedStatement.setInt(6, roomid);
                preparedStatement.executeUpdate();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static boolean deleteRoom(Connection connection, String[] room) {
        int roomid = Integer.parseInt(room[0]);
        try {
            if (roomExists(connection, roomid)) {
                deleteRoom(connection, roomid);
                return true;
            } else {
                return false;
            }
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }

    private static void deleteRoom(Connection connection, int roomid) throws SQLException {
        try {
            String query = "Update room SET status = 1 WHERE roomid = ?";
            try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
                preparedStatement.setInt(1, roomid);
                preparedStatement.executeUpdate();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static boolean renovateRoom(Connection connection, String[] room) {
        int roomid = Integer.parseInt(room[0]);
        try {
            if (roomExists(connection, roomid)) {
                renovateRoom(connection, roomid);
                return true;
            } else {
                return false;
            }
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }

    private static void renovateRoom(Connection connection, int roomid) throws SQLException {
        try {
            String query = "Update room SET status = 2 WHERE room WHERE roomid = ?";
            try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
                preparedStatement.setInt(1, roomid);
                preparedStatement.executeUpdate();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private static boolean roomnrExists(Connection connection, int roomnr) throws SQLException {

        String query = "SELECT Count(*) AS count FROM room WHERE roomnr = ?";
        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, roomnr);

            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                if (resultSet.next()) {
                    int count = resultSet.getInt("count");
                    return count > 0;
                }
            }
        }
        return false;
    }

    private static boolean roomExists(Connection connection, int roomid) throws SQLException {

        String query = "SELECT Count(*) AS count FROM room WHERE roomid = ?";
        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, roomid);

            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                if (resultSet.next()) {
                    int count = resultSet.getInt("count");
                    return count > 0;
                }
            }
        }
        return false;

    }
}
