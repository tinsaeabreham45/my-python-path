'''Return Values'''


# A function doesn’t always have to display its output directly.
# Instead, it can  process some data and then return a value or set of values.4
# def get_formatted_name(first_name, last_name):
#     #full_name = first_name.title() + " " + last_name.title()
#     return first_name.title() + " " + last_name.title()
#
#
# message = get_formatted_name('tinsae', 'abrehm')
# print(message)

# Making an Argument Optional
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name.title() + ' ' + middle_name + ' ' + last_name.title()
    else:
        full_name = first_name + ' ' + last_name
    return full_name


name = get_formatted_name('tinsae', 'Abreham')

print(name)


# Returning a Dictionary

def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person


name = build_person('tinsae', 'abreham')
print(name)


# Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
