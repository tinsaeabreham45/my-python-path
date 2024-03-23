'''
Make a class called User . Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile . Make a method called describe_user() that prints a summary
of the user’s information . Make another method called greet_user() that prints
a personalized greeting to the user .
 Create several instances representing different users, and call both methods
for each user
'''


class User():
    def __init__(self, first_name, last_name, age, status):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.status = status

    def describe_user(self):
        full_name = self.first_name.title() + ' ' + self.last_name.title()
        print(f'the name of the user is {full_name.title()}')
        print(f'the user is {self.age} years old')
        print(f'{full_name.title()} is {self.status}')

    def greet_user(self):
        print(f'Hello {self.first_name.title()} {self.last_name.title()}')


person_1 = User('tinsae', 'aberham', 23, 'student')
person_2 = User('kaleb', 'negus', 20, 'student')

person_1.greet_user()
person_1.describe_user()
print('')
person_2.greet_user()
person_2.describe_user()
