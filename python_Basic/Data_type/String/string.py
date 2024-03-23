#A string is simply a series of characters. Anything inside quotes is considered a string in Python,
#Changing Case in a String with Methods
name = 'tinsae abreham'
print(name.title())
print(name.upper())
print(name.lower())
print(' ')
#Combining or Concatenating Strings
#Python uses the plus symbol (+) to combine strings.

first_name = 'tinsae'
last_name = 'abreham'
full_name = first_name + " " + last_name
print(full_name.upper())
print(' ')

# Adding Whitespace to Strings with Tabs or Newlines
#using tab
print('python')
print('\tpython')
#using new line
print('language: \nC\npython\nc++')
print(' ')
#Stripping Whitespace
# To ensure that no whitespace exists at the right end of a string, use the rstrip() method.
favorite_language = 'python '
print(favorite_language)
favorite_languagee = favorite_language.strip()
print(favorite_languagee)
