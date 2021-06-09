## As part of the 100 days of code, I will be making a simple version of blacjack to play in the terminal



# Step 4: return values - give player option to draw again - A can be 1 or 13
# Step 5: decide when bust
# Step 6: dealers turn
# Step 7: game logic

# Step 1: create deck
suits = ["c", "d", "h", "s"]
card_names = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
cards = []
for card in card_names:
    for suit in suits:
        cards.append(card+suit)
card_values = {}
for card in cards:
    if card[0] == "J" or card[0] == "Q" or card[0] == "K" or card[0] == "A":
        card_values[card] = 10
    else:
        card_values[card] = int(card[0])
print(card_values)

import random
# Step 2: deal cards
def deal_cards():
    pass