from datetime import datetime
import time


def challenge_12():
  """Internet time ((S)NTP) aka clock"""
  def current_time():
    print(chr(27) + "[2J")
    print(datetime.now().strftime("%H:%M:%S"))

    time.sleep(1)
    current_time()
  input('\nPress enter to start...')
  current_time()
