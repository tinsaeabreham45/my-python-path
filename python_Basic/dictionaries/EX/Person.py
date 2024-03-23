'''
 Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.
'''
personal_info = {
    'first_name': 'Tinsae',
    'last_name': 'abreham',
    'age': '23',
    'adress': 'addis ababa',
}
print(personal_info)
print(f'his first name is: {personal_info['first_name'].title()}')
print(f'his last name is: {personal_info['last_name'].title()}')
print(f'he lived in: {personal_info['adress'].title()}\n')
print(f'this is all we know about {personal_info['first_name'].title()} {personal_info['last_name'].title()}')

