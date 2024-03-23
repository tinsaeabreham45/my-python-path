'''
A Simple Dictionary
'''
# A dictionary in Python is a collection of key-value pairs.
# Accessing Values in a Dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
# Adding New Key-Value Pairs
alien_0['x-position'] = 0
alien_0['y-position'] = 12
print(alien_0)
# A Dictionary of Similar Objects
favorite_language = {
    'jon': 'python',
    'kaleb': 'java script',
    'me': 'c++',
}
for name in sorted(favorite_language.keys()):
    print(name)
print(f'my favorite laguage is: {favorite_language['me'].title()}')

######################################################################
print('')
print('')
'''
Looping Through a Dictionary
'''
user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }
for key, value in user_0.items():
    print('\nkey: ' + key)
    print('value: ' + value)



























