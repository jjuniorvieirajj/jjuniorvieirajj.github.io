# create a simple game rock paper scissors
# provide welcome message
# get the user's choice
# get the computer's choice
# compare the choices and determine the winner
# print the result of the game
# ask the user if they want to play again
# say goodbye if they don't want to play again
# use once function to handle the game logic

import random

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock Paper Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print(f"You chose {user_choice}. Computer chose {computer_choice}. {result}")

def main():
    play_game()
    while input("Do you want to play again? (yes/no): ").lower() == "yes":
        play_game()
    print("Goodbye!")

if __name__ == "__main__":
    main()