import random

print("enter a number 0-100 to guess the random number generated")
number=random.randint(0,100)
correct=False

while not correct:
  guess=int(input("enter your guess"))
  if(guess==number):
    correct=True
  elif(guess>number):
    print("guess too high")
  else:
    print("guess too low")
  
