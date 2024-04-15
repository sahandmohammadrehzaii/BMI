import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=100, pady=100)


def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()
    if weight == "" or height == "":
        result_label.config(text="هم وزن و هم قد را وارد کنید!")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="یک عدد معتبر وارد کنید!")


weight_input_label = tkinter.Label(text="وزن خود را وارد کنید (کیلوگرم)")
weight_input_label.pack()
weight_input = tkinter.Entry(width=10)
weight_input.pack()
print("/n")
height_input_label = tkinter.Label(text="قد خود را وارد کنید (سانتی متر)")
height_input_label.pack()
height_input = tkinter.Entry(width=10)
height_input.pack()
calculate_button = tkinter.Button(text="محاسبه کردن", command=calculate_bmi)
calculate_button.pack()
result_label = tkinter.Label()
result_label.pack()


def write_result(bmi):
    result_string = f"بی ام آی شما است {round(bmi, 2)} | شما هستید "
    if bmi <= 16:
        result_string += "به شدت لاغر!"
    elif 16 < bmi <= 17:
        result_string += "نسبتاً لاغر!"
    elif 17 < bmi <= 18.5:
        result_string += "نازک خفیف!"
    elif 18.5 < bmi <= 25:
        result_string += "وزن طبیعی"
    elif 25 < bmi <= 30:
        result_string += "اضافه وزن"
    elif 30 < bmi <= 35:
        result_string += "چاق سطح 3"
    elif 35 < bmi <= 40:
        result_string += "چاق سطح 3"
    else:
        result_string += "چاق سطح 3"
    return result_string


window.mainloop()