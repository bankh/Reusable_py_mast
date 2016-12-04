### Examples regarding the installation as well as test is from the following
# http://tkinter.unpythonic.net/wiki/How_to_install_Tkinter

#=======================
# Imports
#=======================

import Tkinter as tk        # Python 3: "t" lower-case and Python 

#Create instance
win = tk.Tk()

# Add a title
win.title("Python GUI")

# ======
# Front-end Function
# =======

def get_current_window_size():
    win.update()           # To get the runtime size
    print('width    =', win.winfo_width())
    print('height   =', win.winfo_height())

def increase_window_width():
    # min width can not be resized to less
    # default height can be
    win.minsize(width=300, height=1)    #1 = default

    # Disable resizable GUI
    win.resizable(0, 0)

# =====
# Start GUI
# =====

get_current_window_size()
increase_window_width()
print()
get_current_window_size()

win.mainloop()