from tkinter import *
from tkinter import Tk

root = Tk()
root.title("Naughts and Crosses")
root.geometry("300x300")

counter = 0
l=[]
buttonAssign =[None, None, None, None, None, None, None, None, None]

# def imgGen():
winnerImg = PhotoImage(file='winner.png')
player1Img = PhotoImage(file='myButtonP1.png')
player2Img = PhotoImage(file='myButtonP2.png')
emptyImg=PhotoImage(file='myButton.png')

def create_buttons():
	global button1
	for column in range(3):
		for row in range(3):
			print(row+3*column)
			button1 = Button(root, image=emptyImg, width=100, height=100, command=lambda n = row+3*column : handle_button_click(n))
			button1.place(x=column*100, y=row*100)

def handle_button_click(n):
	print("clicked",n)
	buttonAssign[n] = button1
	print(buttonAssign)
	if (counter % 2) == 0:
		currentButton.config(image = player1Img, command = square_taken)
		update_move(n)
		check_win()
	else:
		currentButton.config(image = player2Img, command = square_taken)
		update_move(n)
		check_win()



def square_taken():
	messagebox.showinfo("Square taken")

create_buttons()


root.mainloop()