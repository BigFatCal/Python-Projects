# Step 1: create deck - created this whilst doing blackjack project.
suits = ["c", "d", "h", "s"]
card_names = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
cards = []
for card in card_names:
    for suit in suits:
        cards.append(card+suit)


# Again, taken this from blackjack projec
import random

class Player():

    def __init__(self, name):
        self.name = name

    def deal_cards(self):

        dealt_cards = []
        dealt_count = 0

        while dealt_count < 2:
            random_num = random.randint(1, len(cards)+1)
            random_card = cards.pop(random_num)
            dealt_cards.append(random_card)
            dealt_count += 1
    
        print("{}: {}, {}".format(self.name, dealt_cards[0], dealt_cards[1]))
        return dealt_cards