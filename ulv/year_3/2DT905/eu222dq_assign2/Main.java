import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    private static final int THREADS = 16;

    public static void main(String[] args) {
        if (args.length != 2) {
            System.err.println("Usage: java Main <port> <relative-path-to-public>");
            System.exit(1);
        }

        int port;
        try {
            port = Integer.parseInt(args[0]);
        } catch (NumberFormatException e) {
            System.err.println("Invalid port number");
            return;
        }

        Path publicDir = Paths.get(args[1]);
        if (!Files.isDirectory(publicDir)) {
            System.err.println("Invalid directory: " + publicDir.toString());
            System.exit(1);
        }

        ExecutorService threadPool = Executors.newFixedThreadPool(THREADS);

        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("Server listening on port: " + port);

            Runtime.getRuntime().addShutdownHook(new Thread(threadPool::shutdown));

            while (true) {
                try {
                    Socket clientSocket = serverSocket.accept();
                    System.out.println("\r\nAccepted connection from client: " + clientSocket.getRemoteSocketAddress());
                    threadPool.submit(new ClientHandler(clientSocket, publicDir));
                } catch (IOException e) {
                    System.err.println("Failed to accept client connection: " + e.getMessage());
                }
            }
        } catch (IOException e) {
            System.err.println("Failed to start server: " + e.getMessage());
        } finally {
            threadPool.shutdown();
        }
    }
}

class ClientHandler implements Runnable {
    private final Socket clientSocket;
    private final Path publicDir;

    public ClientHandler(Socket clientSocket, Path publicDir) {
        this.clientSocket = clientSocket;
        this.publicDir = publicDir;
    }

    @Override
    public void run() {
        try (InputStream input = clientSocket.getInputStream();
             OutputStream output = clientSocket.getOutputStream()) {

            BufferedReader reader = new BufferedReader(new InputStreamReader(input));
            String reqLine = reader.readLine();

            System.out.println("Request: " + reqLine);

            String[] reqClean = reqLine.split(" ");

            String requestedPath = reqClean[1];

            if (requestedPath.equals("/redirect")) {
                System.out.println("302: Redirecting to /a/b/c/c.html");
                Redirect(output, "/a/b/c/c.html");
                return;
            }

            if (requestedPath.equals("/test500")) {
                System.out.println("500: Simulated runtime error");
                throw new RuntimeException("Simulated runtime error");
            }

            Path filePath = publicDir.resolve(requestedPath.substring(1)).normalize();

            if (requestedPath.endsWith(".htm")) {
                Path htmlPath = publicDir.resolve(requestedPath.substring(1).replace(".htm", ".html")).normalize();
                if (Files.exists(htmlPath) && !Files.isDirectory(htmlPath)) {
                    filePath = htmlPath;
                }
            }

            if (Files.isDirectory(filePath)) {
                if (Files.exists(filePath.resolve("index.html"))) {
                    filePath = filePath.resolve("index.html");
                } else if (Files.exists(filePath.resolve("index.htm"))) {
                    filePath = filePath.resolve("index.htm");
                }
            }

            if (!filePath.startsWith(publicDir) || !Files.exists(filePath) || !Files.isRegularFile(filePath)) {
                System.out.println("404: File Not Found");
                Response(output, "404 Not Found", "text/plain", "File Not Found".getBytes());
                return;
            }

            String contentType = Files.probeContentType(filePath);
            if (contentType == null) {
                if (filePath.toString().endsWith(".png")) {
                    contentType = "image/png";
                } else if (filePath.toString().endsWith(".html")) {
                    contentType = "text/html";
                } else if (filePath.toString().endsWith(".htm")) {
                    contentType = "text/html";
                } else {
                    contentType = "application/octet-stream";
                }
            }

            try {
                byte[] fileContent = Files.readAllBytes(filePath);
                System.out.println("200: OK, Serving file: " + filePath);
                Response(output, "200 OK", contentType, fileContent);
            } catch (IOException e) {
                System.out.println("500: Internal Server Error");
                Response(output, "500 Internal Server Error", "text/plain", "Internal Server Error".getBytes());
                System.err.println("Error serving file: " + e.getMessage());
            }
        } catch (IOException e) {
            System.err.println("Error handling client: " + e.getMessage());
        } finally {
            try {
                clientSocket.close();
                System.out.println("Connection closed with client: " + clientSocket.getRemoteSocketAddress());
            } catch (IOException e) {
                System.err.println("Failed to close client socket: " + e.getMessage());
            }
        }
    }

    private void Response(OutputStream output, String status, String contentType, byte[] body) throws IOException {
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(output));
        writer.write("HTTP/1.1 " + status + "\r\n");
        writer.write("Content-Type: " + contentType + "\r\n");
        writer.write("Content-Length: " + body.length + "\r\n");
        writer.write("Connection: close\r\n");
        writer.write("\r\n");
        writer.flush();

        output.write(body);
        output.flush();
    }

    private void Redirect(OutputStream output, String location) throws IOException {
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(output));
        writer.write("HTTP/1.1 302 Found\r\n");
        writer.write("Location: " + location + "\r\n");
        writer.write("Connection: close\r\n");
        writer.write("\r\n");
        writer.flush();
    }
}
