'''
Start with a copy of user_profile.py from page 153. Build
a profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you
'''


def user_profile(fname, lname, **user_info):
    profile = {}
    profile['first name'] = fname
    profile['last name'] = lname
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_info = user_profile('tinsae', 'abreham',
                         age=23,
                         school='AASTU',
                         location='Addis Ababa')
print(user_info)
