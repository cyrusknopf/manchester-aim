# aim trainer
# author: Cyrus Knopf
# last edit date: 13:31 25/11/2022
# last edit: colour changes, comments
# resolution: 1280x720

import os.path
import random
import tkinter
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

root = Tk()
root.title("manchester aim")  # root set up
root.geometry("1280x720+50+100")
root.resizable(False, False)
root.config(cursor="tcross")

l = []  # global list to store img1 when generate per target
top10Names = []  # empty lists for leaderboard generation
top10Scores = []
gameLoaded = 0  # auto sets that a game has not been loaded

background = Canvas(root, width=1280, height=720, bg='#191a19')
background.pack()  # canvas creation, dimensions, color


def drawGrid():  # drawing lines for aesthetics
    background.create_line(0, 550, 280, 400, fill='#2b2b2b', width=2)
    background.create_line(1280, 550, 1000, 400, fill='#2b2b2b', width=2)
    background.create_line(280, 400, 1000, 400, fill='#2b2b2b', width=2)
    background.create_line(280, 400, 280, 0, fill='#2b2b2b', width=2)
    background.create_line(1000, 400, 1000, 0, fill='#2b2b2b', width=2)


def pausedPressed(event):  # function handling pause menu
    global pauseLabel
    global paused
    paused = not paused
    if paused == True:
        pauseLabel = Label(background, text='paused')
        pauseLabel.place(relx=0.5, rely=0.5, anchor='center')
        pauseLabel.config(bg='#232423', fg='white',
                          font=("Yu Gothic", 50), width='100')
    else:	#removes the pause menu if pressed while active 
        pauseLabel.destroy()


def bossPressed(event2):  # function handling boss key being pressed
    global bossScreen
    global bossd
    # print("boss pressed")
    bossd = not bossd
    if bossd == True:
        img2 = PhotoImage(file='bossimage.png')
        bossScreen = Label(background, image=img2)
        bossScreen.photo = img2
        bossScreen.place(relx=0, rely=0, anchor=NW)
    else:	#removes the boss view if pressed while active
        bossScreen.destroy()


def clock(i, label):  # clock running with period 1000ns
    global currentTime
    if paused == False and bossd == False:	#checks if pause or boss active
        # print("clock running")
        if i > 0:
            i = i-1
            label.set(i)
            currentTime = clockLabel.cget("text")
            background.after(1000, lambda: clock(i, label))	#executes clock function again
        else:
            clockEnd()  # 0 time left = end game
    else:
        background.after(1000, lambda: clock(i, label))	#else triggers if either pause/boss key active and executes the clock again


def clockStart():  # sets variables, binds and labels for when the clock starts
    global paused
    global bossd
    global timeLeft
    global clockLabel
    global currentScore
    global gameLoaded
    paused = False	#starts game unpaused and no unbossed
    bossd = False
    root.bind('<Escape>', pausedPressed)
    root.bind('<Return>', bossPressed)
    timeLeft = 1 	#time left is a variable (1 or 0) that defines WHETHER there is time left on the clock or not
    if gameLoaded == 1:		#deals with loads or new games
        clockLength = loadedTime
        currentScore = loadedScore
    else:
        clockLength = timeInput
        currentScore = 0
    clockVar = tkinter.StringVar()
    clockVar.set(clockLength)
    clockLabel = Label(background, textvariable=clockVar)	#labels the clock dynamically with StringVar
    clockLabel.place(relx=0.04, rely=0.04, anchor='center')
    clockLabel.config(font=("Yu Gothic", 25), bg='#191a19', fg='white')
    clock(clockLength, clockVar)


def showScore():
    global scoreDisplay
    global currentScore
    global loadedScore
    try:	#deals with load games
        currentScore = loadedScore
    except:
        pass
    scoreDisplay = Label(background, text=str(currentScore), bg='#191a19', fg='white')	#label to display score
    scoreDisplay.config(font=("Yu Gothic", 25))
    scoreDisplay.place(relx=0.5, rely=0.04, anchor='center')


def clockEnd():  # sets binds for game in progress, resets score, calls writing score function
    global timeLeft
    global currentScore
    global tempScore
    root.unbind('<Escape>')		#unbinds in game binds
    root.unbind('<Return>')
    root.unbind('<Delete>')
    timeLeft = 0 	#designates that there is no time left in the game
    tempScore = currentScore	#temp score for writing to leaderboard
    currentScore = -1	#resets current score
    writeAll()


def hit1(e):  # triggers on event of target being hit
    if paused == False:
        global currentScore
        # print("hit1")
        background.delete(target1)  # when target clicked removed and
        genNext()  # triggers next generation
        currentScore = currentScore + 1
        scoreDisplayString = str(currentScore)
        try:
            scoreDisplay.config(text=scoreDisplayString)	#solved errors when displaying score
        except:
            pass


def moveLeft():  # two similar functions to handle movement
    background.move(target1, -0.1, 0)


def moveRight():
    background.move(target1, 0.1, 0)


def moveTarget():  # collision detection, changes direction when hits wall
    global direction
    if paused == False:		#only moves if game not paused
        try:
            if isMoving == True:	#checks to see if target should move
                if background.coords(target1)[0] <= 0:
                    direction = 2
                elif background.coords(target1)[0] >= 1205:
                    direction = 1
                if direction == 1:
                    moveLeft()
                elif direction == 2:
                    moveRight()
        except:
            # print("round finished")
            return
        background.after(1, moveTarget)	#runs the moveTarget function every 1 ms to produce smooth movement
    else:
        background.after(1, moveTarget)


# generates next target once one has been hit,
# if a game is being loaded it uses the position saved in text file
def genNext():
    global x
    global y
    global target1
    global isMoving
    global timeLeft
    global direction
    global gameLoaded
    # print("gameloaded =", gameLoaded)
    if gameLoaded == 1:
        direction = loadedDirection
        isMoving = loadedMoving
        x = loadedX
        y = loadedY
        gameLoaded = 0
    else:
        direction = random.randint(1, 2)
        isMoving = random.randint(0, 1)
        x = random.randint(100, 1180)
        y = random.randint(100, 620)
    if timeLeft == 1:	#while there is still time left on the clock:
        img1 = PhotoImage(file="aimlabSpawn.png")
        l.append(img1)	#add img1 to global list
        target1 = background.create_image(x, y, anchor=NW, image=img1)
        background.tag_bind(target1, '<Button-1>', hit1)  # spawn target
        moveTarget()
    else:	#if there is no time left go back to the menu
        genLB()
        menu()


# writes names to leaderboard, if savedname exists it means a game has
# been loaded and uses the name that was entered from the load
def writeAll():
    global username
    global currentScore
    if os.path.exists("savedname.txt") == True:
        sn = open("savedname.txt", "r")
        username = sn.readlines(1)
        username = str(username)
        username = username.strip("]['""")
        sn.close()
        os.remove("savedname.txt")
    lb = open("leaderboard.txt", "a")	#appends the leaderboard file with name and score
    lb.write(f"{username}\n")
    lb.write(f"{tempScore}\n")
    lb.close()


def genSaveButton():  # generates the save game button while in game
    saveButton = Button(background, text='save&quit', command=saveGame)
    saveButton.place(relx=0.95, rely=0.05, anchor='center')
    saveButton.config(bg='#212121', fg='white', font=("Yu Gothic", 12), width='10')


def saveGame():  # writes current variables to file, overwriting savedgame and savedname
    global savedScore
    global savedX
    global savedY
    global savedDirection
    global savedTime
    global savedMoving
    global username
    savedScore = currentScore
    savedX = x
    savedY = y
    savedDirection = direction
    savedTime = currentTime
    savedMoving = isMoving
    sg = open("savedgame.txt", "a")
    sg.truncate(0)
    sg.write(f"{savedScore}\n")
    sg.write(f"{savedX}\n")
    sg.write(f"{savedY}\n")
    sg.write(f"{savedDirection}\n")
    sg.write(f"{savedTime}\n")
    sg.write(f"{savedMoving}\n")
    sg.close()
    sn = open("savedname.txt", "a")
    sn.truncate(0)
    sn.write(f"{username}")
    sn.close()
    root.destroy()	#quits


def loadGame():  # puts all the needed saved variables in list for loading
    global loadedScore
    global loadedX
    global loadedY
    global loadedDirection
    global loadedTime
    global loadedMoving
    global loadedList
    global loadedName
    global username
    sg = open("savedgame.txt", "r")
    # print("Loaded")
    gameLoaded = 1
    loadedList = []
    loadList = sg.readlines()
    sg.close()
    os.remove("savedgame.txt")
    for i in loadList:
        i = i.strip('\n')
        i = int(i)
        loadedList.append(i)
    sn = open("savedname.txt", "r")
    username = sn.readlines(1)
    loadedScore = loadedList[0]
    loadedX = loadedList[1]
    loadedY = loadedList[2]
    loadedDirection = loadedList[3]
    loadedTime = loadedList[4]
    loadedMoving = loadedList[5]
    startLoadedGame()


def startLoadedGame():  # alternative start game function for when game is loaded
    global loadedScore
    global currentScore
    global gameLoaded
    gameLoaded = 1 		#important variable for generating the game checks if it was loaded
    background.unbind('<B1-Motion>')
    for widget in background.winfo_children():	#clears screen
        widget.destroy()
    showScore()
    try:
        background.delete(nameIco)
        background.delete(clockIco)
        background.delete(logo)
        background.delete(logo2)
    except:
        pass
    currentScore = loadedScore
    root.bind('<Delete>', cheatCode)
    clockStart()
    genNext()
    genSaveButton()


# generates all buttons on the menu, if a saved game file exists a load button is generated
# allows the logo object to be moved by the user

def menu():
    global timeEntry
    global nameEntry
    global startButton
    global logo
    global clockIco
    global nameIco

    for widget in background.winfo_children():	#clears the screen
        widget.destroy()

    nameEntry = Entry(background, justify='center')
    nameEntry.place(relx=0.5, rely=0.7, anchor='center')
    nameEntry.config(bg='#212121', fg='white',
                     font=("Yu Gothic", 25), width='30')

    nameImg = PhotoImage(file='whitename.png')
    l.append(nameImg)
    nameIco = background.create_image(340, 490, anchor=NW, image=nameImg)

    startButton = Button(background, text='start game', command=startGame)
    startButton.place(relx=0.4, rely=0.8, anchor='center')
    startButton.config(bg='#212121', fg='white',
                       font=("Yu Gothic", 12), width='10')

    lbButton = Button(background, text='leaderboards', command=showLB)
    lbButton.place(relx=0.5, rely=0.8, anchor='center')
    lbButton.config(bg='#212121', fg='white',
                    font=("Yu Gothic", 12), width='10')

    timeEntry = Entry(background, justify='center')
    timeEntry.place(relx=0.1, rely=0.9, anchor='center')
    timeEntry.config(bg='#212121', fg='white',
                     font=("Yu Gothic", 25), width='10')

    clockImg = PhotoImage(file='whiteclock.png')
    l.append(clockImg)
    clockIco = background.create_image(7, 636, anchor=NW, image=clockImg)

    if os.path.exists("savedgame.txt") == True:
        loadButton = Button(background, text='load game', command=loadGame)
        loadButton.place(relx=0.6, rely=0.8, anchor='center')
        loadButton.config(bg='#212121', fg='white',
                          font=("Yu Gothic", 12), width='10')

    img3 = PhotoImage(file='mannylablogo.png')
    l.append(img3)
    logo = background.create_image(450, 100, anchor=NW, image=img3)

    background.bind('<B1-Motion>', drag)


def drag(e):	#allows the user to move the logo
    global img3
    global logo2
    background.delete(logo)
    img3 = PhotoImage(file='mannylablogo.png')
    logo2 = background.create_image(e.x, e.y, image=img3)


def startGame():		#starts new game
    global timeInput
    global username
    global timeEntry
    global currentScore
    global gameLoaded
    gameLoaded = 0
    currentScore = 0
    root.bind('<Delete>', cheatCode)
    if nameEntry.get() == '':							#checks that username meets criteria
        messagebox.showinfo(" ", "please enter a name")
    elif len(nameEntry.get()) != 3:
        messagebox.showinfo(" ", "please enter a 3 letter name")
    else:

        try:
            timeInput = timeEntry.get()
        except:
            messagebox.showinfo(" ", "please enter an integer time value")
            startGame()
        else:
            try:
                timeInput = int(timeInput)
            except:
                messagebox.showinfo(" ", "please enter an integer time value")
            else:
                background.unbind('<B1-Motion>')
                root.bind('<Delete>', cheatCode)
                username = nameEntry.get()
                username = str(username)
                username = username.upper()
                for widget in background.winfo_children():		#clears screen
                    widget.destroy()
                showScore()
                try:
                    background.delete(nameIco)
                    background.delete(clockIco)
                    background.delete(logo)
                    background.delete(logo2)
                except:
                    pass
                clockStart()		#executes the start game functions
                genNext()
                genSaveButton()


def cheatCode(cheatEvent):		#cheat code that adds 10 to your score
    global currentScore
    currentScore = currentScore + 10
    print("Somebodys cheating!")


def genLB():		#ran when the leaderboard is shown, this function writes the top 10 scores/names to a list to be made into  a label
    global scoreBoard, top10Names, top10Scores, itemNo, listBoard
    scoreBoard = {}
    lb = open("leaderboard.txt", "r")
    listBoard = lb.readlines()
    lb.close()
    for itemNo in range(len(listBoard)):
        listBoard[itemNo] = listBoard[itemNo].strip('\n')
    for i in range(0, len(listBoard), 2):
        scoreBoard[listBoard[i]] = int(listBoard[i+1])
    for i in range(10):
        thisTop = max(scoreBoard, key=scoreBoard.get)
        top10Names.append(thisTop)
        top10Scores.append(scoreBoard[thisTop])
        scoreBoard.pop(thisTop)


def showLB():
    genLB()
    try:
        background.delete(nameIco)	#clears the screen
        background.delete(clockIco)
        background.delete(logo)
        background.delete(logo2)
    except:
        pass

    for widget in background.winfo_children():
        widget.destroy()

    for i in range(10):		#generates top 10 names labels
        currentLabel = 'label' + str(i)
        currentLabel = Label(background, text=top10Names[i], bg='#191a19', fg='white', font=("Yu Gothic", 25), justify='center')
        currentLabel.place(relx=0.3, rely=0.2+0.06*i, anchor="center")

    for i in range(10):		#generates top 10 score labels
        currentLabel = 'label' + str(i)
        currentLabel = Label(background, text=top10Scores[i], bg='#191a19', fg='white', font=("Yu Gothic", 25), justify='center')
        currentLabel.place(relx=0.6, rely=0.2+0.06*i, anchor="center")

    menuButton = Button(background, text='menu', command=menu)	#generates button to take you back to menu
    menuButton.place(relx=0.5, rely=0.8, anchor='center')
    menuButton.config(bg='#212121', fg='white', font=("Yu Gothic", 12), width='10')


drawGrid()	#draws the lines
menu()		#generates menu
root.mainloop()
