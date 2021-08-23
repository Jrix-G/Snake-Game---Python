#Planet System made by Jason Mourier

from tkinter import *

window = Tk()
window.title("PlanetSytem")
window.minsize(1400, 700)
window.maxsize(1400, 700)

canvas = Canvas(window, width=1400, height=700)



x = 10
y = 10
width = 10
height= 10

alala = canvas.create_rectangle(x, y, x+width, y+height, fill='red')
canvas.pack()

def right(event):
    global x,alala
    x += 10
    canvas.delete(alala)
    alala = canvas.create_rectangle(x, y, x+width, y+height, fill='red')
    canvas.pack()
    print("right")
def left(event):
    global x,alala
    x -= 10
    canvas.delete(alala)
    alala = canvas.create_rectangle(x, y, x+width, y+height, fill='red')
    canvas.pack()
    print("left")
def up(event):
    global y,alala
    y -= 10
    canvas.delete(alala)
    alala = canvas.create_rectangle(x, y, x+width, y+height, fill='red')
    canvas.pack()
    print("up")
def down(event):
    global y,alala
    y += 10
    canvas.delete(alala)
    alala = canvas.create_rectangle(x, y, x+width, y+height, fill='red')
    canvas.pack()
    print("down")



window.bind("<Right>", right)
window.bind("<Left>", left)
window.bind("<Up>", up)
window.bind("<Down>", down)
mainloop()