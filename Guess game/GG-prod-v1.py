import random

def ai_guess(x):
    """AI tries to guess the number chosen by the user."""
    low = 1
    high = x
    feedback = ''
 
    print(f"Think of a number between {low} and {high}, and I'll try to guess it!")
    
    while feedback != 'c':
        if low != high:
            guess = (low + high) // 2  # More efficient binary search
        else:
            guess = low  # Only one number left
        
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c':
            print("Please enter 'H', 'L', or 'C' only.")
    
    print(f'Yay! The AI guessed your number, {guess}, correctly!')

def user_guess(x):
    """User tries to guess the number randomly chosen by the AI."""
    number = random.randint(1, x)
    guess = 0
    
    print(f"I have chosen a number between 1 and {x}. Try to guess it!")
    
    while guess != number:
        try:
            guess = int(input("Enter your guess: "))
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    print(f"Congratulations! You guessed the number {number} correctly!")

def main():
    """Main function to choose game mode."""
    print("Welcome to the Number Guessing Game!")
    print("1: AI guesses your number")
    print("2: You guess the AI's number")
    
    choice = input("Enter 1 or 2 to select a mode: ")
    
    while choice not in ['1', '2']:
        choice = input("Invalid choice! Please enter 1 or 2: ")
    
    x = int(input("Enter the maximum number for the range (e.g., 100): "))
    
    if choice == '1':
        ai_guess(x)
    else:
        user_guess(x)

# Run the game
main()
