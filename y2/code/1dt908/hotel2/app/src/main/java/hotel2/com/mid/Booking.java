package hotel2.com.mid;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import java.util.List;
import java.util.Set;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashSet;
import java.util.Arrays;
import java.util.Calendar;
import java.text.SimpleDateFormat;
import java.text.ParseException;

// TODO Add status to booking To be able to delete booking
// TODO Make the searching based on the status of the booking
// TODO check if the queries are correct

public class Booking {
    public static boolean checkCreateBooking(Connection connection, String[] bookinginfo) {
        try {
            Date startdate = new SimpleDateFormat("yyyy-MM-dd").parse(bookinginfo[0]);
            Date enddate = new SimpleDateFormat("yyyy-MM-dd").parse(bookinginfo[1]);
            String roomid = bookinginfo[2];
            int customerid = Integer.parseInt(bookinginfo[3]);
            int paid = Integer.parseInt(bookinginfo[4]);
            float price = Float.parseFloat(bookinginfo[5]);
            int guestcount = Integer.parseInt(bookinginfo[6]);
            String createdby = bookinginfo[7];

            List<String> roomIds = Arrays.asList(roomid.split(" "));

            if (!roomTaken(connection, roomIds, startdate, enddate)) {
                System.out.println("Rooms are not taken.");
                createBooking(connection, startdate, enddate, roomIds, customerid, paid, price, guestcount, createdby);
                return true;
            } else {
                System.out.println("Room is taken.");
                return false;
            }
        } catch (ParseException e) {
            System.out.println("Invalid date format. Please use yyyy-MM-dd.");
            return false;
        }
    }

    private static void createBooking(Connection connection, Date startdate, Date enddate, List<String> roomid,
            int customerid, int paid, float price, int guestcount, String createdby) {
        String query = "INSERT INTO booking (startdate, enddate, customerid, paid, totalprice, guestamount, createdby, checkin, checkout, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
        try (PreparedStatement preparedStatement = connection.prepareStatement(query,
                Statement.RETURN_GENERATED_KEYS)) {
            preparedStatement.setDate(1, new java.sql.Date(startdate.getTime()));
            preparedStatement.setDate(2, new java.sql.Date(enddate.getTime()));
            preparedStatement.setInt(3, customerid);
            preparedStatement.setInt(4, paid);
            preparedStatement.setFloat(5, price);
            preparedStatement.setInt(6, guestcount);
            preparedStatement.setString(7, createdby);
            preparedStatement.setInt(8, 0);
            preparedStatement.setInt(9, 0);
            preparedStatement.setInt(10, 0);
            preparedStatement.executeUpdate();

            try (ResultSet generatedKeys = preparedStatement.getGeneratedKeys()) {
                if (generatedKeys.next()) {
                    int bookingId = generatedKeys.getInt(1);
                    for (String room : roomid) {
                        insertBookingRoom(connection, bookingId, room);
                    }
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private static void insertBookingRoom(Connection connection, int bookingId, String roomid) {
        String query = "INSERT INTO booking_room (bookingid, roomid) VALUES (?, ?)";
        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, bookingId);
            preparedStatement.setString(2, roomid);
            preparedStatement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static String[][] getBookings(Connection connection, String[] search_for) {
        String search = search_for[0];
        String info = search_for[1];

        if (search.equals("startdate")) {
            return getBookingsByStartDate(connection, info);
        } else if (search.equals("enddate")) {
            return getBookingsByEndDate(connection, info);
        } else {
            System.out.println("Wrong search word");
            return null;
        }
    }

    private static String[][] getBookingsByStartDate(Connection connection, String info) {
        String query = "SELECT b.bookingid, b.startdate, b.enddate, br.roomid, b.customerid, b.paid, b.totalprice, b.guestamount, b.createdby, b.checkin, b.checkout "
                +
                "FROM booking b " +
                "JOIN booking_room br ON b.bookingid = br.bookingid " +
                "WHERE b.startdate = ? and b.status = 0";
        return executeQuery(connection, query, info);
    }

    private static String[][] getBookingsByEndDate(Connection connection, String info) {
        String query = "SELECT b.bookingid, b.startdate, b.enddate, br.roomid, b.customerid, b.paid, b.totalprice, b.guestamount, b.createdby, b.checkin, b.checkout "
                +
                "FROM booking b " +
                "JOIN booking_room br ON b.bookingid = br.bookingid " +
                "WHERE b.enddate = ? and b.status = 0";
        return executeQuery(connection, query, info);
    }

    private static String[][] executeQuery(Connection connection, String query, String info) {
        List<String[]> infoList = new ArrayList<>();
        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setDate(1, java.sql.Date.valueOf(info));
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                    String bookingid = Integer.toString(resultSet.getInt("bookingid"));
                    String start = resultSet.getString("startdate");
                    String end = resultSet.getString("enddate");
                    String customerid = Integer.toString(resultSet.getInt("customerid"));
                    String paid = Integer.toString(resultSet.getInt("paid"));
                    String price = Float.toString(resultSet.getFloat("totalprice"));
                    String guestcount = Integer.toString(resultSet.getInt("guestamount"));
                    String createdby = resultSet.getString("createdby");
                    String checkin = Integer.toString(resultSet.getInt("checkin"));
                    String checkout = Integer.toString(resultSet.getInt("checkout"));

                    String roomid = getRoomIdsForBooking(connection, bookingid);

                    String[] roominformation = { bookingid, start, end, roomid, customerid, paid, price, guestcount,
                            createdby, checkin, checkout };
                    infoList.add(roominformation);
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        String[][] result = infoList.toArray(new String[0][]);

        Set<String> uniqueBookingIds = new HashSet<>();
        List<String[]> uniqueResults = new ArrayList<>();
        for (String[] booking : result) {
            if (uniqueBookingIds.add(booking[0])) {
                uniqueResults.add(booking);
            }
        }
        return uniqueResults.toArray(new String[0][]);
    }

    public static String[][] getBookingCustomer(Connection connection, String[] search_for) {
        String search = search_for[0];
        String info = search_for[1];

        if (search.equals("customerid")) {
            return getBookingCustomerID(connection, info);
        } else {
            System.out.println("Wrong search word");
            return null;
        }
    }

    private static String[][] getBookingCustomerID(Connection connection, String info) {
        String query = "SELECT b.bookingid, b.startdate, b.enddate, br.roomid, b.customerid, b.paid, b.totalprice, b.guestamount, b.createdby, b.checkin, b.checkout "
                +
                "FROM booking b " +
                "JOIN booking_room br ON b.bookingid = br.bookingid " +
                "WHERE b.customerid = ? and b.status = 0";
        List<String[]> infoList = new ArrayList<>();
        int customerid = Integer.parseInt(info);
        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, customerid);
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                    String bookingid = Integer.toString(resultSet.getInt("bookingid"));
                    String start = resultSet.getString("startdate");
                    String end = resultSet.getString("enddate");
                    String paid = Integer.toString(resultSet.getInt("paid"));
                    String price = Float.toString(resultSet.getFloat("totalprice"));
                    String guestcount = Integer.toString(resultSet.getInt("guestamount"));
                    String createdby = resultSet.getString("createdby");
                    String checkin = Integer.toString(resultSet.getInt("checkin"));
                    String checkout = Integer.toString(resultSet.getInt("checkout"));

                    String roomid = getRoomIdsForBooking(connection, bookingid);

                    String[] roominformation = { bookingid, start, end, roomid, info, paid, price, guestcount,
                            createdby, checkin, checkout };
                    infoList.add(roominformation);
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        String[][] result = infoList.toArray(new String[0][]);

        Set<String> uniqueBookingIds = new HashSet<>();
        List<String[]> uniqueResults = new ArrayList<>();
        for (String[] booking : result) {
            if (uniqueBookingIds.add(booking[0])) {
                uniqueResults.add(booking);
            }
        }
        return uniqueResults.toArray(new String[0][]);
    }

    public static String[][] getBookingRoom(Connection connection, String[] search_for) {
        String search = search_for[0];
        String info = search_for[1];

        if (search.equals("roomid")) {
            String[][] bookinginfo = getBookingRoomid(connection, info);
            return bookinginfo;
        } else {
            System.out.println("Wrong search word");
            return null;
        }
    }

    private static String[][] getBookingRoomid(Connection connection, String info) {
        List<String[]> roominfo = new ArrayList<>();
        String query = "SELECT b.bookingid, b.startdate, b.enddate, br.roomid, b.customerid, b.paid, b.totalprice, b.guestamount, b.createdby, b.checkin, b.checkout "
                +
                "FROM booking b " +
                "JOIN booking_room br ON b.bookingid = br.bookingid " +
                "WHERE br.roomid = ? and b.status = 0";
        int roomid = Integer.parseInt(info);
        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, roomid);
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                    String bookingid = Integer.toString(resultSet.getInt("bookingid"));
                    String start = resultSet.getString("startdate");
                    String end = resultSet.getString("enddate");
                    String customerid = Integer.toString(resultSet.getInt("customerid"));
                    String paid = Integer.toString(resultSet.getInt("paid"));
                    String price = Float.toString(resultSet.getFloat("totalprice"));
                    String guestcount = Integer.toString(resultSet.getInt("guestamount"));
                    String createdby = resultSet.getString("createdby");
                    String checkin = Integer.toString(resultSet.getInt("checkin"));
                    String checkout = Integer.toString(resultSet.getInt("checkout"));

                    String roomids = getRoomIdsForBooking(connection, bookingid);

                    String[] roominformation = { bookingid, start, end, roomids, customerid, paid, price, guestcount,
                            createdby, checkin, checkout };
                    roominfo.add(roominformation);
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return roominfo.toArray(new String[0][]);
    }

    private static boolean roomTaken(Connection connection, List<String> roomIds, Date startdate, Date enddate) {
        for (String roomId : roomIds) {
            if (roomTaken(connection, roomId, startdate, enddate)) {
                return true;
            }
        }
        return false;
    }

    private static boolean roomTaken(Connection connection, String roomid, Date startdate, Date enddate) {
        String query = "SELECT * FROM booking b " +
                "JOIN booking_room br ON b.bookingid = br.bookingid " +
                "WHERE br.roomid = ?" +
                "AND ((b.startdate <= ? AND b.enddate > ?) OR (b.startdate < ? AND b.enddate >= ?) OR (b.startdate >= ? AND b.enddate <= ?)) AND b.status = 0";
        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setString(1, roomid);
            preparedStatement.setDate(2, new java.sql.Date(startdate.getTime()));
            preparedStatement.setDate(3, new java.sql.Date(startdate.getTime()));
            preparedStatement.setDate(4, new java.sql.Date(enddate.getTime()));
            preparedStatement.setDate(5, new java.sql.Date(enddate.getTime()));
            preparedStatement.setDate(6, new java.sql.Date(startdate.getTime()));
            preparedStatement.setDate(7, new java.sql.Date(enddate.getTime()));
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                return resultSet.next();
            }
        } catch (SQLException e) {
            e.printStackTrace();
            return true;
        }
    }

    public static void checkIn(Connection connection, String[] booking) {
        int bookingid = Integer.parseInt(booking[0]);
        int paid = Integer.parseInt(booking[1]);
        int checkin = 1;

        checkin(connection, bookingid, checkin, paid);
    }

    private static void checkin(Connection connection, int bookingid, int checkin, int paid) {
        String query = "UPDATE booking SET checkin = ?, paid = ? WHERE bookingid = ?";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, checkin);
            preparedStatement.setInt(2, paid);
            preparedStatement.setInt(3, bookingid);
            preparedStatement.executeUpdate();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void checkOut(Connection connection, String[] booking) {
        int bookingid = Integer.parseInt(booking[0]);
        int paid = Integer.parseInt(booking[1]);
        int checkout = 1;

        checkout(connection, bookingid, checkout, paid);
    }

    private static void checkout(Connection connection, int bookingid, int checkout, int paid) {
        String query = "UPDATE booking SET checkout = ?, paid = ? WHERE bookingid = ?";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, checkout);
            preparedStatement.setInt(2, paid);
            preparedStatement.setInt(3, bookingid);
            preparedStatement.executeUpdate();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static String[][] checkInToday(Connection connection, String[] info) throws ParseException {
        try {
            Date startdate = new SimpleDateFormat("yyyy-MM-dd").parse(info[0]);
            String[][] bookinginfo = getBookingsGoingToCheckIn(connection, startdate);
            return bookinginfo;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    private static String[][] getBookingsGoingToCheckIn(Connection connection, Date date) throws SQLException {
        List<String[]> roominfo = new ArrayList<>();
        String query = "SELECT * FROM booking WHERE checkin = ? AND startdate = ? AND status = 0";
        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, 0);
            preparedStatement.setDate(2, new java.sql.Date(date.getTime()));
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                    String bookingid = Integer.toString(resultSet.getInt("bookingid"));
                    String start = resultSet.getString("startdate");
                    String end = resultSet.getString("enddate");
                    String customerid = Integer.toString(resultSet.getInt("customerid"));
                    String paid = Integer.toString(resultSet.getInt("paid"));
                    String price = Float.toString(resultSet.getFloat("totalprice"));
                    String guestcount = Integer.toString(resultSet.getInt("guestamount"));
                    String createdby = resultSet.getString("createdby");
                    String checkin = Integer.toString(resultSet.getInt("checkin"));
                    String checkout = Integer.toString(resultSet.getInt("checkout"));

                    String roomIds = getRoomIdsForBooking(connection, bookingid);

                    String[] roominformation = { bookingid, start, end, roomIds, customerid, paid, price, guestcount,
                            createdby, checkin, checkout };
                    roominfo.add(roominformation);
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        String[][] bookinginfo = new String[roominfo.size()][];
        roominfo.toArray(bookinginfo);
        return bookinginfo;
    }

    public static String[][] checkOutToday(Connection connection, String[] info) throws ParseException {
        try {
            Date enddate = new SimpleDateFormat("yyyy-MM-dd").parse(info[0]);
            String[][] bookinginfo = getBookingsGoingToCheckOut(connection, enddate);
            return bookinginfo;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    private static String[][] getBookingsGoingToCheckOut(Connection connection, Date date) throws SQLException {
        List<String[]> roominfo = new ArrayList<>();
        String query = "SELECT * FROM booking WHERE checkin = ? AND checkout = ? AND enddate = ? AND status = 0";
        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, 1);
            preparedStatement.setInt(2, 0);
            preparedStatement.setDate(3, new java.sql.Date(date.getTime()));
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                    String bookingid = Integer.toString(resultSet.getInt("bookingid"));
                    String start = resultSet.getString("startdate");
                    String end = resultSet.getString("enddate");
                    String customerid = Integer.toString(resultSet.getInt("customerid"));
                    String paid = Integer.toString(resultSet.getInt("paid"));
                    String price = Float.toString(resultSet.getFloat("totalprice"));
                    String guestcount = Integer.toString(resultSet.getInt("guestamount"));
                    String createdby = resultSet.getString("createdby");
                    String checkin = Integer.toString(resultSet.getInt("checkin"));
                    String checkout = Integer.toString(resultSet.getInt("checkout"));

                    String roomIds = getRoomIdsForBooking(connection, bookingid);

                    String[] roominformation = { bookingid, start, end, roomIds, customerid, paid, price, guestcount,
                            createdby, checkin, checkout };
                    roominfo.add(roominformation);
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        String[][] bookinginfo = new String[roominfo.size()][];
        roominfo.toArray(bookinginfo);
        return bookinginfo;
    }

    public static String getRoomIdsForBooking(Connection connection, String bookingId) throws SQLException {
        StringBuilder roomIdsBuilder = new StringBuilder();
        String query = "SELECT roomid FROM booking_room WHERE bookingid = ?";
        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setString(1, bookingId);
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                    if (roomIdsBuilder.length() > 0) {
                        roomIdsBuilder.append(", ");
                    }
                    roomIdsBuilder.append(resultSet.getString("roomid"));
                }
            }
        }
        return roomIdsBuilder.toString();
    }

    public static String[][] getRoomsNotBooked(Connection connection, String[] info) {
        try {
            Date starDate = new SimpleDateFormat("yyyy-MM-dd").parse(info[0]);
            Date endDate = new SimpleDateFormat("yyyy-MM-dd").parse(info[1]);
            String[][] roominfo = getRoomsNotBooked(connection, starDate, endDate);
            return roominfo;
        } catch (ParseException e) {
            e.printStackTrace();
        }
        return null;
    }

    private static String[][] getRoomsNotBooked(Connection connection, Date startDate, Date endDate) {
        List<String[]> roominfo = new ArrayList<>();
        String query = "SELECT * FROM room WHERE status = 0 AND roomid NOT IN (SELECT roomid FROM booking_room WHERE bookingid IN (SELECT bookingid FROM booking WHERE startdate between ? AND ? OR enddate between ? AND ? AND status = 0))";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setDate(1, new java.sql.Date(startDate.getTime()));
            preparedStatement.setDate(2, new java.sql.Date(endDate.getTime()));
            preparedStatement.setDate(3, new java.sql.Date(startDate.getTime()));
            preparedStatement.setDate(4, new java.sql.Date(endDate.getTime()));
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                    String roomid = Integer.toString(resultSet.getInt("roomid"));
                    String roomnr = Integer.toString(resultSet.getInt("roomnr"));
                    String roomsize = Integer.toString(resultSet.getInt("roomsize"));
                    String type = resultSet.getString("roomtype");
                    String price = Float.toString(resultSet.getFloat("price"));
                    String hotel = resultSet.getString("hotel");
                    String status = Integer.toString(resultSet.getInt("status"));

                    String[] roominformation = { roomid, roomnr, roomsize, type, price, hotel, status };
                    roominfo.add(roominformation);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        String[][] emptyRooms = new String[roominfo.size()][];
        roominfo.toArray(emptyRooms);
        return emptyRooms;
    }

    public static String[] getAmountOfEmptyRooms(Connection connection, String[] info) {
        try {
            Date starDate = new SimpleDateFormat("yyyy-MM-dd").parse(info[0]);
            Date endDate = new SimpleDateFormat("yyyy-MM-dd").parse(info[1]);
            List<String> emptyRoomsList = new ArrayList<>();

            Calendar calendar = Calendar.getInstance();
            calendar.setTime(starDate);
            while (!calendar.getTime().after(endDate)) {
                Date currentDate = calendar.getTime();
                String[] emptyRooms = getAmountOfEmptyRooms(connection, currentDate);
                emptyRoomsList.add(emptyRooms[0]);
                calendar.add(Calendar.DAY_OF_MONTH, 1);
            }
            return emptyRoomsList.toArray(new String[0]);

        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    private static String[] getAmountOfEmptyRooms(Connection connection, Date date) {
        int count = 0;
        String[] amount = new String[1];
        String query = "SELECT DISTINCT roomid FROM room " +
               "WHERE room.status = ? AND roomid NOT IN " +
               "(SELECT room.roomid FROM room " +
               "JOIN booking_room ON room.roomid = booking_room.roomid " +
               "JOIN booking ON booking_room.bookingid = booking.bookingid " +
               "WHERE booking.status = ? AND ? BETWEEN booking.startdate AND booking.enddate)";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, 0);
            preparedStatement.setInt(2, 0);
            preparedStatement.setDate(3, new java.sql.Date(date.getTime()));
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while(resultSet.next()) {
                    count++;
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        amount[0] = Integer.toString(count);
        return amount;
    }
    public static String[][] getEmptyRoomsPerDay(Connection connection, String[] info) {
        try {
            Date startDate = new SimpleDateFormat("yyyy-MM-dd").parse(info[0]);
            Date endDate = new SimpleDateFormat("yyyy-MM-dd").parse(info[1]);
            List<String[]> emptyRoomsList = new ArrayList<>();

            Calendar calendar = Calendar.getInstance();
            calendar.setTime(startDate);
            while (!calendar.getTime().after(endDate)) {
                Date currentDate = calendar.getTime();
                String[] emptyRooms = getEmptyRoomsForDate(connection, currentDate);
                emptyRoomsList.add(emptyRooms);
                calendar.add(Calendar.DAY_OF_MONTH, 1);
            }

            return emptyRoomsList.toArray(new String[0][]);

        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    private static String[] getEmptyRoomsForDate(Connection connection, Date date) {
        List<String> emptyRooms = new ArrayList<>();
        String query = "SELECT roomid FROM room WHERE status = 0 AND roomid NOT IN " +
                "(SELECT roomid FROM booking_room WHERE bookingid IN " +
                "(SELECT bookingid FROM booking WHERE status = 0 AND ? BETWEEN startdate AND enddate OR ? BETWEEN startdate AND enddate))";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setDate(1, new java.sql.Date(date.getTime()));
            preparedStatement.setDate(2, new java.sql.Date(date.getTime()));
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                    emptyRooms.add(resultSet.getString("roomid"));
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return emptyRooms.toArray(new String[0]);
    }

    public static boolean checkUpdateBooking(Connection connection, String[] info) {
        int bookingid = Integer.parseInt(info[0]);
        int guestamount = Integer.parseInt(info[1]);
        int paid = Integer.parseInt(info[2]);

        return checkUpdateBooking(connection, bookingid, guestamount, paid);
    }

    private static boolean checkUpdateBooking(Connection connection, int bookingid, int guestamount, int paid) {
        String query = "update booking set guestamount = ?, paid = ? WHERE bookingid = ?";
        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, guestamount);
            preparedStatement.setInt(2, paid);
            preparedStatement.setInt(3, bookingid);
            preparedStatement.executeUpdate();
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public static boolean isRoomAvailable(Connection connection, String[] info) {
        try {
            Date startDate = new SimpleDateFormat("yyyy-MM-dd").parse(info[0]);
            Date endDate = new SimpleDateFormat("yyyy-MM-dd").parse(info[1]);
            String roomid = info[2];

            boolean isAvailable = isRoomAvailable(connection, startDate, endDate, roomid);
            return isAvailable;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    private static boolean isRoomAvailable(Connection connection, Date startDate, Date endDate, String roomid) {
        String query = "SELECT * FROM booking b " +
                "JOIN booking_room br ON b.bookingid = br.bookingid " +
                "WHERE br.roomid = ? " +
                "AND ((b.startdate <= ? AND b.enddate > ?) OR (b.startdate < ? AND b.enddate >= ?) OR (b.startdate >= ? AND b.enddate <= ?)) AND b.status = 0";
        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setString(1, roomid);
            preparedStatement.setDate(2, new java.sql.Date(startDate.getTime()));
            preparedStatement.setDate(3, new java.sql.Date(startDate.getTime()));
            preparedStatement.setDate(4, new java.sql.Date(endDate.getTime()));
            preparedStatement.setDate(5, new java.sql.Date(endDate.getTime()));
            preparedStatement.setDate(6, new java.sql.Date(startDate.getTime()));
            preparedStatement.setDate(7, new java.sql.Date(endDate.getTime()));
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                return !resultSet.next();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return true;
    }

    public static String[][] getBookingid(Connection connection, String[] info) {
        int bookingid = Integer.parseInt(info[0]);

        return getBookingid(connection, bookingid);
    }

    private static String[][] getBookingid(Connection connection, int searchid) {

        List<String[]> roominfo = new ArrayList<>();
        String query = "SELECT * FROM booking WHERE bookingid = ? AND status = 0";
        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, searchid);
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                    String bookingid = Integer.toString(resultSet.getInt("bookingid"));
                    String start = resultSet.getString("startdate");
                    String end = resultSet.getString("enddate");
                    String customerid = Integer.toString(resultSet.getInt("customerid"));
                    String paid = Integer.toString(resultSet.getInt("paid"));
                    String price = Float.toString(resultSet.getFloat("totalprice"));
                    String guestcount = Integer.toString(resultSet.getInt("guestamount"));
                    String createdby = resultSet.getString("createdby");
                    String checkin = Integer.toString(resultSet.getInt("checkin"));
                    String checkout = Integer.toString(resultSet.getInt("checkout"));

                    String roomIds = getRoomIdsForBooking(connection, bookingid);

                    String[] roominformation = { bookingid, start, end, roomIds, customerid, paid, price, guestcount,
                            createdby, checkin, checkout };
                    roominfo.add(roominformation);
                }
            }
        } catch (SQLException e) {
            return null;
        }
        return roominfo.toArray(new String[roominfo.size()][]);
    }

    public static boolean cancelBooking(Connection connection, String[] info) {
        int bookingid = Integer.parseInt(info[0]);
        int status = 1;

        return cancelBooking(connection, bookingid, status);
    }

    private static boolean cancelBooking(Connection connection, int bookingid, int status) {
        String query = "update booking set status = ? WHERE bookingid = ? ";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, status);
            preparedStatement.setInt(2, bookingid);
            preparedStatement.executeUpdate();
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
    public static String[][] getBookingSingleDate(Connection connection, String[] info) {
        try {
            Date date = new SimpleDateFormat("yyyy-MM-dd").parse(info[0]);
            return getBookingSingleDate(connection, date);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    private static String[][] getBookingSingleDate(Connection connection, Date date) {
        List<String[]> roominfo = new ArrayList<>();
        String query = "Select * From booking where status = 0 AND ? BETWEEN startdate AND enddate";

        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setDate(1, new java.sql.Date(date.getTime()));
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()) {
                    String bookingid = Integer.toString(resultSet.getInt("bookingid"));
                    String start = resultSet.getString("startdate");
                    String end = resultSet.getString("enddate");
                    String customerid = Integer.toString(resultSet.getInt("customerid"));
                    String paid = Integer.toString(resultSet.getInt("paid"));
                    String price = Float.toString(resultSet.getFloat("totalprice"));
                    String guestcount = Integer.toString(resultSet.getInt("guestamount"));
                    String createdby = resultSet.getString("createdby");
                    String checkin = Integer.toString(resultSet.getInt("checkin"));
                    String checkout = Integer.toString(resultSet.getInt("checkout"));

                    String roomIds = getRoomIdsForBooking(connection, bookingid);

                    String[] roominformation = { bookingid, start, end, roomIds, customerid, paid, price, guestcount,
                            createdby, checkin, checkout };
                    roominfo.add(roominformation);
                }
                
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        String[][] Booking = new String[roominfo.size()][];
        roominfo.toArray(Booking);
        return Booking;
    }
}
