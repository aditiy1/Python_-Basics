import random
num=random.randint(1,10)
print(num)

guess=int(input("guess a number between 1 and 10: "))

while guess != num:
  if guess < num:
    print("your guess was lower than the number!")
    guess=int(input("Guess again: "))
    guess=guesses+1
  elif guess > num
    print("your guess was higher than the number!")
  guess=int(input("Guess again: "))
  guess=guesses+1

print("Congrats! You guessed the number!")
  