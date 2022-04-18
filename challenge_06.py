import random

def challenge_06():
  """
  Create a function that plays rock, paper, scissors
  """
  chocie_list = ["rock", "paper", "scissors"]
  player = input("Rock, paper or scissors?: ").lower()
  computer = random.choice(chocie_list)
  print(f"You chose: {player}")
  print(f"Computer chose: {computer}")
  index_player = chocie_list.index(player)
  index_computer = chocie_list.index(computer)
  if index_player == index_computer:
    print("It's a tie!")
  elif index_player == 0 and index_computer == 2:
    print("You win!")
  elif index_player == 1 and index_computer == 0:
    print("You win!")
  elif index_player == 2 and index_computer == 1:
    print("You win!")
  else:
    print("You lose!")

