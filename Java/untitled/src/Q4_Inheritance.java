// Single Inheritance
class Vehicle {
    void start() {
        System.out.println("Vehicle starts");
    }
}

class Car extends Vehicle {
    void drive() {
        System.out.println("Car is driving");
    }
}

// Multilevel Inheritance
class SportsCar extends Car {
    void turbo() {
        System.out.println("Turbo mode ON");
    }
}

public class Q4_Inheritance {
    public static void main(String[] args) {
        System.out.println("Single Inheritance Demo:");
        Car car = new Car();
        car.start();
        car.drive();

        System.out.println("\nMultilevel Inheritance Demo:");
        SportsCar sc = new SportsCar();
        sc.start();
        sc.drive();
        sc.turbo();
    }
}