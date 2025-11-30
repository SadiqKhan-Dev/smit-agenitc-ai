# class car:
#     car(self):
#     print("this is a car")

# class bmw(car):
#     bmw(self):
#         print("this is a bmw")

class car:
    # pass is for if we have no idea what to write in class
    x = "Khyber" # arrtibute
    y = "Supra"
    z = "BMW"
    
# car1 = car() # method
# print(car1.x, car1.y, car1.z)   

# # create  mobile class and usin  class create 3 object

# class Mobile:
#     def __init__(self, brand, model, price):
        
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def display_info(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Price:", self.price)
        
# mobile1 = Mobile("Apple", "iPhone 12", 799.99)
# mobile2 = Mobile("Samsung", "Galaxy S21", 899.99)
# mobile3 = Mobile("Google", "Pixel 5", 699.99)

# mobile1.display_info()
# mobile2.display_info()
# mobile3.display_info()


# class student:
#     name = "Sadiq khan"
#     rollNumber = 419473
#     course = "Agentic Ai"
#     batch = 2

# student1 = student()
# print(student.name, student.rollNumber, student.course, student.batch)
    
# class Mobile:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

#     def inf(self):
#         print(self.brand, self.price)

# mobile1 = Mobile("Apple", 799.99,)
# mobile2 = Mobile("Samsung", 899.99)
# mobile3 = Mobile("Google", 699.99)

# mobile1.inf()
# mobile2.inf()
# mobile3.inf()


# Make a class of laptop with attributes
# name
# ram
# price

# and a method details()


# class Laptop:
#     def __init__(self, name, ram, price):
#         self.name = name
#         self.ram = ram
#         self.price = price
    
#     def info(self):
#         print(self.name, self.ram, self.price)

# Laptop1 = Laptop("Lenovo", 16, 300)
# Laptop2 = Laptop("Dell", 32, 400)
# Laptop3 = Laptop("Asus", 64, 800)
# Laptop1.info()
# Laptop2.info()
# Laptop3.info()


# incapsulation


# class Employee:
#     def __init__(self, name):
#         self.name = name
#         self.__salary = 0

#     def self_salary(self, amount):
#         if amount > 0:
#             self.__salary = amount
#         else:
#             print("Invalid salary amount.")

#     def get_salary(self):
#         return self.__salary
    
# employee1 = Employee("Sadiq khan")
# employee1.self_salary(5000)
# print(employee1.get_salary())

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.__marks = 0

#     def set_marks(self, marks):
#         if 0 <= marks <= 100:
#             self.__marks = marks
#         else:
#             print("Invalid marks.")

#     def get_marks(self):
#         return self.__marks

# student1 = Student("Sadiq khan")
# student1.set_marks(85)
# print(student1.get_marks())




# class person():
#     def __init__(self, name):
#         self.name = name
        

# class student(person):
#     def __init__(self, name, roll_no):
#         super().__init__(name)
#         self.roll_no = roll_no
        
        
# p1 = person("Ali")
# p2 = student("Sadiq khan", 419473)
# print(p1.name)
# print(p2.name, p2.roll_no)



# class Animal:
#     def sound(self):
#         print("Same Sound")

# class Dog(Animal):
#     def sound(self):
#         print("Bark")

# class Cat(Animal):
#     def sound(self):
#         print("Meow")

class Birds:
    def sound(self):
        print("Same Sound")

class Crow(Birds):
    def sound(self):
        print("Kaen Kaen")

class Pigeon(Birds):
    def sound(self):
        print("goorn goorn")

class Duck(Birds):
    def sound(self):
        print("Quack Quack")

# animal1 = Animal()
# animal1.sound()

# dog1 = Dog()
# dog1.sound()

# cat1 = Cat()
# cat1.sound()

bird1 = Birds()
bird1.sound()

crow1 = Crow()
crow1.sound()

pigeon1 = Pigeon()
pigeon1.sound()

duck1 = Duck()
duck1.sound()

