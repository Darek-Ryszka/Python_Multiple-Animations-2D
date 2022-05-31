from tkinter import *
import time

WIDTH = 1000
HEIGHT = 500
xVelocity1 = 1
yVelocity1 = 1
xVelocity2 = 1
yVelocity2 = 1
xVelocity3 = 1
yVelocity3 = 1
window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

ufo_image1 = PhotoImage(file='ufo.png')
my_image1 = canvas.create_image(0, 0, image=ufo_image1, anchor=NW)

ufo_image2 = PhotoImage(file='ufo.png')
my_image2 = canvas.create_image(300, 200, image=ufo_image2, anchor=NW)

ufo_image3 = PhotoImage(file='ufo.png')
my_image3 = canvas.create_image(800, 100, image=ufo_image3, anchor=NW)

image_width1 = ufo_image1.width()
image_height1 = ufo_image1.height()

image_width2 = ufo_image2.width()
image_height2 = ufo_image2.height()

image_width3 = ufo_image3.width()
image_height3 = ufo_image3.height()

while True:
    coordinates1 = canvas.coords(my_image1)
    coordinates2 = canvas.coords(my_image2)
    coordinates3 = canvas.coords(my_image3)
    print(coordinates1, coordinates2, coordinates3)
    if coordinates1[0] >= (WIDTH - image_width1) or coordinates1[0] < 0:
        xVelocity1 = -xVelocity1
    if coordinates1[1] >= (HEIGHT - image_height1) or coordinates1[1] < 0:
        yVelocity1 = -yVelocity1
    if coordinates2[0] >= (WIDTH - image_width2) or coordinates2[0] < 0:
        xVelocity2 = -xVelocity2
    if coordinates2[1] >= (HEIGHT - image_height2) or coordinates2[1] < 0:
        yVelocity2 = -yVelocity2
    if coordinates3[0] >= (WIDTH - image_width3) or coordinates3[0] < 0:
        xVelocity3 = -xVelocity3
    if coordinates3[1] >= (HEIGHT - image_height3) or coordinates3[1] < 0:
        yVelocity3 = -yVelocity3

    canvas.move(my_image1, xVelocity1, yVelocity1)
    canvas.move(my_image2, xVelocity2, yVelocity2)
    canvas.move(my_image3, xVelocity3, yVelocity3)

    window.update()
    time.sleep(0.01)

window.mainloop()
