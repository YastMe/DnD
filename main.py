import openpyxl
import tkinter as tk

def winconfig():
    principal.title("Ficha Python")
    principal.geometry("1920x1080+200+100")
    principal.resizable(width="True", height="True")

principal = tk.Tk()
winconfig()

principal.mainloop()