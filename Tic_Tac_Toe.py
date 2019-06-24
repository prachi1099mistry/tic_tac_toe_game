from tkinter import *               #importing to create game window

import tkinter.messagebox       #import to display the winner
tk=Tk()                                     #creating empty window
tk.title("Tic Tac Toe")             #title of the window

click = True                            #check for the number of clicks

def winCheck():
    if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or                 #first row check
          button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or               #second row check
          button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or               #third row check
          button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or               #Diagonal check
          button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or               #other diagonal check 
          button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or               #first column check
          button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or               #Second column check
          button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):                #third column check
        tkinter.messagebox.showinfo("Winner X","CONGRATULATIONS..You have just won the Game")
        

    elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or            #first row check
          button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or              #second row check
          button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or               #third row check
          button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or               #Diagonal check
          button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or               #other diagonal check 
          button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or               #first column check
          button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or               #Second column check
          button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):                #third column check
        tkinter.messagebox.showinfo("Winner O","CONGRATULATIONS..You have just won the Game")



def checker (buttons):                                                     #function to write X or O
    global click                                                                  #creating a global variable
    if buttons["text"] == " " and click == True:                #for odd clicks print X
        buttons["text"] = "X"
        click = False
        winCheck()                                                                  #check for winner (call the function)
    elif buttons["text"] == " " and click == False:                #for even clicks print O
        buttons["text"] = "O"
        click = True
        winCheck()                                                                  #check for winner (call the function)



buttons = StringVar()                                                           #creating a Stirng variable to store the data X or O
button1 = Button (tk,text=" ", font=('Times 26 bold'),height = 4 , width = 8, command=lambda:checker(button1))
button1.grid(row=1,column=0,sticky= S+N+E+W)            #creating buttons when clicked the functionc 'checker()' is called

button2 = Button (tk,text=" ", font=('Times 26 bold'),height = 4 , width = 8, command=lambda:checker(button2))
button2.grid(row=1,column=1,sticky= S+N+E+W)            #creating buttons when clicked the functionc 'checker()' is called

button3 = Button (tk,text=" ", font=('Times 26 bold'),height = 4 , width = 8, command=lambda:checker(button3))
button3.grid(row=1,column=2,sticky= S+N+E+W)            #creating buttons when clicked the functionc 'checker()' is called

button4 = Button (tk,text=" ", font=('Times 26 bold'),height = 4 , width = 8, command=lambda:checker(button4))
button4.grid(row=2,column=0,sticky= S+N+E+W)            #creating buttons when clicked the functionc 'checker()' is called

button5 = Button (tk,text=" ", font=('Times 26 bold'),height = 4 , width = 8, command=lambda:checker(button5))
button5.grid(row=2,column=1,sticky= S+N+E+W)            #creating buttons when clicked the functionc 'checker()' is called

button6 = Button (tk,text=" ", font=('Times 26 bold'),height = 4 , width = 8, command=lambda:checker(button6))
button6.grid(row=2,column=2,sticky= S+N+E+W)            #creating buttons when clicked the functionc 'checker()' is called

button7 = Button (tk,text=" ", font=('Times 26 bold'),height = 4 , width = 8, command=lambda:checker(button7))
button7.grid(row=3,column=0,sticky= S+N+E+W)            #creating buttons when clicked the functionc 'checker()' is called

button8 = Button (tk,text=" ", font=('Times 26 bold'),height = 4 , width = 8, command=lambda:checker(button8))
button8.grid(row=3,column=1,sticky= S+N+E+W)            #creating buttons when clicked the functionc 'checker()' is called

button9 = Button (tk,text=" ", font=('Times 26 bold'),height = 4 , width = 8, command=lambda:checker(button9))
button9.grid(row=3,column=2,sticky= S+N+E+W)            #creating buttons when clicked the functionc 'checker()' is called

tk.mainloop()                                   #running the tkinter window 
