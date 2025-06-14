# Python program demonstrating conditional statements

print("==== Conditional Statements in Python ====")

# 1. if statement
print("\n1. Using if statement:")
age = 18
if age >= 18:
    print("You are eligible to vote!")

# 2. if..else statement
print("\n2. Using if..else statement:")
number = 15
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# 3. if..elif..else statement
print("\n3. Using if..elif..else statement:")
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score: {score}, Grade: {grade}")

# 4. nested if statement
print("\n4. Using nested if statement:")
num = 15
if num > 0:
    print(f"{num} is positive")
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
elif num < 0:
    print(f"{num} is negative")
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
else:
    print(f"{num} is zero (neither positive nor negative)")
    print("Zero is an even number")
