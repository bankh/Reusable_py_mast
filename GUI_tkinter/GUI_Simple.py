### Examples regarding the installation as well as test is from the following
# http://tkinter.unpythonic.net/wiki/How_to_install_Tkinter

#=======================
# Imports
#=======================

import Tkinter as tk        # Python 3: "t" lower-case and Python
from Tkinter import Menu
import ttk                  # Themed Tkinter

# ======
# Front-end Functions
# =======

def _quit():
    win.quit()      # win will exist when this function is called
    win.destroy()
    exit()

# ========================================================================================
#  Procedural Code
# ========================================================================================
# Create instance
win = tk.Tk()

# Add a title
win.title("Python Projects")

# ========================================================================================
# Creating a Menu Bar
# ========================================================================================

menuBar = Menu()
win.config(menu=menuBar)

# Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

# Add another Menu to the Menu Bar an Item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

# ========================================================================================
# Tab Control/ Notebook introduced here 
# ========================================================================================

tabControl = ttk.Notebook(win)  # Create Tab Control

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')

tab2 = ttk.Frame(tabControl)    # Add a second tab
tabControl.add(tab2, text='Tab 2')

tabControl.pack(expand=1, fill="both")  # Pack to make visible

# Start GUI
win.mainloop()