public class Query {
    private String methodType;
    private String path;
    private String httpVersion;
    private String fileType;

    public Query(String firstLine) {
        methodType = firstLine.split(" ")[0];
        path = firstLine.split(" ")[1];
        httpVersion = firstLine.split(" ")[2];
        fileType = null;
        if (path.length() > 1 && !path.endsWith("html") && !path.endsWith("htm")) {
            if (path.charAt(path.length() - 1) != '/')
                path += '/';
        }
        if (path.equals("/") || !path.contains("."))
            path += "index.html";
        else if (path.charAt(path.length() -1) == '/') // if path ended with /, remove it
            path = path.substring(0, path.length() -1); 
        
        fileType = path.contains("htm") ? "html" : "png";

        if (!path.contains("htm") && !path.contains("png"))
            fileType = "other";
    }

    public String getmethodType() {
        return methodType;
    }

    public String getHttpVersion() {
        return httpVersion;
    }

    public String getPath() {
        return path;
    }

    public String getFileType() {
        return fileType;
    }

}