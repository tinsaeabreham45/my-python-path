'''
Ask the user for a number, and then report whether the
number is a multiple of 10 or not
'''
multiple_of_ten = input('enter the number: ')
multiple_of_ten = int(multiple_of_ten)
if multiple_of_ten % 10 == 0:
    print('your are entered a right number! ')
else:
    print('your number is not amultiple of 10')