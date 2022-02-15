# Importing modules
import random

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
  # Possible scenarios
  # rock_win =[scissors] 
  # rock_loose = [paper]
  
  # scissors_win =[paper]
  # scissors_loose =[rock]
  
  # paper_win =[scissors]
  # paper_loose =[rock]

#Write your code below this line 👇
guess = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if guess >= 3 or guess < 0:
  print("You typed and invalid number, You lose!")
else:
  AI_guess = random.randint(0, 2)
  
  Tools = [rock, paper, scissors]
  decision = Tools[guess]
  
  AI_decision = Tools[AI_guess]
    
  print("You choose\n" + decision + "\nComputer guess is\n" + AI_decision)
  if (AI_decision == rock):
    if decision == scissors:
      print("You lose")
    elif decision == paper:
      print("You win")
    else:
      print("It's a drawn")
  
  if (AI_decision == scissors):
    if decision == paper:
      print("You lose")
    elif decision == rock:
      print("You win")
    else:
      print("It's a drawn")
  
  if (AI_decision == paper):
    if decision == rock:
      print("You lose")
    elif decision == scissors:
      print("You win")
    else:
      print("It's a drawn")
