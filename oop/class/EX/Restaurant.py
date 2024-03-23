'''
Make a class called Restaurant . The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type .
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating that the restaurant is open .
Make an instance called restaurant from your class . Print the two attributes individually, and then call both methods
'''


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'the name of a Restaurant is {self.restaurant_name.title()}')
        print(f'the type of a Restaurant is {self.cuisine_type.title()}')

    def open_restaurant(self):
        print(f'{self.restaurant_name.title()} is now open.')


restaurant = Restaurant('romi burger', 'burger house')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant_1 = Restaurant('hilton', 'hotel')
restaurant_2 = Restaurant('forest', 'bar')
restaurant_1.open_restaurant()
restaurant_2.open_restaurant()
