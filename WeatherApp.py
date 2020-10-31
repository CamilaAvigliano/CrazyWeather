import tkinter as tk
import requests
from tkinter import font

HEIGHT = 500
WIDTH = 600

def test_function (entry):
    print("Esta es la entrada:", entry)

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)
	except:
		final_str = 'There was a problem'

	return final_str
#C:\Users\Seleccion\PycharmProjects\WeatherApp\venv\Lib\site-packages

def get_weather(city):
	weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
	response = requests.get(url, params= params)
	weather = response.json()

	label['text'] = format_response(weather)

root = tk.Tk()
root.title("The weather is crazy, let's check it out!")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='fondo.gif')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg= "#80C1FF", bd=5)
frame.place(relx= 0.5, rely= 0.1, relwidth= 0.75, relheight= 0.1 , anchor="n")

entry = tk.Entry(frame , font=("Courier", 20))
entry.place(relwidth= 0.65  , relheight=1)

button = tk.Button(frame , text ="Let's see!", font=("Times New Roman", 10), command = lambda : get_weather(entry.get()))
button.place(relx= 0.7, relwidth= 0.3, relheight= 1)

lower_frame = tk.Frame(root,bg= "#80C1FF", bd=10)
lower_frame.place(relx= 0.5, rely= 0.25 , relwidth = 0.75 , relheight= 0.6, anchor="n")

label = tk.Label(lower_frame , font =("Times New Roman" , 20))
label.place(relwidth= 1 , relheight= 1)


root.mainloop()
