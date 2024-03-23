name = 'Tinsae'
password = '1234#'
balance = 200
withdraw = 0
user_name = input('Enter name: ')
user_password = input('Enter password: ')
print('\n\t\tWELCOME TO ACCESS BANK')
print('\noptions')
print('----------------------------------')
print('1. Display the current balance')
print('2. add deposite')
print('3. withdraw')
print('4. quit')
print('----------------------------------')
while True:
    # user_name = input('Enter name: ')
    # user_password = input('Enter password: ')
    if name == user_name.title() and password == user_password:
        while True:
            # print('\noptions')
            # print('1. Display the current balance')
            # print('2. add deposite')
            # print('3. withdraw')
            # print('4. quit')
            option = input('your option: ')
            if option == '1':
                print(f'your balance is: {balance}')  # show the current balance

            # ADDING BALANCE

            elif option == '2':
                amount = int(input('enter amount: '))
                if amount < 0:
                    print("you can't add negative balance")
                    break
                else:
                    balance += amount  # add the amount
                    print(f'you add {amount} your balance is  {balance}')
            elif option == '3':
                amount = int(input('enter withdraw amount: '))
                if amount > balance:
                    print('your balance is not enough')
                    continue
                if balance < 50:
                    print("you don't have enough money")
                else:
                    if amount < 0:
                        print("you can't withdraw negative balance")
                        break
                    else:
                        balance -= amount  # Withdrawal amount
                        print(f'your withrawal amount is: {amount} your balance is:  {balance}')
            elif option == '4':
                print('Thank you for using our bank!')
                break
    try_again = input('try agin yes/no')
    if try_again != 'yes':
        print("Thanks for using our banks! HAVE A GOOD DAY.")
        break
