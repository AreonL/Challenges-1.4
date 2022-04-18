def challenge_15():
  """Collatz conjecture"""
  start = int(input('\nEnter a starting number: '))
  count = 0
  while start != 1:
    if start % 2 == 0:
      start = int(start / 2)
    else:
      start = (start * 3) + 1
    count += 1
    print('Nr ' + str(count) + ':', start)
