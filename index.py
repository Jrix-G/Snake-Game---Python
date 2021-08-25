#Planet System made by Jason Mourier

from tkinter import *
from random import *

window = Tk()
window.title("EasySnake")
window.minsize(1400, 700)
window.maxsize(1400, 700)

canvas = Canvas(window, width=1400, height=700)

left2 = ""
right2 = True
up2 = ""
down2 = ""
i = 0

x = 10
y = 10
width = 10
height= 10
tb = []

name12 = canvas.create_rectangle(x, y, x+width, y+height, fill='')
alala2 = canvas.create_rectangle(x, y, x+width, y+height, fill='')
alala = canvas.create_rectangle(x, y, x+width, y+height, fill='')
canvas.pack()

mange = False
xran = randint(10, 500)
yran = randint(10, 300)
while xran%10 != 0:
    xran = randint(10, 500)
while yran%10 != 0:
    yran = randint(10, 300)
mange = canvas.create_rectangle(xran, yran, xran+width, yran+height, fill='red')


def Run():
    
    global left2, up2, down2, right2, x, alala, y, addcanvas, mange, name, tb, tb2, name12, xran, yran
    window.after(100, Run)

    if x > 1390 or x < 0 or y > 690 or y < 0: 
        window.destroy()

    tb += [[x, y]]
    tb2 = tb
    tb2.reverse()
    if x == xran and y == yran:
        canvas.delete(mange)

        addcanvas()

        xran = randint(10, 500)
        yran = randint(10, 300)
        while xran%10 != 0:
            xran = randint(10, 500)
        while yran%10 != 0:
            yran = randint(10, 300)
        mange = canvas.create_rectangle(xran, yran, xran+width, yran+height, fill='red')

    if right2 == True:
        x+=10
        canvas.delete(alala)
        alala = canvas.create_rectangle(x, y, x+width, y+height, fill='green')
        canvas.pack()
    if left2 == True:
        x-=10
        canvas.delete(alala)
        alala = canvas.create_rectangle(x, y, x+width, y+height, fill='green')
        canvas.pack()
    if up2 == True: 
        y-=10
        canvas.delete(alala)
        alala = canvas.create_rectangle(x, y, x+width, y+height, fill='green')
        canvas.pack()
    if down2 == True:
        y+=10
        canvas.delete(alala)
        alala = canvas.create_rectangle(x, y, x+width, y+height, fill='green')
        canvas.pack()

    def right(event):
        global left2, up2, down2, right2
        left2 = False
        up2 = False
        down2 = False
        right2 = True
        
    def left(event):
        global left2, up2, down2, right2
        right2 = False
        up2 = False
        down2 = False
        left2 = True

    def up(event):
        global left2, up2, down2, right2
        right2 = False
        left2 = False
        down2 = False
        up2 = True

    def down(event):
        global left2, up2, down2, right2
        right2 = False
        left2 = False
        down2 = True
        up2 = False

    def addcanvas():
        global i, alala2, name12
        i+=1
        canvas.delete(name12)
        name12 = canvas.create_rectangle(tb2[1][0], tb2[1][1], x+width, y+height, fill='green')
        canvas.pack()

    window.bind("<Right>", right)
    window.bind("<Left>", left)
    window.bind("<Up>", up)
    window.bind("<Down>", down)

window.after(1, Run)
run = True
window.mainloop()