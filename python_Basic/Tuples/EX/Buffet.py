'''
A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
•Use a for loop to print each food the restaurant offers.
•Try to modify one of the items, and make sure that Python rejects the
change.
•The restaurant changes its menu, replacing two of the items with different
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu.
'''
foods = ('Spaghetti Bolognese','Grilled Cheese Sandwich','Caesar Salad','Chicken Stir-Fry','Caprese Salad')
# ANS1
print("All List Of Foods: ")
for food in foods:
    print(food)
print('')
foods = ('Spaghetti Bolognese','Grilled Cheese Sandwich','yyyyyyy','Chicken Stir-Fry','xxxxxx')
#ANS3
print("All List Of Modified Foods: ")
for food in foods:
    print(food)
