import tkinter as tk
from tkinter import *
import requests
from PIL import Image, ImageTk
import constans as c


class Window:
    def __init__(self, master: tk.Tk)-> None:
        self._ent: tk.Entry = Entry(master, width = 45, bg="white",justify="center",fg="black")
        self._btn: tk.Button =Button(master, text="Узнать погоду", bg = "#8aa9f2",
                        font =("Arial", 15, "normal"), fg="white",
                        activebackground="darkblue",
                        command = self.get_weather)
        self._lab: tk.Label = Label(master,text = "Введите название города: ", 
                         width=30,bg="#8aa9f2",
                         font =("Arial", 15, "bold"),                        
                         fg="white",              
                         bd=10)
        self._lab_print: tk.Label = Label(master, text="Погодные данные", bg='#8aa9f2',
                              fg="white",
                              font =("Arial", 15, "bold"), 
                               width = 30, height = 3) #вывод погоды
        
        self.cloud_image: ImageTk.PhotoImage = ImageTk.PhotoImage(Image.open('cloud1.png').resize((150, 100))) # Преобразование в PhotoImage
        self.cloud_label: tk.Label = Label(master, image=self.cloud_image)
        self.cloud_label.config(bg="#8aa9f2")
        
        self.rain_image: ImageTk.PhotoImage =  ImageTk.PhotoImage(Image.open('rain.png').resize((350, 200)))
        self.rain_label: tk.Label = Label(master, image=self.rain_image)
        self.rain_label.config(bg="#8aa9f2")
        
        self.sun_image: ImageTk.PhotoImage =  ImageTk.PhotoImage(Image.open('sun.png').resize((150, 150)))
        self.sun_label: tk.Label = Label(master, image=self.sun_image)
        self.sun_label.config(bg="#8aa9f2")
        
        self.snow_image: ImageTk.PhotoImage =  ImageTk.PhotoImage(Image.open('snow.png').resize((350, 200)))
        self.snow_label: tk.Label = Label(master, image=self.rain_image)
        self.snow_label.config(bg="#8aa9f2")
        
        self._lab.pack() 
        self._ent.pack()
        self._btn.pack()
        self._lab_print.pack(anchor="center", expand=1)       
        
    def load_cloud_image(self)-> None:
        self.cloud_label.pack()
        
    def load_rain_image(self)-> None:
        self.rain_label.pack()
        
    def load_sun_image(self)-> None:
        self.sun_label.pack()
        
    def load_snow_image(self)-> None:
         self.snow_label.pack()
        
    def delete_pictures(self)-> None:
        self.rain_label.pack_forget()
        self.cloud_label.pack_forget()
        self.sun_label.pack_forget()
        self.snow_label.pack_forget()
        
    def get_weather(self): 	
        self.delete_pictures()
        key: str = c.KEY
     	
        url: str = c.URL
        
        city: str = self._ent.get()
        
        if city =="":
            self._lab_print['text'] = c.NO_CITY
        else:
             params: dict[str, str] = {'APPID': key, 'q': city, 'units': 'metric'}
     	
             result: str = requests.get(url, params=params)
     	
             weather = result.json()
             print(weather)
             if weather['cod']==200:
                 self._lab_print['text'] = f'{city} {weather["main"]["temp"]} °C\n Облачность {weather["clouds"]["all"]}%'
                 
                 if "rain" in weather:
                     self.load_rain_image()
                 
                 elif weather["clouds"]["all"]>0:
                     self.load_cloud_image()
                 elif "snow" in weather:
                     self.load_snow_image()
                 else:
                     self.load_sun_image()
                
             else:
                 self._lab_print['text'] = c.INVALID_CITY
            
