# Python program demonstrating various operators

# 1. Arithmetic Operators
print("==== Arithmetic Operators ====")
a = 10
b = 3
print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Floor Division (a // b): {a // b}")
print(f"Modulus (a % b): {a % b}")
print(f"Exponentiation (a ** b): {a ** b}")

# 2. Relational & Logical Operators
print("\n==== Relational Operators ====")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}")

print("\n==== Logical Operators ====")
x = True
y = False
print(f"x = {x}, y = {y}")
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")

# 3. Assignment Operators
print("\n==== Assignment Operators ====")
c = 5
print(f"Initial c = {c}")
c += 3  # equivalent to c = c + 3
print(f"After c += 3: {c}")
c -= 2  # equivalent to c = c - 2
print(f"After c -= 2: {c}")
c *= 4  # equivalent to c = c * 4
print(f"After c *= 4: {c}")
c /= 2  # equivalent to c = c / 2
print(f"After c /= 2: {c}")

# 4. Membership Operators
print("\n==== Membership Operators ====")
my_list = [1, 2, 3, 4, 5]
print(f"my_list = {my_list}")
print(f"3 in my_list: {3 in my_list}")
print(f"6 in my_list: {6 in my_list}")
print(f"6 not in my_list: {6 not in my_list}")
