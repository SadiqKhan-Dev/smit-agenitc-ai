# 3️⃣ School Management System 🏫

# Goal: Manage Teachers, Students, and Staff

# Abstraction: Base class Person

# Encapsulation: Private fields like grades or salary

# Polymorphism: getDetails() shows different info for Student vs Teacher

# Inheritance: Student, Teacher, Staff inherit from Person

from abc import ABC, abstractmethod

class School:
    def __init__(self, teacher, student, staff):
        self.teacher = techer
        self.student = student
        self.staff = staff
        
    @abstractmethod
    def student(self):
        pass
    
    
    
    