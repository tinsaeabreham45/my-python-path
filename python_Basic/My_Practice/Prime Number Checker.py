install
number = int(input('enter the number: '))
for i in range(2, int(number * 0.5)):
    if number % i == 0:
        print('is not prime')
    else:
        print('prime')
