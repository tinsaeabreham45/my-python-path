'''print(5 / 0)'''
# Using try-except Blocks
# try:
#     print(5 / 0)
# except ZeroDivisionError:
#     print("you can't divide by zero")
# Using Exceptions to Prevent Crashes
print('give me two number and let us divide them only.')
print('enter q to quit.')
while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    if second_number == 'q':
        break
    try:
        ans = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('you can not divide by zero! ')
    else:
        print(ans)

        