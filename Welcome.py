import time

def animated_welcome():
    message = "Welcome! We're glad to have you here."
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()  # Move to the next line

def personalized_welcome(name):
    print(f"Hello, {name}! Welcome to our platform.")

def main():
    animated_welcome()
    name = input("Please enter your name: ")
    personalized_welcome(name)

if __name__ == "__main__":
    main()
