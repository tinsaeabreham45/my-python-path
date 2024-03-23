# num = int(input('number: '))
# flag = False
#
# for i in range(2, num):
#     if num % 2 == 0:
#         flag = True
#         break
# if flag:
#     print('it is not prime')
#
# else:
#     print('it is prime')
##################################

lower = 20
upper = 100

for num in range(lower, upper+1):
    if num > 1:
        for i in range(2,num):
            if num%2 == 0:
                break
        else:
            print(num)
