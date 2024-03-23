cart = {'apple': 10, 'mango': 20, 'orange':50, 'banana':25}
item_cart = []
user_cart = []
cost = []
print('Lists: ')
j = 0
for i in cart.keys():
    j += 1
    print(f'{j}.{i}')
    item_cart.append(i)
print(item_cart)
while True:
    options = input('Chose items: ')
    if options == '1':
        cost.append(cart['apple'])
        user_cart.append(item_cart[0])
        print(user_cart)
        print(cost)
    if options == '2':
        cost.append(cart['mango'])
        user_cart.append(item_cart[1])
        print(user_cart)
        print(cost)
    if options == 'done':
        print(f'your items are: {user_cart}')
        print(f'you will be pay: ${sum(cost)}')
        break


