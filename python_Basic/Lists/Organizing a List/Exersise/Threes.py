'''
Make a list of the multiples of 3 from 3 to 30. Use a for loop to
print the numbers in your list.
'''
multiple_of_3 = []
for i in range(3,31,3):
    multiple_of_3.append(i)
print(multiple_of_3)
multiple_of_3_compressed = [i for i in range(3,31,3)]
print(multiple_of_3_compressed)