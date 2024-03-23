'''
Make a list called sandwich_orders and fill it with the names of various sandwiches.
Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.
'''
'''
Using the list sandwich_orders from Exercise 7-8, make sure 
the sandwich 'pastrami' appears in the list at least three times. Add code 
near the beginning of your program to print a message saying the deli has 
run out of pastrami, and then use a while loop to remove all occurrences of 
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up 
in finished_sandwiches.
'''
sandwich_orders = ['Zesty Chicken Fiesta','pastrami','Mediterranean Bliss Wrap',
                   'Smoky Turkey Club','pastrami','Veggie Garden Delight',
                   'Spicy Tuna Tango','Classic Reuben Remix','pastrami',
                   'BBQ Pulled Pork Paradise']

print('The deli is out of pastrami ')
print('we removed pastrami from your order.')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sandwiches = []
while sandwich_orders:
    cooking = sandwich_orders.pop()
    print('I made your ' + cooking.title())
    finished_sandwiches.append(cooking)
print("\n--- All Sandwiches ---")
for sandwich in finished_sandwiches:
    print(sandwich)

