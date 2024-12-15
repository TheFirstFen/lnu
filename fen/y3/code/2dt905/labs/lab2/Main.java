import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    private static int PORT;
    private static final int TPOOL_SIZE = 10;
    private static String DIR;

    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("There should be 2 arguments: {PORT} {SOURCE_DIR}");
            System.out.println("Example execution: java Main 8888 public");
            System.exit(1);
        }
        PORT = Integer.parseInt(args[0]);
        DIR = args[1];

        ExecutorService threadPool = Executors.newFixedThreadPool(TPOOL_SIZE);

        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("Server is listening on port: " + PORT);

            Runtime.getRuntime().addShutdownHook(new Thread(() -> {
                System.out.println("Server is shutting down...");
                threadPool.shutdown();
            }));

            while (true) {
                try {
                    Socket socket = serverSocket.accept();
                    System.out.println("New client connected");
                    threadPool.submit(new ClientHandler(socket, DIR));
                } catch (IOException e) {
                    System.out.println("Failed to accept client. " + e.getMessage());
                }
            }

        } catch (IOException e) {
            System.out.println("Failed to listen on port: " + PORT + ". With exception: " + e.getMessage());
        } finally {
            threadPool.shutdown();
            System.out.println("Server shutdown.");
        }
    }
}

class ClientHandler implements Runnable {
    private final Socket socket;
    private final String path;

    public ClientHandler(Socket socket, String path) {
        this.socket = socket;
        this.path = path;
    }

    @Override
    public void run() {
        try (InputStream input = socket.getInputStream();
                DataOutputStream out = new DataOutputStream(socket.getOutputStream());
                BufferedReader reader = new BufferedReader(new InputStreamReader(input));
                OutputStream output = socket.getOutputStream();
                PrintWriter writer = new PrintWriter(output, true)) {

            String reqLine = reader.readLine();
            while (reqLine == null || reqLine.isEmpty()) {
                return;
            }
            System.out.println("Request Received: " + reqLine);

            String[] reqParts = reqLine.split(" ");
            if (reqParts.length < 2) {
                sendResponse(writer,
                        "HTTP/1.1 400 Bad Request\r\nContent-Type: text/html\r\n\r\n<h1>400 Invalid Request</h1>");
                return;
            }

            String method = reqParts[0];
            String filePath = reqParts[1];

            System.out.println("Method: " + method + "\nRequested file: " + filePath);

            if ("GET".equalsIgnoreCase(method)) {
                System.out.println("GET request received");
                handleGET(writer, output, filePath);
            } else {
                sendResponse(writer,
                        "HTTP/1.1 405 Method Not Allowed\r\nContent-Type: text/html\r\n\r\n<h1>Method Not Allowed</h1>");
            }
        } catch (Exception e) {
            System.err.println("Unexpected error: " + e.getMessage());
            sendResponseOnException(e);

        } finally {
            try {
                socket.close();
                System.out.println("Client connection closed\n");
            } catch (IOException e) {
                System.err.println("Error closing socket: " + e.getMessage());
            }
        }
    }

    private void handleGET(PrintWriter writer, OutputStream output, String filePath) throws IOException {
        if ("/redirect".equals(filePath)) {
            sendRedirect(writer, "/index.html");
            return;
        }

        if ("/error".equals(filePath)) {
            throw new IOException("Simulated Internal Server Error");
            // sendResponse(writer, "HTTP/1.1 500 Internal Server Error\r\nContent-Type:
            // text/html\r\n\r\n<h1>500 Internal Server Error</h1>");
            // return;
        }

        Path file = Paths.get(path, filePath).normalize();

        System.out.println("Serving file from path: " + file.toString());

        if (!file.startsWith(Paths.get(path).normalize())) {
            sendResponse(writer, "HTTP/1.1 403 Forbidden\r\nContent-Type: text/html\r\n\r\n<h1>Forbidden</h1>");
            return;
        }

        if (Files.isDirectory(file)) {
            file = file.resolve("index.html");
        }

        if (Files.exists(file) && !Files.isDirectory(file)) {
            String mimeType = Files.probeContentType(file);
            byte[] fileBytes = Files.readAllBytes(file);

            sendResponse(writer,
                    "HTTP/1.1 200 OK\r\nContent-Type: " + mimeType + "\r\nContent-Length: " + fileBytes.length
                            + "\r\n\r\n");
            output.write(fileBytes);
            output.flush();
        } else if (filePath.endsWith(".htm")) {
            file = Paths.get(path, filePath + "l").normalize();
            if (Files.exists(file) && !Files.isDirectory(file)) {
                String mimeType = Files.probeContentType(file);
                byte[] fileBytes = Files.readAllBytes(file);

                sendResponse(writer,
                        "HTTP/1.1 200 OK\r\nContent-Type: " + mimeType + "\r\nContent-Length: " + fileBytes.length
                                + "\r\n\r\n");
                output.write(fileBytes);
                output.flush();
            } else {
                sendResponseNotFound(writer);
            }
        } else {
            sendResponseNotFound(writer);
        }
    }

    // Send redirect response
    private void sendRedirect(PrintWriter writer, String location) {
        writer.write("HTTP/1.1 302 Found\r\n");
        writer.write("Location: " + location + "\r\n");
        writer.write("\r\n");
        writer.flush();
    }

    // Handles general responses
    private void sendResponse(PrintWriter writer, String response) {
        System.out.println("Response: " + response);
        writer.write(response);
        writer.flush();
    }

    private void sendResponseNotFound(PrintWriter writer) {
        sendResponse(writer, "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<h1>404 File Not Found</h1>");
    }

    // Sends 500 response in case of exception
    private void sendResponseOnException(Exception e) {
        try (OutputStream output = socket.getOutputStream();
                PrintWriter writer = new PrintWriter(output, true)) {

            String errorResponse = "HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/html\r\n\r\n<h1>Internal Server Error: "
                    + e.getMessage() + "</h1>";
            writer.write(errorResponse);
            writer.flush();
        } catch (IOException ex) {
            System.err.println("Failed to send 500 response: " + ex.getMessage());
        }
    }
}
