import customtkinter as ctk
from tkinter import *
from PIL import Image
import os

from backend.calculate import *

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('blue')

appWidth, appHeight = 700, 400

asset_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Assets')


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create our App Window
        x = (self.winfo_screenwidth() // 2) - (appWidth // 2)
        y = (self.winfo_screenheight() // 2) - (appHeight // 2)
        self.geometry(f'{appWidth}x{appHeight}+{x}+{y}')
        self.resizable(False, False)
        self.title('محاسبه گر شاخص توده بدنی')
        self.iconbitmap('Assets/BMI Logo.ico')
        self.configure(fg_color='#E5CFF7')

        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=1, uniform='a')
        self.rowconfigure(0, weight=1, )

        self.bg_image = ctk.CTkImage(Image.open(os.path.join(asset_path, 'bg.png')),
                                     size=(appWidth, appHeight))

        self.bg_image_label = ctk.CTkLabel(self, text='', image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0, columnspan=2, )

        self.frame = CalculateFrame(self, fg_color='#E5CFF7')
        self.frame.grid(row=0, column=1, padx=(10, 60), pady=45, sticky='nsew')

        self.mainloop()


class CalculateFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.columnconfigure(0, weight=1)

        self.height_var = StringVar()
        self.weight_var = StringVar()

        self.frame_title = self.create_label(self, text='طراحی شده توسط سهند محمدرضایی و طاها فام علی پور', font_used='helvetica', fontsize=15)
        self.frame_title.grid(row=0, column=0, sticky='w')

        self.height_label = self.create_label(self, text='قد بر اساس سانتی متر نوشته شود', font_used='helvetica', fontsize=16)
        self.height_label.grid(row=1, column=0, pady=(0, 10), sticky='ew')

        self.height_slider = self.create_slider(self, min_value=0, max_value=200,
                                                command=lambda value: self.update_entry_value(value, self.height_var))

        self.height_slider.grid(row=2, column=0, sticky='ew')

        # Set Entry widget initial value
        self.height_var.set("{:.2f}".format(self.height_slider.get()))

        self.height_entry = self.create_entry(self, var=self.height_var)
        self.height_entry.grid(row=3, column=0, pady=10)

        self.weight_label = self.create_label(self, text='وزن بر اساس کیلو گرم موشته شود', font_used='helvetica', fontsize=16)
        self.weight_label.grid(row=4, column=0, pady=10, sticky='ew')

        self.weight_slider = self.create_slider(self, min_value=0, max_value=100,
                                                command=lambda value: self.update_entry_value(value, self.weight_var))
        self.weight_slider.grid(row=5, column=0, sticky='ew')

        # Set Entry widget initial value
        self.weight_var.set("{:.2f}".format(self.weight_slider.get()))

        self.weight_entry = self.create_entry(self, var=self.weight_var)
        self.weight_entry.grid(row=6, column=0, pady=10)

        self.result = self.create_label(self, text='بی ام آی شما هست: 0.00', font_used='montserrat', fontsize=16)
        self.result.grid(row=7, column=0, sticky='w')

        self.category = self.create_label(self, text='دسته بندی:', font_used='montserrat', fontsize=16)
        self.category.grid(row=8, column=0, sticky='w')

        # Event - Binding to Entry Widgets
        self.height_entry.bind("<KeyRelease>",
                               lambda event: self.update_slider_value(self.height_slider, self.height_var))
        self.weight_entry.bind("<KeyRelease>",
                               lambda event: self.update_slider_value(self.weight_slider, self.weight_var))

    @staticmethod
    def create_label(master, text, font_used, fontsize):
        label = ctk.CTkLabel(master, text=text, text_color='#713ABE', font=(font_used, fontsize))
        return label

    @staticmethod
    def create_slider(master, min_value, max_value, command):
        slider = ctk.CTkSlider(master, from_=min_value, to=max_value, height=20, fg_color='#9D76C1',
                               progress_color='#5A2E98', button_color='#713ABE', button_hover_color='#5A2E98',
                               command=command)
        return slider

    @staticmethod
    def create_entry(master, var):
        entry = ctk.CTkEntry(master, font=('helvetica', 16), text_color='#713ABE', border_color='#5A2E98',
                             border_width=1, fg_color='#E5CFF7', justify='center', textvariable=var)
        return entry

    def update_slider_value(self, slider, entry_var, ):
        try:
            value = float(entry_var.get())
            if slider.cget('from_') <= value <= slider.cget('to'):
                slider.set(value)
            else:
                entry_var.set("{:.2f}".format(slider.get()))
        except ValueError:
            entry_var.set("{:.2f}".format(slider.get()))

        self.update_bmi_and_category()

    def update_entry_value(self, value, entry_var, ):
        entry_var.set("{:.2f}".format(value))
        self.update_bmi_and_category()

    def update_bmi_and_category(self, ):
        height_value_cm = self.height_slider.get()
        weight_value_kg = self.weight_slider.get()

        bmi = calculate_bmi(height_value_cm, weight_value_kg)

        self.result.configure(text=f'بی ام آی: {bmi:.2f}')

        category = get_bmi_category(bmi)
        self.category.configure(text=f'دسته بندی: {category}')


if __name__ == '__main__':
    App()
