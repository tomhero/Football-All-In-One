#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" ProJect """
import time
from Tkinter import *
from PIL import Image, ImageTk
import tkMessageBox
import tkFont

class Program(object):
    def __init__(self):
        self.root = Tk()
        self.root.geometry('650x450+350+150')
        my_font = tkFont.Font(self.root, family='TH SarabunPSK', size=36, weight="bold")
        self.root.title('Wellcome to Sport Day All in one')
        app_name = Label(self.root, text='ป้ายกีฬาพาเพลิน ,Sport Day All in one', font=my_font)
        app_name.place(x=20,y=0)
        image1 = Image.open("test.bmp")
        photo = ImageTk.PhotoImage(image1)
        but = Button(self.root, image=photo, cursor="plus", command=self.football)
        but.image = photo
        but.place(x=25, y=50)
        but.image = image1
        self.root.mainloop()
        
    def football(self):
        self.ball = Toplevel()
        self.ball.geometry('%dx%d'% (1920, 1080))
        self.ball.title('Football')
        label1 = Label(self.ball, text='Hello').place(x=50, y=50)
        bg_image = Image.open("fifa_15.jpg")
        bg_image = bg_image.resize((1920,1080), Image.ANTIALIAS)
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_pic = Label(self.ball, image=bg_photo)
        bg_pic.place(x=0, y=0)
        self.ball.mainloop()

    

Program()

        
