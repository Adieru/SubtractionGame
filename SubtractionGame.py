import tkinter as tk
from tkinter import ttk, simpledialog, PhotoImage, Frame

#setting window
window = tk.Tk()
window.geometry("900x500")

my_label = ttk.Label(window, text="Game of Nim", font=("Arial", 25))
my_label.pack(side=tk.TOP, fill=tk.Y, expand=False, pady=5)




#giving initial values to vars
stick_frame = Frame(window)
play_buttons_frame = Frame(window) 
stick_frame.pack()
play_buttons_frame.pack()
stick_image = PhotoImage(file = "matchStick.png")

user_turns = 0
current_tiles = 0
gametiles = []

#initialize game
def reset_game():
    #accessing the global variables
    global user_turns
    global current_tiles
    global gametiles
    global window
    global stick_frame
    global maximum
    
    #setting minima and maxima
    maximum = simpledialog.askinteger("Input", "How many sticks can you remove per turn?", 
                                  parent = window, minvalue = 2, maxvalue = 12)

    num_Sticks = simpledialog.askinteger("Input", "How many sticks shall we play with?", 
                                         parent = window, minvalue=(maximum + 1), maxvalue = 50)

    #setting the number of tiles used
    current_tiles = num_Sticks

    #show current tiles/sticks
    for each in range(num_Sticks):

        gametiles.append(tk.Button(stick_frame, image = stick_image,
                                   height = 900 , width = 35, borderwidth = 0))

        gametiles[each].config(command = lambda: remove_tile("user"))


        #initialize the tiles as buttons
        gametiles[each].pack(side = tk.LEFT, fill = tk.X, expand = False, padx = 5)

    #Setting up buttons for computer's  turns
    comp_turn = tk.Button(play_buttons_frame, text = "let the computer have its turn" ,
                          height = 100, width = 200, borderwidth = 1)
    comp_turn.config(command= lambda: computer_turn())
    comp_turn.pack(side = tk.BOTTOM, fill = tk.X, expand = False, pady = 5)


    

#removing tiles
def remove_tile(who):

    #variables
    global gametiles
    global user_turns
    global maximum
    global current_tiles

    #checking if the player can return or not
    if(who == "user"):
        if(user_turns < maximum):
            current_tiles -= 1
            gametiles[current_tiles].destroy()

        else:
            return False

    else:
        #Computer turn
        current_tiles -= 1
        gametiles[current_tiles].destroy()


    return True


#player's turn

#computer turn
def computer_turn():
    return 

reset_game()

window.mainloop()