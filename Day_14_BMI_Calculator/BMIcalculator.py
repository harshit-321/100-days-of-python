# BMI Calculator Project
# ----------------------

print("Welcome to the BMI Calculator!")

# Taking user input
weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

# Calculating BMI
bmi = weight / (height ** 2)

# Display BMI
print(f"\nYour BMI is: {bmi:.2f}")

# Determine BMI Category
if bmi < 18.5:
    print("Category: Underweight")
e
