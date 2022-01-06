from tkinter import *
# 
# ------------ Initialisation of Main Window ----------
# 
window = Tk()
window.title("EasySnakeMenu")
window.minsize(400, 400)
window.maxsize(400, 400)


def run_program():
    window.destroy()
    import snake.py
    
button = Button(window, text='Run', command=run_program)
button.pack(side = 'top')




window.mainloop()
