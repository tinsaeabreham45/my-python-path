'''
Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.

'''
people = {
    'person1': {
        'name': 'John Doe',
        'age': 25,
        'city': 'New York',
        'occupation': 'Engineer'
    },
    'person2': {
        'name': 'Jane Smith',
        'age': 30,
        'city': 'Los Angeles',
        'occupation': 'Teacher'
    },
    'person3': {
        'name': 'Bob Johnson',
        'age': 22,
        'city': 'Chicago',
        'occupation': 'Student'
    },
    'person4': {
        'name': 'Alice Williams',
        'age': 28,
        'city': 'San Francisco',
        'occupation': 'Software Developer'
    }
}
for person, person_info in people.items():
    print('\n' + person+':')
    name = person_info['name']
    age = person_info['age']
    city = person_info['city']
    occupation = person_info['occupation']

    print('\tName: '+ name)
    print('\tage: ' + str(age))
    print('\tcity: ' + city)
    print('\toccupation' + occupation)


