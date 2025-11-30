class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Card Brand is {self.brand}")
        print(self.model)
        print(self.year)


car1 = Car("Toyota", "v1", 1992)
car2 = Car("Toyota", "v2", 1992)
car3 = Car("Toyota", "v3", 1992)
car4 = Car("Toyota", "v4", 1992)
car5 = Car("Toyota", "v5", 1992)


car1.display_info()
print("\n")
car2.display_info()
car3.display_info()
car4.display_info()
car5.display_info()
