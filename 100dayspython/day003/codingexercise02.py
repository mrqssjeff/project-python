print("Body Mass Index Calculator 2.0!")
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in Kg: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi:.1f}. You are underweight!")
elif bmi < 25:
    print(f"Your BMI is {bmi:.1f}. You have a normal weight!")
elif bmi < 30:
    print(f"Your BMI is {bmi:.1f}. You are overweight!")
elif bmi < 35:
    print(f"Your BMI is {bmi:.1f}. You are obese!")
else:
    print(f"Your BMI is {bmi:.1f}. You are clinically obese!")