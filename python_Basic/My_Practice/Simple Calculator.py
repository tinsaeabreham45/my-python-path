'''
Create a basic calculator that can perform operations like addition, subtraction, multiplication, and division.
Take input from the user for two numbers and the operation to be performed
'''
calculator_active = True
while calculator_active:
    num1 = input('enter the first number: ')
    num2 = input('enter the second number:  ')
    print('click q to quit')
    num1 = int(num1)
    num2 = int(num2)
    oprator = input('enter the oprators or q to quit: ')
    if oprator == 'q':
        print('thank you for using my calculator')
        calculator_active = False
    else:
        if oprator == '+':
            print(f'the answer is {num1+num2}')
        elif oprator == '-':
            print(f'the answer is {num1-num2}')
        elif oprator == '*':
            print(f'the answer is {num1*num2}')
        elif oprator == '/':
            print(f'the answer is {num1/num2}')
        else:
            print('invalid oprators!')

