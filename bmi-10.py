
try:
    w=float(input("enter the weight in Kg ="))
    h=float(input("enter the height in cm other than zero = "))
    if (w==0 or h==0): 
        print("Invalid Input : Enter the values other than zeros")
    else: 
        height=float((h/100)**2)              
        BMI=float(w/height)                                                         
        BMI=round(BMI,2)
        print("Your BMI is \n",BMI)
        if(BMI<18.5):
            print("You're underweight")
        elif(BMI>=18.5 and BMI<=24.99):
            print("You're Normal")
        elif(BMI>=25.0 and BMI<=29.99):
            print("You're overweight")
        elif(BMI>=30.0 and BMI<=34.99):
            print("You're obese I")
        elif(BMI>=35.0 and BMI<=39.99):
            print("You're obese II")
        elif(BMI>40.0):
            print("You're obese III")
        else:
            print("enter the correct values")
except ValueError:
    print("Invalid Input enter the numbers only")