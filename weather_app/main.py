import json
from tkinter import *
import tkinter as tk
from tkinter import font
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk


root = Tk()
root.title("Weather Forecast")
root.geometry("850x640+400+80")
root.resizable(False,False)
root.configure(bg='#bdb9b9')

def getplacename():
    try:
        placename = search_text.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(placename)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime('%I:%M %p')
        clock.config(text=current_time)
        name.config(text='Current Time: ')

        api_key = "https://api.openweathermap.org/data/2.5/weather?q="+ placename + "&appid=3534c512263d2b83b12d639c93d88192"

        json_data = requests.get(api_key).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,'°'))
        c.config(text=(condition,'|','FEELS','LIKE',temp,'°'))

        dotdot1.config(text=temp)
        dotdot2.config(text=wind)
        dotdot3.config(text=humidity)
        dotdot4.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather Forecast","Invalid Entry!!")



sun_image = PhotoImage(file= r'C:\Users\Aman Shrivastav\Python39\Weather_App\images\sun.png')
sun_dis = Label(image=sun_image,bg='#bdb9b9')
sun_dis.place(x=0,y=0)


search_box = PhotoImage(file=r'C:\Users\Aman Shrivastav\Python39\Weather_App\images\search.png')
searchimage = Label(root,image=search_box,bg='#bdb9b9')
searchimage.place(x=350,y=50)

search_text = tk.Entry(root,justify="center",width=18,font=("poppins",25,"bold"),bg="#343434",border=0,fg="white")
search_text.place(x=400,y=70)
search_text.focus()

search_icon = PhotoImage(file=r'C:\Users\Aman Shrivastav\Python39\Weather_App\images\search_icon.png')
search_icon_label=Button(image=search_icon,borderwidth=0,bg='#343434',command=getplacename,fg='#343434')
search_icon_label.place(x=728,y=64)

name = Label(root,font=('arial',15,'bold'),bg='#bdb9b9')
name.place(x=30,y=250)
clock = Label(root,font=('Helvetica',20),bg='#bdb9b9')
clock.place(x=30,y=290)

t = Label(font=('arial',70,'bold'),fg='#ee666d',bg='#bdb9b9')
t.place(x=450,y=150)
c= Label(font=('arial',15,'bold'),bg='#bdb9b9')
c.place(x=450,y=250)


label1 = Label(root,text="Currently: ",font=("Helvetica",15,'bold'),fg='#343434',bg='#bdb9b9')
label1.place(x=250,y=350)

label2 = Label(root,text="Wind Speed: ",font=("Helvetica",15,'bold'),fg='#343434',bg='#bdb9b9')
label2.place(x=250,y=400)

label3 = Label(root,text="Humidity: ",font=("Helvetica",15,'bold'),fg='#343434',bg='#bdb9b9')
label3.place(x=250,y=450)

label4 = Label(root,text="Pressure: ",font=("Helvetica",15,'bold'),fg='#343434',bg='#bdb9b9')
label4.place(x=250,y=500)

dotdot1 = Label(root,text='...',font=("arial",20,'bold'),fg='white',bg='#bdb9b9')
dotdot1.place(x=500,y=338)

dotdot2 = Label(root,text='...',font=("arial",20,'bold'),fg='white',bg='#bdb9b9')
dotdot2.place(x=500,y=392)

dotdot3 = Label(root,text='...',font=("arial",20,'bold'),fg='white',bg='#bdb9b9')
dotdot3.place(x=500,y=440)

dotdot4 = Label(root,text='...',font=("arial",20,'bold'),fg='white',bg='#bdb9b9')
dotdot4.place(x=500,y=492)
root.mainloop()