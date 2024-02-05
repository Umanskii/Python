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

def calculate_loan_amount(price, downpayment):
    return price - downpayment

def get_loan_details():
    loan_term = int(input("Enter the loan term (in years): "))
    annual_interest_rate = float(input("Enter the annual interest rate (%): "))
    return loan_term, annual_interest_rate

def calculate_monthly_payment(loan_amount, loan_term, annual_interest_rate):
    monthly_interest_rate = annual_interest_rate / (12 * 100)
    num_payments = loan_term * 12
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)
    return monthly_payment

def main():
    name, price, credit_score = get_user_input()
    downpayment_percentage = check_credit_score(name, credit_score)
    downpayment = calculate_downpayment(price, downpayment_percentage)
    
    print(f"Dear {name}, your down payment is ${downpayment}")
    
    loan_amount = calculate_loan_amount(price, downpayment)
    print(f"Loan amount: ${loan_amount}")
    
    loan_term, annual_interest_rate = get_loan_details()
    monthly_payment = calculate_monthly_payment(loan_amount, loan_term, annual_interest_rate)
    print(f"Your monthly mortgage payment is: ${monthly_payment:.2f}")

if __name__ == "__main__":
    main()
