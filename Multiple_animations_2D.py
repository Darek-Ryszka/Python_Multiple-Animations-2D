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

background_photo = PhotoImage(file='earth.png')
background = canvas.create_image(0, 0, image=background_photo, anchor=NW)

ufo_image_1 = PhotoImage(file='ufo.png')
my_image_1 = canvas.create_image(0, 0, image=ufo_image_1, anchor=NW)

ufo_image_2 = PhotoImage(file='ufo.png')
my_image_2 = canvas.create_image(300, 200, image=ufo_image_2, anchor=NW)

ufo_image_3 = PhotoImage(file='ufo.png')
my_image_3 = canvas.create_image(800, 100, image=ufo_image_3, anchor=NW)

image_width_1 = ufo_image_1.width()
image_height_1 = ufo_image_1.height()

image_width_2 = ufo_image_2.width()
image_height_2 = ufo_image_2.height()

image_width_3 = ufo_image_3.width()
image_height_3 = ufo_image_3.height()

while True:
    coordinates1 = canvas.coords(my_image_1)
    coordinates2 = canvas.coords(my_image_2)
    coordinates3 = canvas.coords(my_image_3)
    print(coordinates1, coordinates2, coordinates3)
    if coordinates1[0] >= (WIDTH - image_width_1) or coordinates1[0] < 0:
        xVelocity1 = -xVelocity1
    if coordinates1[1] >= (HEIGHT - image_height_1) or coordinates1[1] < 0:
        yVelocity1 = -yVelocity1
    if coordinates2[0] >= (WIDTH - image_width_2) or coordinates2[0] < 0:
        xVelocity2 = -xVelocity2
    if coordinates2[1] >= (HEIGHT - image_height_2) or coordinates2[1] < 0:
        yVelocity2 = -yVelocity2
    if coordinates3[0] >= (WIDTH - image_width_3) or coordinates3[0] < 0:
        xVelocity3 = -xVelocity3
    if coordinates3[1] >= (HEIGHT - image_height_3) or coordinates3[1] < 0:
        yVelocity3 = -yVelocity3

    canvas.move(my_image_1, xVelocity1, yVelocity1)
    canvas.move(my_image_2, xVelocity2, yVelocity2)
    canvas.move(my_image_3, xVelocity3, yVelocity3)

    window.update()
    time.sleep(0.01)

window.mainloop()
