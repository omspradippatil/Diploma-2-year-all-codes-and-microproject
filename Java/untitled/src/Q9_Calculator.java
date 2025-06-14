import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Q9_Calculator {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Simple Calculator");
        JTextField tf1 = new JTextField();
        JTextField tf2 = new JTextField();
        JTextField result = new JTextField();

        JButton add = new JButton("+");
        JButton sub = new JButton("-");
        JButton mul = new JButton("*");
        JButton div = new JButton("/");

        tf1.setHorizontalAlignment(JTextField.CENTER);
        tf2.setHorizontalAlignment(JTextField.CENTER);
        result.setHorizontalAlignment(JTextField.CENTER);
        result.setEditable(false);

        frame.setLayout(new GridLayout(5, 1));
        frame.add(tf1);
        frame.add(tf2);
        frame.add(result);

        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(1, 4));
        panel.add(add);
        panel.add(sub);
        panel.add(mul);
        panel.add(div);

        frame.add(panel);

        ActionListener action = e -> {
            int a = Integer.parseInt(tf1.getText());
            int b = Integer.parseInt(tf2.getText());
            if (e.getSource() == add) result.setText("Sum: " + (a + b));
            if (e.getSource() == sub) result.setText("Diff: " + (a - b));
            if (e.getSource() == mul) result.setText("Product: " + (a * b));
            if (e.getSource() == div) result.setText("Quotient: " + (a / b));
        };

        add.addActionListener(action);
        sub.addActionListener(action);
        mul.addActionListener(action);
        div.addActionListener(action);

        frame.setSize(400, 300);
        frame.setVisible(true);
    }
}
