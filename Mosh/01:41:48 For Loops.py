# For loop is a way to iterate through a list. For example over the list [1, 2, 3, 4, 5, 6]
# Run this python code: to see Example Output!

# Example 1
print("Exaple 1 output")

for item in range(10):
    print(item)  # print item in the list in range from 0 to 9

# Example 2
print("Exaple 2 output")
for item in range(5, 10):
    print(item)  # print item in the list in range from 5 to 10

# Example 3
print("Exaple 3 output")
for item in range(2, 10, 2):
    print(item)  # print item in the list in range from 2 to 10 with step

# Example 4
print("Exaple 4 output")

prices = [10, 20, 30, 40]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")