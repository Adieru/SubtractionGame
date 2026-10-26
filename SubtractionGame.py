import tkinter as tk
from tkinter import ttk, simpledialog

#setting window
window = tk.Tk()
window.geometry("800x600")

my_label = ttk.Label(window, text="Game of Nim", font=("Arial", 25))
my_label.pack(side=tk.TOP, fill=tk.Y, expand=False, pady=5)

#initialize game
def reset_game():
    #variables
    global user_turns
    global current_tiles
    global gametiles
    global window
    global stick_frame
    global maxiumum
    
    #giving initial values to vars
    user_turns = 0
    
    #setting minima and maxima
    maximum = simpledialog.askinteger("Input", "How many sticks can you remove per turn?", 
                                  parent = window, minvalue = 2, maxvalue = 12)

    num_Sticks = simpledialog.askinteger("Input", "How many sticks shall we play with?", 
                                         parent = window, minvalue=(maximum + 1), maxvalue = 50)

    #setting the number of tiles used
    current_tiles = num_Sticks

#removing tiles

#player's turn

#computer turn

window.mainloop()