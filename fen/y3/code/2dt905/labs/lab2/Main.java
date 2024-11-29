import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.nio.charset.StandardCharsets;

public class Main {
  private static int PORT;
  private static final int TPOOL_SIZE = 10;
  private static String DIR;

  public static void main(String[] args) {
    if (args.length != 2) {
      System.out.println("There should be 2 arguments: {PORT} {DIR_NAME}");
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

      while(true) {
        try {
          Socket socket = serverSocket.accept();
          socket.setReceiveBufferSize(131072);
          socket.setSoTimeout(30000);
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
        sendResponse(writer, "HTTP/1.1 400 Bad Request\r\nContent-Type: text/html\r\n\r\n<h1>400 Invalid Request</h1>");
        return;
      }

      String method = reqParts[0];
      String filePath = reqParts[1];

      System.out.println("Method: " + method + "\nRequested file: " + filePath);

      if ("GET".equalsIgnoreCase(method)) {
        handleGET(writer, output, filePath);
      } else if ("POST".equalsIgnoreCase(method)) {
        handlePOST(reader, input, writer, filePath);
      } else {
        sendResponse(writer, "HTTP/1.1 405 Method Not Allowed\r\nContent-Type: text/html\r\n\r\n<h1>Method Not Allowed</h1>");
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

      sendResponse(writer, "HTTP/1.1 200 OK\r\nContent-Type: " + mimeType + "\r\nContent-Length: " + fileBytes.length + "\r\n\r\n");

      output.write(fileBytes);
      output.flush();
    } else {
      sendResponse(writer, "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<h1>404 Not Found</h1>");
    }
  }

  private void handlePOST(BufferedReader reader, InputStream input, PrintWriter writer, String filePath) throws IOException {
    if (!"/upload".equals(filePath)) {
        sendResponse(writer, "HTTP/1.1 404 Not Found\r\n\r\nPage not found");
        return;
    }

    String line;
    int contentLength = 0;
    String boundary = null;

    // Parse headers
    while (!(line = reader.readLine()).isEmpty()) {
        System.out.println(line); // Debugging headers
        if (line.toLowerCase().startsWith("content-length:")) {
            contentLength = Integer.parseInt(line.split(":")[1].trim());
        } else if (line.toLowerCase().startsWith("content-type:") && line.contains("boundary=")) {
            boundary = "--" + line.split("boundary=")[1].trim();
        }
    }

    // Validate headers
    if (contentLength == 0 || boundary == null) {
        sendResponse(writer, "HTTP/1.1 400 Bad Request\r\n\r\nMissing Content-Length or Boundary");
        return;
    }

    System.out.println("Content-Length: " + contentLength);
    System.out.println("Boundary: " + boundary);

    // Read the body in chunks and ensure the exact number of bytes are read
    ByteArrayOutputStream bodyStream = new ByteArrayOutputStream();
    byte[] buffer = new byte[8192]; // 8 KB buffer
    int totalRead = 0, bytesRead;

    // Open the input stream directly
    InputStream inputStream = socket.getInputStream();
    while (totalRead < contentLength) {
        bytesRead = inputStream.read();
        if (bytesRead == -1) {
            System.out.println("Unexpected end of stream. Read " + totalRead + " out of " + contentLength);
            sendResponse(writer, "HTTP/1.1 400 Bad Request\r\n\r\nIncomplete body received");
            return;
        }

        // Add the bytes read to the body stream
        bodyStream.write(buffer, 0, bytesRead);
        totalRead += bytesRead;
        System.out.println("Read " + bytesRead + " bytes, Total: " + totalRead + "/" + contentLength);

        // Ensure that we read exactly Content-Length bytes
        if (totalRead > contentLength) {
            System.out.println("Mismatch: Expected " + contentLength + " bytes, but read " + totalRead);
            sendResponse(writer, "HTTP/1.1 400 Bad Request\r\n\r\nMismatch between Content-Length and actual data");
            return;
        }
    }

    // Process multipart data
    String bodyString = bodyStream.toString(StandardCharsets.UTF_8);

    // If the last boundary part is included, trim it
    if (bodyString.endsWith(boundary + "--")) {
        bodyString = bodyString.substring(0, bodyString.length() - (boundary.length() + 2)); // Remove trailing boundary
    }

    // Split by boundary and process each part
    String[] parts = bodyString.split(boundary);

    for (String part : parts) {
        if (part.contains("Content-Disposition") && part.contains("filename=")) {
            String[] headers = part.split("\r\n");
            String fileName = null;

            // Extract file name from the header
            for (String header : headers) {
                if (header.contains("filename=")) {
                    fileName = header.split("filename=")[1].replace("\"", "");
                }
            }

            if (fileName == null || !fileName.endsWith(".png")) {
                sendResponse(writer, "HTTP/1.1 415 Unsupported Media Type\r\n\r\nOnly PNG files are allowed");
                return;
            }

            int dataStart = part.indexOf("\r\n\r\n") + 4;
            int dataEnd = part.lastIndexOf("\r\n");
            if (dataStart == -1 || dataEnd == -1 || dataStart >= dataEnd) {
                sendResponse(writer, "HTTP/1.1 400 Bad Request\r\n\r\nInvalid part structure");
                return;
            }

            byte[] fileData = part.substring(dataStart, dataEnd).getBytes();

            // Save file to the uploads directory
            Path uploadDir = Paths.get(path, "uploads").normalize();
            if (!Files.exists(uploadDir)) {
                Files.createDirectories(uploadDir);
            }

            Path uploadFilePath = uploadDir.resolve(fileName);
            Files.write(uploadFilePath, fileData);

            sendResponse(writer, "HTTP/1.1 200 OK\r\n\r\nFile uploaded successfully: " + fileName);
            return;
        }
    }

    sendResponse(writer, "HTTP/1.1 400 Bad Request\r\n\r\nInvalid multipart form data");
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

        String errorResponse = "HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/html\r\n\r\n<h1>Internal Server Error: " + e.getMessage() + "</h1>";
        writer.write(errorResponse);
        writer.flush();
    } catch (IOException ex) {
        System.err.println("Failed to send 500 response: " + ex.getMessage());
    }
  }
}
