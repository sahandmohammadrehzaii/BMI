from tkinter import *
from tkinter import messagebox


def reset():
    height.delete(0, 'end')
    weight.delete(0, 'end')


def bmi_cal():
    kg = int(weight.get())
    m = int(height.get()) / 100
    bmi = kg / m ** 2
    bmi = round(bmi, 1)
    bmi_index_over18(bmi)


def bmi_index_over18(bmi):
    if bmi < 18.5:
        messagebox.showinfo('BMI', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('BMI', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('BMI', f'BMI = {bmi} is Overweight')
    elif bmi > 29.9:
        messagebox.showinfo('BMI', f'BMI = {bmi} is Obesity')
    else:
        messagebox.showerror('BMI', 'something went wrong!')

def info():
    messagebox.showinfo('Info', 'v1, you can calculate your bmi.')

root = Tk()
root.title("طراحی شده توسط طاها دژبانی")

var = IntVar()

frame = Frame(root, padx=10, pady=10)
frame.pack(expand=True)

age = Label(frame, text="طراحی شده توسط طاها دژبانی", fg='blue')
age.grid(row=2, column=1)

frame2 = Frame(frame)
frame2.grid(row=2, column=2, pady=10)


height_label = Label(frame, text="لطفا قد تان را وارد کنید:")
height_label.grid(row=3, column=1)
weight_label = Label(frame, text="لطفا وزن تان را وارد کنید:")
weight_label.grid(row=4, column=1)

height = Entry(frame)
height.grid(row=3, column=2, pady=5)
weight = Entry(frame)
weight.grid(row=4, column=2, pady=5)

frame3 = Frame(frame)
frame3.grid(row=5, column=3, pady=10)

calculate_b = Button(frame3, text="محاسبه کردن", command=bmi_cal)
calculate_b.pack(side=LEFT)

reset_b = Button(frame3, text="پاکسازی", command=reset)
reset_b.pack(side=RIGHT)

info_b = Button(frame3, text="اطلاعات", command=info)
info_b.pack(side=RIGHT)

root.mainloop()