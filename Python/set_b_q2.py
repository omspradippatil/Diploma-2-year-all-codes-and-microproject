# Python program demonstrating loop control statements

# 1. break statement
print("==== Break Statement ====")
print("Finding the first even number in a list:")
numbers = [1, 3, 5, 8, 9, 11]
for num in numbers:
    if num % 2 == 0:
        print(f"Found even number: {num}")
        break
print("Loop exited using break\n")

# 2. continue statement
print("==== Continue Statement ====")
print("Printing only odd numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num, end=" ")
print("\nOdd numbers printed using continue\n")

# 3. pass statement
print("==== Pass Statement ====")
print("Using pass as a placeholder:")
for i in range(5):
    if i == 3:
        pass  # Does nothing, just a placeholder
        print(f"Reached {i} - using pass")
    else:
        print(f"Value: {i}")
print("Loop completed with pass statement\n")

# 4. else clause with loops
print("==== Else Clause with Loops ====")
print("Finding a specific number in a list:")
search_num = 7
numbers = [1, 3, 5, 9]

for num in numbers:
    if num == search_num:
        print(f"Found {search_num}!")
        break
else:
    # This executes if the loop completes without a break
    print(f"{search_num} not found in the list")

print("\nUsing else with while loop:")
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
else:
    print("\nWhile loop completed - count reached", count)
