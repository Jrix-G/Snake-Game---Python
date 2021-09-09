#EasySnake made by Jason

from tkinter import *
from random import *

window = Tk()
window.title("EasySnake")
window.minsize(700, 700)
window.maxsize(700, 700)

canvas = Canvas(window, width=700, height=700)

left2 = ""
right2 = True
up2 = ""
down2 = ""
i = 0
longueurserp = 1

x = 10
y = 10
width = 10
height= 10

tab = []
name = canvas.create_rectangle(x, y, x+width, y+height, fill='')
mange = False
xran = randint(10, 600)
yran = randint(10, 600)
while xran%10 != 0:
    xran = randint(10, 600)
while yran%10 != 0:
    yran = randint(10, 600)
mange = canvas.create_rectangle(xran, yran, xran+width, yran+height, fill='red')

tb = []
def Run():
    global left2, up2, down2, right2, x, alala, y, addcanvas, mange, name, tb, tb2, name12, xran, yran, longueurserp, tab, impaire
    window.after(50, Run)

    tab = []
    tb += [[x, y]]
    tb2 = tb
    tb2.reverse()

    if x > 690 or x < 0 or y > 690 or y < 0: 
        x = 20
        y = 20
        longueurserp = 1
        left2 = False
        up2 = False
        down2 = False
        right2 = True
    
    impaire = 0
    longueurtableau = len(tb)-1
    for i in range(longueurserp):
        if i%2 == 0: 
            o = i/2
            tab += [tb[int(o)]]
        else:
            if len(tb) > 2: 
                tab += [tb[longueurtableau-impaire]]
                impaire+=1
    
    if len(tab) > 1: #Vérificateur que le serpent ne se passe pas dessus ou se touche
            for i in range(len(tab)):
                m = 0
                for n in range(len(tab)):
                    if tab[i] == tab[n]:
                        m += 1
                        if m == 2:
                            longueurserp = 1


    if x == xran and y == yran:
        canvas.delete(mange)
        addcanvas()

        xran = randint(10, 600)
        yran = randint(10, 600)
        while xran%10 != 0:
            xran = randint(10, 600)
        while yran%10 != 0:
            yran = randint(10, 600)
        mange = canvas.create_rectangle(xran, yran, xran+width, yran+height, fill='red')

    if right2 == True:
        x+=10
        canvas.delete("all")
        for i in range(len(tab)):
            name = canvas.create_rectangle(tab[i][0], tab[i][1], tab[i][0]+width, tab[i][1]+height, fill='green')
            mange = canvas.create_rectangle(xran, yran, xran+width, yran+height, fill='red')
        canvas.pack()
        
    if left2 == True:
        x-=10
        canvas.delete("all")
        for i in range(len(tab)):
            name = canvas.create_rectangle(tab[i][0], tab[i][1], tab[i][0]+width, tab[i][1]+height, fill='green')
            mange = canvas.create_rectangle(xran, yran, xran+width, yran+height, fill='red')
        canvas.pack()
    if up2 == True: 
        y-=10
        canvas.delete("all")
        for i in range(len(tab)):
            name = canvas.create_rectangle(tab[i][0], tab[i][1], tab[i][0]+width, tab[i][1]+height, fill='green')
            mange = canvas.create_rectangle(xran, yran, xran+width, yran+height, fill='red')
        canvas.pack()
    if down2 == True:
        y+=10
        canvas.delete("all")
        for i in range(len(tab)):
            name = canvas.create_rectangle(tab[i][0], tab[i][1], tab[i][0]+width, tab[i][1]+height, fill='green')
            mange = canvas.create_rectangle(xran, yran, xran+width, yran+height, fill='red')
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
        global longueurserp
        longueurserp += 1

    window.bind("<Right>", right)
    window.bind("<Left>", left)
    window.bind("<Up>", up)
    window.bind("<Down>", down)

    canvas.create_text([500, 10], anchor=CENTER, text=longueurserp)
window.after(1, Run)
run = True
window.mainloop()
