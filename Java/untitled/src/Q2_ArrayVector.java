import java.util.Vector;

public class Q2_ArrayVector {
    public static void main(String[] args) {
        // Array declaration and initialization
        int[] marks = {90, 85, 70, 88, 76};
        System.out.println("Array Elements:");
        for (int i = 0; i < marks.length; i++) {
            System.out.println("Index " + i + ": " + marks[i]);
        }

        // Sum and average using array
        int sum = 0;
        for (int m : marks) {
            sum += m;
        }
        double avg = (double) sum / marks.length;
        System.out.println("Total: " + sum);
        System.out.println("Average: " + avg);

        // Vector demonstration
        Vector<String> names = new Vector<>();
        names.add("Om");
        names.add("Amit");
        names.add("Ravi");

        System.out.println("\nVector Elements:");
        for (int i = 0; i < names.size(); i++) {
            System.out.println("Name " + (i + 1) + ": " + names.get(i));
        }

        // Adding and removing elements
        names.add("Sneha");
        System.out.println("After adding Sneha: " + names);

        names.remove("Amit");
        System.out.println("After removing Amit: " + names);

        // Check element and size
        System.out.println("Contains Ravi? " + names.contains("Ravi"));
        System.out.println("Size of Vector: " + names.size());
    }
}
