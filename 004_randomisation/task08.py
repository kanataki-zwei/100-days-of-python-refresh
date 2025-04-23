# rock paper scissors
import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
moves = ['rock', 'paper', 'scissors']
program_choice = random.choice(moves)
player_choice = input("Welcome to Rock Paper Scissors.\n Select 1 for Rock, 2 for Paper, and 3 for Scissors: ")

if player_choice == '1':
    if program_choice == 'rock':
        print(f"Your move:\n{rock}\nComputer's move:\n{rock}\nGame Draw!")
    elif program_choice == 'paper':
        print(f"Your move:\n{rock}\nComputer's move:\n{paper}\nYou Lose!")
    elif program_choice == 'scissors':
        print(f"Your move:\n{rock}\nComputer's move:\n{scissors}\nYou Win!")
elif player_choice == '2':
    if program_choice == 'rock':
        print(f"Your move:\n{paper}\nComputer's move:\n{rock}\nYou Win!")
    elif program_choice == 'paper':
        print(f"Your move:\n{paper}\nComputer's move:\n{paper}\nGame Draw!")
    elif program_choice == 'scissors':
        print(f"Your move:\n{paper}\nComputer's move:\n{scissors}\nYou Lose!")
elif player_choice == '3':
    if program_choice == 'rock':
        print(f"Your move:\n{scissors}\nComputer's move:\n{rock}\nYou Lose!")
    elif program_choice == 'paper':
        print(f"Your move:\n{scissors}\nComputer's move:\n{paper}\nYou Win!")
    elif program_choice == 'scissors':
        print(f"Your move:\n{scissors}\nComputer's move:\n{scissors}\nGame Draw!")
else:
    print("Please select a valid choice: 1, 2, or 3")