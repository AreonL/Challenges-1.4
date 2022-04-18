def challenge_18():
  """File explorer"""
  print("Simulate explorer..")
  def menu():
    print("ls | list files and maps in current dir")
    print("cd | change directory")
    print("exit | exit program")
    print("cd .. | go back one directory")

  root = ["file.txt", "file2.txt", "dir/"]
  dir = ["hidden.txt"]
  current_dir = "C:/"
  while True:
    print("You are currently in:", current_dir)
    user_inp = input("Enter command: ")
    if "ls" in user_inp:
      if current_dir == "C:/":
        for i in root:
          print(i)
      else:
        for i in dir:
          print(i)
    elif "cd" in user_inp:
      if user_inp.split(" ")[1] == "dir":
        current_dir += "dir/"
      elif user_inp.split(" ")[1] == "..":
        current_dir = current_dir[:-4]
    elif "exit" in user_inp:
      break
    elif "help" in user_inp:
      menu()
    input("\nPress enter to continue...")