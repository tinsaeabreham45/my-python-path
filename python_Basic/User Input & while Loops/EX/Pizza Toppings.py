'''
Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.
'''
prompt = 'enter your pizza topping here quit to finished:  '
active = True
toppings = []
while active:
    message = input(prompt)
    if message.lower() == 'quit':
        print('Thanks')
        active = False
    else:
        print(message)
        toppings.append(message)


print('\nyour toppings are: ')
for topping in toppings:
    print('-'+topping)

