public class Q6_ExceptionHandling {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        try {
            int x = 5 / 0; // Arithmetic error
            System.out.println(nums[5]); // Array index error
        } catch (ArithmeticException e) {
            System.out.println("Can't divide by zero!");
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Invalid array index!");
        } catch (Exception e) {
            System.out.println("Some other error: " + e);
        } finally {
            System.out.println("Always runs finally block.");
        }

        System.out.println("Program continues after exception...");
    }
}
