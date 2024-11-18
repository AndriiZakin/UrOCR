import tkinter as tk
from tkinter import scrolledtext

def show_manual():
    help_text = """
    Menu Functions Help:

    1. Open File:
       - Description: Opens a file dialog to select a file and load its contents.
       - Usage: Click on 'Open File' in the menu.

    2. Save File:
       - Description: Opens a file dialog to select a location and save the current contents.
       - Usage: Click on 'Save File' in the menu.

    3. Exit:
       - Description: Closes the application.
       - Usage: Click on 'Exit' in the menu.

    4. Draw Histogram:
       - Description: Opens a dialog to select a file and draw a histogram based on the data.
       - Usage: Click on 'Draw Histogram' in the menu.

    5. Draw Scatter Plot:
       - Description: Opens a dialog to select a file and draw a scatter plot based on the data.
       - Usage: Click on 'Draw Scatter Plot' in the menu.

    6. Draw Line Plot:
       - Description: Opens a dialog to select a file and draw a line plot based on the data.
       - Usage: Click on 'Draw Line Plot' in the menu.

    7. Draw Bar Plot:
       - Description: Opens a dialog to select a file and draw a bar plot based on the data.
       - Usage: Click on 'Draw Bar Plot' in the menu.

    8. Show Help:
       - Description: Opens this help dialog with descriptions of all menu functions.
       - Usage: Click on 'Show Help' in the menu.
    """

    root = tk.Tk()
    root.title("Help - Menu Functions")

    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
    text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    text_area.insert(tk.INSERT, help_text)
    text_area.configure(state='disabled')

    root.mainloop()
