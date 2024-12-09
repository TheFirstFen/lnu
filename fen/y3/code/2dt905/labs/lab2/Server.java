import java.net.ServerSocket;
import java.net.Socket;
import java.io.*;
import java.lang.Thread;

class Server {
    final static String RN = "\r\n";

    String host = "localhost";
    Socket connectionSocket;
    public static void main(String args[]) {
        String realtivePath;
        int port = 0;
        if (args.length == 2) {
            try {
                port = Integer.parseInt(args[0]);
                realtivePath = args[1];
                File file = new File(realtivePath);
                if (file.exists()) {
                    if (file.isDirectory()) {
                        System.out.println("Server source file exists!");
                        System.out.println("Detailed path: " + file.getAbsolutePath());
                        realtivePath += '/';
                        new Server().establishConnection(port, realtivePath);
                    } else {
                        System.out.println("Dictionary given: " + file.getAbsolutePath()  + " is not a dictionary.");
                        System.exit(1);
                    }
                } else {
                    System.out.println("Dictionary given: " + file.getAbsolutePath()  + " does not exist.");
                    System.exit(1);
                }
            } catch (NumberFormatException e) {
                System.err.println("Port number " + args[0] + " must be an integer.");
                System.exit(1);
            }
        } else {
            System.err.println("Arguments should be sent as: port path\ne.g. '80 public'");
            System.exit(1);
        }
    }

    void establishConnection(int port, String relativePath) {
        ServerSocket socket;
        try {
            socket = new ServerSocket(port); 
            System.out.println("Server Started on port " + port);
            while (true) {
                connectionSocket = socket.accept();
                Request request = new Request(connectionSocket, relativePath);
                Thread thread = new Thread(request);
                thread.start();
                System.out.println("Assigned a new client to a seperate thread.");
            }
        } catch (IOException e) {
            System.out.println("Server failed to start on port " + port);
            e.printStackTrace();
        } 
    }
}