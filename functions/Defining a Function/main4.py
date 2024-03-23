'''Passing a List'''


def greet_users(names):
    for name in names:
        print(f'Hello {name.title()}!')


username = ['Tinsae', 'haylu', 'mekdes']
greet_users(username)
print(' ')
# Modifying a List in a Function
'''
Any changes made to the list inside the function’s body are permanent, allowing 
you to work efficiently even when you’re dealing with large amounts of data.
'''
'''
                # This is a code with out a function
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)
print('\nthe following models are printed: ')
for models in completed_models:
    print(models)'''
# This is more organised and readable
############################################################
'''def print_model(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print('\nthe following models are printed: ')
    for models in completed_models:
        print(models)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_model(unprinted_designs, completed_models)
show_completed_models(completed_models)
'''
###############################################################

            #Preventing a Function from Modifying a List
'''
we can use the copy list in the above example to keep the original one.

'''
            #Passing an Arbitrary Number of Arguments
'''
we use * to indicate we can add as many of as parameter 
'''
def make_pizza(*toppings):
    for topping in toppings:
        print('- '+topping)

make_pizza('pepperoni')
make_pizza('pepperoni','mushrooms','green peppers')

















