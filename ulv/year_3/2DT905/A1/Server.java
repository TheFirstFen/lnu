import java.net.*;
import java.io.*;
import java.nio.file.*;

public class Server {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage : java Server <port> <relative-path-to-public>");
            return;
        }

        int port;
        String publicDir;

        try {
            port = Integer.parseInt(args[0]);
            publicDir = args[1];
        } catch (NumberFormatException e) {
            System.out.println("Invalid port number");
            return;
        }

        File publicDirectory = new File(publicDir);
        if (!publicDirectory.isDirectory()) {
            System.out.println("Invalid public directory: " + publicDir);
            return;
        }

        System.out.println("Starting server on port " + port + "serving files from " + publicDir);

        try (ServerSocket serverSocket = new ServerSocket(port)){
            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("New connection from " + clientSocket.getInetAddress());

                new ClientHandler(clientSocket, publicDirectory).start();
            }
        } catch (Exception e) {
            System.out.println("Server error: " + e.getMessage());
        }
    }
}

class ClientHandler extends Thread {
    private final Socket socket;
    private final File publicDirectory;

    public ClientHandler(Socket socket, File publicDirectory) {
        this.socket = socket;
        this.publicDirectory = publicDirectory;
    }

    @Override
    public void run() {
        try (
            InputStream input = socket.getInputStream();
            OutputStream output = socket.getOutputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(input));
        ) {
            String requestLine = reader.readLine();
            if (requestLine == null || !requestLine.startsWith("GET")){
                sendResponse(output, 400, "Bad Request", "text/plain");
                return;
            }

            String[] requestParts = requestLine.split(" ");
            String requestPath = requestParts[1];

            Path requestedPath = publicDirectory.toPath().resolve(requestPath.substring(1)).normalize();
        }
    }
}
