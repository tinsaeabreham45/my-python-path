'''Creating and using a Class
Let’s start by writing a simple class, Dog, that represents a dog—not one dog in particular, but any dog.

What do we know about most pet dogs? Well, they all have a name and age.
We also know that most dogs sit and roll over. Those two pieces of information (name and age) and those two behaviors
(sit and roll over) will go in our Dog class because they’re common to most dogs.
After our class is written,
we’ll use it to make individual instances, each of which represents one specific dog.
'''
class Dog():
    '''a simple attempt to model a dog. '''
    def __init__(self,name,age):
        '''Initializing name and age attribute  '''
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

'''
The __init__() method at w is a special method 
Python runs automatically whenever we create a new instance based on the 
Dog class.
'''
'''Making an Instance from a Class'''

my_dog = Dog('buchi', 10)
your_dog = Dog('mechal', 12)
print(f"my dog name is {my_dog.name.title()}")
print(f"my dog age is {my_dog.age}")
print(f"my dog name is {your_dog.name.title()}")
print(f"my dog age is {your_dog.age}")
my_dog.sit()
my_dog.roll_over()