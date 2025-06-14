class Student {
    String name;
    int age;

    // Default constructor
    Student() {
        name = "Unknown";
        age = 0;
    }

    // Parameterized constructor
    Student(String n, int a) {
        name = n;
        age = a;
    }

    // Copy constructor
    Student(Student s) {
        name = s.name;
        age = s.age;
    }

    void display() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}

public class Q3_Constructors {
    public static void main(String[] args) {
        // Using default constructor
        Student s1 = new Student();
        s1.display();

        // Using parameterized constructor
        Student s2 = new Student("Om", 18);
        s2.display();

        // Using copy constructor
        Student s3 = new Student(s2);
        s3.display();

        // More examples
        Student s4 = new Student("Amit", 20);
        Student s5 = new Student(s4);
        s4.display();
        s5.display();
    }
    
}
