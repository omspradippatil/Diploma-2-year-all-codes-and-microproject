# Python program to perform operations on Sets

# 1. Create a Set
print("==== Creating Sets ====")
# Empty set (cannot use {} as that creates a dictionary)
empty_set = set()
print("Empty set:", empty_set)

# Set with items
numbers_set = {1, 2, 3, 4, 5}
print("Set of numbers:", numbers_set)

# Set with mixed data types
mixed_set = {1, "Hello", 3.14, True}
print("Mixed data types set:", mixed_set)

# Set with duplicate values (duplicates are automatically removed)
duplicate_set = {1, 2, 2, 3, 3, 3, 4, 5, 5}
print("Set with duplicate values:", duplicate_set)

# Set using set() constructor
constructed_set = set(("apple", "banana", "cherry"))
print("Set created using constructor:", constructed_set)

# Creating set from a list
list_to_set = set([1, 2, 3, 2, 4, 5, 4])
print("Set created from a list with duplicates:", list_to_set)

# 2. Access Set
print("\n==== Accessing Set Elements ====")
fruits = {"apple", "banana", "cherry", "date", "elderberry"}
print("Original set:", fruits)

# Cannot access by index since sets are unordered
print("Cannot access by index since sets are unordered.")

# Checking if an item exists in the set
print("Is 'apple' in the set?", "apple" in fruits)
print("Is 'grape' in the set?", "grape" in fruits)

# Iterating through a set
print("\nIterating through the set:")
for fruit in fruits:
    print(fruit)

# 3. Update Set
print("\n==== Updating Set Elements ====")
print("Before update:", fruits)

# Add a single item
fruits.add("fig")
print("After adding 'fig':", fruits)

# Add multiple items
fruits.update(["grape", "kiwi", "lemon"])
print("After updating with multiple fruits:", fruits)

# Using update with another set
fruits.update({"mango", "orange"})
print("After updating with another set:", fruits)

# 4. Delete Set
print("\n==== Deleting Set Elements ====")
print("Before deletion:", fruits)

# Remove specific item
fruits.remove("banana")
print("After removing 'banana':", fruits)

# Remove using discard (no error if item doesn't exist)
fruits.discard("watermelon")  # Won't raise an error even if "watermelon" doesn't exist
print("After discarding 'watermelon':", fruits)

# Pop a random item (since sets are unordered)
popped_item = fruits.pop()
print(f"Popped item: {popped_item}")
print("After popping:", fruits)

# Clear all items
fruits_copy = fruits.copy()
fruits_copy.clear()
print("After clearing all items:", fruits_copy)

# Delete the entire set
del fruits_copy
print("The set 'fruits_copy' no longer exists")

# Demonstrating set operations
print("\n==== Set Operations ====")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (set1 - set2):", set1.difference(set2))
print("Difference (set2 - set1):", set2.difference(set1))
print("Symmetric Difference:", set1.symmetric_difference(set2))
