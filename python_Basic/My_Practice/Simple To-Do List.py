'''
Develop a basic to-do list where users can add tasks, mark them as completed, and view their current tasks.
'''
tasks = []
done_tasks = []
while True:
    add_task = True
    print('\nChose options: ')
    print('1. display the current task list')
    print('2. add a new task')
    print('3. done tasks')
    options = input('chose the options: ')
    if options == '1':
        print('your tasks are: ')
        for i,j in tasks:
            print(i)
    elif options == '2':
        while add_task:
            task = input('add task here: ')
            if task == 'done':
                break
            else:
                tasks.append(task)
        print(f'you add a new task {task} in to your task lists.')
    elif options == '3':
        done_task = input('what task are you done? ')
        tasks.remove(done_task)
        done_tasks.append(done_task)
        print('you are done to days {done_task}')

