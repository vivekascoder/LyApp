#URl: https://www.google.com/search?q=infinity+lyrics&oq=
#infinity+lyrics&aqs=chrome.0.0l6.7793j0j7&sourceid=
#chrome&ie=UTF-8
#  Cadmium Melody Lyrics
#  ../cadmium-melody.mp3
import threading
from playsound import playsound
import time

def getSoundLength(filename):
    try:
        from mutagen.mp3 import MP3
        audio = MP3(filename)
        return audio.info.length
    except:
        "Getting Error Call vivekascoder."

def getLyricsFromGoogle(l, f):
    try:
        from requests_html import HTMLSession
        session = HTMLSession()
        sp = l.split()
        lyric = ""
        for i in sp:
            lyric += i + "+"
        lyric = lyric[:-1]
        url = "https://www.google.com/search?q="+lyric+"&oq="+ lyric +"&aqs=chrome.0.0l6.7793j0j7&sourceid=chrome&ie=UTF-8"
        r = session.get(url)
        lyric_div = r.html.find("span[jsname='YS01Ge']")
        whole_lyric = []
        for i in range(len(lyric_div)):
            #print(lyric_div[i].text)
            #time.sleep((getSoundLength(f)/len(lyric_div))/2)
            whole_lyric.append(lyric_div[i].text)
        return whole_lyric
            
    except:
        return "Getting Error Call vivekascoder."

class Back(threading.Thread):
    def __init__(self, f):
        threading.Thread.__init__(self)
        self.f = f
    def run(self):
        playsound(self.f)
##if __name__ == '__main__':
##    l = input("Enter Song Name To Search: ")
##    f = input("Enter File Name: ")
##    lyapp = Lyapp(f)
##    lyapp.start()
##    print(getLyricsFromGoogle(l, f))
