'''
Create a list of mixed data types (e.g., strings, numbers, and booleans).
Write a loop to iterate through the list and print out only the items that are of type string.
Add a new string to the list.
Remove the third item from the list.
Print the final list.
'''
mixed_data = ['apple','banana',3,True,2,'four']
strings = [i for i in mixed_data if isinstance(i, str)]
integers = [i for i in mixed_data if isinstance(i, int)]
Booleans = [i for i in mixed_data if isinstance(i, bool)]
print(strings)
print(integers)
print(Booleans)
del mixed_data[2]
print(mixed_data)
