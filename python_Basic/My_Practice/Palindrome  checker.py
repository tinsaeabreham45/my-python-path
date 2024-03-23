user_word = input('enter a word to check: ')
if user_word == user_word[::-1]:
    print('the word is Palindrome.')
else:
    print('it is not Palindrome word')
