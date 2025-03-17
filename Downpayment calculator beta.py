def get_user_input():
    name = input("Enter your full name: ")
    price = int(input("Enter the house price: "))
    credit_score = int(input("Enter your credit score: "))
    has_cosigner = input("Do you have a co-signer? (yes/no): ").lower() == "yes"
    return name, price, credit_score, has_cosigner


def check_credit_score(name, credit_score):
    if credit_score >= 700:
        print(f"{name}, Congratulations! You have good credit.")
        return 0.1  # 10% down payment for good credit
    elif 500 <= credit_score < 700:
        print(f"{name}, Your credit score is below the threshold for good credit.")
        return 0.2  # 20% down payment for fair credit
    else:
        message = (
        f"Dear {name},\n"
        "We appreciate your interest in a home loan. After careful consideration,\n"
        "we regret to inform you that your loan application has been declined due to a credit score below our minimum requirements.\n"
        "We understand that financial situations can vary, and we encourage you to work on improving your credit score over time.\n"
        "If you have any questions or need assistance, please don't hesitate to reach out to us.\n"
        "Thank you for considering us for your home financing needs."
    )
    print(message)
    exit()


def calculate_downpayment(price, downpayment_percentage):
    return price * downpayment_percentage


def apply_cosigner_discount(downpayment, has_cosigner):
    if has_cosigner:
        return downpayment * 0.1  # 10% discount for having a co-signer
    return 0


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
    name, price, credit_score, has_cosigner = get_user_input()
    downpayment_percentage = check_credit_score(name, credit_score)
    downpayment = calculate_downpayment(price, downpayment_percentage)

    cosigner_discount = apply_cosigner_discount(downpayment, has_cosigner)
    downpayment -= cosigner_discount

    print(f"Dear {name}, your down payment is ${downpayment}")

    loan_amount = calculate_loan_amount(price, downpayment)
    print(f"Loan amount: ${loan_amount}")

    loan_term, annual_interest_rate = get_loan_details()
    monthly_payment = calculate_monthly_payment(loan_amount, loan_term, annual_interest_rate)
    print(f"Your monthly mortgage payment is: ${monthly_payment:.2f}")


if __name__ == "__main__":
    main()