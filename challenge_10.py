import random
import requests
import json

def challenge_10():
  """Random sentence generator (defined word)"""
  url = 'https://random-word-api.herokuapp.com/word'
  # url2 = 'https://wordsapiv1.p.mashape.com/words/' # This api sucks.. 2500 per day.. yeah sure bud..
  res = requests.get(url)
  word = json.loads(res.text)[0].lower().capitalize()
  if random.randint(0, 1) == 0:
    print(f'\"{word}\" is an amazing word!')
  else:
    print(f'\"{word}\" is not that good of a word..')