import threading
from Read_excel import *
import tkinter as tk
from tkinter import  ttk, messagebox
import sys
#from PIL import Image, ImageTk

# ============================= Script =====================
def login_to_testSuit_record():
    # Login to webpage
    # Send_Tag_htlm(cf.ID_tag, cf.timeout, cf.IDuser_id)
    # print("error_flag", cf.error_flag)
    # Send_Tag_htlm(cf.ID_tag, cf.timeout, cf.password_id)
    # Click_Tag_htlm(cf.text_Tag, cf.timeout, cf.Login_text)
   
    # Click link ** ID_test **
    Click_LinkText(cf.timeout, cf.ID_test_linktext)
    
    # Click Planning & Browse
    Click_Tag_htlm(cf.title_tag, cf.timeout, cf.Planning_title)
    time.sleep(3) # Browse test plan still run click() if not sleep, but won't actually click
    Click_Tag_htlm(cf.ID_tag, cf.timeout, cf.Browse_testplan_id) # text "browse test plan" can find 2 element => use ID

    Click_FilterText_TestPlan(cf.timeout, cf.TestPlan_linktext[0])

    print("filled 1439")
    Click_LinkText(cf.timeout, cf.TestPlan_linktext)
    
    #Click Test suit execution records
    Click_Tag_htlm(cf.text_Tag, cf.timeout, cf.Testsuit_records_text)
    
def show_message():
    messagebox.showinfo(title= 'input info', message= "u got meee :)))")

def Step():
    setup()
    login_to_testSuit_record()  
    #Run_TestSuit()
    Edit_testSuit_record()  # click finish and backpage 2 time
    cf.driver.delete_all_cookies()

def main():
    check_page_login = threading.Thread(name='check_login', target=check_login, daemon= True)
    check_page_login.start()
    id_entry = entry_id.get()
    pass_entry = entry_pass.get()
    test_plan = entry_Testplan.get()
    cf.IDuser_id = np.append(cf.IDuser_id, id_entry )
    cf.password_id = np.append(cf.password_id, pass_entry)
    cf.TestPlan_linktext = np.append(cf.TestPlan_linktext, test_plan)
    cf.TestPlan_linktext = np.append(cf.TestPlan_linktext, test_plan)
    while(True):
        cf.error_flag = 0
        cf.complete_flag = 0
        cf.end_flag = 0
        print("ok let's start")
        Step()
        if(cf.end_flag == 1):
            cf.driver.quit()
            show_message()
            sys.exit()
            break

def check_login():
    while(True):
        try:
            visible = Check_element_isDisplay(cf.login_form)
            if(visible is True):
                print("fill login")
                Send_key_id(cf.timeout, cf.IDuser_id)
                Send_key_id(cf.timeout, cf.password_id)
                Click_Text(cf.timeout, cf.Login_text)
                time.sleep(10)
                print("End login")
        except: 
            pass
       





if __name__ == "__main__":
    win = tk.Tk()
    win.title("Script Tool")
    win.geometry("280x160")
    #icon = ImageTk.PhotoImage(Image.open("datalogic2.png"))
    # frame = ttk.Frame(win, width = 300, height = 250)
    # frame.grid(win)

    # create label
    #label_img = ttk.Label(image = icon, width = 30)
    label_content = ttk.Label(win, text = " Run Test Plan On Jazz_page" )
    label_id = ttk.Label(win, text="ID User:")
    label_pass = ttk.Label(win, text="Password:")
    label_TestPlan_id = ttk.Label(win, text="TestPlan ID:")

    #label_img.place(relx=0.05, rely=0.02, anchor=tk.N)
    label_content.place(relx=0.5, rely=0.05, anchor=tk.N)
    label_id.place(relx=0.20, rely=0.25, anchor=tk.N)
    label_pass.place(relx=0.20, rely=0.45, anchor=tk.N)
    label_TestPlan_id.place(relx=0.20, rely=0.65, anchor=tk.N)
   # lable_pass.pack(win, sticky = tk.E + tk.W)

    # create text entry
    entry_id = ttk.Entry(win)
    entry_pass = ttk.Entry(win, show = "*")
    entry_Testplan = ttk.Entry(win)
    
    entry_id.place(relx=0.65, rely=0.25, anchor=tk.N)
    entry_pass.place(relx=0.65, rely=0.45, anchor=tk.N)
    entry_Testplan.place(relx=0.65, rely=0.65, anchor=tk.N)

    # create button
    button = ttk.Button(win, text='Run', command = main)
    #button.bind("<Button-1>", main)
    #button.bind("<Button-1>", )
    button.place(relx=0.5, rely=1, anchor = tk.S)

    win.mainloop()

    


