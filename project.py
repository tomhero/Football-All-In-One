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
        image = Image.open("test.bmp")
        photo = ImageTk.PhotoImage(image)
        test_photo = Label(self.root, image=photo).place(x=20, y=50)
        but = Button(self.root, image=photo, cursor="plus", command=self.new).place(x=25, y=50)
        self.root.mainloop()
        
    def new(self):
        ball = Tk()
        ball.geometry('1366x768')
        label1 = Label(ball, text='Hello').place(x=50, y=50)

        self.root.mainloop()

Program()


        
