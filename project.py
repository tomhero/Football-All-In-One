#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" ProJect """
import time
from Tkinter import *
#from ImageTk import PhotoImage
from PIL import Image, ImageTk
import tkMessageBox
import tkFont

class Football(object):
    def __init__(self):
        self.ball = Toplevel()
        self.ball.geometry('%dx%d' % (1366, 768))
        bg_image = Image.open("fifa_15.jpg")
        bg_image = bg_image.resize((1366, 768), Image.ANTIALIAS)
        bg_photo =  ImageTk.PhotoImage(bg_image)
        bg_pic = Label(self.ball, image=bg_photo)
        bg_pic.pack()
        but1 = Button(self.ball, text="+++++1", command=self.change).place(x=50, y=500)
        but_re = Button(self.ball, text="RESET!!", command=self.reset).place(x=200, y=500)
        but2 = Button(self.ball, text="+++++2").place(x=500, y=500)
        but_st = Button(self.ball, text="start", command=self.Start).place(x=1000, y=500)

        #font
        self.big_font = tkFont.Font(self.ball, family='TH SarabunPSK', size=280, weight="bold")

        #Var for stopwacth
        but_st = Button(self.ball, text="start", command=self.Start).place(x=1000, y=500)
        self.minit, self.sec = 0, 0
        self.time_font = tkFont.Font(self.ball, family='TH SarabunPSK', size=50, weight="bold")
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = 0
        print "__init__ ->"
        self.timestr = StringVar()               
        self.makeWidgets()

        #loop
        self.ball.mainloop()

    def change(self):
        box1 = Label(self.ball, text="%.2d" % (self.idx1), font=self.big_font, bg="black", fg="white").place(x=50, y=100)
        self.idx1 += 1

    def reset(self):
        self.idx1 = 0
        box1 = Label(self.ball, text="%.2d" % (self.idx1), font=self.big_font, bg="black", fg="white").place(x=50, y=100)
        self.idx1 += 1

    #stopwacth
    def makeWidgets(self):                         
        """ Make the time label. """
        l = Label(self.ball, textvariable=self.timestr, font=self.time_font)
        self._setTime(self._elapsedtime)
        print "makeWidgets ->",
        l.place(x=1000, y=150)
    
    def _update(self): 
        """ Update the label with elapsed time. """
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        print "_update ->",
        self._timer = self.ball.after(50, self._update)
    
    def _setTime(self, elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        #hseconds = int((elap - minutes*60.0 - seconds)*100)
        print "_setTime ->",
        self.timestr.set('%02d:%02d' % (minutes, seconds))
        
    def Start(self):                                                     
        """ Start the stopwatch, ignore if running. """
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1        
    
    def Stop(self):                                    
        """ Stop the stopwatch, ignore if stopped. """
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = 0
    
    def Reset(self):                                  
        """ Reset the stopwatch. """
        self._start = time.time()         
        self._elapsedtime = 0.0    
        self._setTime(self._elapsedtime)

class Main(object):
    def __init__(self):
        root = Tk()
        root.geometry('650x450+350+150')
        my_font = tkFont.Font(root, family='TH SarabunPSK', size=36, weight="bold")
        root.title('Sport Day All in one')
        app_name = Label(root, text='Sport All in one', font=my_font)
        app_name.pack()
        image1 = Image.open("test.bmp") #open image file 
        image1 = image1.resize((200, 100), Image.ANTIALIAS) #resize image to def button size
        photo = ImageTk.PhotoImage(image1)
        but = Button(root, image=photo, cursor="plus", command=self.football)
        but.pack()
        root.mainloop()

    def football(self):
        self.fb1 = Football()

app = Main()
