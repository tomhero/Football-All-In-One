""" ProJect """
from Tkinter import *
from PIL import Image, ImageTk
import tkMessageBox

class Program(object):
    def __init__(self):
        self.root = Tk()
        self.root.geometry('650x450+350+150')
        self.root.title('Wellcome to Sport Day All in one')
        app_name = Label(self.root, text='Sport Day All in one')
        but = Button(self.root, text="GO!", fg='green', bg='black')
        app_name.place(x=280,y=0)
        but.place(x=320, y=25)
        image = Image.open("test.bmp")
        photo = ImageTk.PhotoImage(image)

    def warp():
        Football()
        self.root.destroy()


        self.root.mainloop()

class Football(object):
    def __init__(self):
        self.ball = Tk()
        self.ball.geometry('1366x768')

        self.ball.mainloop()

Program()




        
