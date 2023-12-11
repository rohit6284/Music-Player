                                #* Music Player

from tkinter import *
import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import os

#* Create a GUI window:-
root = Tk()
root.title("Music Player")
root.geometry("920x670")
root.configure(background="#000000")
root.resizable(False,False)

mixer.init()

#* Create a function to open a file:-
def AddMusic():
        path = filedialog.askdirectory()
        if path:
                os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
                if song.endswith(".mp3"):
                        Playlist.insert(END, song)


def play_song():
        Music_Name = Playlist.get(ACTIVE)
        mixer.music.load(Playlist.get(ACTIVE))
        mixer.music.play()
        music.config(text=Music_Name[0:-4])


#* icon:-
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

Top = PhotoImage(file="header.png")
Label(root, image=Top, bg="black", bd=0).pack()


#* Buttons:-
ButtonPlay = PhotoImage(file="play.png")
Button(root, image=ButtonPlay, bg="black", bd=0, command=play_song).place(x=720, y=400)

ButtonStop = PhotoImage(file="stop.png")
Button(root, image=ButtonStop, bg="black", bd=0, command=mixer.music.stop).place(x=650, y=500)

ButtonResume = PhotoImage(file="resume.png")
Button(root, image=ButtonResume, bg="black", bd=0, command=mixer.music.unpause).place(x=730, y=500)

ButtonPause = PhotoImage(file="pause.png")
Button(root, image=ButtonPause, bg="black", bd=0, command=mixer.music.pause).place(x=810, y=500)

#* Music Name Display:-
music = Label(root,text="",font=("times new roman","12"),fg="white",bg="black")
music.place(x=750,y=340,anchor="center")

#* Menu Bar:-
Menu = PhotoImage(file="menubar.png")
Label(root, image=Menu, bg="#0f1a2b").pack(padx=10, pady=50, side=LEFT)

Frame_Music = Frame(root,bg="black", bd=5)
Frame_Music.place(x=20, y=350, width=560, height=250)

Button(root, text="Open Folder", width=15, height=2, font=("times new roman",
        12, "bold"), fg="Black", bg="#00FFCC",command=AddMusic).place(x=30, y=300)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 11, "bold"), bg="black", fg="grey",
                        selectbackground="#1a2421", cursor="hand2", bd=5, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)

#* Execute Tkinter:-
root.mainloop()