import random

playing = True
number = str(random.randint(10, 20))

print("I will generate a number from 10 to 19 and you have to guess the number. The game ends when you get the answer correct")

while playing:
    guess = input("Guess a number")
    if number == guess:
        print("You won the game")
        print("The number was", number)
        break
    
    else:
        print("Haha, you are wrong")
        
