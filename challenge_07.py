import random

def challenge_07():
  """
  Project Euler, first 10
  """
  def problem_1():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    print("Problem 1: Multiples of 3 and 5")
    sum = 0
    for i in range(1001):
      if i % 3 == 0 or i % 5 == 0:
        sum += i
    print('The anweser is: ', sum, '\n')

  def problem_2():
    """
    Each new term in the Fibonacci sequence is generated by adding the previous two terms.
    By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million,
    find the sum of the even-valued terms
    """
    print("Problem 2: Even Fibonacci numbers")
    first_num = 1
    second_num = 2
    sum = 0
    print_list = [1]
    while second_num < 4000000:
      print_list.append(second_num)
      sum = first_num + second_num
      first_num = second_num
      second_num = sum
    print('The anweser is: ', print_list, '\n')


  def problem_3():
    """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    """
    print("Problem 3: Largest prime factor")

    divide = 2
    num = 600851475143
    list_of_prime = []
    while num > 1:
      if num % divide == 0:
        num = num / divide
        list_of_prime.append(divide)
      else:
        divide += 1
    print('Answer is: ', list_of_prime, '\n')

  def problem_4():
    print("Problem 4: Largest palindrome product")
    """Zzzz"""

  def problem_5():
    print("Problem 5: Smallest multiple")



  def problem_6():
    print("Problem 6: Sum square difference")



  def problem_7():
    print("Problem 7: 10001st prime")



  def problem_8():
    print("Problem 8: Largest product in a series")



  def problem_9():
    print("Problem 9: Special Pythagorean triplet")



  def problem_10():
    print("Problem 10: Summation of primes")



  problem_1()
  problem_2()
  problem_3()
  problem_4()
  problem_5()
  problem_6()
  problem_7()
  problem_8()
  problem_9()
  problem_10()