'''
Create a program that takes a string input from the user and prints the reversed version of that string.
'''
'''
# way 1
user_input = input('enter word: ')
reversed_string = user_input[::-1]
print(reversed_string)
'''
'''
# way 2
user_input = input('enter word: ')
reversed_string = ''
for i in reversed(user_input):
    reversed_string += i
print('reverse string is: '+reversed_string)
'''

# way 3
user_input = input('enter word: ')
reversed_string = ''.join(reversed(user_input))
print('reverse string is: '+reversed_string)
