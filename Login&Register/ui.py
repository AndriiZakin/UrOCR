import tkinter as tk
from tkinter import messagebox, Toplevel, Label
import re
from db_manager import DBManager

class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def show_tip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _, _ = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 25
        y = y + self.widget.winfo_rooty() + 20
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def create_tooltip(widget, text):
    tool_tip = ToolTip(widget)
    def enter(event):
        tool_tip.show_tip(text)
    def leave(event):
        tool_tip.hide_tip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

class TkinterGUI:
    def __init__(self, root):
        self.db_manager = DBManager()
        self.root = root
        self.setup_ui()

    # Adjusted setup_ui method within TkinterGUI class
    def setup_ui(self):
        self.root.title("Login or Register")
        self.root.geometry("500x400")
    
        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(pady=10)
    
        self.middle_frame = tk.Frame(self.root)
        self.middle_frame.pack(pady=5)
    
        self.bottom_frame = tk.Frame(self.root)
        self.bottom_frame.pack(pady=10)
    
        self.username_label = tk.Label(self.top_frame, text="Username:")
        self.username_label.pack(side=tk.LEFT)
        self.username_entry = tk.Entry(self.top_frame)
        self.username_entry.pack(side=tk.RIGHT)
    
        self.password_label = tk.Label(self.middle_frame, text="Password:")
        self.password_label.pack(side=tk.LEFT)
    
        # Password requirements button - now positioned to the left of the password entry
        self.password_req_button = tk.Button(self.middle_frame, text="?")
        self.password_req_button.pack(side=tk.LEFT, padx=(0,5))
        password_requirements = "Password must be at least 8 characters long, include uppercase and lowercase letters, at least one digit, and one special character."
        create_tooltip(self.password_req_button, password_requirements)
            
        self.password_entry = tk.Entry(self.middle_frame, show="*")
        self.password_entry.pack(side=tk.LEFT)
    
        self.register_button = tk.Button(self.bottom_frame, text="Register", command=self.register)
        self.register_button.pack(side=tk.LEFT, padx=5)
        self.login_button = tk.Button(self.bottom_frame, text="Login", command=self.login)
        self.login_button.pack(side=tk.RIGHT, padx=5)
    
        self.help_button = tk.Button(self.root, text="Help", command=self.show_help)
        self.help_button.pack(side=tk.BOTTOM, pady=5)
    
        self.guest_login_button = tk.Button(self.root, text="Login as Guest", command=self.login_as_guest)
        self.guest_login_button.pack(side=tk.BOTTOM)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not re.match(r"^[a-zA-Z0-9_]+$", username):
            messagebox.showinfo("Error", "Username can only contain alphanumeric characters and underscores")
            return
        
        if password:
            if len(password) < 8:
                messagebox.showinfo("Error","Password must be at least 8 characters long.")
                return

            elif not re.search("[A-Z]", password):
                messagebox.showinfo("Error","Password must contain at least one uppercase letter.")
                return

            elif not re.search("[a-z]", password):
                messagebox.showinfo("Error","Password must contain at least one lowercase letter.")
                return

            elif not re.search("[0-9]", password):
                messagebox.showinfo("Error","Password must contain at least one digit.")
                return

            elif not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
                messagebox.showinfo("Error","Password must contain at least one special character.")
                return
            else:
                pass
        
        else:
            messagebox.showinfo("Error","Password cannot be empty.")
            return

        if self.db_manager.register_user(username, password):
            messagebox.showinfo("Success", "User registered successfully")
        else:
            messagebox.showinfo("Error", "Registration failed. User might already exist.")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.db_manager.login_user(username, password):
            messagebox.showinfo("Success", "Login successful")
        else:
            messagebox.showinfo("Error", "Invalid username or password")

    def show_help(self):
        messagebox.showinfo("Help", "Enter your username and password. If you are new, click Register to create an account.")

    def login_as_guest(self):
        messagebox.showwarning("Warning", "You are logging in as a guest. Your data won't be saved.")
        # Implement the logic for guest login

if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterGUI(root)
    root.mainloop()