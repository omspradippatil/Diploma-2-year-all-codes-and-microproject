import java.io.*;
import java.net.*;

public class Q10_URLDemo {
    public static void main(String[] args) {
        try {
            URL url = new URL("https://ompradippatil.netlify.app/");
            System.out.println("Protocol: " + url.getProtocol());
            System.out.println("Host: " + url.getHost());
            System.out.println("Port: " + url.getPort());
            System.out.println("Path: " + url.getPath());
            System.out.println("File: " + url.getFile());

            URLConnection conn = url.openConnection();
            System.out.println("\nContent Type: " + conn.getContentType());
            System.out.println("Date: " + conn.getDate());
            System.out.println("Last Modified: " + conn.getLastModified());
            System.out.println("Content Length: " + conn.getContentLength());

            System.out.println("\n--- Content Preview ---");
            BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String line;
            int count = 0;
            while ((line = in.readLine()) != null && count < 5) {
                System.out.println(line);
                count++;
            }
            in.close();

        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
