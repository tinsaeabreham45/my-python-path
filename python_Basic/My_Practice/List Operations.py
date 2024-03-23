'''
Perform basic operations on lists.
Create a program that allows the user to add elements to a list, remove elements, and display the current contents of the list.
'''
my_list = []
while True:
    print('\noptions')
    print('1. Display the current list')
    print('2. add an element from the list')
    print('3. Remove an element from the list')
    print('4. quit')

    option = input('chose the options: ')
    if option == '1':
        print(f'current list: {my_list}')
    elif option == '2':
        element = input("Enter the element to add: ")
        my_list.append(element)
        print(f'element {element} is added to the list.')
    elif option == "3":
        if option in my_list:
            my_list.remove(element)
            print(f'the element {element} is removed from the list.')
        else:
            print(f'the element {element} is not found.')
    elif option == '4':
        print('GoodBye!')
        break
    else:
        print('invalid value')
