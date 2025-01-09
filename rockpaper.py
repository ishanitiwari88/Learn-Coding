import random

def get_user_choice():
    while True:
        choice = input("You: ").lower().strip()
        if choice in ['rock', 'paper', 'scissors', 'quit']:
            return choice 
        else:
            print("invalid input")
            
def get_winner(user_choice, computer_choice):
    if user_choice==computer_choice:
        return "tie"
    
    winning_moves = {
        'rock':'scissors',
        'paper':'rock',
        'scissors':'paper'
    }
    
    if winning_moves[user_choice]==computer_choice:
        return "user"
    return "computer"
    
def get_scores(user_score, computer_score):
    print(f"Scores- You: {user_score} | Robo: {computer_score}")
    
def main():

    print("\nWELCOME TO THE ROCK, PAPER, SCISSORS GAME! \nYour choices are- rock, paper, scissors. \nType quit when you want to leave the game")

    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        if user_choice == 'quit':  # Check for quit condition first
            break
        
        computer_choice = random.choice(['rock', 'paper', 'scissors'])  
        print("Robo X: ", computer_choice)
        
        result = get_winner(user_choice, computer_choice)
        
        if result=='tie':
            print("It's a tie!")
        elif result=="user":
            print(f"{user_choice} beats {computer_choice}")
            user_score += 1
        elif result=="computer":
            print(f"{computer_choice} beats {user_choice}")
            computer_score += 1
        get_scores(user_score, computer_score)
        print()
   
    print("\nFinal Score:")
    get_scores(user_score, computer_score)
  
if __name__ == "__main__":
    main()

    
