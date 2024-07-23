

import tkinter
import customtkinter
from pytube import YouTube
import time
from tkinter import *

bpm = 80
meter = "4/4"
go = False
Bars = 0

is_on = False




def switch():
    global is_on
    global Bars
    hold = meter.get()
    print(hold[0])
    wait_time = 60/int(bpm.get())*int(hold[0])
    # Determine is on or off
    if is_on:
        is_on = False
        Bars = 0
    else:
        is_on = True
        while is_on == True:
            time.sleep(wait_time)
            Bars += 1
            print(Bars)
            restLabel.configure(text = Bars)
            app.update()
            
    
            
app = customtkinter.CTk()
app.geometry("800x500")
app.title("Rest Counter")

title = customtkinter.CTkLabel(app, text="Type Your Desired BPM")
title.pack(padx=10,pady=10)

bpm_var = tkinter.StringVar()
bpm = customtkinter.CTkEntry(app, width=100, height = 40, textvariable=bpm_var)
bpm.pack()

subtitle = customtkinter.CTkLabel(app, text="Type Your Desired Meter")
subtitle.pack(padx=10,pady=10)

meter_var = tkinter.StringVar()
meter = customtkinter.CTkEntry(app, width=100, height = 40, textvariable=meter_var)
meter.pack()

timePassed = customtkinter.CTkLabel(app, text="Bars Counted")
timePassed.pack(padx=10,pady=10)

restLabel = customtkinter.CTkLabel(app,text=Bars)
restLabel.pack()

run = customtkinter.CTkButton(app, text="Start/Stop", command = switch)
run.pack(padx = 10, pady = 10)

app.mainloop()