import lib
import tkinter as tk
from tkinter import  ttk, messagebox

def show_message():
    messagebox.showinfo(title= 'input info', message= lib.plus)



def setup_win():
    pass

def get_entry():
    id_entry = entry_id.get()
    print((id_entry))

def main():
    setup_win()





if __name__ == "__main__":
    win = tk.Tk()
    win.title("Script Tool")
    win.geometry("280x160")
    # frame = ttk.Frame(win, width = 300, height = 250)
    # frame.grid(win)

    # create label
    label_content = ttk.Label(win, text = " Run Test Plan On Jazz_page" )
    label_id = ttk.Label(win, text="ID User:")
    label_pass = ttk.Label(win, text="Password:")
    label_TestPlan_id = ttk.Label(win, text="TestPlan ID:")
    label_content.place(relx=0.5, rely=0.05, anchor=tk.N)
    label_id.place(relx=0.20, rely=0.25, anchor=tk.N)
    label_pass.place(relx=0.20, rely=0.45, anchor=tk.N)
    label_TestPlan_id.place(relx=0.20, rely=0.65, anchor=tk.N)
   # lable_pass.pack(win, sticky = tk.E + tk.W)

    # create text entry
    entry_id = ttk.Entry(win)
    entry_pass = ttk.Entry(win)
    entry_Testplan = ttk.Entry(win)
    # entry_id.grid(row=3, column=3)
    # entry_pass.grid(row=5, column=3)
    # entry_Testplan.grid(row=7, column=3)
    entry_id.place(relx=0.65, rely=0.25, anchor=tk.N)
    entry_pass.place(relx=0.65, rely=0.45, anchor=tk.N)
    entry_Testplan.place(relx=0.65, rely=0.65, anchor=tk.N)

    # create button
    button = ttk.Button(win, text='Run', command=get_entry)
    button.place(relx=0.5, rely=1, anchor = tk.S)

    # create text entry
    # text_entry = ttk.ent Entry(win, width= 20, bg ="black")
    # text_entry.grid(column = 2, row = 0)
    # loop
    win.mainloop()
    main()