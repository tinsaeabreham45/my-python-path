'''
Develop a program where the computer generates a random number between 1 and 100, and the user has to guess the number.
Provide hints like "too high" or "too low" after each guess.
'''
import random
'''
# simple program
random_number = random.randint(1, 10)
chance = 0
while True:
    user_guess = input('guess the number the number us between 1-10: ')
    user_guess = int(user_guess)
    chance += 1
    if chance == 3:
        print('Sorry you have used all your chances')
        break
    else:
        if user_guess == random_number:
            print('f"Congratulations! You guessed the number' + str(random_number)+ 'in' + str(chance)+ 'chances')
            break
        elif user_guess < random_number:
            print('Too low! Try again.')
        else:
            print("Too high! Try again.")
'''
# updated program
while True:
    secret_number = random.randint(1,20)
    print("Welcome to the Number Guessing Game!")
    print("I've selected a random number between 1 and 100. Try to guess it")
    chance = 0
    max_chance = 3
    while chance < max_chance:
        user_guess = int(input('Your Guess: '))
        chance += 1

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number}  in {chance} attempts.")
            break
        elif user_guess < secret_number:
            print('Too small! try again ')
        else:
            print("Too high! Try again.")
    if chance == max_chance:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
    play_again = input('would you like to play again ? yes/no').lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye.")
        break






































