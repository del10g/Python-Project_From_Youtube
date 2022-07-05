from gc import DEBUG_UNCOLLECTABLE
import random

def guess(x):
  random_number = random.randint(1,x)
  guess = 0
  print(random_number)
  while guess != random_number:
    guess = input("Enter a number between 1 - {}".format(x))

guess(100)