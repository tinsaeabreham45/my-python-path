'''
Write a separate Privileges class . The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7 .
Move the show_privileges() method to this class . Make a Privileges instance
as an attribute in the Admin class . Create a new instance of Admin and use your
method to show its privileges
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


class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('Admin: ')
        for i in self.privileges:
            print('-' + i)


class Admin(User):
    def __init__(self, first_name, last_name, age, status):
        super().__init__(first_name, last_name, age, status)

        self.privilege = Privileges()

    # def show_privileges(self):
    #     print('Admin: ')
    #     for i in self.privileges:
    #         print('-' + i)


Admin = Admin('tinsae', 'aberham', 23, 'student')
Admin.describe_user()
Admin.privilege.show_privileges()
