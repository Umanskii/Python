weight_lbs = input ("What is your weight in lbs? ")
weight_kg = float(weight_lbs) * 0.45359237

print(f"Your weight in kg is {weight_kg}") 
print(f"Your weight in kg is {int(weight_kg)}") #use int() to convert to int equal number

print(type(weight_lbs)) # <class'str'>  
print(type(weight_kg)) # <class 'float'>