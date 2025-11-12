# 1. Settings
import random
player_wins = 0
computer_wins = 0

# 2. Main Code
print("Let's play rock, paper, or scissors")
for i in range(3):
  player_choice = (input("\nChoose one: ").lower())
  choices = ["rock", "paper", "scissors"]
  computer_choice = random.choice(choices)
  print(f"Computer chose: {computer_choice}\n")

  if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
    winner = "Player"
  elif player_choice == computer_choice:
    winner = "Tie"
  else:
    winner = "Computer"

  if winner == "Player":
    player_wins += 1
  elif winner == "Computer":
    computer_wins += 1

  print(f"Current Score - Player: {player_wins}, Computer: {computer_wins}.")

# 3. End
print("Result:")
if player_wins > computer_wins:
  print("\nCongratulations! You won.")
elif player_wins == computer_wins:
  print("\nIt's a tie.")
else:
  print("\nComputer won!")