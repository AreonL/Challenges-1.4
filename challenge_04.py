letters_encrypt = "abcdefghijklmnopqrstuvwxyz"
letters_decrypt = "zyxwvutsrqponmlkjihgfedcba"

def challenge_04():
  choice = input("Encrypt or Decrypt?: ").lower()
  word = input("What word to encrypt?: ").lower()
  res = ''
  if choice == "encrypt":
    letters = list(word)
    for i in letters:
      index = letters_encrypt.index(i)
      res += letters_decrypt[index]
    print(res)
  elif choice == "decrypt":
    letters = list(word)
    for i in letters:
      index = letters_decrypt.index(i)
      res += letters_encrypt[index]
    print(res)
  else:
    print("Invalid input")
