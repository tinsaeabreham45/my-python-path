'''
The for loop takes a collection of items and executes a block of code once
for each item in the collection. In contrast, the while loop runs as long as,
or while, a certain condition is true.
'''
#The while Loop in Action
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
# prompt = '\ntell me something and i will say it again: '
# prompt += '\n enter "quit" to quit. '
# message = ''
# while message != 'quit':
#     message = input(prompt)
#     print(message)


'''Using a Flag'''

# a flag is a boolean variable that is used as a condition to control the loop's execution.
prompt = '\ntell me something and i will say it again: '
prompt += '\n enter "quit" to quit. '
active = True #Flag
while active:
    message = input(prompt)
    if message.lower() == 'quit':
        active = False
    else:
        print(message)











