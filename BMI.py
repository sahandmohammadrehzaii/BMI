from tkinter import *
from tkinter import messagebox
import sys

# Debug mode flag
DEBUG = False

def debug_print(message):
    """Print debug messages if DEBUG mode is enabled"""
    if DEBUG:
        print(f"[DEBUG] {message}")

def reset():
    """Clear height and weight input fields"""
    debug_print("Resetting input fields")
    height.delete(0, 'end')
    weight.delete(0, 'end')


def bmi_cal():
    """Calculate BMI from height and weight inputs"""
    try:
        debug_print(f"Height input: {height.get()}")
        debug_print(f"Weight input: {weight.get()}")
        
        kg = float(weight.get())  # Changed to float for decimal support
        cm = float(height.get())  # Changed to float for decimal support
        
        if kg <= 0 or cm <= 0:
            messagebox.showerror('Error', 'Height and weight must be positive numbers!')
            debug_print("Error: Negative or zero values entered")
            return
        
        m = cm / 100
        bmi = kg / (m ** 2)
        bmi = round(bmi, 1)
        
        debug_print(f"Calculated BMI: {bmi}")
        bmi_index_over18(bmi)
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers!')
        debug_print("Error: Invalid input format")
    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {str(e)}')
        debug_print(f"Error: {str(e)}")


def bmi_index_over18(bmi):
    """Categorize BMI and display result"""
    debug_print(f"Categorizing BMI: {bmi}")
    
    if bmi < 18.5:
        messagebox.showinfo('BMI', f'BMI = {bmi} is Underweight')
    elif bmi <= 24.9:  # Fixed: was (bmi > 18.5) and (bmi < 24.9)
        messagebox.showinfo('BMI', f'BMI = {bmi} is Normal')
    elif bmi <= 29.9:  # Fixed: was (bmi > 24.9) and (bmi < 29.9)
        messagebox.showinfo('BMI', f'BMI = {bmi} is Overweight')
    else:  # bmi > 29.9
        messagebox.showinfo('BMI', f'BMI = {bmi} is Obesity')

def info():
    """Display application information"""
    info_text = '''BMI Calculator v1.1

You can calculate your Body Mass Index (BMI).

BMI Categories:
• < 18.5: Underweight
• 18.5 - 24.9: Normal
• 25.0 - 29.9: Overweight
• ≥ 30.0: Obesity

Designed by: طاها دژبانی'''
    messagebox.showinfo('Info', info_text)
    debug_print("Info dialog displayed")

# Check for debug mode from command line arguments
if '--debug' in sys.argv:
    DEBUG = True
    print("Debug mode enabled")

try:
    root = Tk()
    root.title("طراحی شده توسط طاها دژبانی")
    debug_print("Application window created")
except Exception as e:
    print(f"Error: Unable to initialize tkinter. Make sure tkinter is installed.")
    print(f"Details: {str(e)}")
    sys.exit(1)

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

debug_print("Starting main loop")
try:
    root.mainloop()
except KeyboardInterrupt:
    debug_print("Application interrupted by user")
    print("\nApplication closed.")
except Exception as e:
    print(f"Error during execution: {str(e)}")
    debug_print(f"Fatal error: {str(e)}")
    sys.exit(1)