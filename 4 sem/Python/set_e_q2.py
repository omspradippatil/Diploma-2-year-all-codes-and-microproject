# Python program to demonstrate user-defined functions

# 1. Function without argument
print("==== Function without argument ====")

def greet():
    """This function greets the user"""
    print("Hello! Welcome to the world of Python functions.")
    
def calculate_square_of_10():
    """This function calculates the square of 10"""
    square = 10 ** 2
    return square

# Calling functions without arguments
print("Calling greet() function:")
greet()

print("\nCalling calculate_square_of_10() function:")
result = calculate_square_of_10()
print(f"Square of 10 is: {result}")

def get_current_date():
    """This function returns the current date"""
    import datetime
    return datetime.date.today()

print("\nCalling get_current_date() function:")
today = get_current_date()
print(f"Today's date is: {today}")

# 2. Function with argument
print("\n==== Function with argument ====")

def greet_person(name):
    """This function greets the person whose name is passed as an argument"""
    print(f"Hello, {name}! How are you today?")
    
def calculate_square(number):
    """This function calculates the square of a given number"""
    square = number ** 2
    return square

def add_numbers(a, b):
    """This function adds two numbers"""
    return a + b

# Calling functions with arguments
print("Calling greet_person() function:")
greet_person("Alice")

print("\nCalling calculate_square() function:")
result = calculate_square(7)
print(f"Square of 7 is: {result}")

print("\nCalling add_numbers() function:")
sum_result = add_numbers(10, 15)
print(f"Sum of 10 and 15 is: {sum_result}")

# Function with default parameters
def greet_with_message(name, message="Good day!"):
    """Function with a default parameter"""
    print(f"Hello, {name}! {message}")

print("\nFunction with default parameter:")
greet_with_message("Bob")
greet_with_message("Charlie", "Have a great day!")

# Function with variable number of arguments
def calculate_average(*numbers):
    """Function that calculates average of variable number of arguments"""
    total = sum(numbers)
    count = len(numbers)
    return total / count if count > 0 else 0

print("\nFunction with variable number of arguments:")
avg = calculate_average(5, 10, 15, 20, 25)
print(f"Average: {avg}")

# Function with keyword arguments
def display_info(**kwargs):
    """Function that handles keyword arguments"""
    print("Information:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\nFunction with keyword arguments:")
display_info(name="David", age=30, occupation="Developer")
