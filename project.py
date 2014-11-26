#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" ProJect """
import time
from Tkinter import *
from ImageTk import PhotoImage
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

        #image
        self.img = list()
        self.img.append(ImageTk.PhotoImage(file="1.jpg"))
        self.img.append(ImageTk.PhotoImage(file="2.jpg"))
        self.img.append(ImageTk.PhotoImage(file="3.jpg"))
        self.idx1, self.idx2 = 0, 0

        #loop
        self.ball.mainloop()

    def change(self):
        if self.idx < len(self.img)-1:
            box1 = Label(self.ball, image=self.img[self.idx]).place(x=10, y=20)
            self.idx += 1
        else:
            box1 = Label(self.ball, image=self.img[self.idx]).place(x=10, y=20)

    def reset(self):
        self.idx = 0
        box1 = Label(self.ball, image=self.img[self.idx]).place(x=10, y=20)

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
