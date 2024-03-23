'''
Create a list of strings where each string is a name.
Use a for loop to iterate through the list and print a greeting message for each person, such as "Hello, [name]!".
Create a second list of numbers.
Use a nested for loop to iterate through both lists simultaneously and print messages like "Hello, [name]! Your assigned number is [number]."
Calculate and print the average of the numbers in the second list.
Ask the user to input a new name and a number, and add them to the respective lists.
Print the updated lists
'''
name = ['Alice','Bob','Charlie','David','Emily','Henry']
num = [j for j in range(1,7)]

for i in range(len(name)):
    print(f'Hello: {name[i]} this is you ID: {num[i]}')