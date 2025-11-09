# ==========================================
# 🗂️ TOPIC 5: DICTIONARIES (5 Assignments)
# ==========================================

# Assignment 1: Student Info

student = {
    "name": "Sadiq",
    "age": 25,
    "grade": "A+"
}
print(f"{student['name']} is {student['age']} years old got the grade {student['grade']}")
print("-" * 40)

# Assignment 2: Update Dictionary
car_info = {
    "Brand": "Nissan Skyline GTR R-34", 
    "Year": 1999,
    "Color": "Blue"
}

car_info['Color'] = "Red"

print("Updated Car Info:", car_info)
print("Updated Car Year info:", car_info['Year'] == 2000)
print("-" * 40)


# Assignment 3: Loop Through Dictionary
countries = {
    "Pakistan": "Islamabad",
    "Turkey": "Ankara",
    "Japan": "Tokyo"
}

for country, capital in countries.items():
    print(f"{country} > {capital}")
print("-" * 40)


# Assignment 4: Dictionary of Prices

vagi_prices = {
    "green pepper": 2.5,
    "onion": 1.5,
    "tomato": 3.0,
    "carrot": 2.0
}
vagi_product = input("Enter the vegetable name: (e.g., onion, tomato): ").strip().lower()

# if condition
if vagi_product in vagi_prices:
    print(f"The price of {vagi_product} is ${vagi_prices[vagi_product]}")
else:
    print(f"Sorry, {vagi_product} is not available.")
print("-" * 40)

# Assignment 5: Nested Dictionary
students = {
    "Ahmed": {"age": 21, "grade": "A"},
    "Fatima": {"age": 22, "grade": "A+"},
    "Ali": {"age": 20, "grade": "B"},
    "Omar": {"age": 19, "grade": "C"}
}

for name, info in students.items():
    print(f"{name} is {info['age']} years old and got the grade {info['grade']}")