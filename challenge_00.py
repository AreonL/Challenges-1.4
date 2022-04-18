import random

def challenge_00():
  """This challenge makes no sense lmao"""
  letters = 'abcdefghijklmnopqrstuvwxyz'
  vowels = 'aeiou'
  input_string = input("How many letters?: ")
  name = ''
  for i in range(int(input_string)):
    if i == 0:
      index = random.randint(0, len(vowels) - 1)
      name += vowels[index].upper()
    else:
      index = random.randint(0, len(letters) - 1)
      name += letters[index]
  print(f'Your new name is: {name}')