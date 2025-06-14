import java.awt.*;
import java.awt.event.*;

public class Q7_AWTForm {
    public static void main(String[] args) {
        Frame f = new Frame("Login Form");

        Label nameLabel = new Label("Name:");
        TextField nameField = new TextField();

        Label passLabel = new Label("Password:");
        TextField passField = new TextField();
        passField.setEchoChar('*');

        Button loginButton = new Button("Login");

        nameLabel.setBounds(50, 50, 60, 20);
        nameField.setBounds(120, 50, 150, 20);

        passLabel.setBounds(50, 90, 60, 20);
        passField.setBounds(120, 90, 150, 20);

        loginButton.setBounds(120, 130, 80, 30);

        f.add(nameLabel);
        f.add(nameField);
        f.add(passLabel);
        f.add(passField);
        f.add(loginButton);

        f.setSize(350, 250);
        f.setLayout(null);
        f.setVisible(true);

        f.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                f.dispose();
            }
        });
    }
}
