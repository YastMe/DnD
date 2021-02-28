import openpyxl
import tkinter as tk

def winconfig():
    principal.title("Ficha Python")
    principal.geometry("500x300+200+100")
    principal.resizable(width="False", height="False")

principal = tk.Tk()
winconfig()

principal.mainloop()