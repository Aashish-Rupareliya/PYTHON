# main.py
import tkinter as tk
from tkinter import messagebox
from user import User

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Product Management Application")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Welcome to Product Management System")
        self.label.pack(pady=10)
        
        self.login_button = tk.Button(self, text="Login", command=self.show_login_form)
        self.login_button.pack(pady=5)
        
        self.register_button = tk.Button(self, text="Register", command=self.show_register_form)
        self.register_button.pack(pady=5)

    def show_login_form(self):
        self.clear_window()
        self.label = tk.Label(self, text="Login")
        self.label.pack(pady=10)
        
        self.username_label = tk.Label(self, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()
        
        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=5)

    def show_register_form(self):
        self.clear_window()
        self.label = tk.Label(self, text="Register")
        self.label.pack(pady=10)
        
        self.username_label = tk.Label(self, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.role_label = tk.Label(self, text="Role (product_manager/customer)")
        self.role_label.pack()
        self.role_entry = tk.Entry(self)
        self.role_entry.pack()

        self.register_button = tk.Button(self, text="Register", command=self.register)
        self.register_button.pack(pady=5)

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = User.login(username, password)
        if user:
            messagebox.showinfo("Login Success", f"Logged in as {user[0]}")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_entry.get()
        user = User(username, password, role)
        if user.register():
            messagebox.showinfo("Registration Success", "User registered successfully")
        else:
            messagebox.showerror("Registration Failed", "User registration failed")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
