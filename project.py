#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" ProJect """
import time
from Tkinter import *
#from ImageTk import PhotoImage
import ttk
from PIL import Image, ImageTk
import tkMessageBox
import tkFont

class Football(object):
    def __init__(self):
        self.ball = Toplevel()
        self.screen_width = self.ball.winfo_screenwidth()
        self.screen_height = self.ball.winfo_screenheight()
        self.screen_all = self.screen_width*self.screen_height
        self.ball.overrideredirect(True)
        self.ball.geometry("{0}x{1}+0+0".format(self.screen_width, self.screen_height))
        bg_image = Image.open("fifa_15.jpg")
        bg_image = bg_image.resize((self.screen_width, self.screen_height), Image.ANTIALIAS)
        bg_photo =  ImageTk.PhotoImage(bg_image)
        bg_pic = Label(self.ball, image=bg_photo)
        bg_pic.pack()
        but_font = tkFont.Font(self.ball, size=int(self.screen_width*0.01), weight="bold")
        but_quit = Button(self.ball, text='CLOSE', bg='#ff2424', font=but_font, command=self.quit_fx)
        but_quit.place(x=self.screen_width*0.935, y=self.screen_height*0.015)
        but1 = Button(self.ball, text="ADD 1 POINT", font=but_font, command=self.change).place(x=self.screen_width*0.06, y=self.screen_height*0.55)
        but_re = Button(self.ball, text="RESET POINT", font=but_font, command=self.reset).place(x=self.screen_width*0.45, y=self.screen_height*0.9)
        but2 = Button(self.ball, text="ADD 1 POINT", font=but_font, command=self.change2).place(x=self.screen_width*0.71, y=self.screen_height*0.55)
        but_start = Button(self.ball, text="start", font=but_font, command=self.Start).place(x=self.screen_width*0.433, y=self.screen_height*0.12)
        but_stop = Button(self.ball, text="stop", font=but_font, command=self.Stop).place(x=self.screen_width*0.4875, y=self.screen_height*0.12)
        but_reset = Button(self.ball, text="reset", font=but_font, command=self.Reset).place(x=self.screen_width*0.54, y=self.screen_height*0.12)

        #font
        self.big_font = tkFont.Font(self.ball, size=int(self.screen_width*0.15), weight="bold")

        #Var for stopwacth
        self.minit, self.sec = 0, 0
        self.time_font = tkFont.Font(self.ball, size=int(self.screen_width*0.03), weight="bold")
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = 0
        print "__init__ ->"
        self.timestr = StringVar()               
        self.makeWidgets()
        #Score
        self.idx1 = 0
        self.idx2 = 0
        box1 = Label(self.ball, text="%.2d" % (self.idx1), font=self.big_font, bg="#080405", fg="white").place(x=self.screen_width*0.06, y=self.screen_height*0.1)
        box2 = Label(self.ball, text="%.2d" % (self.idx2), font=self.big_font, bg="#080405", fg="white").place(x=self.screen_width*0.71, y=self.screen_height*0.1)

        #loop
        self.ball.mainloop()

    def quit_fx(self):
            self.ball.destroy()

    def change(self):
        self.idx1 += 1
        box1 = Label(self.ball, text="%.2d" % (self.idx1), font=self.big_font, bg="#080405", fg="white").place(x=self.screen_width*0.06, y=self.screen_height*0.1)

    def change2(self):
        self.idx2 += 1
        box2 = Label(self.ball, text="%.2d" % (self.idx2), font=self.big_font, bg="#080405", fg="white").place(x=self.screen_width*0.71, y=self.screen_height*0.1)

    def reset(self):
        self.idx1 = 0
        self.idx2 = 0
        box1 = Label(self.ball, text="%.2d" % (self.idx1), font=self.big_font, bg="#080405", fg="white").place(x=self.screen_width*0.06, y=self.screen_height*0.1)
        box2 = Label(self.ball, text="%.2d" % (self.idx2), font=self.big_font, bg="#080405", fg="white").place(x=self.screen_width*0.71, y=self.screen_height*0.1)

    #stopwacth
    def makeWidgets(self):                         
        """ Make the time label. """
        l = Label(self.ball, textvariable=self.timestr, fg='#eb000c', font=self.time_font)
        self._setTime(self._elapsedtime)
        print "makeWidgets ->",
        l.place(x=self.screen_width*0.455, y=self.screen_height*0.02)
    
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
            self.ball.after_cancel(self._timer)            
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
#self.box_value = StringVar()
 #       self.box = ttk.Combobox(root, textvariable=self.box_value, 
  #                              state='readonly')
   #     self.box['values'] = ('1920x1080', '1680x1050', '1600x900', '1400x1050',  '1366x768', '1360x768', '1280x1024', \
    #                          '1280x768', '1280x720', '1024x768', '1024x600', '800x600')
     #   self.box.current(1)
      #  self.box.pack()
