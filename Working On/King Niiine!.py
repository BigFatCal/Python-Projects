# Step 1: create deck - created this whilst doing blackjack project.
suits = ["c", "d", "h", "s"]
card_names = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
cards = []
for card in card_names:
    for suit in suits:
        cards.append(card+suit)

# might not need card values for this but it's here just in case
card_values = {}
for card in cards:
    if card[0] == "J" or card[0] == "Q" or card[0] == "K" or card[0] == "A":
        card_values[card] = 10
    else:
        card_values[card] = int(card[0])