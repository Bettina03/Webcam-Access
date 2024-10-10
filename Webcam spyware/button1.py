import _tkinter as tk
root = tk.Tk()
def button1_clicked():
    password_window = tk.Toplevel(root)
    password_window.title("Enter Password")
    password_window.geometry("400X300")
    password_label = tk.Label(password_window, text="Enter Password:")
    password_label.pack()
    password_entry = tk.Entry(password_window, show="*")
    password_entry.pack()
    def ok_button():
        password = tk.Tk()
        subprocess = tk.Tk()
        success_label = tk.Tk()
        if password_entry.get()==password:
            subprocess.run([r'disable_cam.bat'], text=True)
            password_window.destroy()
            success_label.config(text="Camera Disabled Successfully") 
        else:
            error_label.config(text="Incorrect Password")
            password_entry.delete(0, tk.END)
    ok_button = tk.Button(password_window, text="OK", command=ok_button)
    ok_button.pack()
    error_label = tk.Label(password_window, text="", font=("Arial", 12), bg="#f2f2f2", fg="#ff0000")
    error_label.pack()
def button2_clicked():
    password_window = tk.Toplevel(root)
    password_window.title("Enter Password")
    password_window.geometry("400X300")
    password_label = tk.Label(password_window, text="Enter Password:")
    password_label.pack()
    password_entry = tk.Entry(password_window, show="*")
    password_entry.pack()
    def ok_button():
        password = tk.Tk()
        subprocess = tk.Tk()
        success_label = tk.Tk()
        if password_entry.get()==password:
            subprocess.run([r'enable_cam.bat'], text=True)
            password_window.destroy()
            success_label.config(text="Camera Enabled Successfully")
        else:
            error_label.config(text="Incorrect Password")
            password_entry.delete(0, tk.END)
    ok_button = tk.Button(password_window, text="OK", command=ok_button)
    ok_button.pack()
    error_label = tk.Label(password_window, text="", font=("Arial", 12), bg="#f2f2f2", fg="#ff0000")
    error_label.pack()
root.mainloop()