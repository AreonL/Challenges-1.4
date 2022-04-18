import random

def challenge_02():
  conv = input("Convert to F or C?: ").upper()
  numb = float(input("What degree?: "))
  if conv == 'F':
    print(f'{numb} degrees F is {(numb - 32) * 5/9} degrees C')
  elif conv == 'C':
    print(f'{numb} degrees C is {(numb * 9/5) + 32} degrees F')
  else:
    print("Invalid input")