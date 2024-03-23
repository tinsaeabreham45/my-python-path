'''def greet_user():  # creating function
    # Display a simple greeting.  # Docstrings are enclosed in triple quotes, which Python looks for when it generates documentation for the functions in your programs.
    print('Hello user') # the only actual coe


greet_user() # calling a function'''


                                # Passing Information to a Function
'''def greet_user(username):
#     The function now expects you to provide a value for username each
# time you call it. When you call greet_user(), you can pass it a name, such as
# 'tinsae', inside the parentheses:
    
    print(f'Hello {username.title()} !')
greet_user('tinsae')
'''
                                #Arguments and Parameters
# The variable username in the definition of greet_user() is an example of a
# parameter, a piece of information the function needs to do its job.
# The value 'tinsae' in greet_user('jesse') is an example of an argument. An argument
# is a piece of information that is passed from a function call to a function.