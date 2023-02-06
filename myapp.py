import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root=Tk()
root.title("Text to speech")
root.geometry("900x500")
root.resizable(False, False)
root.configure(bg="#305065")

engine= pyttsx3.init()

for voice in engine.getProperty('voices'):
    print(voice)

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[5].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[6].id)
            engine.say(text)
            engine.runAndWait()

    if (text):
        if (speed =='Fast'):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()


def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text ,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()

    if (text):
        if (speed =='Fast'):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()



# icon
image_icon=PhotoImage(file="C:/Users/Emwing/Desktop/Python_files/text_to_speech_tkinter/speak.png")
root.iconphoto(False,image_icon)

# top frame
top_frame=Frame(root, bg="white", width=900, height=70)
top_frame.place(x=0,y=0)

logo=PhotoImage(file="C:/Users/Emwing/Desktop/Python_files/text_to_speech_tkinter/logo.png")
Label(top_frame, image=logo, bg="white").place(x=10, y=5)

Label(top_frame, text="TEXT TO SPEECH", font="arial 20 bold", bg="white", fg="black").place(x=90, y=10)

# text field
text_area=Text(root,font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=140, width=500, height=250)

Label(root, text="VOICE", font="arial 15 bold", bg="#305065", fg="white").place(x=550, y=140)
Label(root, text="SPEED", font="arial 15 bold", bg="#305065", fg="white").place(x=730, y=140)


gender_combobox=Combobox(root, values=['Male', 'Female'], font="arial 14", state='r', width=10)
gender_combobox.place(x=550, y=180)
gender_combobox.set('Male')

speed_combobox=Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state='r', width=10)
speed_combobox.place(x=730, y=180)
speed_combobox.set('Normal')

imageicon=PhotoImage(file="C:/Users/Emwing/Desktop/Python_files/text_to_speech_tkinter/speak.png")
button=Button(root, text=" Speak", compound=LEFT, image=imageicon, width=120, font="arial 14 bold", command=speaknow)
button.place(x=550, y=250)

imageicon2=PhotoImage(file="C:/Users/Emwing/Desktop/Python_files/text_to_speech_tkinter/down_arrow.png")
save=Button(root, text=" Save", compound=LEFT, image=imageicon2, width=120, bg="#37c790", font="arial 14 bold", command=download)
save.place(x=730, y=250)



root.mainloop()
