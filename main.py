import tkinter as tk
from GUI.LoginRegister.ui import TkinterGUI

'''1. make login more beautifull
   2. creare a help button
   3. login as a guest button(after pressing Warning 'your data won't be saved')
   '''

def main():
    root = tk.Tk()
    app = TkinterGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()