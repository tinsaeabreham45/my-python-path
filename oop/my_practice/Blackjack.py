from random import randint


# creating the game class which will hold all game methods and attributes

class Blackjack():
    def __init__(self):
        self.deck = []  # set an empty lists
        self.suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
        self.values = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")

    # Generating the Deck
    # create a method that creates a deck of 52 cards, each card
    # should be a tuple with a value and suit
    def make_deck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append((value, suit))

    # Pulling a Card from the Deck
    def pull_card(self):
        return self.deck.pop(randint(0, len(self.deck) - 1))


# Creating a Player Class

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []

    # Adding Cards to the Player’s Hand
    def add_card(self, card):
        self.hand.append(card)

    # Showing a Player’s Hand
    def show_hand(self, dealer_start=True):
        print(f"\n{self.name}")
        print('#########')
        for i in range(len(self.hand)):
            if self.name == 'dealer' and i == 0 and dealer_start:
                print("- of - ")
            else:
                card = self.hand[i]
                print(f"{card[0]} of {card[1]}")

    # Calculating the Hand Total
    def calculate_hand(self, dealer_start=True):
        total = 0
        aces = 0
        card_values = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9,
                       10: 10, "J": 10, "Q": 10, "K": 10, "A": 11}

        if self.name == 'dealer' and dealer_start:
            card = self.hand[1]
            return card_values[card[0]]

        for card in self.hand:
            if card[0] == 'A':
                aces += 1

            else:
                total += card_values[card[0]]
        for i in range(aces):
            if total + 11 > 21:
                total += 21

            else:
                total += 11
        return total


game = Blackjack()
game.make_deck()
name = input('what is your name: ')
player = Player(name)
dealer = Player('dealer')
for i in range(2):
    player.add_card(game.pull_card())
    dealer.add_card(game.pull_card())

player.show_hand()
dealer.show_hand()
# Handling the Player’s Turn

player_bust = False
while input("Would you like to stay or hit?").lower() != "stay":
    # pull card and put into player's hand
    player.add_card(game.pull_card())
    # show both hands using method
    player.show_hand()
    dealer.show_hand()
    # # check if over 21
    if player.calculate_hand() > 21:
        player_bust = True
        print('you lose!')
        break  # break out of the player's loop

# Handling the Dealer’s Turn

dealer_bust = False
if not player_bust:
    while dealer.calculate_hand() < 17:
        # pull card and put into player's hand
        dealer.add_card(game.pull_card())
        # # check if over 21
        if dealer.calculate_hand() > 21:
            dealer_bust = True
            print('you Win!')
            break  # break out of the dealer's loop

