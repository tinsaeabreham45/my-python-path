#A list is a collection of items in a particular order.
#In Python, square brackets ([]) indicate a list, and individual elements...
# in the list are separated by commas.

bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
#Accessing Elements in a List
print(bicycles[0].title())
print(bicycles[3].title())
# to call the last item from the list we use [-1]
print(bicycles[-1].title())
#Changing, Adding, and Removing Elements

print('we cahnge trek to canva')
bicycles[0]= 'canva'
print(bicycles)
# Python provides several ways to add new data to existing lists.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# .append() is always add a new item to the end of a list
motorcycles.append('ducati')
print(motorcycles)
# .inster() we can inster a new item in specific index
motorcycles.insert(0,'ducati')
print(motorcycles)
# removing elements from the list using del, pop(), by value
# using del statment
#If you know the position of the item you want to remove from a list, you can use the del statement.
del motorcycles[0]
print(motorcycles)
# using pop method
#The pop() method removes the last item in a list, but it lets you work with that item after removing it.
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)