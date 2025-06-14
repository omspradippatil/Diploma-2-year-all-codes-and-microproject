interface Shape {
    void area();
    void perimeter();
}

class Rectangle implements Shape {
    int length = 10, breadth = 5;

    public void area() {
        System.out.println("Area: " + (length * breadth));
    }

    public void perimeter() {
        System.out.println("Perimeter: " + 2 * (length + breadth));
    }
}

public class Q5_Interface {
    public static void main(String[] args) {
        Rectangle r = new Rectangle();
        r.area();
        r.perimeter();
    }
}
