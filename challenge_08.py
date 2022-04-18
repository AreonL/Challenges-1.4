import requests
import json
import numpy as np

def challenge_08():
  """Hangman"""
  url = 'https://random-word-api.herokuapp.com/word'
  res = requests.get(url)
  word = list(json.loads(res.text)[0].upper())
  lives = 6
  word_display = ['_'] * len(word)
  guesses = []
  while True:
    print(f'\nGuesses left: {lives}')
    print('\nWord:', " ".join(word_display))
    print('Misses:', ", ".join(guesses))
    user_letter = input('Guess: ').upper()
    if user_letter in word:
      values = np.array(word)
      corr_index = np.where(values == user_letter)[0]
      for i in corr_index:
        word_display[i] = user_letter
      if '_' not in word_display:
        print("\nThe word is:", "".join(word))
        print('You win!')
        break
    else:
      guesses.append(user_letter)
      lives -= 1
      if lives == 0:
        print("You lost!")
        print("The word was:", "".join(word))
        break
