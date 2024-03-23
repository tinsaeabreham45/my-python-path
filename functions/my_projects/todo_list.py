tasks = []
done_tasks = []


def show_tasks():
    print('#####################')

    if tasks:
        print('\nhere is your tasks: ')
        for j, i in enumerate(tasks, start=1):
            print(f'{j}. {i}')
    else:
        print('your list is empty')
    print('#####################')
    return todo_list_app()


def add_tasks():
    user_active = True
    while user_active:
        user_input = input('Enter task or q to quit: ')
        if user_input == 'q':
            return todo_list_app()
            # break
        else:
            tasks.append(user_input)
            print(f'{user_input} has been added to user task lists.')


def remove_tasks():
    print('\noptions')
    print('1. remove')
    print('2. done task')
    option = input('What do you want to do? ')
    if option == '1':
        active = True
        while active:
            remove_task = input('enter task or q to quit: ')
            if remove_task == 'q':
                return todo_list_app()
            if remove_task in tasks:
                tasks.remove(remove_task)
                print(f'{remove_task} removed from task lists.')
            else:
                print(f'the task {remove_task} is not found on your list.')
            # return todo_list_app()
    elif option == '2':
        active = True
        while active:
            done_task = input('enter done task or q to quit: ')
            if done_task == 'q':
                return todo_list_app()
            if done_task in tasks:
                tasks.remove(done_task)
                done_tasks.append(done_task)
                print('you have finished {done_task}')
            else:
                print(f'the task {done_task} is not found on your list.')


def show_done_tasks():
    print('#####################')

    if done_tasks:
        print('\nhere is your Done Tasks: ')
        for j, i in enumerate(done_tasks, start=1):
            print(f'{j}. {i}')
    else:
        print('you are not done anything yet!')
    print('#####################')
    return todo_list_app()


def todo_list_app():
    while True:
        print('\noptions')
        print('1. Display the current todo lists')
        print('2. Add Tasks')
        print('3. Remove a Task')
        print('4. Show Done Tasks')
        print('5. quit')

        option = input('What do you want to do? ')
        if option == '1':
            return show_tasks()

        elif option == '2':
            return add_tasks()

        elif option == '3':
            return remove_tasks()

        elif option == '4':
            return show_done_tasks()
        elif option == '5':
            print('Thank you! Have a GoodGay! ')
            break
        else:
            print('invalid value')
    # return todo_list_app()


todo_list_app()
