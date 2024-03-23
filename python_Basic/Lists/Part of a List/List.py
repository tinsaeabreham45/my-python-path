'''
Slicing a List
To make a slice, you specify the index of the first and last elements you
want to work with.
'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[2:])
'''
Looping Through a Slice
'''
print('here are the first 3 players in my team')
for i in players[:3]:
    print(i.title())
print('')
'''
Copying a List
To copy a list, you can make a slice that includes the entire original list 
by omitting the first index and the second index ([:]).
'''
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]
print('Here is my favorite foods: ')
print(my_foods )
print('\nHere is my friends favorite foods: ')
print(friends_foods)
