import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;

public class Main {
    private static int PORT = 8888;
    private static final int TPOOL_SIZE = 10;
    private static String DIR = "public/";

    public static void main(String[] args) {
        if (args.length == 2) {
            System.out.println("There should be 2 arguments: {PORT} {SOURCE_DIR}");
            System.out.println("Example execution: java Main 8888 public");
            System.exit(1);
        }
        // PORT = Integer.parseInt(args[0]);
        // DIR = args[1];

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
    private static int numberOfImages = 0;

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
            } else if ("POST".equalsIgnoreCase(method)) {
                System.out.println("POST request received");
                handlePOST(reader, input, output, writer, filePath);
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
            throw new RuntimeException("Simulated server error");
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
            file = Paths.get(path, filePath + "l").normalize(); // Try to serve .html if .htm is requested
            if (Files.exists(file) && !Files.isDirectory(file)) {
                String mimeType = Files.probeContentType(file);
                byte[] fileBytes = Files.readAllBytes(file);

                sendResponse(writer,
                        "HTTP/1.1 200 OK\r\nContent-Type: " + mimeType + "\r\nContent-Length: " + fileBytes.length
                                + "\r\n\r\n");
                output.write(fileBytes);
                output.flush();
            } else {
                sendResponse(writer,
                        "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<h1>File Not Found</h1>");
            }
        } else {
            sendResponse(writer, "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<h1>File Not Found</h1>");
        }
    }

    private void handlePOST(BufferedReader reader, InputStream input, OutputStream out, PrintWriter writer,
            String filePath) {
        System.out.println("Entered handlePOST method");

        try {
            // Read the headers
            String line;
            while (!(line = reader.readLine()).isEmpty()) {
                System.out.println("Header: " + line);
            }

            // Read the body
            StringBuilder body = new StringBuilder();
            while (reader.ready()) {
                body.append((char) reader.read());
            }
            System.out.println("Body: " + body.toString());

            byte[] bodyBytes = body.toString().getBytes();

            // Process the request body and generate a response
            String response = processPostRequest(bodyBytes, filePath, numberOfImages);
            numberOfImages++;
            sendResponse(writer, response);

        } catch (IOException e) {
            System.err.println("Error in handlePOST: " + e.getMessage());
            sendResponse(writer,
                    "HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/html\r\n\r\n<h1>Internal Server Error</h1>");
        } finally {
            try {
                input.close();
                out.close();
            } catch (IOException e) {
                System.err.println("Error closing streams: " + e.getMessage());
            }
        }
    }

    private String processPostRequest(byte[] body, String filePath, int numberOfImages) {
        String response = "";
        byte[] imageAr = new byte[1];
        String s = "";
        boolean catched = false;
        int j = 0;
        int size = 0;
        try {
            for (byte i : body) {
                if ((char) i == '\n') {
                    if (s.contains("PNG")) { // the png image data starts with 'ﾉPNG'
                        catched = true;
                        imageAr = new byte[size + 1];
                        for (int x = 0; x < s.length(); x++) { // Error 500 Internal Server Error
                            imageAr[j] = (byte) s.charAt(x);
                            j++;
                        }
                    } else if (s.contains("------") && catched) { // the binary data ends with ------webkit..
                        break;
                    } else if (s.contains("Content-Length:")) {
                        String string = (s.split(" ")[1]);
                        string = string.substring(0, string.length() - 1); // because of unwanted last byte 'null'
                        size = Integer.parseInt(string);

                        if (size > 1048576) {
                            throw new Exception("size over the limit");
                        }
                    }
                    s = "";
                } else {
                    s += (char) i;
                }
                if (catched) {
                    imageAr[j] = i;
                    j++;
                }
                if (s.equals("Upload Image")) { // last line in inputstream is the value of the upload button in
                    if (!catched)
                        throw new Exception("File is not of type png");
                    break;
                }
            }
            BufferedImage image = ImageIO.read(new ByteArrayInputStream(imageAr));
            String imagePath = filePath + "s/uploaded_image_" + numberOfImages + ".png";
            File file = new File(imagePath);
            ImageIO.write(image, "png", file);
            response = "HTTP/1.1 200 OK\r\nContent-Length: " + file.length()
                    + "\r\nConnection: close\r\nContent-Type: text/html\r\n\r\n<h1>Image uploaded successfully!</h1>\r\n<a href='"
                    + imagePath + "'> <img src='" + imagePath + "'/> </a>";
            System.out.println("Image uploaded successfully to " + file.getPath());
        } catch (Exception e) {
            response = "HTTP/1.1 500 Internal Server Error\r\nConnection: close\r\nContent-Type: text/html\r\n\r\n<h1>500 Internal Server Error!</h1>";
            System.err.println("File failed to upload! " + e.getMessage());
        }
        return response;
    }

    private void sendRedirect(PrintWriter writer, String location) {
        writer.write("HTTP/1.1 302 Found\r\n");
        writer.write("Location: " + location + "\r\n");
        writer.write("\r\n");
        writer.flush();
    }

    private void sendResponse(PrintWriter writer, String response) {
        System.out.println("Response: " + response);
        writer.write(response);
        writer.flush();
    }

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
