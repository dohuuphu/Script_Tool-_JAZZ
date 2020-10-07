import lib
import tkinter as tk
from tkinter import  ttk, messagebox

def show_message():
    messagebox.showinfo(title= 'input info', message= lib.plus())

def setup_win():
    win = tk.Tk()
    win.title("Script Tool")

    #create label
    lable = ttk.Label(win, text = "222")
    lable.grid(column = 100 , row = 100)
    #create button
    button = ttk.Button(win, text= 'run', command = show_message )
    button.grid(column = 1, row = 0)
    win.mainloop()


def main():
    setup_win()





if __name__ == "__main__":
    main()