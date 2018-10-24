"""
---------------------------------------------------------------------------------|
The-CG
                                                                                 |
Last Edit: 10/23/2018
                                                                                 |
Blank Tkinter GUI | Two seperate windows |

                                                                                 |
Version: 1.0.0
                                                                                 |
grid and pack configurations
                                                                                 |
                                                                                 |
I find this like "Blank Document" in Word, a starting "Blank Document"
---------------------------------------------------------------------------------|
"""


"""
Author:
Last Edited:
Version:

Description of the prgram or inteded goal 
words
words
words :D
"""
#    Needed imports
import tkinter as tk
import time
# Math is needed for the Calculator
import math

# Declared Variables
LARGE_FONT = ("Verdana", 20)
SMALL_FONT = ("Verdana", 16)
version = "V0.0.0"

#---------------------------------------------------------------------------------|
#     Tkinter Pages Here                                                          |
#---------------------------------------------------------------------------------|
# Creates the first page. Each following window or page will be a class
class starting_Or_Menu_Page:      # Grid Mode
    def __init__(self, master):
        current_Time = time.strftime("%a, %d, %b, %Y, %H:%M:%S")
        
        # Creates the frame and grid
        self.master = master
        self.frame = tk.Frame(self.master)
        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]
        self.master.title("Blank tkinter Document  |  " + current_Time + "  |  |  " + version)        
        self.frame.grid()
        
        # Creates and places Labels
        self.welcomeLabel = tk.Label(self.frame, text = "Welcome to my First Thought about a blank tkinter file to start from!", font = SMALL_FONT).grid(row = 0, column = 0)
        
        # Creates and places Buttons in the grid
        self.button1 = tk.Button(self.frame, text = 'New Empty Window', width = 25, font=SMALL_FONT, command = self.new_window).grid(row = 1, column = 0)
        
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows).grid(row = 10, column = 0)
        
        
    # functions
    def close_windows(self):
        self.master.destroy()
        
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        #          this is where the class goes for the desired window
        self.app = second_Window_In_Pack_Form(self.newWindow)
        
    def open_calculator(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = calculator(self.newWindow)





class second_Window_In_Pack_Form: # In Pack mode
    def __init__(self, master):
        current_Time = time.strftime("%a, %d, %b, %Y, %H:%M:%S")
        
        self.master = master
        self.frame = tk.Frame(self.master)
        
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, font=SMALL_FONT, command = self.close_windows)
        self.quitButton.pack()
        
        self.frame.pack()
    
    # functions
    def close_windows(self):
        self.master.destroy()

#---------------------------------------------------------------------------------|
#                                                                                 |
#---------------------------------------------------------------------------------|
#   Run
def main(): 
    root = tk.Tk()
    app = starting_Or_Menu_Page(root)
    root.mainloop()

if __name__ == '__main__':
    main()