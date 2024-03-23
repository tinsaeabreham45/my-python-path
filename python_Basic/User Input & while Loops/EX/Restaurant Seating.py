'''
Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message
saying they’ll have to wait for a table. Otherwise, report that their table is ready
'''
people_number = input('hiw many people are gonna sit on the dinner? ')
people_number = int(people_number)
if people_number > 8:
    print('sorry! you have to wait for a table')
else:
    print('you table is ready.')