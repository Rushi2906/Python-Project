from tkinter import *
from tkinter import messagebox
import datetime
import time,sys
from pygame import mixer
from PIL import ImageTk,Image
import winsound

def alarm(set_alarm_timer):
    if set_alarm_timer=="":
        messagebox.askretrycancel("ErrorMessage","Please Enter Value")
    else:
        while True:
            time.sleep(1)
            current_time = datetime.datetime.now()
            now = current_time.strftime("%H:%M")
            date = current_time.strftime("%d/%m/%Y")
            print("The set Date is : ",date)
            print(now)
            if now == set_alarm_timer:
                print("Time to Wake up")
                play_music()

def play_music():
    mixer.init()
    mixer.music.load("alarm_tone_2.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(30)
        mixer.music.stop()
        sys.exit()

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}"
    print(set_alarm_timer)
    alarm(set_alarm_timer)


clock = Tk()

clock.title("My Alarm Clock ")
clock.geometry("800x400")
time_format = Label(clock, text="Enter time in 24 hour format!",fg="red",bg="black",font="Arial", width=50).place(x=135,y=250)
setYourAlarm = Label(clock, text="Set your Alarm", fg="blue", bg="black", relief="solid", font=("Helevetica",12,"bold"), width=60, height=3, ).place(x=110,y=10)

hour = StringVar()
min = StringVar()

# Labels
Label(clock, text="Enter Hour : ", fg="white", bg="black", width=20, height=1).place(x=200,y=100)
Label(clock, text="Enter Minute : ", fg="white", bg="black", width=20).place(x=200,y=150)

# take input from user
hourTime = Entry(clock, textvariable = hour, bg="black", fg="white", width=10).place(x=400,y=100)
minTime = Entry(clock, textvariable = min, bg="black", fg="white", width=10).place(x=400,y=150)

# Image
# img = ImageTk.PhotoImage(Image.open(""))

submit = Button(clock, text="Set Alarm", fg="red", width=10,command=actual_time).place(x=350,y=200)

clock.mainloop()