#Importing the Tkinter module library
from tkinter import *

#Importing the random function
import random

#Tic Tac Toe Game
# -Game class to group our functions together
# -Display (x,y)
# -Board (rows and columns)
# -Place pieces ('x', 'o')

#Defining the functions that we will need
def next_turn(row, column):
    
    #Access to our player
    global player
    
    #We want to see if the button is empty 
    if buttons[row][column]['text'] == "" and check_winner() is False:
        
        if player == list_players[0]:
            buttons[row][column]['text'] = player
            
            #If there is no winner, switch user for their turn
            if check_winner() is False:
                player = list_players[1]
                label.config(text=(list_players[1]+" turn"))
            
            elif check_winner() is True:
                label.config(text=(list_players[0] + " wins"))
            
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))
        else: 
            buttons[row][column]['text'] = player
            
            #If there is no winner, switch user for their turn
            if check_winner() is False:
                player = list_players[0]
                label.config(text=(list_players[0]+" turn"))
            
            elif check_winner() is True:
                label.config(text=(list_players[1] + " wins"))
            
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))    


def check_winner():
    #Check horizontal winners
    for row in range(3):
        if buttons [row][0]['text'] == buttons [row][1]['text'] == buttons [row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
        
    #Check vertical winners
    for column in range(3):
        if buttons [0][column]['text'] == buttons [1][column]['text'] == buttons [2][column]['text'] !="":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    #Check diagonal winners
    if buttons [0][0]['text'] == buttons [1][1]['text'] == buttons [2][2]['text'] !="":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    
    elif buttons [0][2]['text'] == buttons [1][1]['text'] == buttons [2][0]['text'] !="":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    
    else:
        return False

#Empty spaces function
def empty_spaces():
    spaces = 9
    
    for row in range(3):
        for column in range(3):
            #If buttons are not empty, delete an empty space
            if buttons [row][column]['text'] != "":
                spaces -=1
    if spaces == 0:
        return False
    else:
        return True

#Restarts a new game
def new_game():
    
    global player
    
    #Chooses random player for their first turn
    player = random.choice(list_players)
    label.config(text= player + " turn")
    
    #Clears buttons on the grid
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text = "", bg="#F0F0F0")


#Main body of the program

#Creating the basic window interface
window = Tk()
window.title("Tic-Tac-Toe")

#Creating a list of players
list_players = ["X","O"]

#Selecting a random player by passing our list of players
player = random.choice(list_players)

#Creating a 2D list of buttons
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

#Helps display the users turn
label = Label(text=player + " turn", font=('consolas',40))
label.pack(side="top")

#Restarts the game button
#Changing the text and font of the reset button
reset_button = Button(text = "restart", font=('consolas', 20), command = new_game) #When clicking this button, it will call the new game function
reset_button.pack (side = "top")

#A frame is used as the foundation class to implement complex widgets
frame = Frame(window)
#Makes the program fill in the window
frame.pack()

#Nested for loop to diplsay the buttons on each spot of the grind
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2, #dimensions and no text for the buttons
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)
        

window.mainloop()



#End of body program