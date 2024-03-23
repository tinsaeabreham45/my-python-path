import random

game_word = ['rock', 'paper', 'scissor']

while True:
    random_word = random.choice(game_word)
    print('\nlet us play a game!')
    print('chose the word: ')
    print('rock')
    print('paper')
    print('scissor')
    chance = 0
    max_chance = 3
    while chance < max_chance:
        user_word = input('chose: ')
        # chance += 1
        # win part
        if user_word == 'rock' and random_word == 'scissor':
            print(f"Congratulations! You WIN the Game in {chance} attempts.")
            break
        elif user_word == 'paper' and random_word == 'rock':
            print(f"Congratulations! You WIN the Game in {chance} attempts.")
            break
        elif user_word == 'scissor' and random_word == 'paper':
            print(f"Congratulations! You WIN the Game in {chance} attempts.")
            break
        else:
            print(f'you lose! the word was {random_word}')
    play_again = input('would you like to play again ? yes/no').lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye.")
        break
