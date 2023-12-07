import tkinter as tk
import customtkinter
import api_file as api
from PIL import ImageTk, Image
import os

class DragDropWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("MyWeather")
        self.geometry("347x350")
        self.resizable(0, 0)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images2")
        
        sunny = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"sunny.png")), size=(180, 140))
        rain = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"rain.png")), size=(180, 140))
        moon = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"moon.png")), size=(180, 140))
        refreshicon = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"captcha.png")), size=(25, 25))

        downarrow = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"arrow1.png")), size=(20, 20))
        uparrow = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"arrow2.png")), size=(20, 20))

        mainFrame = customtkinter.CTkFrame(self, fg_color="#5DA7B1", width=350, height=350, border_width=5, border_color="#096C82", corner_radius=20) #corner_radius=20
        mainFrame.pack()

        weatherIconStatus = customtkinter.CTkLabel(mainFrame, image=sunny, fg_color="#5DA7B1", bg_color="#5DA7B1", width=120, height=120, corner_radius=0, text="")
        weatherIconStatus.place(x=17, y=18)

        downarrowval = customtkinter.CTkLabel(mainFrame, text=f'{api.first_min}' + '°', text_color="white", image=downarrow ,compound='left' ,font=customtkinter.CTkFont(weight="bold", size=22))
        downarrowval.place(x=130,y=220, anchor=tk.CENTER)

        uparrowval = customtkinter.CTkLabel(mainFrame, text=f"{api.first_max}" + '°', text_color="white", compound='left' ,image=uparrow,font=customtkinter.CTkFont(weight="bold", size=22))
        uparrowval.place(x=70,y=220, anchor=tk.CENTER)

        refreshButton = customtkinter.CTkButton(mainFrame, image=refreshicon, fg_color="#5DA7B1", width=25, height=25, text="", bg_color="#5DA7B1", hover_color="#338A95", corner_radius=20, command=self.inclick)
        refreshButton.place(relx=0.9, rely=0.1, anchor=tk.CENTER)

        tempritureStatus = customtkinter.CTkLabel(mainFrame, text=f'{api.first_celsiy}' + '°', text_color="white", fg_color="#5DA7B1", corner_radius=0, font=customtkinter.CTkFont(weight="bold", size=60))
        tempritureStatus.place(relx=0.8, rely=0.7, anchor=tk.CENTER)

        cityName = customtkinter.CTkLabel(mainFrame, text=api.first_city_name, text_color="white", fg_color="#5DA7B1", corner_radius=0, font=customtkinter.CTkFont(weight="bold", size=50))
        cityName.place(relx=0.65, rely=0.88, anchor=tk.CENTER)

        cityDescription = customtkinter.CTkLabel(mainFrame, text=api.first_description, text_color='white', fg_color='#5DA7B1', corner_radius=0, font=customtkinter.CTkFont(weight="bold", size=26))
        cityDescription.place(x=37,y=162)

        

    def inclick(self):
        # api.refresh_in_widget()
        print('Weather has been refreshed')



app = DragDropWindow()
app.mainloop()
