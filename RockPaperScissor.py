import random

def get_user_choice():
    choice = input("Rock, paper, or scissors? ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice.")
        choice = input("Rock, paper, or scissors? ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win the game!")
            user_score += 1
        else:
            print("The Computer wins!")
            computer_score += 1

        print(f"\nScore -> You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing the game!!")
            break

if __name__ == "__main__":
    main()
