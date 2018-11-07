version = "0.0.3"
"""
---------------------------------------------------------------------------------|
                                                                                 |
tkinterBlank.py
                                                                                 |
The-CG
                                                                                 |
Last Edit: 11/06/2018
                                                                                 |
Blank tkinter GUI | Two seperate windows |
                                                                                 |
Version 0.0.2
                                                                                 |
grid and pack configurations
                                                                                 |
                                                                                 |
Create a blank tkinter G.U.I.
                                                                                 |
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
#    imports tkinter
import tkinter as tk
# Time is needed for window titles to have lovcal time displayed
import time
# Math is needed for the sqrt2FacCommand Command
import math

#    Note:
# [I] Suffix == integers only
#---------------------------------------------------------------------------------|



# Declared Variables
#            ("typeOfFont", sizeOfFont[I])
LARGE_FONT = ("Verdana", 20)
SMALL_FONT = ("Verdana", 16)

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
        
        # Create Variables
        
        #self.value1 = tk.BooleanVar()  # Boolean
        self._value2 = tk.DoubleVar()   # Float
        #self.value3 = tk.StringVar()   # String
        #self.value4 = tk.IntVar()      # Integer
        
        # Creates entry feild
        self._firstValueEntry = tk.Entry(self.frame, textvariable = self._value2)
        self._firstValueEntry.grid(row = 2, column = 0)
        
        # Creates and places Labels
        self.welcomeLabel = tk.Label(self.frame, text = "Welcome to my First Thought about a blank tkinter file to start from!", font = SMALL_FONT).grid(row = 0, column = 0)
        
        # Creates and places Buttons in the grid
        self.button1 = tk.Button(self.frame, text = 'New Empty Window', width = 25, font=SMALL_FONT, command = self.new_window).grid(row = 1, column = 0)
        
        self.button2 = tk.Button(self.frame, text = 'Sqrt( x**(4!) )', command = self.sqrt2FacCommand).grid(row = 5, column = 0)
        
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows).grid(row = 10, column = 0)
        
        
    # starting_Or_Menu_Page functions
    def close_windows(self):
        self.master.destroy()
        
    def sqrt2FacCommand(self):
        #        To aquire the entrty variable
        value1 = self._firstValueEntry.get()
        value1 = float(value1)
        
        value1New = value1**(4*3*2*1)
        
        outValue = math.sqrt(value1New)
        
        self.resultLabel = tk.Label(self.frame, text = str(outValue))
        self.resultLabel.grid(row = 6, column = 0)
        
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        #          this is where the class goes for the desired window
        self.app = second_Window_In_Pack_Form(self.newWindow)
        
    def open_calculator(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = calculator(self.newWindow)



#---------------------------------------------------------------------------------|
#     second page                                                                 |
#---------------------------------------------------------------------------------|




class second_Window_In_Pack_Form: # In Pack mode
    def __init__(self, master):
        current_Time = time.strftime("%a, %d, %b, %Y, %H:%M:%S")
        
        self.master = master
        self.frame = tk.Frame(self.master)
        
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, font=SMALL_FONT, command = self.close_windows)
        self.quitButton.pack()
        
        self.frame.pack()
    
    # second_Window_In_Pack_Form functions
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