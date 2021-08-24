#Planet System made by Jason Mourier

from tkinter import *
from typing import get_origin

window = Tk()
window.title("PlanetSytem")
window.minsize(1400, 700)
window.maxsize(1400, 700)

canvas = Canvas(window, width=1400, height=700)

left2 = ""
right2 = ""
up2 = ""
down2 = ""
i = 0

x = 10
y = 10
width = 10
height= 10

alala2 = canvas.create_rectangle(x, y, x+width, y+height, fill='red')
alala = canvas.create_rectangle(x, y, x+width, y+height, fill='red')
canvas.pack()

mange = 0

def Run():
    
    global left2, up2, down2, right2, x, alala, y, addcanvas, mange
    window.after(120, Run)

    if x > 1390 or x < 0 or y > 690 or y < 0: 
        window.destroy()

    if right2 == True:
        x+=10
        canvas.delete(alala)
        alala = canvas.create_rectangle(x, y, x+width, y+height, fill='red')
        canvas.pack()
        if mange < 1:
            mange+=1
            addcanvas()
    if left2 == True:
        x-=10
        canvas.delete(alala)
        alala = canvas.create_rectangle(x, y, x+width, y+height, fill='red')
        canvas.pack()
    if up2 == True: 
        y-=10
        canvas.delete(alala)
        alala = canvas.create_rectangle(x, y, x+width, y+height, fill='red')
        canvas.pack()
    if down2 == True:
        y+=10
        canvas.delete(alala)
        alala = canvas.create_rectangle(x, y, x+width, y+height, fill='red')
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
        global i, alala2
        i+=1
        name = str(i)
        name = canvas.create_rectangle(x, y, x+width, y+height, fill='green')
        canvas.pack()
        canvas.delete(i)
    window.bind("<Right>", right)
    window.bind("<Left>", left)
    window.bind("<Up>", up)
    window.bind("<Down>", down)

window.after(1, Run)
run = True
window.mainloop()