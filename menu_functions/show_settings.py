import tkinter as tk
from tkinter import messagebox

def show_settings():
    def save_settings():
        # Here you can add code to save the settings
        messagebox.showinfo("Settings", "Settings saved successfully!")

    root = tk.Tk()
    root.title("Settings")

    # Example settings
    tk.Label(root, text="Setting 1:").grid(row=0, column=0, padx=10, pady=10)
    setting1_entry = tk.Entry(root)
    setting1_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Setting 2:").grid(row=1, column=0, padx=10, pady=10)
    setting2_entry = tk.Entry(root)
    setting2_entry.grid(row=1, column=1, padx=10, pady=10)

    save_button = tk.Button(root, text="Save", command=save_settings)
    save_button.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()
