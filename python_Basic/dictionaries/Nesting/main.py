'''A List of Dictionaries'''
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0,alien_1,alien_2]
# for alien in aliens:
#     print(alien)
students = []
for student_number in range(50):
    student_info = {'name': 'John Doe', 'age': 18, 'grade': 12, 'favorite_language': 'Python', }
    students.append(student_info)
for student in students[0:5]:
    if student['name'] == 'John Doe':
        student['name'] = 'Tinsae'
        student['age'] = 23
        student['grade'] = 10
        student['favorite_language'] = 'C++'
for student in students[0:10]:
    print(student)
print('....')

print('the information continue till 50 data')
print('the total number of student is:' + str(len(students)))
# LIST IN DICTIONERY
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print('you ordered a ' + pizza['crust'] + '-crust pizza with following toppings: ')
for topping in pizza['toppings']:
    print('\t' + topping)

# A Dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print('\nusername:  '+ username)
    full_name = user_info['first']+ " " +user_info['last']
    location = user_info['location']

    print('\tFull name: '+ full_name)
    print('\tLocation: '+ location)
