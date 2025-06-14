# Python program demonstrating built-in functions/methods on List

my_list = [5, 2, 8, 1, 9, 3, 7, 4, 6, 5]
print("Original list:", my_list)

# 1. len() - Returns the number of items in a list
print("\n1. len() - Length of list")
print("Length of my_list:", len(my_list))

# 2. sorted() - Returns a sorted version of the list
print("\n2. sorted() - Sort the list")
print("Sorted list (ascending):", sorted(my_list))
print("Sorted list (descending):", sorted(my_list, reverse=True))
print("Original list remains unchanged:", my_list)

# 3. list.sort() - Sort the list in place
print("\n3. sort() - Sort the list in place")
my_list.sort()
print("After sort():", my_list)
my_list.sort(reverse=True)
print("After sort(reverse=True):", my_list)

# 4. list.append() - Add item to the end of the list
print("\n4. append() - Add item to the end")
my_list = [1, 2, 3, 4, 5]  # Reset the list
print("Before append():", my_list)
my_list.append(6)
print("After append(6):", my_list)

# 5. list.extend() - Add all items from another iterable
print("\n5. extend() - Add items from another list")
print("Before extend():", my_list)
my_list.extend([7, 8, 9])
print("After extend([7, 8, 9]):", my_list)

# 6. list.insert() - Insert item at specific position
print("\n6. insert() - Insert item at specific position")
print("Before insert():", my_list)
my_list.insert(2, 10)
print("After insert(2, 10):", my_list)

# 7. list.remove() - Remove first occurrence of item
print("\n7. remove() - Remove item by value")
my_list = [1, 2, 3, 2, 4, 5]  # Reset with duplicate
print("Before remove():", my_list)
my_list.remove(2)
print("After remove(2):", my_list)  # Removes first 2

# 8. list.pop() - Remove item at given position
print("\n8. pop() - Remove item by index")
print("Before pop():", my_list)
popped_item = my_list.pop(2)
print(f"Popped item at index 2: {popped_item}")
print("After pop(2):", my_list)

# 9. list.index() - Return index of first occurrence
print("\n9. index() - Find index of an item")
my_list = [10, 20, 30, 40, 30, 50]
print("List:", my_list)
index = my_list.index(30)
print("Index of first occurrence of 30:", index)

# 10. list.count() - Count occurrences of an item
print("\n10. count() - Count occurrences of an item")
print("List:", my_list)
count = my_list.count(30)
print("Count of 30 in the list:", count)

# 11. list.reverse() - Reverse the list in place
print("\n11. reverse() - Reverse the list")
print("Before reverse():", my_list)
my_list.reverse()
print("After reverse():", my_list)

# 12. list.copy() - Return a shallow copy of the list
print("\n12. copy() - Create a copy of the list")
list_copy = my_list.copy()
print("Original list:", my_list)
print("Copied list:", list_copy)
