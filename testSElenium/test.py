from action_funtion import *
#from variable import *
#global error_flag
#import variable as cf
import tkinter as tk
from tkinter import  ttk, messagebox

def setup2():
    global error_flag
    cf.driver.get("https://rationalcld.dl.net/qm/web/console/ID%20%28Test%29#action=com.ibm.rqm.planning.home.actionDispatcher&subAction=viewTestPlan&id=1439")
    Send_Tag_htlm(cf.ID_tag, cf.timeout, cf.IDuser_id)
    print("error", cf.error_flag)
    Send_Tag_htlm(cf.ID_tag, cf.timeout, cf.password_id)
    
    #Click_Tag_htlm(cf.text_Tag, cf.timeout, cf.Login_text)
    #Click_Tag_htlm(text_Tag, timeout, Testsuit_records_text)
    #Check_Result()

    # # Click Run
    # Click_Tag_htlm(aria_label_tag ,timeout, Run_btn_arialable)
    # Click_Tag_htlm(Class_tag, timeout, Run_testsuit_class)
    # Edit_build_record()

def show_message():
    messagebox.showinfo(title= 'input info', message= "u got meee :)))")

def setup_win():
    win = tk.Tk()
    win.title("Script Tool")

    #create label
    lable = ttk.Label(win, text = "Click to Run Project")
    lable.grid(column = 0 , row = 0)
    #create button
    button = ttk.Button(win, text= 'run', command = setup2)
    button.grid(column = 2, row = 0)
    button = ttk.Button(win, text= 'info message', command = show_message)
    button.grid(column = 1, row = 0)
    win.mainloop()

def main():
    #global er
    #setup2()
    #setup_win()
    for a in len(5):
        print("ấ")

if __name__ == "__main__":
    main()
    