def calculate_bmi():
    height = input("Height in centimeters: ")

    weight = input("Weight in kilograms: ")

    try:
        height = float(height)
        weight = float(weight)

        height = height / 100

        bmi = weight / (height * height)

        print("Your BMI is: {:.2f}".format(bmi))

    except:
        print("Please enter a valid number.")


if __name__ == '__main__':
    calculate_bmi()