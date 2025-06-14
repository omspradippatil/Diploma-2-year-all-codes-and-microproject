# Python program demonstrating looping statements

# 1. while loop
print("==== While Loop ====")
print("Counting from 1 to 5 using while loop:")
count = 1
while count <= 5:
    print(count, end=" ")
    count += 1
print("\n")

# Calculating factorial using while loop
num = 5
factorial = 1
i = 1
print(f"Calculating factorial of {num} using while loop:")
while i <= num:
    factorial *= i
    i += 1
print(f"{num}! = {factorial}\n")

# 2. for loop
print("==== For Loop ====")
print("Iterating through a range:")
for i in range(5):
    print(i, end=" ")
print("\n")

print("Iterating through a list:")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
    print(fruit, end=" | ")
print("\n")

# 3. nested loop
print("==== Nested Loop ====")
print("Multiplication table from 1 to 3:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}")
    print("-" * 10)  # Separator between tables

print("\nCreating a pattern:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
