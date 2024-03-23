'''
: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
'''
favorite_number = {
    'my': 23,
    'bereket': 7,
    'tinsae': 12,
    'sara': 45,
    'kaleb': 44,
}
#print(favorite_number)
friend = ['bereket','sara']
for name in favorite_number.keys():
    print(name.title())
    if name in friend:
        print(f'Hi {name.title()} i see that your vaforite number is:' + str(favorite_number[name]))