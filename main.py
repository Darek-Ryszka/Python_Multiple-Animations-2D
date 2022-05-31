from tkinter import *
import time

WIDTH = 1000
HEIGHT = 500
window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

ufo_image1 = PhotoImage(file='ufo.png')
my_image1 = canvas.create_image(0, 0, image=ufo_image1, anchor=NW)

ufo_image2 = PhotoImage(file='ufo.png')
my_image2 = canvas.create_image(300, 200, image=ufo_image2, anchor=NW)

ufo_image3 = PhotoImage(file='ufo.png')
my_image3 = canvas.create_image(800, 100, image=ufo_image3, anchor=NW)

window.mainloop()
