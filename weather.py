from tkinter import*
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x550+300+200")
root.resizable(False, False)

def buscarClima():
  try:
    city=textfield.get()

    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    print(result)

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CLIMA ACTUAL")
    

    #weather
    api="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=ac185c80e383d5564d3ec8958911b62e"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp,"°"))
    c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
    w.config(text=wind)
    h.config(text=(humidity,"%"))
    d.config(text=description)
    p.config(text=pressure)
  except Exception as e:
    messagebox.showerror("Weather App", "Ingreso Inválido")

  

#caja de búsqueda
search_image=PhotoImage(file="search.png")
miImagen=Label(image=search_image)
miImagen.place(x=20, y=20)

textfield=tk.Entry(root, justify="center",width=20,font=("poppins",20,"bold"),bg="gray25",border=0,fg="white")
textfield.place(x=100,y=50)
textfield.focus()

search_icon=PhotoImage(file="lupa.png")
miImagen_icono=Button(image=search_icon,borderwidth=0,cursor="hand2",command=buscarClima)
miImagen_icono.place(x=490,y=34)

#logo
logo_image=PhotoImage(file="logo.png")
logo=Label(image=logo_image)
logo.place(x=180, y=180)

#bottom ox

Frame_image=PhotoImage(file="box.png")
frame_miImagen=Label(image=Frame_image)
frame_miImagen.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",25,"bold"))
name.place(x=30,y=160)
clock=Label(root, font=("Helvetica",20))
clock.place(x=30,y=270)

#label
label1=Label(root, text="VIENTO",font=("Helvetica",12,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=100, y=470)

label2=Label(root, text="HUMEDAD",font=("Helvetica",12,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=240, y=470)

label3=Label(root, text="DESCRIPCIÓN",font=("Helvetica",12,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=440, y=470)

label4=Label(root, text="PRESIÓN",font=("Helvetica",12,"bold"),fg="white",bg="#1ab5ef")
label4.place(x=670, y=470)

t=Label(font=("arial",50, "bold"),fg="#ee666d")
t.place(x=500, y=180)

c=Label(font=("arial",15,"bold"))
c.place(x=470, y=255)

w=Label(text="...", font=("arial",16,"bold"),bg="#1ab5ef")
w.place(x=105,y=490)

h=Label(text="...", font=("arial",16,"bold"),bg="#1ab5ef")
h.place(x=255,y=490)

d=Label(text="...", font=("arial",16,"bold"),bg="#1ab5ef")
d.place(x=440,y=490)

p=Label(text="...", font=("arial",16,"bold"),bg="#1ab5ef")
p.place(x=680,y=490)


root.mainloop()
