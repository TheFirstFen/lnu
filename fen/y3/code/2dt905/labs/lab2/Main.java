import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
  private static final int PORT = 8888;
  private static final int TPOOL_SIZE = 10;
  private static final String DIR = "public";

  public static void main(String[] args) {
    ExecutorService threadPool = Executors.newFixedThreadPool(TPOOL_SIZE);

    try (ServerSocket serverSocket = new ServerSocket(PORT)) {
      System.out.println("Server is listening on port: " + PORT);

      while(true) {
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
         BufferedReader reader = new BufferedReader(new InputStreamReader(input));
         OutputStream output = socket.getOutputStream();
         PrintWriter writer = new PrintWriter(output, true)) {
      
      String reqLine = reader.readLine();
      while (reqLine == null || reqLine.isEmpty()) {
        return;
      }
      System.out.println("Request: " + reqLine);

      String[] reqParts = reqLine.split(" ");
      if (reqParts.length < 2 || !"GET".equalsIgnoreCase(reqParts[0])) {
        writer.write("HTTP/1.1 400 Bad Request\r\n\r\nInvalid Request");
        writer.flush();
        return;
      }

      String filePath = reqParts[1];
      Path file = Paths.get(path, filePath).normalize();

      if (Files.isDirectory(file)) {
            file = file.resolve("index.html");
      }

      if (Files.exists(file) && !Files.isDirectory(file)) {
        String mimeType = Files.probeContentType(file);
        byte[] fileBytes = Files.readAllBytes(file);

        // Response headers
        writer.write("HTTP/1.1 200 OK\r\n");
        writer.write("Content-Type: " + mimeType + "\r\n");
        writer.write("Content-Length: " + fileBytes.length + "\r\n");
        writer.write("\r\n");
        writer.flush();

        // File content
        output.write(fileBytes);
        output.flush();
      } else {
        writer.write("HTTP/1.1 404 Not Found\r\n\r\nFile Not Found");
        writer.flush();
      }
    } catch (IOException e) {
      System.err.println("I/O error handling client: " + e.getMessage());
    } finally {
      try {
        socket.close();
        System.out.println("Client connection closed");
      } catch (IOException e) {
        System.err.println("Error closing socket: " + e.getMessage());
      }
    }
  }
}
