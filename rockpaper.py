import random

print("\nWELCOME TO THE ROCK, PAPER, SCISSORS GAME! \nYour choices are- rock, paper, scissors. \nType quit when you want to leave the game")
choices=['rock', 'paper', 'scissors']

points_user = []
points_computer = []

while True:
    user = input("You: ")
    if user == 'quit':  # Check for quit condition first
        break
        
    computer = random.choice(choices)  # Removed 'quit' from computer's choices
    print("Robo X: ", computer)
    
    
    if user =='rock':
        if computer=='rock':
            print("it's a tie")
            print("you: ", points_user, "robo X: ", points_computer)
        elif computer=='paper':
            print(f"{computer} beats {user}.")
            points_computer.append(1)
            print("you: ", points_user, "robo X: ", points_computer)
        elif computer=='scissors':
            print(f"{user} beats {computer}")
            points_user.append(1)
            print("you: ", points_user, "robo X: ", points_computer)
    elif user =='paper':
        if computer=='paper':
            print("it's a tie")
            print("you: ", points_user, "robo X: ", points_computer)
        elif computer=='scissors':
            print(f"{computer} beats {user}.")
            points_computer.append(1)
            print("you: ", points_user, "robo X: ", points_computer)
        elif computer=='rock':
            print(f"{user} beats {computer}")
            points_user.append(1)
            print("you: ", points_user, "robo X: ", points_computer)
    elif user =='scissors':
        if computer=='scissors':
            print("it's a tie")
            print("you: ", points_user, "robo X: ", points_computer)
        elif computer=='rock':
            print(f"{computer} beats {user}.")
            points_computer.append(1)
            print("you: ", points_user, "robo X: ", points_computer)
        elif computer=='paper':
            print(f"{user} beats {computer}")
            points_user.append(1)
            print("you: ", points_user, "robo X: ", points_computer)

    