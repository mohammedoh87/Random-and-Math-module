import random
while True:
    user_action = input("ENter a choice from rock or paper or scissor ")
    possible_actions = ["rock", "scissor", "paper"]
    computer_action = random.choice(possible_actions)
    print(f"You chose {user_action} and the computer chose {computer_action}")
    
    if user_action == computer_action:
        print("It is the tie")
    elif user_action == "rock":
        if computer_action == "scissor":
            print("You won")
        else:
            print("You lose")
    elif user_action == "paper":
        if computer_action == "rock":
            print("You won")
        else:
            print("You lose")
    elif user_action == "scissor":
        if computer_action == "paper":
            print("You won")
        else:
            print("You lose")
    play_again = input("Do you want to play again Y, N: ")
    if play_again != "Y":
        break

