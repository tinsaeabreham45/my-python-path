'''
Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name.
Call show_magicians() to see that the list has actually been modified.
'''


def show_magicians(magician_name):
    while magician_name:
        current_name = magician_name.pop()
        print("great magician: " + current_name)
        great_magician.append(current_name)


def make_great(great_magician):
    print('\nthis are a great magician name: ')
    for n in great_magician:
        print(n)


magician_name = ['ali', 'sortu', 'nahod', 'delcarl']
great_magician = []
show_magicians(magician_name)
make_great(great_magician)
