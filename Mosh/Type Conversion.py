birth_year = int(input("What is your birth year? "))
age = 2024 - birth_year 
print(f"You are {age} years old.")
if age >= 18:
    print("You can vote.")

print(type(age)) # <class 'int'>
print(type(birth_year)) # <class 'int'>

