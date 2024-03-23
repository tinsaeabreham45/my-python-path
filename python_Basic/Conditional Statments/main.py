'''
At the heart of every if statement is an expression that can be evaluated as
True or False and is called a conditional test
To find out whether a particular value is already in a list, use the keyword in.
'''
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' not in requested_toppings)
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print('\n' + user.title() + ',' + ' you can post a response if you wish.')
car = 'subaru'
print("\nIs car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
    requested_toppings = ['mushrooms', 'extra cheese']
    if 'mushrooms' in requested_toppings:
        print("Adding mushrooms.")
    elif 'pepperoni' in requested_toppings:
        print("Adding pepperoni.")
    elif 'extra cheese' in requested_toppings:
        print("Adding extra cheese.")

    print("\nFinished making your pizza!\n")
    '''
    #############################
    Using if Statements with Lists
    #############################
    '''
for requested_topping in requested_toppings:
    if requested_topping == 'onions':
        print('sorry we are out of onions for now!')
    else:
        print('Adding ' + requested_topping + '.')
