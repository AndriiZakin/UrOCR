import tkinter as tk
from tkinter import messagebox

# Colors
BG_COLOR = "white"
FG_COLOR = "blue"
TEXT_COLOR = "black"

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Login/Register")
        self.root.geometry("400x300")
        self.root.config(bg=BG_COLOR)

        # Configure grid layout for resizing
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.create_login_frame()

    def create_login_frame(self):
        self.clear_frame()
        self.login_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.login_frame.grid(row=0, column=0, sticky="nsew")

        # Configure rows and columns in the frame for resizing
        self.login_frame.grid_rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
        self.login_frame.grid_columnconfigure(0, weight=1)

        tk.Label(self.login_frame, text="Login", font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR).grid(row=0, column=0, pady=10)
        
        tk.Label(self.login_frame, text="Username", fg=TEXT_COLOR, bg=BG_COLOR).grid(row=1, column=0, sticky="ew")
        self.login_username_entry = tk.Entry(self.login_frame)
        self.login_username_entry.grid(row=2, column=0, padx=20, sticky="ew")

        tk.Label(self.login_frame, text="Password", fg=TEXT_COLOR, bg=BG_COLOR).grid(row=3, column=0, sticky="ew")
        self.login_password_entry = tk.Entry(self.login_frame, show="*")
        self.login_password_entry.grid(row=4, column=0, padx=20, sticky="ew")

        tk.Button(self.login_frame, text="Login", command=self.login, bg=FG_COLOR, fg=BG_COLOR).grid(row=5, column=0, pady=10, sticky="ew")
        tk.Button(self.login_frame, text="Go to Register", command=self.create_register_frame, bg=BG_COLOR, fg=FG_COLOR).grid(row=6, column=0, pady=5, sticky="ew")

    def create_register_frame(self):
        self.clear_frame()
        self.register_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.register_frame.grid(row=0, column=0, sticky="nsew")

        # Configure rows and columns in the frame for resizing
        self.register_frame.grid_rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=1)
        self.register_frame.grid_columnconfigure(0, weight=1)

        tk.Label(self.register_frame, text="Register", font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR).grid(row=0, column=0, pady=10)

        tk.Label(self.register_frame, text="Username", fg=TEXT_COLOR, bg=BG_COLOR).grid(row=1, column=0, sticky="ew")
        self.register_username_entry = tk.Entry(self.register_frame)
        self.register_username_entry.grid(row=2, column=0, padx=20, sticky="ew")

        tk.Label(self.register_frame, text="Password", fg=TEXT_COLOR, bg=BG_COLOR).grid(row=3, column=0, sticky="ew")
        self.register_password_entry = tk.Entry(self.register_frame, show="*")
        self.register_password_entry.grid(row=4, column=0, padx=20, sticky="ew")

        tk.Label(self.register_frame, text="Confirm Password", fg=TEXT_COLOR, bg=BG_COLOR).grid(row=5, column=0, sticky="ew")
        self.register_confirm_password_entry = tk.Entry(self.register_frame, show="*")
        self.register_confirm_password_entry.grid(row=6, column=0, padx=20, sticky="ew")

        tk.Button(self.register_frame, text="Register", command=self.register, bg=FG_COLOR, fg=BG_COLOR).grid(row=7, column=0, pady=10, sticky="ew")
        tk.Button(self.register_frame, text="Go to Login", command=self.create_login_frame, bg=BG_COLOR, fg=FG_COLOR).grid(row=8, column=0, pady=5, sticky="ew")

    def login(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()
        if username and password:
            messagebox.showinfo("Login", "Login Successful!")
        else:
            messagebox.showwarning("Login", "Please enter both fields")

    def register(self):
        username = self.register_username_entry.get()
        password = self.register_password_entry.get()
        confirm_password = self.register_confirm_password_entry.get()
        if username and password == confirm_password:
            messagebox.showinfo("Register", "Registration Successful!")
        else:
            messagebox.showwarning("Register", "Passwords do not match or fields are empty")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
