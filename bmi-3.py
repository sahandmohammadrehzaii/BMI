import tkinter as tk

project = tk.Tk()

file = tk.Text(project)

file.insert(tk.END, """
weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))
age = int(input("Enter your age in years: "))

bmi = (weight * 703) / (height ** 2)

avg_weight_male = 199.8 # 
avg_weight_female = 170.8 # 
avg_height_male = 69.0 # 
avg_height_female = 63.5 # 
avg_bmi_male = 29.5 # 
avg_bmi_female = 30.0 # 

print("You entered:")
print(f"Weight: {weight} pounds")
print(f"Height: {height} inches")
print(f"Age: {age} years")
print(f"BMI: {bmi:.1f}")

gender = input("Enter your gender (M/F): ")

gender = gender.lower()

if gender == "m":
    print("Compared to the national average for men:")
    if weight > avg_weight_male:
        print(f"Your weight is {weight - avg_weight_male:.1f} pounds above average.")
    elif weight < avg_weight_male:
        print(f"Your weight is {avg_weight_male - weight:.1f} pounds below average.")
    else:
        print("Your weight is equal to the average.")

    if height > avg_height_male:
        print(f"Your height is {height - avg_height_male:.1f} inches above average.")
    elif height < avg_height_male:
        print(f"Your height is {avg_height_male - height:.1f} inches below average.")
    else:
        print("Your height is equal to the average.")

    if bmi > avg_bmi_male:
        print(f"Your BMI is {bmi - avg_bmi_male:.1f} above average.")
    elif bmi < avg_bmi_male:
        print(f"Your BMI is {avg_bmi_male - bmi:.1f} below average.")
    else:
        print("Your BMI is equal to the average.")

elif gender == "f":
    print("Compared to the national average for women:")
    if weight > avg_weight_female:
        print(f"Your weight is {weight - avg_weight_female:.1f} pounds above average.")
    elif weight < avg_weight_female:
        print(f"Your weight is {avg_weight_female - weight:.1f} pounds below average.")
    else:
        print("Your weight is equal to the average.")

    if height > avg_height_female:
        print(f"Your height is {height - avg_height_female:.1f} inches above average.")
    elif height < avg_height_female:
        print(f"Your height is {avg_height_female - height:.1f} inches below average.")
    else:
        print("Your height is equal to the average.")

    if bmi > avg_bmi_female:
        print(f"Your BMI is {bmi - avg_bmi_female:.1f} above average.")
    elif bmi < avg_bmi_female:
        print(f"Your BMI is {avg_bmi_female - bmi:.1f} below average.")
    else:
        print("Your BMI is equal to the average.")

else:
    print("Invalid gender input.")

""")

# run the code
exec(file.get(1.0, tk.END))