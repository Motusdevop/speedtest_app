from tkinter import *

from speedtest import Speedtest

def test():
	downspeed = Speedtest().download()
	uploadspeed = Speedtest().upload()
	downspeed = round(downspeed / (10**6), 2)
	uploadspeed = round(uploadspeed / (10**6), 2)
	downspeed = str(downspeed) + " Мбит"
	uploadspeed = str(uploadspeed) + " Мбит"
	download.config(text="Скорость Загрузки:\n" + downspeed)
	upload.config(text="Скорость Отдачи:\n" + uploadspeed)

root = Tk()

root.title("SpeedTest by Motus")
root.geometry("300x400")

button = Button(root, text="Разогнаться", font=40, command=test)
button.pack(side=BOTTOM, pady=40)

download = Label(root, text="Скорость Загрузки:\n-", font=35)
upload = Label(root, text="Скорость Отдачи:\n-", font=35)
download.pack(pady= (50, 0))
upload.pack(pady=(30, 0))

root.mainloop()