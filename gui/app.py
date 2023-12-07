from PIL import ImageTk, Image
import tkinter as tk
import customtkinter
import sqlite3
import os
from datetime import datetime
import api_file as api



customtkinter.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# API
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__(fg_color="#5DA7B1")
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images2")

        # WINDOW CONFIG
        self.title("MyWeather")
        self.geometry("1200x800")
        self.resizable(0, 0)

        connect = sqlite3.connect('myweather.db')
        cursor = connect.cursor()

        cursor.execute('SELECT name FROM account ORDER BY rowid DESC LIMIT 1')
        name = cursor.fetchone()
        cursor.execute('SELECT last_name FROM account ORDER BY rowid DESC LIMIT 1')
        lasty_name = cursor.fetchone()
        connect.commit()
        connect.close()
        # Time    
        def getdate():

            now = datetime.now()
            day = now.strftime("%A")
            current_date_time = now.strftime("%d.%m.%Y")
            time = now.strftime("%H:%M")
            dataDate.configure(text=current_date_time)
            dataDay.configure(text=day)
            dataTime.configure(text=time)
            self.after(8000, getdate)

        
        weatherScroll = customtkinter.CTkScrollableFrame(self, width=275, height=800, fg_color="#096C82", corner_radius=0, scrollbar_button_color="#C5DFE3", scrollbar_button_hover_color="#B5CCCF", scrollbar_fg_color="#085769")
        weatherScroll.pack(anchor=tk.NW)

        weatherStat = customtkinter.CTkFrame(weatherScroll, width=275, height=90, fg_color="#4599A4", border_width=2, corner_radius=20,border_color="white")
        weatherStat.pack(pady=15, padx=10)

        weatherStatDegrees = customtkinter.CTkLabel(weatherStat, text='11' + '°', text_color="white", font=('Roboto Slab Thin',80))

        maxDegree = customtkinter.CTkLabel(weatherStat, text=f'Максимальна' + f'{api.first_max}' + '°', text_color="#FFFFFF", font=('Roboto Slab Bold',40))
        
        minDegree = customtkinter.CTkLabel(weatherStat, text=f'Мінімальна' + f'{api.first_min}' + '°', text_color="#FFFFFF", font=('Roboto Slab Bold',40))


        potochna = customtkinter.CTkLabel(weatherStat, text='Поточна Позиція', fg_color='transparent', text_color="white", font=('Roboto Slab Bold',16))
        potochna.place(x=8,y=8)

        weatherStatName = customtkinter.CTkLabel(weatherStat, text=api.first_city_name.lower().capitalize(),fg_color='transparent', text_color="white", font=('Roboto Slab Bold', 12))
        weatherStatName.place(x=14,y=33)
        
        weatherStatDegrees = customtkinter.CTkLabel(weatherStat, text=f'{api.first_celsiy}' + '°', text_color="white", font=('Roboto Slab Bold',40))
        weatherStatDegrees.place(relx=0.85, rely=0.4, anchor=tk.CENTER)

        weatherStatDesc = customtkinter.CTkLabel(weatherStat, text=f"{api.first_description}", text_color="#FFFFFF", font=('Roboto Slab Bold',13))
        weatherStatDesc.place(x=6, y=55)

        kiivWeatherStat = customtkinter.CTkFrame(weatherScroll, width=275, height=90, fg_color="#096C82", corner_radius=20, border_width=2, border_color="white")
        kiivWeatherStat.pack(pady=15, padx=10)

        kiivWeatherStatName = customtkinter.CTkLabel(kiivWeatherStat, text=api.kyiv_city_name, fg_color="#096C82", text_color="white", font=('Roboto Slab Bold',20))
        kiivWeatherStatName.place(relx=0.14, rely=0.23, anchor=tk.CENTER)

        kiivWeatherStatDegrees = customtkinter.CTkLabel(kiivWeatherStat, text=f"{api.kyiv_celsiy}" + "°", text_color="white", font=('Roboto Slab Bold',40))
        kiivWeatherStatDegrees.place(relx=0.85, rely=0.4, anchor=tk.CENTER)

        kiivWeatherStatDesc = customtkinter.CTkLabel(kiivWeatherStat, text=api.kyiv_description, text_color="white", font=('Roboto Slab Bold',13))
        kiivWeatherStatDesc.place(x=14, y=55)

        romeWeatherStat = customtkinter.CTkFrame(weatherScroll,  width=275, height=90, corner_radius=20, fg_color="#096C82", border_width=2, border_color="white")
        romeWeatherStat.pack(pady=15, padx=10)

        romeWeatherStatName = customtkinter.CTkLabel(romeWeatherStat, text=f"{api.rome_city_name}", fg_color="#096C82", text_color="white", font=('Roboto Slab Bold',20))
        romeWeatherStatName.place(relx=0.14, rely=0.23, anchor=tk.CENTER)

        romeWeatherStatDegrees = customtkinter.CTkLabel(romeWeatherStat, text=f'{api.rome_celsiy}' + '°', text_color="white", font=('Roboto Slab Bold',40))
        romeWeatherStatDegrees.place(relx=0.85, rely=0.4, anchor=tk.CENTER)

        romeWeatherStatDesc = customtkinter.CTkLabel(romeWeatherStat, text=api.rome_description, text_color="white", font=('Roboto Slab Bold',13))
        romeWeatherStatDesc.place(x=14, y=55)

        londonWeatherStat = customtkinter.CTkFrame(weatherScroll, width=275, height=90, corner_radius=20, fg_color="#096C82", border_width=2, border_color="white")
        londonWeatherStat.pack(pady=15, padx=10)

        londonWeatherStatName = customtkinter.CTkLabel(londonWeatherStat, text=api.london_city_name, fg_color="#096C82", text_color="white", font=('Roboto Slab Bold',20))
        londonWeatherStatName.place(relx=0.19, rely=0.23, anchor=tk.CENTER)

        londonWeatherStatDegrees = customtkinter.CTkLabel(londonWeatherStat, text=f'{api.london_celsiy}' + "°", text_color="white", font=('Roboto Slab Bold',40))
        londonWeatherStatDegrees.place(relx=0.85, rely=0.4, anchor=tk.CENTER)

        londonWeatherStatDesc = customtkinter.CTkLabel(londonWeatherStat, text=api.london_description, text_color="white", font=('Roboto Slab Bold',13))
        londonWeatherStatDesc.place(x=14, y=55)

        warsawWeatherStat = customtkinter.CTkFrame(weatherScroll, width=275, height=90, corner_radius=20, fg_color="#096C82", border_width=2, border_color="white")
        warsawWeatherStat.pack(pady=15, padx=10)

        warsawWeatherStatName = customtkinter.CTkLabel(warsawWeatherStat, text=api.warsaw_city_name, fg_color="#096C82", text_color="white", font=('Roboto Slab Bold',20))
        warsawWeatherStatName.place(relx=0.2, rely=0.23, anchor=tk.CENTER)

        warsawWeatherStatDegrees = customtkinter.CTkLabel(warsawWeatherStat, text=f'{api.warsaw_celsiy}' + "°", text_color="white", font=('Roboto Slab Bold',40))
        warsawWeatherStatDegrees.place(relx=0.85, rely=0.4, anchor=tk.CENTER)

        warsawWeatherStatDesc = customtkinter.CTkLabel(warsawWeatherStat, text=api.warsaw_description, text_color="white", font=('Roboto Slab Bold',13))
        warsawWeatherStatDesc.place(x=14, y=55)

        pragueWeatherStat = customtkinter.CTkFrame(weatherScroll, width=275, height=90, corner_radius=20, fg_color="#096C82", border_width=2, border_color="white")
        pragueWeatherStat.pack(pady=15, padx=10)

        pragueWeatherStatName = customtkinter.CTkLabel(pragueWeatherStat, text=api.prague_city_name, fg_color="#096C82", text_color="white", font=('Roboto Slab Bold',20))
        pragueWeatherStatName.place(relx=0.17, rely=0.23, anchor=tk.CENTER)

        pragueWeatherStatDegrees = customtkinter.CTkLabel(pragueWeatherStat, text=f'{api.prague_celsiy}' + "°", text_color="white", font=('Roboto Slab Bold',40))
        pragueWeatherStatDegrees.place(relx=0.85, rely=0.4, anchor=tk.CENTER)

        pragueWeatherStatDesc = customtkinter.CTkLabel(pragueWeatherStat, text=api.prague_description, text_color="white", font=('Roboto Slab Bold',13))
        pragueWeatherStatDesc.place(x=14, y=55)

        accounticon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "user.png")), size=(35,35))

        accountButton = customtkinter.CTkButton(self, width=40, height=40, fg_color="#5DA7B1", text="", hover_color="#5AA0AA", image=accounticon, command = self.opencabinet) #5DA7B1
        accountButton.place(relx=0.28, rely=0.05, anchor=tk.CENTER)

        accountUserName = customtkinter.CTkLabel(self, text=f"{name[0]} " + f"{lasty_name[0]}", text_color="white", font=('Roboto Slab Bold', 15), wraplength=180)
        accountUserName.place(relx=0.36, rely=0.05, anchor=tk.CENTER)

        
        searchframe = customtkinter.CTkFrame(self,width=300, height=40,corner_radius=100,border_width=3, border_color="#91DCE6" , fg_color="#096C82")
        searchframe.place(relx=0.86, rely=0.05, anchor=tk.CENTER)

        searchInput = customtkinter.CTkEntry(searchframe, width=230, height=30, fg_color='transparent', text_color="white", font=('Roboto Slab Bold',18), placeholder_text="Пошук міста...", placeholder_text_color="#91DCE6")
        searchInput.place(x=49,y=5)


        #weatherStatusIcon = ImageTk.PhotoImage(Image.open("/images/sunny.png"))


        weatherStatusIcon = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"sunny.png")), size=(171, 159))

        searchIcon = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"search.png")), size=(20, 20))

        searchButton = customtkinter.CTkButton(searchframe, width=40, height=20, corner_radius=100, text="", fg_color="#096C82", hover_color="#096C82", image=searchIcon, command=api.searchinput)
        searchButton.place(x=9,y=6)

        potochnaMain = customtkinter.CTkLabel(self, text="Поточна позиція", font=('Roboto Slab Bold', 35), text_color="white")
        potochnaMain.place(x=576,y=101)

        weatherStatusFrame = customtkinter.CTkLabel(self, fg_color="#5DA7B1", width=171, height=159, image=weatherStatusIcon, text="")
        weatherStatusFrame.place(x=450,y=220, anchor = tk.CENTER)

        degreesLabel = customtkinter.CTkLabel(self, text=f'{api.first_celsiy}' + '°', fg_color="#5DA7B1", text_color="white", font=('Roboto Slab Medium',80))
        degreesLabel.place(x=697,y=230, anchor = tk.CENTER)

        cityName = customtkinter.CTkLabel(self, text=f'{api.first_city_name.lower().capitalize()}', fg_color="#5DA7B1", text_color="white", font=('Roboto Slab Bold',22))
        cityName.place(x=689,y=162, anchor=tk.CENTER)

        weatherShortDesc = customtkinter.CTkLabel(self, text=api.first_description, fg_color="#5DA7B1", text_color="white", font=customtkinter.CTkFont(weight="bold", size=20), wraplength=110)
        weatherShortDesc.place(x=663,y=284)

        downarrowimgico = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"arrow1.png")), size=(25, 25))
        uparrowimgico = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"arrow2.png")), size=(25, 25))
        
        downarrowimg = customtkinter.CTkLabel(self, text=f'{api.first_min}' + '°', text_color="white",image=downarrowimgico, compound='left', font=('Roboto Slab Bold',30))
        downarrowimg.place(x=673,y=350)

        uparrowimg = customtkinter.CTkLabel(self, text=f"{api.first_max}" + '°', text_color="white",image=uparrowimgico, compound='left', font=('Roboto Slab Bold',30))
        uparrowimg.place(x=738,y=350)

        dataDay = customtkinter.CTkLabel(self, text="day", fg_color="#5DA7B1", text_color="white", font=('Roboto Slab Bold',34))
        dataDay.place(relx=0.83, rely=0.18, anchor=tk.CENTER)

        dataDate = customtkinter.CTkLabel(self, text="date", fg_color="#5DA7B1", text_color="white", font=('Roboto Slab Bold',45))
        dataDate.place(relx=0.83, rely=0.25, anchor=tk.CENTER)

        dataTime = customtkinter.CTkLabel(self, text="time", fg_color="#5DA7B1", text_color="white", font=('Roboto Slab Bold',35))
        dataTime.place(relx=0.83, rely=0.32, anchor=tk.CENTER)

        left = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"left.png")), size=(8, 21))
        right = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"right.png")), size=(8, 21))

        leftSwitch = customtkinter.CTkButton(self, text=" ", width=30,image=left, height=30, corner_radius=10, fg_color="transparent")
        leftSwitch.place(x=292,y=524)

        rightSwitch = customtkinter.CTkButton(self, text=" ", width=30,image=right, height=30, corner_radius=10, fg_color="transparent")
        rightSwitch.place(x=1160,y=524)

        sunny = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"sunny.png")), size=(50, 50))
        rain = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"rain.png")), size=(50, 50))
        moon = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"moon.png")), size=(50, 50))
        
        inlinePositionFrame = customtkinter.CTkFrame(self, width=818, height=240, corner_radius=20, fg_color="#5DA7B1", border_width=5, border_color="#E2F5F7")
        inlinePositionFrame.place(x=329,y=430)
                # ('Roboto Slab Bold',45)
        customtkinter.CTkLabel(inlinePositionFrame, text="Захід сонця о 16:05.  Очікується дощова погода приблизно о 19:00", text_color="white", font=("Roboto Slab Bold", 14)).pack(padx=10, pady=23)
        
        inpos = customtkinter.CTkFrame(inlinePositionFrame, width=55, height=149, fg_color="transparent")
        inpos.pack(side="left", padx=20, pady=26)

        inpostime = customtkinter.CTkLabel(inpos, text="Зараз", text_color="white", font=customtkinter.CTkFont(weight="bold", size=20))
        inpostime.pack()

        inposicon = customtkinter.CTkLabel(inpos, text="", image=sunny, fg_color="transparent", width=50, height=50)
        inposicon.pack()

        inposdeegres = customtkinter.CTkLabel(inpos, text=f"{api.first_celsiy}°", text_color="white", font=customtkinter.CTkFont(weight="bold", size=23))
        inposdeegres.pack()

        inpos2 = customtkinter.CTkFrame(inlinePositionFrame, width=55, height=149, fg_color="transparent")
        inpos2.pack(side="left", padx=20, pady=10)

        inpostime2 = customtkinter.CTkLabel(inpos2, text="15:00", text_color="white", font=customtkinter.CTkFont(weight="bold", size=20))
        inpostime2.pack()

        inposicon2 = customtkinter.CTkLabel(inpos2, text="", image=moon, fg_color="transparent", width=50, height=50)
        inposicon2.pack()

        inposdeegres2 = customtkinter.CTkLabel(inpos2, text="5°", text_color="white", font=customtkinter.CTkFont(weight="bold", size=23))
        inposdeegres2.pack()

        inpos3 = customtkinter.CTkFrame(inlinePositionFrame, width=55, height=149, fg_color="transparent")
        inpos3.pack(side="left", padx=20, pady=10)

        inpostime3 = customtkinter.CTkLabel(inpos3, text="16:00", text_color="white", font=customtkinter.CTkFont(weight="bold", size=20))
        inpostime3.pack()

        inposicon3 = customtkinter.CTkLabel(inpos3, text="", image=moon, fg_color="transparent", width=50, height=50)
        inposicon3.pack()

        inposdeegres3 = customtkinter.CTkLabel(inpos3, text="4°", text_color="white", font=customtkinter.CTkFont(weight="bold", size=23))
        inposdeegres3.pack()

        inpos4 = customtkinter.CTkFrame(inlinePositionFrame, width=55, height=149, fg_color="transparent")
        inpos4.pack(side="left", padx=20, pady=10)

        inpostime4 = customtkinter.CTkLabel(inpos4, text="17:00", text_color="white", font=customtkinter.CTkFont(weight="bold", size=20))
        inpostime4.pack()

        inposicon4 = customtkinter.CTkLabel(inpos4, text="", image=sunny, fg_color="transparent", width=50, height=50)
        inposicon4.pack()

        inposdeegres4 = customtkinter.CTkLabel(inpos4, text=f"{} °", text_color="white", font=customtkinter.CTkFont(weight="bold", size=23))
        inposdeegres4.pack()

        inpos5 = customtkinter.CTkFrame(inlinePositionFrame, width=55, height=149, fg_color="transparent")
        inpos5.pack(side="left", padx=20, pady=10)

        inpostime5 = customtkinter.CTkLabel(inpos5, text="18:00", text_color="white", font=customtkinter.CTkFont(weight="bold", size=20))
        inpostime5.pack()

        inposicon5 = customtkinter.CTkLabel(inpos5, text="", image=sunny, fg_color="transparent", width=50, height=50)
        inposicon5.pack()

        inposdeegres5 = customtkinter.CTkLabel(inpos5, text=f"{api.fifth_hour} °", text_color="white", font=customtkinter.CTkFont(weight="bold", size=23))
        inposdeegres5.pack()

        inpos6 = customtkinter.CTkFrame(inlinePositionFrame, width=55, height=149, fg_color="transparent")
        inpos6.pack(side="left", padx=20, pady=10)

        inpostime6 = customtkinter.CTkLabel(inpos6, text="19:00", text_color="white", font=customtkinter.CTkFont(weight="bold", size=20))
        inpostime6.pack()

        inposicon6 = customtkinter.CTkLabel(inpos6, text="", image=sunny, fg_color="transparent", width=50, height=50)
        inposicon6.pack()

        inposdeegres6 = customtkinter.CTkLabel(inpos6, text="6°", text_color="white", font=customtkinter.CTkFont(weight="bold", size=23))
        inposdeegres6.pack()

        inpos7 = customtkinter.CTkFrame(inlinePositionFrame, width=55, height=149, fg_color="transparent")
        inpos7.pack(side="left", padx=20, pady=10)

        inpostime7 = customtkinter.CTkLabel(inpos7, text="20:00", text_color="white", font=customtkinter.CTkFont(weight="bold", size=20))
        inpostime7.pack()

        inposicon7 = customtkinter.CTkLabel(inpos7, text="", image=sunny, fg_color="transparent", width=50, height=50)
        inposicon7.pack()

        inposdeegres7 = customtkinter.CTkLabel(inpos7, text=f"°", text_color="white", font=customtkinter.CTkFont(weight="bold", size=23))
        inposdeegres7.pack()

        inpos8 = customtkinter.CTkFrame(inlinePositionFrame, width=55, height=149, fg_color="transparent")
        inpos8.pack(side="left", padx=20, pady=10)

        inpostime8 = customtkinter.CTkLabel(inpos8, text="21:00", text_color="white", font=customtkinter.CTkFont(weight="bold", size=20))
        inpostime8.pack()

        inposicon8 = customtkinter.CTkLabel(inpos8, text="", image=sunny, fg_color="transparent", width=50, height=50)
        inposicon8.pack()

        inposdeegres8 = customtkinter.CTkLabel(inpos8, text=f"{api.eighth_hour}°", text_color="white", font=customtkinter.CTkFont(weight="bold", size=23))
        inposdeegres8.pack()

        inpos9 = customtkinter.CTkFrame(inlinePositionFrame, width=55, height=149, fg_color="transparent")
        inpos9.pack(side="left", padx=20, pady=10)

        inpostime9 = customtkinter.CTkLabel(inpos9, text="22:00", text_color="white", font=customtkinter.CTkFont(weight="bold", size=20))
        inpostime9.pack()

        inposicon9 = customtkinter.CTkLabel(inpos9, text=f"{api.nineth_hour}", image=sunny, fg_color="transparent", width=50, height=50)
        inposicon9.pack()

        inposdeegres9 = customtkinter.CTkLabel(inpos9, text="5°", text_color="white", font=customtkinter.CTkFont(weight="bold", size=23))
        inposdeegres9.pack()

        # self.protocol("WM_DELETE_WINDOW", self.onclosing)
        getdate()

    def opencabinet(self):

        self.destroy()

        file_name = __file__ + '/../account.py'

        os.system(f"python {file_name}")



    
    # def onclosing(self):
    #     self.destroy()
    #     python = r'C:\Users\Димон\AppData\Local\Programs\Python\Python312\python.exe'
    #     file_name = r'F:\python\work_with_weather_app\gui\widget.py'

    #     os.system(f"python {file_name}")


app1 = App()
app1.mainloop()
