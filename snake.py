from tkinter import *

root = Tk()
root.title("snake")
root.geometry("720x720+50+100")
root.resizable(False, False)
canv = Canvas(root, width=1000, height=1000, bg='grey')
canv.pack()

snakehead = canv.create_oval(10,10,30,30, fill='white')
e=1

def moveright(e):
    right()
def right():
    canv.move(snakehead, 10, 0)
    root.after(500, right)
def moveleft(e):
    left()
def left():
    canv.move(snakehead, -10, 0)
    root.after(500, left)
def moveup(e):
    up()
def up():
    canv.move(snakehead, 0, -10)
    root.after(500, up)
def movedown(e):
    down()
def down():
    canv.move(snakehead, 0, 10)
    root.after(500, down)


root.bind("<Left>", moveleft)
root.bind("<Right>", moveright)
root.bind("<Up>", moveup)
root.bind("<Down>", movedown)

root.mainloop()