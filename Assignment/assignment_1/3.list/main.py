# ==========================================
# 📋 TOPIC 3: LISTS (5 Assignments)
# ==========================================

# Assignment 1: Student Names

smit_students_names = ["Arsalan", "Abid", "Abdul Hadi", "Haseeb"]
# adding stduent into list
smit_students_names.append("Ayaz")
# removing student from list
smit_students_names.remove("Abid")
print(smit_students_names)
print(len(smit_students_names))
print("-" * 80)

# Assignment 2: Shopping List
shoping_list = ["tomatoes", "Green Chillies", "Spinach", "Cucumber"]
shoping_list[0] = "Lemons" # updating the list first item
print("Updated Shopping List", shoping_list)
print("Number of items to he grocery List:", len(shoping_list))
print("-" * 80)

# Assignment 3: Sorting Practice
# print("-" * 80)
fruits = ["Water Melon", "Apple", "Banana", "Grapes", "Pineapple"]
print("original list b/f sorting:", fruits)
print("-" * 80)
fruits.sort()
print("Sorted List in Ascending Order:", fruits)
print("-" * 80)


# Assignment 4: Favorite Movies
movies_fav = ["Unstoppable", "Die Hard 4", "Fast and Furious 7", "John Wick", "The Dark Knight"]
print(f"First Two Favorite Movies: {movies_fav[0:2]}")
print(f"Last Movie: {movies_fav[-1]}")
print("-" * 80)
print(f"Movies Length: {len(movies_fav)}")

# Assignment 5: Sum of Numbers
numbers_sum = [15, 4, 51, 26,30]
print(f"Total Sum of Numbers: {sum(numbers_sum)}")
print("-" * 80)
print(f"Average of Numbers: {sum(numbers_sum) / len(numbers_sum)}")
print("-" * 80)