w = float(input("Enter your weight in kilograms\n = "))
h = float(input("Enter your height in centimeters\n = "))/100
BMI = w/(h**2)
print(BMI ,"\n")
if (BMI<18.5):
    print ("Underweight")
if (18.5 < BMI < 25):
    print ("Normal")
if (25 < BMI < 30):
    print ("Overweight")