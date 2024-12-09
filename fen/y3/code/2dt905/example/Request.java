import java.io.*;
import java.net.Socket;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;

public class Request implements Runnable {

  Socket socket;
  String relativePath;
  LocalDateTime date;
  String formattedDate;
  final static String RN = "\r\n";

  public Request(Socket socket, String relativePath) {
    this.socket = socket;
    this.relativePath = relativePath;
    date = LocalDateTime.now();
    DateTimeFormatter myFormatObj = DateTimeFormatter.ofPattern("yyy-MM-dd HH:mm:ss");
    formattedDate = date.format(myFormatObj);
  }

  @Override
  public void run() {
    try {
      DataOutputStream out = new DataOutputStream(socket.getOutputStream());
      InputStream inputStream = socket.getInputStream();
      byte[] array = new byte[1000024]; // 1mb
      inputStream.read(array);
      String line = "", firstLine = "", secondLine = "";
      for (byte b : array) {
        if (line.contains("HTTP/1.1") || line.contains("HTTP/1.0")) {// end of the first line
          firstLine = line;
          line = "";
          continue;
        } else if (b == 13 && firstLine.length() > 1) { // end of the second line
          secondLine = line;
          break;
        } else if (firstLine.length() > 1 && b == 0) { // no second line
          break;
        }
        line += (char) b;
      }
      Query query = new Query(firstLine);
      System.out.println(secondLine + ", Method: "
          + query.getmethodType() + ", Path: "
          + query.getPath() + ", Version: "
          + query.getHttpVersion());

      if (query.getmethodType().equals("GET"))
        System.out.println(get(relativePath, query, out));
      else if (query.getmethodType().equals("POST"))
        System.out.println(post(relativePath, query, out, array));
      out.flush();
      out.close();
      inputStream.close();
    } catch (Exception e) { // error code 400 Bad Request
      System.out.println(e);
    }
  }

  String get(String relativePath, Query q, DataOutputStream out) throws IOException {
    String response = "";
    FileInputStream fileInputStream = null;
    try {
      String path = relativePath + q.getPath();
      boolean redirect = false;
      if (q.getPath().endsWith("htm")) { // redirect code 302
        path += "l";
        redirect = true;
      }
      File file = new File(path);
      fileInputStream = new FileInputStream(file);
      System.out.println("Server request file does exists!");
      response += q.getHttpVersion() + (redirect ? " 302 FOUND" : " 200 OK") + RN;
      response += "Date: " + formattedDate + RN;
      response += "Content-Length: " + file.length() + RN;
      response += "Connection: close" + RN;
      response += "Content-Type: " + fileType(q.getFileType()) + RN;
      if (redirect)
        response += "Location: " + q.getPath() + "l" + RN;
      out.writeBytes(response);
      out.writeBytes(RN);

      byte[] bf = new byte[1024];
      int bytes = 0;
      while ((bytes = fileInputStream.read(bf)) != -1) {
        out.write(bf, 0, bytes);
      }
      fileInputStream.close();

    } catch (FileNotFoundException e1) {
      System.out.println("Server request file does not exists!");
      response += "HTTP/1.1 404 Not Found" + RN;
      response += "Date: " + formattedDate + RN;
      response += "Connection: close" + RN;
      response += "Content-Type: text/html" + RN;
      out.writeBytes(response);
      out.writeBytes(RN);
    }
    response = response.replace(RN, ", ");
    response = response.replace(q.getHttpVersion(), "Version: " + q.getHttpVersion() + ", Response:");
    response = response.substring(0, response.length() - 2);
    return "Client: " + socket.getLocalAddress().getHostName() + ":" + socket.getLocalPort() + ", " + response;
  }

  String post(String relativePath, Query q, DataOutputStream out, byte[] inputArray) throws IOException {
    String response = "";
    byte[] imageAr = new byte[1];
    String s = "";
    boolean catched = false;
    int j = 0;
    int size = 0;
    try {
      for (byte i : inputArray) {
        if ((char) i == '\n') {
          if (s.contains("ﾉPNG")) { // the png image data starts with 'ﾉPNG'
            catched = true;
            imageAr = new byte[size + 1];
            for (int x = 0; x < s.length(); x++) {
              imageAr[j] = (byte) s.charAt(x);
              j++;
            }

          } else if (s.contains("------") && catched) { // the binary data ends with ------webkit..
            break;
          } else if (s.contains("Content-Length:")) {
            String string = (s.split(" ")[1]);
            string = string.substring(0, string.length() - 1); // because of unwanted last byte 'null'
            size = Integer.parseInt(string);

            if (size > 1000000) {
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
        if (s.equals("Upload Image")) { // last line in inputstream is the value of the upload button in upload.html
          if (!catched)
            throw new Exception("File is not of type png");
          break;
        }
      }
      BufferedImage image = ImageIO.read(new ByteArrayInputStream(imageAr));
      File file = new File(relativePath + "/uploaded.png");
      ImageIO.write(image, "png", file);
      response += q.getHttpVersion() + " 200 OK" + RN;
      response += "Date: " + formattedDate + RN;
      response += "Content-Length: " + file.length() + RN;
      response += "Connection: close" + RN;
      response += "Content-Type: text/html" + RN;
      out.writeBytes(response);
      out.writeBytes(RN);
      out.writeBytes("<h1>Image uploaded sucessfully!</h1>");
      out.writeBytes("<a href='" + "uploaded.png" + "'> <img src='uploaded.png'/> </a>");
      System.out.println("Image uploaded successfully to " + file.getPath());
    } catch (Exception e) {
      response += q.getHttpVersion() + " 500 Internal Server Error" + RN;
      response += "Date: " + formattedDate + RN;
      response += "Connection: close" + RN;
      response += "Content-Type: text/html" + RN;
      out.writeBytes(response);
      out.writeBytes(RN);
      out.writeBytes("<h1>500 Internal Server Error!</h1>");
      System.out.println("File failed to upload! " + e.getMessage());
    }
    response = response.replace(RN, ", ");
    response = response.replace(q.getHttpVersion(), "Version: " + q.getHttpVersion() + ", Response:");
    response = response.substring(0, response.length() - 2);
    return "Client: " + socket.getLocalAddress().getHostName() + ":" + socket.getLocalPort() + ", " + response;
  }

  String fileType(String type) {
    if (type.equals("html"))
      return "text/html";
    else if (type.equals("png"))
      return "image/png";
    return "application/octet-stream";
  }
}