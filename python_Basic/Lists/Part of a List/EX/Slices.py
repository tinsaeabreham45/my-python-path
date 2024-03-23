'''
Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
•Print the message, The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
•Print the message, Three items from the middle of the list are:. Use a slice
to print three items from the middle of the list.
•Print the message, The last three items in the list are:. Use a slice to print
the last three items in the list.
'''
pizzas = ['mamma mia margherita','bold pepperoni blast','mediterranean deligh']
friends_pizza = pizzas[:]
pizzas.append('larval')
friends_pizza.append('soshii')
print(pizzas)
print(friends_pizza)