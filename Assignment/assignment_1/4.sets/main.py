# ==========================================
# 🔢 TOPIC 4: SETS (5 Assignments)
# ==========================================

# Assignment 1: Unique Numbers

uni_numbers = {1, 2, 2, 3, 4, 4, 5, 8}
print(f"unuque numbers are: {uni_numbers}")
print("-" * 80)

# Assignment 2: Set Operations

A = {1, 2, 4, 5, 8}
B = {6, 1 , 0, 3, 9}
print(f"A unuion B is: {A / B}")
print(f"Intersection of A and B is :{A & B}")
print("-" * 80)

# Assignment 3: Adding & Removing

student_names = {"Ali", "Omar", "Hassan", "Hasseb"}
student_names.add("Arsalan")
student_names.remove("Hassan")
print(f"Updated student names are: {student_names}")
print("-" * 80)

# Assignment 4: Membership Check

numbers = {10, 20, 30, 40, 50}
print(f"Is 30 in the set? {5 in numbers}")
print("-" * 80)

# Assignment 5: Convert List to Set
num_list = [1, 2, 2, 3, 4, 4, 5]
num_set = set(num_list)
print("Original List:", num_list)
print("Converted Set:", num_set)
print("-" * 80)