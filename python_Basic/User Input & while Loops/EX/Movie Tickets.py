'''A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
'''
prompt = '\nEnter your age here or enter 0 to stop the program: '
active = True
while active:
    message = input(prompt)
    message = int(message)
    if message == 0:
        print('thank you for using our theater.')
        active = False
    else:
        if message < 3:
            print('the ticket is free for you!')
        if 3 <= message < 12 :
            print('the ticket is $10')
        if message >= 12:
            print('the ticket it $15')
