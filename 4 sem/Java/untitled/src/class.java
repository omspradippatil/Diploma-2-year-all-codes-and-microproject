interface Exam {
    int sports = 20;
}

class Student {
    int roll = 1, m1 = 70, m2 = 65, m3 = 75;
    String name = "Rahul";
}

class Result extends Student implements Exam {
    void display() {
        int total = m1 + m2 + m3 + sports;
        System.out.println(roll + " " + name + " Total: " + total);
    }

    public static void main(String[] args) {
        new Result().display();
    }
}
