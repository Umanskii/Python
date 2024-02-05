#simple program to calculate the down payment

# Get user input for house price and credit score
name = input("Enter your full name: ")
price = int(input("Enter the house price: "))
credit_score = int(input("Enter your credit score: "))

# Check the credit score and provide a response
if credit_score >= 700:
    print(f"{name} Congratulations! You have good credit.")
    downpayment = price * 0.1  # 10% down payment for good credit
else:
    print(f"{name} Sorry, your credit score is below the threshold for good credit.")
    downpayment = price * 0.2  # 20% down payment for lower credit

print(f"Dear {name}, your Down payment is ${downpayment}")

    