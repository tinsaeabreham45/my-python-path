'''
An ice cream stand is a specific kind of restaurant . Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171) . Either version of
the class will work; just pick the one you like better . Add an attribute called
flavors that stores a list of ice cream flavors . Write a method that displays
these flavors . Create an instance of IceCreamStand, and call this method
'''


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        long_name = 'Name is ' + self.restaurant_name + 'it is a ' + self.cuisine_type
        return long_name

    def open_restaurant(self):
        print(f'{self.restaurant_name.title()} is now open.')


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

        self.flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint Chocolate Chip']

    def flavor_list(self):
        print(f'the icecream flavors are:\n{self.flavors}')


IceCreamStand = IceCreamStand('IceCreamStand', 'IceCream cafe')
print(IceCreamStand.describe_restaurant())
print('')
IceCreamStand.flavor_list()
