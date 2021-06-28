# creating the symbols

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to rock paper scissors!\nTry and beat the computer in a best of 3 game!\n")

#getting the user pick
def user_pick():
  accepeted = False
  while accepeted == False:
    user_input = input("Rock, paper or scissors? ")

    if user_input[0].lower() == "s":
      print("You chose scissors!")
      print(scissors)
      accepeted = True
      return scissors

    elif user_input[0].lower() == "r":
      print("You chose rock!")
      accepeted = True
      print(rock)
      return rock

    elif user_input[0].lower() == "p":
      print("You chose paper!")
      accepeted = True
      print(paper)
      return paper

    else:
      print("That's not a valid choice! Please try again!")
    
import random

#randomly getting the computers choice
def computer_choice():
  x = random.randint(1,3)
  if x == 1:
    print("The computer chose scissors!")
    print(scissors)
    return scissors
  elif x == 2:
    print("The computer chose rock!")
    print(rock)
    return rock
  else:
    print("The computer chose paper!")
    print(paper)
    return paper


#function to decide who wins!
def decide_winner(your_pick, computer_pick):
  
  if your_pick == scissors:
    if computer_pick == scissors:
      who_won = "Draw"
      return who_won
    elif computer_pick == rock:
      who_won = "The computer won"
      return who_won
    elif computer_pick == paper:
      who_won = "You won"
      return who_won

  elif your_pick == rock:
    if computer_pick == scissors:
      who_won = "You won"
      return who_won
    elif computer_pick == rock:
      who_won = "Draw"
      return who_won
    elif computer_pick == paper:
      who_won = "The computer won"
      return who_won
    
  elif your_pick == paper:
    if computer_pick == scissors:
      who_won = "The computer won"
      return who_won
    elif computer_pick == rock:
      who_won = "You won"
      return who_won
    elif computer_pick == paper:
      who_won = "Draw"
      return who_won

# replay function

def replay():
  ans = input("Would you like to play again? ")
  if ans[0].lower() == "y":
    return True
  else:
    return False
  

# game logic

game_on = True
user_wins = 0
computer_wins = 0
while game_on:
  while (user_wins + computer_wins) < 3:
    output = "{}!".format(decide_winner(user_pick(), computer_choice()))
    print(output)
    if output == "Draw!":
      print("No one gets a point :(")
    elif output == "You won!":
      user_wins += 1
      print("Your points: {}\nComputer points: {}".format(str(user_wins), str(computer_wins)))
    else:
      computer_wins += 1
      print("Your points: {}\nComputer points: {}".format(str(user_wins), str(computer_wins)))

  if computer_wins > user_wins:
      print("\nThe computer won! Better luck next time\n")
  else:
      print("\nYou won! Well done!\n")

  if replay():
    user_wins = 0
    computer_wins = 0
    print("\nCool! Let's go again!")
  else:
    print("\nOkay, maybe another time!")
    break