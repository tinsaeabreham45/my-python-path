'''
Python refers to values that cannot
change as immutable, and an immutable list is called a tuple.
'''
dimensions = (200,50) # size of rectangle which is constant
print('Original Dimensions')
#Looping Through All Values in a Tuple
for dimension in dimensions:
    print(dimension)

dimensions = (500,40)
print('Modified Dimension')
for dimension in dimensions:
    print(dimension)
