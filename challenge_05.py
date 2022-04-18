def challenge_05():
  for i in range(1, 100):
    res = ''
    if i % 3 == 0:
      res += "Fizz"
    if i % 5 == 0:
      res += "Buzz"
    if len(res):
      print(res)
    else:
      print(i)
  input("\nPress Enter to continue...")
