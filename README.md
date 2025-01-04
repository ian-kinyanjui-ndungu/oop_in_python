# oop_in_python
oop principles implemented in python

Car and ElectricCar Class Implementation
This project demonstrates object-oriented programming (OOP) concepts in Python by implementing a Car class and its subclass ElectricCar. The code showcases features like inheritance, polymorphism, encapsulation, and constructors.

Features
Car Class
The Car class represents a general car with attributes and methods:

Attributes:

make: Manufacturer of the car (e.g., Toyota).
model: Model of the car (e.g., Corolla).
year: Year of manufacture (e.g., 2020).
color: Color of the car (e.g., Blue).
Methods:

start(): Simulates starting the car with a sound effect.
stop(): Simulates turning the car off.
display_details(): Returns a string with details about the car.
ElectricCar Class
The ElectricCar subclass inherits from the Car class and extends its functionality:

Additional Attribute:

battery_capacity: Battery capacity in kWh (e.g., 75 kWh).
Additional Method:

charge(): Simulates charging the electric car's battery.
Overridden Method:

start(): Starts the car silently, overriding the start() method of the base Car class.
Code Structure
Base Class:

Car: Contains basic attributes and methods common to all cars.
Subclass:

ElectricCar: Inherits from Car and adds functionality specific to electric cars.
Object Instantiation:

Two objects are created:
A regular gas-powered car (gas_car).
An electric car (electric_car).
Testing Methods:

Calls various methods to demonstrate encapsulation, inheritance, and polymorphism.
Example Output
Running the script produces the following output:

mathematica
Copy code
2020 Blue Toyota Corolla
The Blue Toyota Corolla starts with a roar!
The Toyota Corolla is now off.
2023 Red Tesla Model 3
The Red Tesla Model 3 starts silently!
The Tesla Model 3 is charging its 75 kWh battery.
Concepts Demonstrated
Encapsulation: Data is managed through attributes and methods.
Constructors: Objects are initialized with specific values using __init__.
Inheritance: The ElectricCar class inherits attributes and methods from the Car class.
Polymorphism: The start() method is overridden in the ElectricCar class.
How to Use
Copy the code into a Python file (e.g., car_classes.py).
Run the file using Python 3.x:
bash
Copy code
python car_classes.py
Observe the output demonstrating the functionality of both classes.
