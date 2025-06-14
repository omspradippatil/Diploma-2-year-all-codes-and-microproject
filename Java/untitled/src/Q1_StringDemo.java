public class Q1_StringDemo {
    public static void main(String[] args) {
        // String methods demo
        String str = "Hello Java";
        System.out.println("Original: " + str);
        System.out.println("Length: " + str.length());
        System.out.println("Upper Case: " + str.toUpperCase());
        System.out.println("Lower Case: " + str.toLowerCase());
        System.out.println("Char at 1: " + str.charAt(1));
        System.out.println("Substring (0 to 5): " + str.substring(0, 5));
        System.out.println("Replace 'Java' with 'World': " + str.replace("Java", "World"));

        // Checking equality
        String str2 = "Hello Java";
        System.out.println("Equals: " + str.equals(str2));
        System.out.println("Equals Ignore Case: " + str.equalsIgnoreCase("hello java"));

        // Concatenation
        String newStr = str.concat(" Programming");
        System.out.println("Concatenated: " + newStr);

        // Index of and contains
        System.out.println("Index of 'J': " + str.indexOf('J'));
        System.out.println("Contains 'Java': " + str.contains("Java"));

        // StringBuffer methods demo
        StringBuffer sb = new StringBuffer("Welcome");
        System.out.println("\nStringBuffer Original: " + sb);

        // Append and insert
        sb.append(" to Java");
        System.out.println("After Append: " + sb);
        sb.insert(8, "World ");
        System.out.println("After Insert: " + sb);

        // Delete and replace
        sb.delete(0, 7);
        System.out.println("After Delete: " + sb);
        sb.replace(0, 5, "Hello");
        System.out.println("After Replace: " + sb);

        // Reverse and capacity
        sb.reverse();
        System.out.println("After Reverse: " + sb);
        System.out.println("Capacity: " + sb.capacity());

        // Ensure capacity
        sb.ensureCapacity(100);
        System.out.println("New Capacity (after ensure): " + sb.capacity());

        // Final version
        sb.reverse(); // get back to original direction
        System.out.println("Final StringBuffer: " + sb);
    }
}
