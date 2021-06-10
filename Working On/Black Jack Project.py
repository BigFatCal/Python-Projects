## As part of the 100 days of code, I will be making a simple version of blacjack to play in the terminal

import random
# Creating deck in a visual way
suits = [" of Clubs", " of Diamonds", " of Hearts", " of Spades"]
card_names = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
cards = []
for card in card_names:
    for suit in suits:
        cards.append(card+suit)

# Assigning corresponding values to each card
card_values = {}
for card in cards:
    if card[0] == "J" or card[0] == "Q" or card[0] == "K" or card[0] == "A":
        card_values[card] = 10
    else:
        card_values[card] = int(card[0])

# Creating a player class, so each function can be called easier and more efficiently
class Player():

    def __init__(self, name):
        self.name = name

    def deal_two_cards(self):

        dealt_cards = []
        dealt_count = 0

        while dealt_count < 2:
            random_num = random.randint(1, len(cards)+1)
            random_card = cards.pop(random_num)
            dealt_cards.append(random_card)
            dealt_count += 1
    
        print("{}: {}, {}".format(self.name, dealt_cards[0], dealt_cards[1]))
        return dealt_cards[0], dealt_cards[1]

    def deal_one_card(self):

        random_num = random.randint(1, len(cards)+1)
        random_card = cards.pop(random_num)
        print("{} pulled: {}".format(self.name, random_card))
        return random_card

    def hit(self, choice):

        if choice[0].lower() == "h":
            extra_card = self.deal_one_card()
            return extra_card

# Carry on in the morning good sir.

class CardsInPlay():

    def __init__(self, card_name):

        self.holding = card_name

    def card_value(self):

        pass

