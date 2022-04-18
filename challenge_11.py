import random

def challenge_11():
  """Password Generator"""
  # atleast 10 length
  # atleast 1 uppercase
  # atleast 1 lowercase
  # atleast 1 number
  # atleast 1 special character
  letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  special_characters = "!@#$%^&*()_+"
  numbers = "1234567890"
  everything = letters + special_characters + numbers
  while True:
    password = ""
    for _ in range(10):
      password += random.choice(everything)
    upper = False
    lower = False
    number = False
    special = False
    for i in password:
      if i.isupper():
        upper = True
      if i.islower():
        lower = True
      if i in numbers:
        number = True
      if i in special_characters:
        special = True

    if upper and lower and number and special:
      print(f"Your password is: {password}")
      break
