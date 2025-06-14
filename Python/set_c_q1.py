# Python program to perform operations on Lists

# 1. Create a List
print("==== Creating Lists ====")
# Empty list
empty_list = []
print("Empty list:", empty_list)

# List with items
numbers = [10, 20, 30, 40, 50]
print("List of numbers:", numbers)

# List with mixed data types
mixed_list = [1, "Hello", 3.14, True]
print("Mixed data types list:", mixed_list)

# List using list() constructor
constructed_list = list(("apple", "banana", "cherry"))
print("List created using constructor:", constructed_list)

# 2. Access List
print("\n==== Accessing List Elements ====")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("Original list:", fruits)

# Accessing by index
print("First item:", fruits[0])
print("Last item:", fruits[-1])
print("Second item:", fruits[1])

# Slicing
print("First three items:", fruits[0:3])
print("All items except first two:", fruits[2:])
print("Last three items:", fruits[-3:])

# 3. Update List
print("\n==== Updating List Elements ====")
print("Before update:", fruits)
fruits[1] = "blueberry"  # Update a single item
print("After updating second item:", fruits)

# Updating a range of items
fruits[1:3] = ["blackberry", "cranberry"]
print("After updating a range:", fruits)

# Append items
fruits.append("fig")
print("After appending 'fig':", fruits)

# Insert item at specific position
fruits.insert(2, "grape")
print("After inserting 'grape' at index 2:", fruits)

# Extend list with another list
fruits.extend(["kiwi", "lemon"])
print("After extending with two more fruits:", fruits)

# 4. Delete List
print("\n==== Deleting List Elements ====")
print("Before deletion:", fruits)

# Remove specific item
fruits.remove("blackberry")
print("After removing 'blackberry':", fruits)

# Remove by index using pop()
popped_fruit = fruits.pop(1)
print(f"Popped {popped_fruit} from index 1:", fruits)

# Delete using del keyword
del fruits[0]
print("After deleting first item:", fruits)

# Clear all items
fruits_copy = fruits.copy()  # Make a copy to demonstrate clear()
fruits_copy.clear()
print("After clearing all items:", fruits_copy)

# Delete the entire list
del fruits_copy  # This deletes the list completely
print("The list 'fruits_copy' no longer exists")

print("\nRemaining list:", fruits)

