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
    lable.grid(column = 0 , row = 0)
    #create button
    button = ttk.Button(win, text= 'run', command = show_message )
    button.grid(column = 2, row = 0)
    win.mainloop()


def main():
    print("a: ", lib.a)
    lib.plus()
    print("a: ", lib.a)
    setup_win()





if __name__ == "__main__":
    main()