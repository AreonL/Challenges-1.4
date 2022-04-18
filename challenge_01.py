import random

def challenge_01():
  x = input("Heads or Tails?: ").lower()
  res = random.randint(0, 1)
  if x == 'heads':
    if res == 0:
      print("You win!")
    else:
      print("You lose! It was Tails")
  elif x == 'tails':
    if res == 1:
      print("You win!")
    else:
      print('You lose! It was Heads')
  else:
    print("Invalid input")