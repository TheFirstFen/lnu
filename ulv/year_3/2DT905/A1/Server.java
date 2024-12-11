import java.io.*;
import java.net.*;
import java.nio.file.*;
import java.util.concurrent.*;

public class Server {

    private final int port;
    private final File publicDir;

    public Server(int port, String publicDirPath) {
        this.port = port;
        this.publicDir = new File(publicDirPath);

        if (!this.publicDir.exists() || !this.publicDir.isDirectory()) {
            throw new IllegalArgumentException("Invalid public directory path.");
        }
    }

    public void start() {
        System.out.println("Starting server on port " + port);
        System.out.println("Serving files from: " + publicDir.getAbsolutePath());

        try (ServerSocket serverSocket = new ServerSocket(port)) {
            ExecutorService threadPool = Executors.newCachedThreadPool();

            while (true) {
                Socket clientSocket = serverSocket.accept();
                threadPool.submit(() -> handleClient(clientSocket));
            }
        } catch (IOException e) {
            System.err.println("Error starting server: " + e.getMessage());
        }
    }

    private void handleClient(Socket clientSocket) {
        try (
            InputStream input = clientSocket.getInputStream();
            OutputStream output = clientSocket.getOutputStream()
        ) {
            BufferedReader reader = new BufferedReader(new InputStreamReader(input));
            String requestLine = reader.readLine();

            if (requestLine == null || !requestLine.startsWith("GET")) {
                sendErrorResponse(output, 400, "Bad Request");
                return;
            }

            String[] requestParts = requestLine.split(" ");
            if (requestParts.length < 2) {
                sendErrorResponse(output, 400, "Bad Request");
                return;
            }

            String requestedPath = requestParts[1];
            if (requestedPath.equals("/")) {
                requestedPath = "/index.html";
            }

            File requestedFile = new File(publicDir, requestedPath);

            if (requestedFile.isDirectory()) {
                requestedFile = new File(requestedFile, "index.html");
            }

            if (!requestedFile.getCanonicalPath().startsWith(publicDir.getCanonicalPath())) {
                sendErrorResponse(output, 403, "Forbidden");
                return;
            }

            if (!requestedFile.exists() || requestedFile.isDirectory()) {
                sendErrorResponse(output, 404, "Not Found");
                return;
            }

            sendFileResponse(output, requestedFile);

        } catch (IOException e) {
            System.err.println("Error handling client: " + e.getMessage());
        } finally {
            try {
                clientSocket.close();
            } catch (IOException e) {
                System.err.println("Error closing client socket: " + e.getMessage());
            }
        }
    }

    private void sendErrorResponse(OutputStream output, int statusCode, String message) throws IOException {
        String response = "HTTP/1.1 " + statusCode + " " + message + "\r\n" +
                "Content-Type: text/html\r\n" +
                "\r\n" +
                "<html><body><h1>" + message + "</h1></body></html>";
        output.write(response.getBytes());
    }

    private void sendFileResponse(OutputStream output, File file) throws IOException {
        String contentType = Files.probeContentType(file.toPath());
        if (contentType == null) {
            contentType = "application/octet-stream";
        }

        byte[] fileBytes = Files.readAllBytes(file.toPath());
        String responseHeaders = "HTTP/1.1 200 OK\r\n" +
                "Content-Type: " + contentType + "\r\n" +
                "Content-Length: " + fileBytes.length + "\r\n" +
                "\r\n";

        output.write(responseHeaders.getBytes());
        output.write(fileBytes);
    }

    public static void main(String[] args) {
        if (args.length != 2) {
            System.err.println("Usage: java SimpleWebServer <port> <public_directory>");
            return;
        }

        try {
            int port = Integer.parseInt(args[0]);
            String publicDirPath = args[1];

            Server server = new Server(port, publicDirPath);
            server.start();

        } catch (NumberFormatException e) {
            System.err.println("Invalid port number.");
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
        }
    }
}
