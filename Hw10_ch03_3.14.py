weight = int(input("Enter your weight in pounds:"))
height = int(input("Enter your height in inches:"))
BMI = weight*(703/(height**2))
print("Your BMI is:", BMI)
if BMI > 18.5 and BMI < 25:
    print("You have an optimal weight!")
elif BMI < 18.5:
    print("You are underweight!")
else:
    print("You are overweight!")