def challenge_19():
  """Count words in a string"""
  string = input("Enter a string: ")
  words = string.split()
  print("Words:", len(words))
  count = 0
  for i in words:
    for j in i:
      count += 1
  print("Count:", count)
