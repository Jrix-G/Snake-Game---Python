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
left2 = True
right2 = True
up2 = True
down2 = True
def Run():
    global left2, up2, down2, right2
    window.after(100, Run)
    print(right2)
    if right2 == True:
        global x,alala
        x+=10
        print("Oui")
        canvas.delete(alala)
        alala = canvas.create_rectangle(x, y, x+width, y+height, fill='red')
        canvas.pack()
    def right(event):
        global left2, up2, down2, right2
        left2 = False
        up2 = False
        down2 = False

        global x,alala
        x += 10
        canvas.delete(alala)
        alala = canvas.create_rectangle(x, y, x+width, y+height, fill='red')
        canvas.pack()
        print("right")
        if x > 1390 or x < 0 or y > 690 or y < 0:
            window.destroy()
        right2 = True
        
        
    def left(event):
        global left2, up2, down2, right2
        global x,alala
        right2 = False
        up2 = False
        down2 = False
        
        x -= 10
        canvas.delete(alala)
        alala = canvas.create_rectangle(x, y, x+width, y+height, fill='red')
        canvas.pack()
        print("left")
        if x > 1390 or x < 0 or y > 690 or y < 0:
            window.destroy()
        addcanvas()
    def up(event):
        global y,alala
        y -= 10
        canvas.delete(alala)
        alala = canvas.create_rectangle(x, y, x+width, y+height, fill='red')
        canvas.pack()
        print("up")
        if x > 1390 or x < 0 or y > 690 or y < 0:
            window.destroy()
    def down(event):
        global y,alala
        y += 10
        canvas.delete(alala)
        alala = canvas.create_rectangle(x, y, x+width, y+height, fill='red')
        canvas.pack()
        print("down")
        if x > 1390 or x < 0 or y > 690 or y < 0:
            window.destroy()
    def addcanvas():
        pass

    window.bind("<Right>", right)
    window.bind("<Left>", left)
    window.bind("<Up>", up)
    window.bind("<Down>", down)

window.after(1, Run)
run = True
window.mainloop()