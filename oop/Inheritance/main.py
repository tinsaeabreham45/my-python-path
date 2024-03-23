'''
As an example, let’s model an electric car. An electric car is just a specific kind of car,
so we can base our new ElectricCar class on the Car class we wrote earlier.
Then we’ll only have to write code for the attributes and behavior specific to electric cars.
'''


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 30

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    #  Modifying an attribute’s Value through a Method

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def fill_gas_tank(self):  # Overriding Methods from the Parent Class
        print("This car has a gas tank!")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)  # super function create a connection between parent and child
        # Defining Attributes and Methods for the Child Class
        self.battery_size = 70

    def describe_battery_size(self):
        print(f'this car has {self.battery_size} battery size')

    def fill_gas_tank(self):  # Overriding Methods from the Parent Class
        print("This car doesn't need a gas tank!")

    # Instances as Attributes


'''
        You can break your large class into smaller 
        classes that work together. 
        For example, if we continue adding detail to the ElectricCar class, we 
        might notice that we’re adding many attributes and methods specific to 
        the car’s battery. 
'''


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery_size()
# my_tesla.fill_gas_tank()
my_tesla.describe_battery_size()
