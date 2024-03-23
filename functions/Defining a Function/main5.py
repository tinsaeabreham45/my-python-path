'''Using Arbitrary Keyword Arguments'''
'''
The double asterisks before the parameter ** cause Python to create
an empty dictionary
'''


def build_profile(first_name, last_name, **user_info):
    profile = {}
    profile['First Name'] = first_name.title()
    profile['Last Name'] = last_name.title()
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_info = build_profile('Tinsae', 'abreham',
                          Location='Bishoftu',
                          Field='Electromechanical',
                          Age=23, )

print(user_info)























