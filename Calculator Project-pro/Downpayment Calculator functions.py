def get_user_input():
    name = input("Enter your full name: ")
    price = int(input("Enter the house price: "))
    credit_score = int(input("Enter your credit score: "))
    return name, price, credit_score

def check_credit_score(name, credit_score):
    if credit_score >= 700:
        print(f"{name}, Congratulations! You have good credit.")
        return 0.1  # 10% down payment for good credit
    else:
        print(f"{name}, Sorry, your credit score is below the threshold for good credit.")
        return 0.2  # 20% down payment for lower credit

def calculate_downpayment(price, downpayment_percentage):
    return price * downpayment_percentage

def main():
    name, price, credit_score = get_user_input()
    downpayment_percentage = check_credit_score(name, credit_score)
    downpayment = calculate_downpayment(price, downpayment_percentage)
    print(f"Dear {name}, your down payment is ${downpayment}")


#if __name__ == "__main__":
    main()