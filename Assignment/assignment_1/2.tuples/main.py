# ==========================================
# 🍎 TOPIC 2: TUPLES (5 Assignments)
# ==========================================

# Assignment 1: Favorite Fruits

cars = ("Toyota", "Honda", "Ford", "BMW", "Audi")
print("First Favorite Car:", cars[0])
print("Last Favorite car", cars[-1])
print("My Total Favorite Cars are", Len(cars))
print("-" * 80)

# Assignment 2: Tuple of Marks
marks = (85, 95, 75, 40,30,50,60)
print(f"Highest Rank Stundent Marks is: {max(marks)}")
print(f"Lowest Rank Stundent Marks is: {min(marks)}")
print(f"Total Marks Obtained by Student is: {sum(marks)}")
print(f"Average Marks Obtained by Student is: {sum(marks)/len(marks)}")
print("-" * 80)

# Assignment 3: Tuple Slicing
# RandomNumber in Tuple I'm Using for Tuple Slicing
numbers = (51,5, 11, 20, 35, 45, 60, 75, 80, 95)
print(f"First 2 Number are: {numbers[0:2]}")
print(f"last 2 number are from tuple is: {numbers[-2:]}")
print(f"Middle Number from tuple isL {numbers[3:4]}")
print("-" * 80)

# Assignment 5: Count & Find in Tuple
students_Names = ("Sadiq", "Ali", "Ahmed", "Kha", "Omer")
print(f"Count of 1st Student Name is {students_Names.count('Sadiq')}")
print(f"Count of 1st Student Name Index is {students_Names.index('Omer')}")
print("-" * 80)