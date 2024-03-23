number = int(input('enter number: '))
expand_number = []
num_str = str(number)
for i in num_str:
    i = int(i)
    expand_number.append(i)
digit_sum = sum(expand_number)
print(f'the sum of the digits are {digit_sum}')
