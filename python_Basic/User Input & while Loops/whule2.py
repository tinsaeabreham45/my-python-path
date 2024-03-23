#Moving Items from One List to Another
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print('verifying user: '+ current_users.title())
    confirmed_users.append(current_users)

print('\nThe following users have been confirmed ')
for user in confirmed_users:
    print(user.title())
#Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
#Filling a Dictionary with User Input