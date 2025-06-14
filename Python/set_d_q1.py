# Python program to perform operations on Tuples

# 1. Create a Tuple
print("==== Creating Tuples ====")
# Empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# Tuple with one element (note the comma)
single_item_tuple = (1,)
print("Single item tuple:", single_item_tuple)

# Tuple with items
numbers_tuple = (1, 2, 3, 4, 5)
print("Tuple of numbers:", numbers_tuple)

# Tuple with mixed data types
mixed_tuple = (1, "Hello", 3.14, True)
print("Mixed data types tuple:", mixed_tuple)

# Tuple using tuple() constructor
constructed_tuple = tuple(("apple", "banana", "cherry"))
print("Tuple created using constructor:", constructed_tuple)

# Creating tuple without parentheses (packing)
tuple_packing = 10, 20, 30, 40
print("Tuple created by packing:", tuple_packing)

# 2. Access Tuple
print("\n==== Accessing Tuple Elements ====")
fruits = ("apple", "banana", "cherry", "date", "elderberry")
print("Original tuple:", fruits)

# Accessing by index
print("First item:", fruits[0])
print("Last item:", fruits[-1])
print("Second item:", fruits[1])

# Slicing
print("First three items:", fruits[0:3])
print("All items except first two:", fruits[2:])
print("Last three items:", fruits[-3:])

# Unpacking tuple
print("\nUnpacking tuple:")
a, b, c, d, e = fruits
print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")

# 3. Print Tuple
print("\n==== Printing Tuples ====")
print("Complete tuple:", fruits)
print("Formatted printing:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 4. Delete Tuple
print("\n==== Deleting Tuple ====")
# Cannot delete individual items (tuples are immutable)
print("Tuples are immutable, so we cannot delete individual items.")

# Delete the entire tuple
colors = ("red", "green", "blue")
print("Tuple before deletion:", colors)
del colors
print("The tuple 'colors' no longer exists")

# 5. Convert tuple into list and vice-versa
print("\n==== Converting Between Tuple and List ====")
# Tuple to list
tuple_example = (1, 2, 3, 4, 5)
print("Original tuple:", tuple_example)
list_from_tuple = list(tuple_example)
print("Converted to list:", list_from_tuple)

# Modify the list
list_from_tuple.append(6)
list_from_tuple[0] = 10
print("Modified list:", list_from_tuple)

# List to tuple
tuple_from_list = tuple(list_from_tuple)
print("Converted back to tuple:", tuple_from_list)
