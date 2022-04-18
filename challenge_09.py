def challenge_09():
  """Love calculator"""
  # Use the word LOVES To calculate the % of love untill 2 number left
  # Example, L = 1, O = 1, V = 0, E = 1, S = 2 = 11012 => (1 + 1, 1 + 0, 0 + 1, 1 + 2) = 2113 => (2 + 1, 1 + 1, 1 + 3) = 324
  # => (3 + 2, 2 + 4) = 56%
  your_name = list(input('Your name: ').upper())
  crush_name = list(input('Crush name: ').upper())
  LOVES = {"L": 0, "O": 0, "V": 0, "E": 0, "S": 0}
  for i in "LOVES":
    if i in your_name:
      LOVES[i] += 1
    if i in crush_name:
      LOVES[i] += 1
  str_value = ""
  for v in LOVES.values():
    str_value += str(v)
  # "12010"
  for _ in range(3):
    new_value = ""
    for i in range(len(str_value) - 1):
      new_value += str(int(str_value[i]) + int(str_value[i+1]))
    str_value = new_value
  print(f"\nYour love percent is {str_value}%")
