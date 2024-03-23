# Python provides a number of different ways to organize your lists, depending on the situation.
"""
sort() method

"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
'''
To maintain the original order of a list but present it in a sorted order, you 
can use the sorted() function. 
'''
print(sorted(cars))
print(cars)
'''
Printing a List in Reverse Order
'''
cars.reverse()
print(cars)
# fFinding the Length of a List
#len() function is used to know the length of the list
print(len(cars))
