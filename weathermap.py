from tkinter import *
from tkinter import font
from PIL import ImageTk,Image 
from urllib.request import urlopen
import json
from tkinter import messagebox as msg

file="image3.png"

def getTemp():  
    try:
        CityName = city_name.get()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={CityName}&appid=3b6fc998272abf055734591058b4c655&units=metric"
        data = urlopen(url)
        data1 = json.loads(data.read())
        # main_data = data1['main']
        temp = data1['main']['temp']
        # print(temp)
        message_data = f"{CityName}'s temperature is : {temp}°C"
        msg.showinfo("Temperature", message_data)
        city_name.set("")

    except:
        msg.showerror("Error","Please Enter correct the city name ")
        city_name.set("")
    


root= Tk()
root.geometry("1000x900")
root.title("Weather Map")
root.wm_iconbitmap("icon1.ico")

city_name = StringVar()

img = ImageTk.PhotoImage(Image.open(file))
l1 = Label(root,image=img)
l1.pack()

Label(root,text="Enter the City Name", font=("Arial",20)).place(x=400,y=40)
Entry(root,textvariable=city_name,width=16, font=("Arial",20)).place(x=400, y=100, height=40)

Button(root,text="Submit",command=getTemp).place(x=480, y=170,height=50,width=60)

root.mainloop()