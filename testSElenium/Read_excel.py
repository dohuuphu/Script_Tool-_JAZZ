import pandas
import numpy as np
#from action_funtion import *
from Duy_Test import *

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
    if(max_len != 0):
        for i in range(cf.save_forloop, max_len):
            name1 = name2 = name3 =[]
            try:   # Machine 1 
                if(cf.error_flag ==  1):
                    print("error_flag = 1")
                    break
                name1 = ["name1", str(MC1[i])]
                if(name1[1] != "0"):  # name1 = 0 when that test_suit was run
                    Click_Tag_htlm(cf.text_Tag, cf.timeout, name1)
                    if(cf.error_flag ==  0): # if test_suit was Clicked, page_path + 1
                        count = count + 1
                    Click_Tag_htlm(cf.aria_label_tag, cf.timeout, cf.Run_btn_arialable, count-1)
                    Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Run_testsuit_class, count-1)
                    Change_Machine_For_Testcase(cf.timeout, 'TestExecute-PC',Get_TimesPage(cf.timeout,2+count))   # Duy_test
                    Edit_build_record()
                    Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Finish_class)
                    #time.sleep(5)
                    #print(" CLICK CANCEL, PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                    #Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Cancel_testsuit_class)
                    print(" BACKKKKKKKKKK, PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                    cf.driver.back() 
                    time.sleep(3) 
                    cf.driver.back()
                    #time.sleep(3)
                    if(cf.error_flag ==  0): # make sure rename test_suit after click "finish"
                        MC1[i] = 0
            except:
                print("name1 fail")
                pass

            try:    # Machine 2
                if(cf.error_flag ==  1):
                    print("error_flag = 1")
                    break
                name2 = ["name2", str(MC2[i])]
                if(name2[1] != "0"):  # name2 = 0 when that test_suit was run
                    Click_Tag_htlm(cf.text_Tag, cf.timeout, name2)
                    if(cf.error_flag ==  0): # if test_suit was Clicked page_path + 1
                        count = count + 1
                    Click_Tag_htlm(cf.aria_label_tag ,cf.timeout, cf.Run_btn_arialable, count-1)
                    Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Run_testsuit_class, count-1)
                    Change_Machine_For_Testcase(cf.timeout, 'TestComplete14_',Get_TimesPage(cf.timeout,2+count))   # Duy_test
                    Edit_build_record()
                    Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Finish_class)
                    Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Finish_class)
                    #time.sleep(5)
                    #print(" CLICK CANCEL, PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                    #Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Cancel_testsuit_class)
                    print(" BACKKKKKKKKKK, PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                    cf.driver.back() 
                    time.sleep(3) 
                    cf.driver.back()
                    #time.sleep(3))
                    if(cf.error_flag ==  0): # make sure rename test_suit after click "finish"
                        MC2[i] = 0
            except:
                print("name2 fail")
                pass

            try:    # Machine 3
                if(cf.error_flag ==  1):
                    print("error_flag = 1")
                    break
                name3 = ["name3", str(MC3[i])] 
                if(name3[1] != "0"):  # name3 = 0 when that test_suit was run
                    Click_Tag_htlm(cf.text_Tag, cf.timeout, name3)
                    if(cf.error_flag ==  0): # if test_suit was Clicked page_path + 1
                        count = count + 1
                    Click_Tag_htlm(cf.aria_label_tag, cf.timeout, cf.Run_btn_arialable, count-1)
                    Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Run_testsuit_class, count-1)
                    Change_Machine_For_Testcase(cf.timeout, 'TEST02-PC',Get_TimesPage(cf.timeout,2+count))   # Duy_test
                    Edit_build_record()
                    Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Finish_class)
                    #time.sleep(5)
                    #print(" CLICK CANCEL, PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                    #Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Cancel_testsuit_class)
                    print(" BACKKKKKKKKKK, PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                    cf.driver.back() 
                    time.sleep(3) 
                    cf.driver.back()
                    #time.sleep(3)
                    if(cf.error_flag ==  0): # make sure rename test_suit after click "finish"
                        MC3[i] = 0
                    
            except:
                print("name3 fail")
                pass
            print("MC1: " + str(name1))
            print("MC2: " + str(name2))
            print("MC3: " + str(name3))
            if(cf.error_flag ==  0):
                Check_Result()
                #cf.save_forloop = i+1


            if(i == (max_len - 1) and cf.error_flag ==  0): # end_flag =1 when run full for loop
                cf.end_flag = 1
            else: cf.end_flag = 0
    else:
        cf.end_flag = 1


def Edit_testSuit_record():    
    if(cf.error_flag == 0):
        if(cf.get_data_excel == 0):
            cf.MC1 = find_setup_MC1()
            cf.MC2 = find_setup_MC2()
            cf.MC3 = find_setup_MC3()
            # print("MC1: " + str(MC1))
            # print("MC2: " + str(MC2))
            # print("MC3: " + str(MC3))
            MC_Array = [cf.MC1, cf.MC2, cf.MC3]
            find_max_ArrMachine(MC_Array)
            cf.get_data_excel = 1
        Edit_MC(cf.MC1, cf.MC2, cf.MC3)

# if __name__ == "__main__":
#     main()