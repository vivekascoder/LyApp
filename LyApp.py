# Designing A Gui Version Of LyApp
from tkinter import *
from tkinter import ttk
import lyric_scrapper as m
from lyric_scrapper import Back

class LyApp(Tk):
    def __init__(self):
        super(LyApp, self).__init__()
        self.title("LyApp 1.0")
        self.minsize(640, 400)
        self.wm_iconbitmap("lyapp.ico")
        self.resizable(False, False)
        self.draw()
    def draw(self):
        Label(self, text="LyApp", font=("arial", 30, "bold"),\
              bg="#333", fg="white", justify=CENTER,\
              pady=3, width=27).place(x=0, y=0)
        Label(self, text="Song Name:").place(x=10, y=80)
        Label(self, text="Song Path:").place(x=340, y=80)
        self.songname = Entry(self, width=35)
        self.songname.place(x=100, y=80)
        self.songpath = Entry(self, width=30)
        self.songpath.place(x=430, y=80)

        # Lyric ListBox
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.lybox = Listbox(self, width=103, height=15)
        self.lybox.place(x=0, y=120)
        self.lybox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.lybox.yview)
        self.btn = ttk.Button(self, text="Load Song And Lyrics",\
                            command=self.load).place(x=250, y=370)
    def load(self):
        name = self.songname.get()
        path = self.songpath.get()
        whole_lyric = m.getLyricsFromGoogle(name, path)
        back = Back(path)
        back.start()
        for i in whole_lyric:
            self.lybox.insert(END, i)
ly = LyApp()
ly.mainloop()
