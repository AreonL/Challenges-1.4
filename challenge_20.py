import random


def challenge_20():
  """Minesweeper"""
  # 0.0, 0.1, 0.2, 0.3, 0.4
  # 1.0, 1.1, 1.2, 1.3, 1.4
  # 2.0, 2.1, 2.2, 2.3, 2.4
  # 3.0, 3.1, 3.2, 3.3, 3.4
  # 4.0, 4.1, 4.2, 4.3, 4.4
  # 1 1 _ _ X
  # 1 X _ _ _
  # X _ _ _ _
  # _ _ _ _ _
  # _ _ X _ _
  fields = [['_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_']]
  mine_field = {}
  for i in range(5):
    for j in range(5):
      mine_field[str(i) + str(j)] = '_'
  print(mine_field)
  # mine_field = [['_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_']]

  def display_board():
    display = ""
    display_bombs = ""
    for row in fields:
      display += ' '.join(row) + '\n'
    count = 0
    for i in mine_field.values():
      count += 1
      display_bombs += i + " "
      if count % 5 == 0:
        display_bombs = display_bombs[:-1] + '\n'
    print(chr(27) + "[2J")
    print(display)
    print(display_bombs)

  mine_position = []

  def add_numbers():
    for bomb_xy in mine_position:
      x, y = bomb_xy[0]-1, bomb_xy[1]-1
      temp_y = y
      for _ in range(3):
        y = temp_y
        for _ in range(3):
          if x >= 0 and x <= 4 and y >= 0 and y <= 4:
            if mine_field[str(x)+str(y)] in ('M', 'P', 'F'):
              y += 1
              continue
            else:
              print(x, y, "this", bomb_xy)
              if mine_field[str(x)+str(y)] == '_':
                mine_field[str(x)+str(y)] = "0"
              mine_field[str(x)+str(y)] = str(int(mine_field[str(x)+str(y)]) + 1)
          y += 1
        x += 1

  def gen_bombs():
    display_board()
    choice = "0.0-P" # input("Choose a field to start (eg, 0.0-P): ")
    choice = choice.split("-")
    field_c = choice[0].split(".")
    x, y = int(field_c[0]), int(field_c[1])
    fields[x][y] = choice[1]
    mine_field[str(x) + str(y)] = choice[1]
    count = 0
    while count < 3:
      mine_x = random.randint(0, 4)
      mine_y = random.randint(0, 4)
      if not (x == mine_x and y == mine_y) and (mine_x, mine_y) not in mine_position:
        mine_field[str(mine_x) + str(mine_y)] = 'M'
        mine_position.append((mine_x, mine_y))
        count += 1

    display_board()
    add_numbers()
    display_board()


    # start()

  gen_bombs()

  def start():
    while True:
      display_board()
      choice = "0.1-P" # input("Choose a field to start (eg, 0.0-P): ")
      choice = choice.split("-")
      field_c = choice[0].split(".")
      x, y = int(field_c[0]), int(field_c[1])
      if choice[1] == 'P':
        if mine_field[x][y] == 'M':
          print("You lost!")
          break

      input("Press enter to continue...")

