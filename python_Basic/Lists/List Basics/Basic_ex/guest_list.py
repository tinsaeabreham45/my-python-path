# Q1
'''
Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
'''
# Q2
'''
Changing Guest List: You just heard that one of your guests can’t make the 
dinner, so you need to send out a new set of invitations. You’ll have to think of 
someone else to invite.
•	 Start with your program from Exercise 3-4. Add a print statement at the 
end of your program stating the name of the guest who can’t make it.
•	 Modify your list, replacing the name of the guest who can’t make it with 
the name of the new person you are inviting.
•	 Print a second set of invitation messages, one for each person who is still 
in your list.
'''
# Q3
'''
More Guests: You just found a bigger dinner table, so now more space is 
available. Think of three more guests to invite to dinner.
•	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a 
bigger dinner table.
•	 Use insert() to add one new guest to the beginning of your list.
•	 Use insert() to add one new guest to the middle of your list.
•	 Use append() to add one new guest to the end of your list.
•	 Print a new set of invitation messages, one for each person in your list.

'''
print('\t\t\t INVITATION CARD')
person = ['tewodros','tiliksew','tibebe']
print(person)
print('')
card = 'Would you like to join me for dinner ' + person[0].title()
print(card)
card = 'Would you like to join me for dinner ' + person[1].title()
print(card)
card = 'Would you like to join me for dinner ' + person[2].title()
print(card)
print(' ')
print(person[1].title() + ' can\'t make it')
print(' ')
person.append('tinsae')
person.remove('tiliksew')
print('Updated List')
print(person)
card = 'Would you like to join me for dinner ' + person[0].title()
print(card)
card = 'Would you like to join me for dinner ' + person[1].title()
print(card)
card = 'Would you like to join me for dinner ' + person[2].title()
print(card)
print(' ')
print('i found more friends to came')
person.insert(0,'habib')
person.insert(1, 'kedus')
person.append('yakob')
print('')
print('Updated Lists')
print(person)
print('')
card = 'Would you like to join me for dinner ' + person[0].title()
print(card)
card = 'Would you like to join me for dinner ' + person[1].title()
print(card)
card = 'Would you like to join me for dinner ' + person[2].title()
print(card)
card = 'Would you like to join me for dinner ' + person[3].title()
print(card)
card = 'Would you like to join me for dinner ' + person[4].title()
print(card)
card = 'Would you like to join me for dinner ' + person[5].title()
print(card)
print(' ')
print('Sorry! You Can Only Invite 2 Person')

remove_1 = person.pop(0)
print(remove_1 + ' has been removed')
remove_2 = person.pop(3)
print(remove_2 + ' has been removed')
remove_3 = person.pop(1)
print(remove_3 + ' has been removed ')
remove_4 = person.pop(2)
print(remove_4 + ' has been removed')
print(' ')
print('Updated List')
print(person)
print(' ')
card = 'Would you like to join me for dinner ' + person[0].title()
print(card)
card = 'Would you like to join me for dinner ' + person[1].title()
print(card)
print(' ')
print(str(len(person)) + ' person  are invited ')
print('\t\t\tGETTING PLEASE!')

