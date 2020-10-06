import pandas
import numpy as np
from action_funtion import *

# data = pandas.read_excel('Data_Main.xlsx',sheet_name='Data_Main')
# loc =data.loc[data['Machine Name'].isin(['TEST02-PC'])]
# #loc =data.loc[data['Machine Name'] == 0].index[0]
# #iloc = data.iloc[]
# ##loc = loc.tolist()
# #print(data['Machine Name'].tolist())
# print("loc")
# print(loc.index)
# name = data.loc[data['Name'].index[4]].tolist()
# print("name")
# print(name[2])

def find_setup_MC1():
    name=[]
    file_excel = pandas.read_excel('Data_Main.xlsx',sheet_name='Data_Main')
    MC1_list =file_excel.loc[file_excel['Machine Name'].isin(['TestExecute-PC'])]
    list_index = MC1_list.index #[0,2] row
    for i in range(len(list_index)):
         value = file_excel.loc[file_excel['Name'].index[list_index[i]]].tolist()[2]
         name = np.append(name, value)
    # print("row_number: " + str(list_index))
    # print("Machine_name: " + str(name))
    return(name)

def find_setup_MC2():
    name=[]
    file_excel = pandas.read_excel('Data_Main.xlsx',sheet_name='Data_Main')
    MC1_list =file_excel.loc[file_excel['Machine Name'].isin(['TestComplete14_'])]
    list_index = MC1_list.index #[0,2] row
    for i in range(len(list_index)):
         value = file_excel.loc[file_excel['Name'].index[list_index[i]]].tolist()[2]
         name = np.append(name, value)
    # print("row_number: " + str(list_index))
    # print("Machine_name: " + str(name))
    return(name)

def find_setup_MC3():
    name=[]
    file_excel = pandas.read_excel('Data_Main.xlsx',sheet_name='Data_Main')
    MC1_list =file_excel.loc[file_excel['Machine Name'].isin(['TEST02-PC'])]
    list_index = MC1_list.index #[0,2] row
    for i in range(len(list_index)):
         value = file_excel.loc[file_excel['Name'].index[list_index[i]]].tolist()[2]
         name = np.append(name, value)
    # print("row_number: " + str(list_index))
    # print("Machine_name: " + str(name))
    return(name)

max_len = 0

def find_max_ArrMachine(array):
    global max_len
    max_len = 0
    for i in array:
        if(len(i) > max_len):
            max_len = len(i) 
    print("max length arr: " + str(max_len))

def Edit_MC(MC1, MC2, MC3):
    name1 = name2 = name3 =[]
    count = 0
    for i in range(max_len):
        name1 = name2 = name3 =[]
        try:
            name1 = ["name1", str(MC1[i])]
            Click_Tag_htlm(text_Tag, timeout, name1)
            Click_Tag_htlm(aria_label_tag ,timeout, Run_btn_arialable, count)
            Click_Tag_htlm(Class_tag, timeout, Run_testsuit_class, count)
            Edit_build_record()
            time.sleep(5)
            print(" CLICK CANCEL, PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            Click_Tag_htlm(Class_tag, timeout, Cancel_testsuit_class)
            print(" BACKKKKKKKKKK, PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            time.sleep(3)
            driver.back()
            count = count+1 
            time.sleep(3)
            # remmove name in arr after run testsuit
        except:
            print("name1 fail")
            pass
        try: 
            name2 = ["name2", str(MC2[i])]
            Click_Tag_htlm(text_Tag, timeout, name2)
            Click_Tag_htlm(aria_label_tag ,timeout, Run_btn_arialable, count)
            Click_Tag_htlm(Class_tag, timeout, Run_testsuit_class, count)
            Edit_build_record()
            time.sleep(5)
            print(" CLICK CANCEL, PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            Click_Tag_htlm(Class_tag, timeout, Cancel_testsuit_class)
            print(" BACKKKKKKKKKK, PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            time.sleep(3)
            driver.back()
            count = count+1
            time.sleep(3)
        except:
            print("name2 fail")
            pass
        try: 
            name3 = ["name3", str(MC3[i])] 
            Click_Tag_htlm(text_Tag, timeout, name3)
            Click_Tag_htlm(aria_label_tag ,timeout, Run_btn_arialable, count)
            Click_Tag_htlm(Class_tag, timeout, Run_testsuit_class, count)
            Edit_build_record()
            time.sleep(5)
            print(" CLICK CANCEL, PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            Click_Tag_htlm(Class_tag, timeout, Cancel_testsuit_class)
            print(" BACKKKKKKKKKK, PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            time.sleep(3)
            driver.back()
            count = count+1
            time.sleep(3)
        except:
            print("name3 fail")
            pass
        print("MC1: " + str(name1))
        print("MC2: " + str(name2))
        print("MC3: " + str(name3))


def Edit_testSuit_record():
    MC1 = find_setup_MC1()
    MC2 = find_setup_MC2()
    MC3 = find_setup_MC3()
    # print("MC1: " + str(MC1))
    # print("MC2: " + str(MC2))
    # print("MC3: " + str(MC3))
    MC_Array = [MC1, MC2, MC3]
    find_max_ArrMachine(MC_Array)
    Edit_MC(MC1, MC2, MC3)

# if __name__ == "__main__":
#     main()