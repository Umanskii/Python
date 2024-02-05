'''
Write Python code to check buyrs downpayment
Price is $1M
if buyer has a good credit, they need to put down 10%
otherwise, they need to put down 20%
print downpayment
'''

price = input("Enter the House price: ")
good_credit = input("Enter credit score: ")
good_credit = True

if good_credit:
    downpayment = price * 0.1
    print(downpayment)
else:
    downpayment = price * 0.2
    print(f"Down payment is ${downpayment}")