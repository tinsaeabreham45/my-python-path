'''Make a list of magician’s names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list.
'''

def show_magicians(magician_name):
    for magician in magician_name:
        print(magician)

magician_name = ['ali','sortu','nahod','delcarl']
show_magicians(magician_name)
