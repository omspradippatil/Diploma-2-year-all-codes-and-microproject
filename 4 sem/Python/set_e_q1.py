# Python program to perform operations on Dictionaries

# 1. Create a Dictionary
print("==== Creating Dictionaries ====")
# Empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)

# Dictionary with items
student = {
    "name": "John",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics", "English"]
}
print("Student dictionary:", student)

# Dictionary with mixed data types
mixed_dict = {
    1: "Integer key",
    "string_key": 42,
    (1, 2): "Tuple key",
    3.14: "Float key"
}
print("Mixed data types dictionary:", mixed_dict)

# Dictionary using dict() constructor
constructed_dict = dict(name="Alice", age=25, city="New York")
print("Dictionary created using constructor:", constructed_dict)

# 2. Access Dictionary
print("\n==== Accessing Dictionary Elements ====")
print("Original dictionary:", student)

# Accessing by key
print("Name:", student["name"])
print("Age:", student["age"])

# Using get() method (safer, returns None or default if key doesn't exist)
print("Grade:", student.get("grade"))
print("Address:", student.get("address", "Not available"))

# Get all keys, values, and items
print("\nKeys:", student.keys())
print("Values:", student.values())
print("Key-Value pairs:", student.items())

# 3. Update Dictionary
print("\n==== Updating Dictionary Elements ====")
print("Before update:", student)

# Update a single item
student["age"] = 21
print("After updating age:", student)

# Add a new item
student["address"] = "123 College St"
print("After adding address:", student)

# Update multiple items at once
student.update({"grade": "A+", "year": "Sophomore"})
print("After updating multiple items:", student)

# 4. Delete Dictionary
print("\n==== Deleting Dictionary Elements ====")
print("Before deletion:", student)

# Remove specific item using pop()
removed_age = student.pop("age")
print(f"Removed age: {removed_age}")
print("After removing age:", student)

# Remove item using del keyword
del student["address"]
print("After deleting address:", student)

# Remove and return last inserted item (Python 3.7+)
item = student.popitem()
print(f"Popped item: {item}")
print("After popitem():", student)

# Clear all items
student_copy = student.copy()
student_copy.clear()
print("After clearing all items:", student_copy)

# Delete the entire dictionary
del student_copy
print("The dictionary 'student_copy' no longer exists")

# 5. Looping through Dictionary
print("\n==== Looping through Dictionary ====")
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020,
    "color": "Blue"
}

print("Looping through keys:")
for key in car:
    print(key)

print("\nLooping through values:")
for value in car.values():
    print(value)

print("\nLooping through key-value pairs:")
for key, value in car.items():
    print(f"{key}: {value}")

# Nested dictionaries
print("\nNested Dictionary example:")
family = {
    "child1": {
        "name": "Emma",
        "age": 10
    },
    "child2": {
        "name": "Jack",
        "age": 8
    }
}
print("Family dictionary:", family)
print("Name of child1:", family["child1"]["name"])
