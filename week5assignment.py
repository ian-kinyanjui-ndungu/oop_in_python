# Base class is Car
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def start(self):
        return f"The {self.color} {self.make} {self.model} starts with a roar!"

    def stop(self):
        return f"The {self.make} {self.model} is now off."

    def display_details(self):
        return f"{self.year} {self.color} {self.make} {self.model}"

# Subclass: ElectricCar (Inheritance)
class ElectricCar(Car):
    def __init__(self, make, model, year, color, battery_capacity):
        # Using super() to inherit attributes from the Car class
        super().__init__(make, model, year, color)
        self.battery_capacity = battery_capacity  # Unique to ElectricCar

    def charge(self):
        return f"The {self.make} {self.model} is charging its {self.battery_capacity} kWh battery."

    # Overriding the start method for ElectricCar
    def start(self):
        return f"The {self.color} {self.make} {self.model} starts silently!"

# Create instances of both classes
gas_car = Car("Toyota", "Corolla", 2020, "Blue")
electric_car = ElectricCar("Tesla", "Model 3", 2023, "Red", 75)

# Test methods
print(gas_car.display_details())
print(gas_car.start())
print(gas_car.stop())

print(electric_car.display_details())
print(electric_car.start())  # Polymorphism: overridden method
print(electric_car.charge())
