'''
- One advantage of functions is the way they separate blocks of code from
your main program.
-You can go a step further by storing your functions in a separate file called a module and then importing
that module into your main program.
- There are several ways to import a module, and I’ll show you each of
these briefly
1. Importing an Entire Module
    -To start importing functions, we first need to create a module. A module
     is a file ending in .py

2. Importing Specific Functions
    from module_name import function_name
3.Using as to Give a Function an Alias
    If the name of a function you’re importing might conflict with an existing name in your program or if the function name is long,
    you can use a short, unique alias—an alternate name similar to a nickname for the function.
    You’ll give the function this special nickname when you import the function.
    The as keyword renames a function using the alias you provide:

    from module_name import function_name as fn

4. Importing All Functions in a Module
    from module_name import *
'''