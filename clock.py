from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import time
import os
import pyautogui

program = Tk()

def date():

    hour = int(time.strftime("%H"))
    minute = int(time.strftime("%M"))
    second = int(time.strftime("%S"))
    tpl1 = str(hour) + " : " + str(minute) + " : " + str(second) + " : "
    lab1.config(text=tpl1)
    lab1.after(1000, date)
    enHour = enterHour.get()
    enMinute = enterMinute.get()
    enSecond = enterSecond.get()
    tpl2 = str(enHour) + " : " + str(enMinute) + " : " + str(enSecond)
    lab2.config(text=tpl2)
    hr = hour-int(enHour)
    mn = minute-int(enMinute)
    sc = second-int(enSecond)
    ehour = hr*3600
    eminute = mn*60
    esecond = sc*1
    timDate = float(ehour) + float(eminute) + float(esecond)
    print("hour : ", hour)
    print("enHour : ", enHour)
    print("minute : ", minute)
    print("enMinute : ", enMinute)
    print("second : ", second)
    print("enSecond : ", enSecond)
    if timDate < 0:
        timDate = timDate*-1
    print(timDate)
    pyautogui.sleep(seconds=timDate)

    if enHour == hour and enMinute == minute and enSecond == second:
        tkinter.messagebox.showwarning(message="it's time")

lab1 = Label(program, text="", font=50, fg="red")
lab1.pack(pady=20)
labHour = Label(program, text="Hour", font=30, fg="yellow")
labHour.pack()
enterHour = ttk.Entry(program)
enterHour.pack()
labMinute = Label(program, text="Minute", font=30, fg="yellow")
labMinute.pack()
enterMinute = ttk.Entry(program)
enterMinute.pack()
labSecond = Label(program, text="Second", font=30, fg="yellow")
labSecond.pack()
enterSecond = ttk.Entry(program)
enterSecond.pack()
btn = ttk.Button(program, text="enter")
btn.pack(pady=20)
lab2 = Label(program, text="", font=50, fg="red")
lab2.pack(pady=20)
btn.config(command=date)

hour = int(time.strftime("%H"))
minute = int(time.strftime("%M"))
second = int(time.strftime("%S"))
tpl1 = str(hour) + " : " + str(minute) + " : " + str(second) + " : "
lab1.config(text=tpl1)
lab1.after(1000, date)

program.mainloop()
os.system("pause")
