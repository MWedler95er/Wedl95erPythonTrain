class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    def car_start(self):
        return f"The car {self.brand} {self.model} is starting."

    def car_stop(self):
        return f"The car {self.brand} {self.model} is stopping."


my_car = Car("Toyota", "Corolla", 2020)
print(my_car)
print(my_car.car_start())
print(my_car.car_stop())
