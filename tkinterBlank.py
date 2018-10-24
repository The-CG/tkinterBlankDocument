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
version = "V1.0.0"

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
        
        #     Delete comment marks Below to create the Button that opens the calculator window
        #self.button2 = tk.Button(self.frame, text = 'Calculator', width = 25, font=SMALL_FONT, command = self.new_window).grid(row = 2, column = 0)
        #
        
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

#---------------------------------------------------------------------------------------|
#
# Remove following sets of 3 Quotation marks(Multiline comment) for a simple calculator
#                                 p.s. dont forget to open the button line above as well!
"""
class calculator:
    def __init__(self, master):
        current_Time = time.strftime("%a, %d, %b, %Y, %H:%M:%S")
        
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.grid()
        self._LARGE_FONT = ("Verdana", 20)
        self._SMALL_FONT = ("Verdana", 12)
        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]
        self.master.title("OmniCalc  |  Calculator  0.0.1      " + current_Time)
        
        

        self._value1 = tk.DoubleVar()
        self._value2 = tk.DoubleVar()
        
        
        self._welcomeLabel = tk.Label(self.frame, text = "Welcome to the Calculator", font = self._LARGE_FONT).grid(row = 0, column = 0)
        self._welcomeInstructions = tk.Label(self.frame, text = "Enter your values first then press desired operator", font = self._SMALL_FONT).grid(row = 1, column = 0)
        #------CALCULATOR-------------------------------------------------------------|
        self._firstValueLabel = tk.Label(self.frame, text = "Value 1", font = self._SMALL_FONT).grid(row = 2, column = 0)
        self._secondValueLabel = tk.Label(self.frame, text = "Value 2", font = self._SMALL_FONT).grid(row = 3, column = 0)
    
        self._firstValueEntry = tk.Entry(self.frame, textvariable = self._value1, font = self._SMALL_FONT,)
        self._firstValueEntry.grid(row = 2, column = 1)
        self._secondValueEntry = tk.Entry(self.frame, textvariable = self._value2, font = self._SMALL_FONT,)
        self._secondValueEntry.grid(row = 3, column = 1)
        
        
        self._cleanResultLabelLabel = tk.Button(self.frame, text = "Clean Label?", command = self._cleanResultLabel).grid(row = 0, column = 3)
        
        self._calcButtonAdd = tk.Button(self.frame, text = "Addition", font = self._SMALL_FONT, command = self._calculateAddition).grid(row = 5, column = 0)
        self._calcButtonSub = tk.Button(self.frame, text = "Subtraction", font = self._SMALL_FONT, command = self._calculateSubtraction).grid(row = 6, column = 0)
        self._calcButtonMul = tk.Button(self.frame, text = "Multiplication", font = self._SMALL_FONT, command = self._calculateMultiplication).grid(row = 5, column = 1)
        self._calcButtonDiv = tk.Button(self.frame, text = "Division", font = self._SMALL_FONT, command = self._calculateDivision).grid(row = 6, column = 1)
        self._calcButtonExp = tk.Button(self.frame, text = "Exponentiation", font = self._SMALL_FONT, command = self._calculateExponentiation).grid(row = 6, column = 1)
        self._calcButtonSub = tk.Button(self.frame, text = "Square Root", font = self._SMALL_FONT, command = self._calculateSquareRoot).grid(row = 2, column = 2)
        
        self._emptyLabel = tk.Label(self.frame, text = "    ", font = self._LARGE_FONT).grid(row = 10, column = 2)
        self._exitButton = tk.Button(self.frame, text = "Quit", command = self.close_windows).grid(row = 11, column = 1)
#--------------------------------------------------------------------------------|
#                Calculator button functions                                     |
#--------------------------------------------------------------------------------|
    def _calculateSubtraction(self):
        value1 = float(self._firstValueEntry.get())
        value2 = float(self._secondValueEntry.get())
        result = value1 - value2
        self._resultLabel = tk.Label(self.frame, text = str(result), font=self._LARGE_FONT)
        self._resultLabel.grid(row = 4, column = 3)
    
    def _calculateAddition(self):
        value1 = float(self._firstValueEntry.get())
        value2 = float(self._secondValueEntry.get())
        result = value1 + value2
        self._resultLabel = tk.Label(self.frame, text = str(result), font=self._LARGE_FONT)
        self._resultLabel.grid(row = 4, column = 3)
        
    def _calculateMultiplication(self):
        value1 = float(self._firstValueEntry.get())
        value2 = float(self._secondValueEntry.get())
        result = value1 * value2
        self._resultLabel = tk.Label(self.frame, text = str(result), font=self._LARGE_FONT)
        self._resultLabel.grid(row = 4, column = 3)
        
    def _calculateDivision(self):
        value1 = float(self._firstValueEntry.get())
        value2 = float(self._secondValueEntry.get())
        result = value1 / value2
        self._resultLabel = tk.Label(self.frame, text= str(result), font=self._LARGE_FONT)
        self._resultLabel.grid(row = 4, column = 3)
        
    def _calculateExponentiation(self):
        value1 = float(self._firstValueEntry.get())
        value2 = float(self._secondValueEntry.get())
        result = value1 ** value2
        self._resultLabel = tk.Label(self.frame, text= str(result), font=self._LARGE_FONT)
        self._resultLabel.grid(row = 4, column = 3)
        
    def _calculateSquareRoot(self):
        sqrtValue = float(self._firstValueEntry.get())
        result = math.sqrt(sqrtValue)
        self._resultLabel = tk.Label(self.frame, text= str(result), font=self._LARGE_FONT)
        self._resultLabel.grid(row = 4, column = 3)
    #--------------------------------------------------------|
    def close_windows(self):
        self.master.destroy()
        
    def _cleanResultLabel(self):
        self._resultLabel = tk.Label(self.frame, text = "                             ", font=self._LARGE_FONT)
        self._resultLabel.grid(row = 4, column = 3)

"""
# Remove above sets of 3 Quotation marks(Multiline comment) for a simple calculator
#---------------------------------------------------------------------------------------|



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