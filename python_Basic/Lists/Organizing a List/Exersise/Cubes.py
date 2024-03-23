'''
A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube.
'''
cubes = []
for cube in range(1,11):
    cubes.append(cube**3)
print(cubes)

compressed_cube = [cubes**3 for cubes in range(1,11)]
print(compressed_cube)