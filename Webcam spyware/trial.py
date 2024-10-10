import tkinter as tk
from tkinter import messagebox
from tkinter import *
import subprocess
import webbrowser
import base64
from PIL import ImageTk, Image
import io
import tempfile
import sys
import os

# Replace with the correct password
password = "Hacker@1"

# Create the main window and buttons
root = tk.Tk()
root.title("WebCam Security")
root.geometry("600x500")
window_width = 600
window_height = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg='black')



button_frame = tk.Frame(root, bg="black")
success_label = tk.Label(button_frame, text="", font=("Calibri", 12, "bold"), bg="black", fg="#0b03fc")
success_label.pack(pady=10)


# Define the function to be executed when the first button is clicked
def button1_clicked():
    # Create a password prompt dialog box
    password_window = tk.Toplevel(root)
    password_window.title("Provide the Password to gain access:")
    password_window.geometry("400x300")
    password_label = tk.Label(password_window, text="Enter Password:")
    password_label.pack()
    password_entry = tk.Entry(password_window, show="#")
    password_entry.pack()
    def ok_button():
        if password_entry.get()==password:
            command = r'REG DELETE "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam" /v Value /f'
            subprocess.call(command, shell=True)
            password_window.destroy()
            success_label.config(text="Camera Enabled Successfully")
        else:
            error_label.config(text="The entered password is invalid. Please try again.")
            password_entry.delete(0, tk.END)
    ok_button = tk.Button(password_window, text="OK", command=ok_button)
    ok_button.pack()
    error_label = tk.Label(password_window, text="", font=("Calibri", 12), bg="white", fg="white")
    error_label.pack()
    
# Define the function to be executed when the second button is clicked
def button2_clicked():
    # Create a password prompt dialog box
    password_window = tk.Toplevel(root)
    password_window.title("Provide the Password to gain access:")
    password_window.geometry("400x300")
    password_label = tk.Label(password_window, text="Enter Password:")
    password_label.pack()
    password_entry = tk.Entry(password_window, show="#")
    password_entry.pack()
    def ok_button():
        if password_entry.get()==password:
            delete_cmd = r'REG DELETE "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam" /v Value /f'
            subprocess.run(delete_cmd, shell=True)
            add_cmd = r'REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam" /v Value /t REG_DWORD /d 0 /f'
            subprocess.run(add_cmd, shell=True)
            password_window.destroy()
        else:
            error_label.config(text="The entered password is invalid. Please try again.")
            password_entry.delete(0, tk.END)
    ok_button = tk.Button(password_window, text="OK", command=ok_button)
    ok_button.pack()
    error_label = tk.Label(password_window, text="", font=("Calibri", 12), bg="#f2f2f2", fg="#ff0000")


project_label = tk.Label(root,text="Implementing robust security system!! ",font=("Calibri", 18,"bold"),bg="black",fg="white")
project_label.pack(pady=25)


button1 = tk.Button(button_frame, text="Enable Camera",font=("Calibri", 14, "bold"),padx=10, pady=5,command=button1_clicked,bg="orange",fg="white")
button2 = tk.Button(button_frame, text="Disable Camera",font=("Calibri", 14, "bold"),padx=10, pady=5,command=button2_clicked,bg="orange",fg="white")
# Pack the buttons in the frame

button1.pack(side="top", fill="x", padx=80, pady=20)
button2.pack(side="bottom", fill="x", padx=80, pady=20)

# Pack the frame in the root window
button_frame.pack(expand=True)


# Start the main event loop
root.mainloop()