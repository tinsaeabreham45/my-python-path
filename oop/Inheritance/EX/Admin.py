'''
An administrator is a special kind of user . Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171) . Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on .
Write a method called show_privileges() that lists the administrator’s set of
privileges . Create an instance of Admin, and call your method
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


class Admin(User):
    def __init__(self,first_name, last_name, age, status):
        super().__init__(first_name,last_name,age,status)

        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('Admin: ')
        for i in self.privileges:
            print('-'+i)


Admin = Admin('tinsae', 'aberham', 23, 'student')
Admin.describe_user()
print('')
Admin.show_privileges()