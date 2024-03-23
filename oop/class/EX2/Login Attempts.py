'''
Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166) . Write a method called increment_login_attempts() that increments the value of
login_attempts by 1 . Write
another method called reset_login_attempts() that resets the value of login_
 attempts to 0 .
 Make an instance of the User class and call increment_login_attempts()
several times . Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts() . Print login_attempts again to
make sure it was reset to 0
'''


class User():
    def __init__(self, first_name, last_name, age, status):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.status = status
        self.login_attempts = 0

    def describe_user(self):
        full_name = self.first_name.title() + ' ' + self.last_name.title()
        print(f'the name of the user is {full_name.title()}')
        print(f'the user is {self.age} years old')
        print(f'{full_name.title()} is {self.status}')

    def attempt_number(self):
        print(self.first_name + ' your login attempts is ' + str(self.login_attempts))



    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('Tinsae', 'Abreham', 23, 'Student')

user.increment_login_attempts(3)
user.attempt_number()

user.reset_login_attempts()
user.attempt_number()

user.increment_login_attempts(2)
user.attempt_number()
