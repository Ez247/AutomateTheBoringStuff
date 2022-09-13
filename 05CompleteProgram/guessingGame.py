#Guess the number of Game

import random
print("Hello, whats your name?")

name = input()
secretNumber = random.randint(0, 20)
print(f"Well, {name}, I'm thinking of a number between 0 and 20.")

#Ask the player to make six guesses
for guessesTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())
    
    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break
    
if guess == secretNumber:
    print(F"Good job, {name}!. You guessed my number in {guessesTaken} guesses.")
else:
    print(f"Nope. The number I was thinking of was {secretNumber}.")  

        
        