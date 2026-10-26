import tkinter as tk
from tkinter import ttk, simpledialog, PhotoImage, Frame

#setting window
window = tk.Tk()
window.geometry("800x600")

my_label = ttk.Label(window, text="Game of Nim", font=("Arial", 25))
my_label.pack(side=tk.TOP, fill=tk.Y, expand=False, pady=5)




#giving initial values to vars
stick_frame = Frame(window)
stick_frame.pack()
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
                                   height = 350 , width = 35, borderwidth = 0))

        gametiles[each].config(command = lambda: remove_tile("user", maximum))


        #initialize the tiles as buttons
        gametiles[each].pack(side = tk.LEFT, fill = tk.X, expand = False, padx = 5)
    

#removing tiles
def remove_tile(who, value):
    return


#player's turn

#computer turn

reset_game()

window.mainloop()