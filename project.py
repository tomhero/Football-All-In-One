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
        but_font_ok = tkFont.Font(self.ball, size=int(self.screen_width*0.015), weight="bold")
        but_quit = Button(self.ball, text='CLOSE', bg='#ff2424', font=but_font, command=self.quit_fx)
        but_quit.place(x=self.screen_width*0.935, y=self.screen_height*0.015)
        but1 = Button(self.ball, text="ADD 1 POINT", font=but_font, command=self.change).place(x=self.screen_width*0.06, y=self.screen_height*0.55)
        but_re = Button(self.ball, text="RESET POINT", font=but_font, command=self.reset).place(x=self.screen_width*0.46, y=self.screen_height*0.9)
        but2 = Button(self.ball, text="ADD 1 POINT", font=but_font, command=self.change2).place(x=self.screen_width*0.71, y=self.screen_height*0.55)
        but_start = Button(self.ball, text="start", font=but_font, command=self.Start).place(x=self.screen_width*0.433, y=self.screen_height*0.12)
        but_stop = Button(self.ball, text="stop", font=but_font, command=self.Stop).place(x=self.screen_width*0.4875, y=self.screen_height*0.12)
        but_reset = Button(self.ball, text="reset", font=but_font, command=self.Reset).place(x=self.screen_width*0.54, y=self.screen_height*0.12)
        self.name1, self.name2 = StringVar(), StringVar()
        self.en1 = Entry(self.ball, textvariable=self.name1, font=but_font)
        self.en1.place(x=self.screen_width*0.06, y=self.screen_height*0.05)
        self.en2 = Entry(self.ball, textvariable=self.name2, font=but_font)
        self.en2.place(x=self.screen_width*0.71, y=self.screen_height*0.05)
        self.buto1 = Button(self.ball, text="OK", font=but_font_ok, command=self.make_name1) #but ok
        self.buto1.place(x=self.screen_width*0.215, y=self.screen_height*0.011)
        self.buto2 = Button(self.ball, text="OK", font=but_font_ok, command=self.make_name2)
        self.buto2.place(x=self.screen_width*0.865, y=self.screen_height*0.011)
        self.ask1 = Label(self.ball, text="Please enter your Name", font=but_font)
        self.ask1.place(x=self.screen_width*0.06, y=self.screen_height*0.01)
        self.ask2 = Label(self.ball, text="Please enter your Name", font=but_font)
        self.ask2.place(x=self.screen_width*0.71, y=self.screen_height*0.01)
        but_win = Button(self.ball, text="Finish", font=but_font, command=self.win).place(x=self.screen_width*0.48, y=self.screen_height*0.35)
        

        #font
        self.big_font = tkFont.Font(self.ball, size=int(self.screen_width*0.15), weight="bold")
        self.but_font2 = tkFont.Font(self.ball, size=int(self.screen_width*0.02), weight="bold")
        

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

    def make_name1(self):
        self.en1.destroy()
        self.buto1.destroy()
        self.ask1.destroy()
        Label(self.ball, text=self.name1.get(), font=self.but_font2, fg='#fa0', bg="#080405").place(x=self.screen_width*0.06, y=self.screen_height*0.05)

    def make_name2(self):
        self.en2.destroy()
        self.buto2.destroy()
        self.ask2.destroy()
        Label(self.ball, text=self.name2.get(), font=self.but_font2, fg='#fa0', bg="#080405").place(x=self.screen_width*0.71, y=self.screen_height*0.05)

    def win(self):
        self.win = Tk()
        self.win.geometry('%dx%d+%d+%d' % (self.screen_width*0.3, self.screen_height*0.11, self.screen_width*0.35, self.screen_height*0.2))
        self.font_butwin = tkFont.Font(self.win, size=int(self.screen_width*0.01), weight="bold")
        if self.idx1 > self.idx2:
            Label(self.win, text='The Winner Is '+self.name1.get(), font=self.font_butwin).pack()
        elif self.idx1 < self.idx2:
            Label(self.win, text='The Winner Is '+self.name2.get(), font=self.font_butwin).pack()
        else:
            Label(self.win, text='Draw', font=self.font_butwin).pack()
            
        

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
        l = Label(self.ball, textvariable=self.timestr, fg='#87ff3d', bg="#080405", font=self.time_font)
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
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        root.geometry('%dx%d+%d+%d' % (self.screen_width*0.5, self.screen_height*0.5, self.screen_width*0.22, self.screen_height*0.2))
        my_font = tkFont.Font(root, family='TH SarabunPSK', size=36, weight="bold")
        root.title('Sport Day All in one')
        app_name = Label(root, text='Sport All in one', font=my_font)
        app_name.pack()
        image1 = Image.open("ball.jpg") #open image file 
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
