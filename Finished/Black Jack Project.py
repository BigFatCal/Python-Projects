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

            dealt_cards.append(cards.pop())
            dealt_count += 1
    
        return dealt_cards[0], dealt_cards[1]

    def deal_one_card(self):

        random_card = cards.pop()

        return random_card

    def hit(self, choice):

        if choice[0].lower() == "h":
            extra_card = self.deal_one_card()
            return extra_card

# Getting card values
def get_card_value(card):

    return card_values[card]

# Replay function 
def replay():
  ans = input("Would you like to play again? ")
  if ans[0].lower() == "y":
    return True
  else:
    return False


# Start of play and game logic
start = input("Weclome to Blackjack! Are you ready to play?(y/n) ")
playing = False

if start[0].lower() == "n":
    print("Nevermind, come back another day")
else:
    playing = True

dealer = Player("Dealer")
user = Player(input("What is your name? "))

if playing == True:

    random.shuffle(cards)

    dealer_starting = dealer.deal_one_card()
    user_starting = user.deal_two_cards()

    user_count = 0
    dealer_count = 0

    dealer_count += get_card_value(dealer_starting) 
    user_count += get_card_value(user_starting[0]) 
    user_count += get_card_value(user_starting[1])
    print("Your starting hand: {}, {}\nYour starting count: {}".format(user_starting[0], user_starting[1], str(user_count)))
    print("Dealer shows: {}".format(dealer_starting))

while playing:
    
    if user_count == 21:
        print("Winner Winner Chicken Dinner!")
        playing = False

    elif user_count > 21:
        print("You've bust! Loser.")
        playing = False

    else: 
        user_turn = True 

        while user_turn:

            user_choice = input("Hit or stick? ")

            if user_choice[0].lower() == "h":

                print("You chose hit!") 
                next_card = user.deal_one_card()
                print("You've been dealt the: " + next_card)
                
                # Checking for an ace, if so, only adding 1 instead of 11
                if get_card_value(next_card) == 11 and user_count >= 11:
                    user_count += 1
                else:
                    user_count += get_card_value(next_card)
                    print("Your count: " + str(user_count))

                if user_count > 20:
                    if user_count == 21:
                        print("Winner Winner Chicken Dinner!")
                        playing = False
                        break
                    else:

                        print("You've bust! Loser.")
                        playing = False
                        break

            else:
                print("You chose stick!")
                print("Your final count: " + str(user_count))
                break
        
        # Dealers turn 
        if user_count < 21:
            while dealer_count < 22 or dealer_count < user_count:

                next_dealer_card = dealer.deal_one_card()

                if get_card_value(next_dealer_card) == 11 and dealer_count >= 11:
                    dealer_count += 1
                else:
                    dealer_count += get_card_value(next_dealer_card)
                    print("The dealer drew {}\nDealer count: {}".format(next_dealer_card, str(dealer_count)))
                
                

            if dealer_count > 22:

                print("The dealer bust! You win!")
               

            else:

                print("You beat the house! Well done!")
                

    if replay():
        user_count = 0
        dealer_count = 0
        print("\nCool! Let's go again!")
    else:
        print("\nOkay, maybe another time!")
        playing = False
        break        
        
   