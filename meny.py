from challenges import *

def main():
  choice = input("\n\nSelect new challenge: ")
  match choice:
    case '0' | '00':
      challenge_00()
    case '1' | '01':
      challenge_01()
    case '2' | '02':
      challenge_02()
    case '3' | '03':
      challenge_03()
    case '4' | '04':
      challenge_04()
    case '5' | '05':
      challenge_05()
    case '6' | '06':
      challenge_06()
    case '7' | '07':
      challenge_07()
    case '8' | '08':
      challenge_08()
    case '9' | '09':
      challenge_09()
    case '10':
      challenge_10()
    case '11':
      challenge_11()
    case '12':
      challenge_12()
    case '13':
      challenge_13()
    case '14':
      challenge_14()
    case '15':
      challenge_15()
    case '16':
      challenge_16()
    case '17':
      challenge_17()
    case '18':
      challenge_18()
    case '19':
      challenge_19()
    case '20':
      challenge_20()


  print("\n")


if __name__ == '__main__':
  main()