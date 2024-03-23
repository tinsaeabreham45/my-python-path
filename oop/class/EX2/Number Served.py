'''
Start with your program from Exercise 9-1 (page 166) .
Add an attribute called number_served with a default value of 0 . Create an
instance called restaurant from this class . Print the number of customers the
restaurant has served, and then change this value and print it again .
 Add a method called set_number_served() that lets you set the number
of customers that have been served . Call this method with a new number and
print the value again
'''


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        restaurant_name = 'Name of restaurant is ' + self.restaurant_name.title()
        return restaurant_name

    # def open_restaurant(self):
    #     print(f'{self.restaurant_name.title()} is now open.')

    def customer_number(self):
        print("This Restaurant serve " + str(self.number_served) + " customer today.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self,cursomer):
        self.number_served += cursomer

restaurant = Restaurant('romi burger', 'burger house')
print(restaurant.describe_restaurant())
restaurant.set_number_served(25)
restaurant.customer_number()

restaurant.increment_number_served(10)
restaurant.customer_number()