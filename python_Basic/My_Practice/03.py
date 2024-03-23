'''
Create a list of numbers.
Write a loop to iterate through the list and print out the square of each number.
Calculate and print the sum of all the numbers in the list.
Find and print the largest number in the list.
Create a new list that contains only the even numbers from the original list.
Ask the user to input a number and check if it exists in the list. Print an appropriate message.
'''
square_numbers = [i**2 for i in range(1,21)]
print(square_numbers)
add_numbers = [i for i in range(1,21)]
print(sum(add_numbers))
print(max(add_numbers))
even_num = [i for i in add_numbers if i%2==0]
print(even_num)