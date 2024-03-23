'''
Looping Through an Entire List
'''
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ' is the best')
print('')
'''
Making Numerical Lists
range() function used to generate a series of number 
and we can change this generated value into list of numbers
'''
for value in range(1,6):
    print(value)
number = list(range(1,6))
print(number)
even_number = list(range(2,11,2))
print(even_number)

squares = []
for square in range(1,11):
    squares.append(square**2)
print(squares)
'''
List Comprehensions
The approach described earlier for generating the list squares consisted of 
using three or four lines of code. A list comprehension allows you to generate 
this same list in just one line of code.
'''
squaress = [value**2 for value in range(1,11)]
print(squaress)
nums = [num for num in range(1,11)]
print(nums)