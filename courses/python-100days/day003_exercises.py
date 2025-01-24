# Exercise 1 - Odd or Even
num = int(input("Which number do you want to test? "))

if num % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


# Exercise 2 - BMI Calculator
weight = 85
height = 1.85

bmi = weight / (height**2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")
