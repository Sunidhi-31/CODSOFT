import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        display_result(user_choice, computer_choice, winner)
        print(f"\nCurrent Scores: You - {user_score} | Computer - {computer_score}")
        
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing! Final Scores:")
            print(f"You - {user_score} | Computer - {computer_score}")
            break

if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors Game!")
    play_game()
