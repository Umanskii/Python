# Game beta version 1. added exit code with brake, 2. 

import random

def play():
    results = []  # List to store game results

    while True:
        user = input("\nChoose: 'r' for rock, 'p' for paper, 's' for scissors, or 'q' to quit: ").lower()
        
        if user == 'q': # Exit game
            print("\nGame Over! Here are your results:")
            print_results(results)
            break

        if user not in ['r', 'p', 's']: # !!! maybe add another List here with some txt
            print("Invalid choice! Please choose 'r', 'p', or 's'.")
            continue

        computer = random.choice(['r', 'p', 's']) # ??? add List here?

        print(f"\nYou chose {user}, and the computer chose {computer}.")

        if user == computer:
            result = "Tie"
            print("It's a tie!")
        elif is_win(user, computer):
            result = "Win"
            print("You won!")
        else:
            result = "Loss"
            print("You lost!")

        # Store the result . 
        results.append((user, computer, result))

def is_win(player, opponent):
    """Return True if the player wins against the opponent"""
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

def print_results(results):
    """Prints a summary of the game results"""
    wins = sum(1 for _, _, result in results if result == "Win")
    losses = sum(1 for _, _, result in results if result == "Loss")
    ties = sum(1 for _, _, result in results if result == "Tie")

    print(f"\nTotal Games Played: {len(results)}")
    print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")

    print("\nDetailed Game History:")
    for i, (user, computer, result) in enumerate(results, 1):
        print(f"Game {i}: You chose {user}, Computer chose {computer} → {result}")

# Start the game
play()
