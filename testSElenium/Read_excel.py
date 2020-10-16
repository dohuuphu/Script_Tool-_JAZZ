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

def find_setup_MC1(sheet):
    name=[]
    file_excel = pandas.read_excel('Data_Main.xlsx',sheet_name=sheet[0])
    MC1_list =file_excel.loc[file_excel['Machine Name'].isin(['TestExecute-PC'])]
    list_index = MC1_list.index #[0,2] row
    for i in range(len(list_index)):
         value = file_excel.loc[file_excel['Name'].index[list_index[i]]].tolist()[2]
         name = np.append(name, value)
    # print("row_number: " + str(list_index))
    # print("Machine_name: " + str(name))
    return(name)

def find_setup_MC2(sheet):
    name=[]
    file_excel = pandas.read_excel('Data_Main.xlsx',sheet_name=sheet[0])
    MC1_list =file_excel.loc[file_excel['Machine Name'].isin(['TestComplete14_'])]
    list_index = MC1_list.index #[0,2] row
    for i in range(len(list_index)):
         value = file_excel.loc[file_excel['Name'].index[list_index[i]]].tolist()[2]
         name = np.append(name, value)
    # print("row_number: " + str(list_index))
    # print("Machine_name: " + str(name))
    return(name)

def find_setup_MC3(sheet):
    name=[]
    file_excel = pandas.read_excel('Data_Main.xlsx',sheet_name=sheet[0])
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

def Edit_Machine(MC1, MC2, MC3):
    name1 = name2 = name3 =[]
    #global count
    cf.count_page = 0
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
                        cf.count_page = cf.count_page + 1
                    Click_Tag_htlm(cf.aria_label_tag, cf.timeout, cf.Run_btn_arialable, cf.count_page-1)
                    Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Run_testsuit_class, cf.count_page-1)
                    Change_Machine_For_Testcase(cf.timeout, 'TestExecute-PC',Get_TimesPage(cf.timeout))   # Duy_test
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
                        cf.count_page = cf.count_page + 1
                    Click_Tag_htlm(cf.aria_label_tag ,cf.timeout, cf.Run_btn_arialable, cf.count_page-1)
                    Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Run_testsuit_class, cf.count_page-1)
                    Change_Machine_For_Testcase(cf.timeout, 'TestComplete14_',Get_TimesPage(cf.timeout))   # Duy_test
                    Edit_build_record()
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
                        cf.count_page = cf.count_page + 1
                    Click_Tag_htlm(cf.aria_label_tag, cf.timeout, cf.Run_btn_arialable, cf.count_page-1)
                    Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Run_testsuit_class, cf.count_page-1)
                    Change_Machine_For_Testcase(cf.timeout, 'TEST02-PC',Get_TimesPage(cf.timeout))   # Duy_test
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


def Edit_Machine2(MC1, MC2, MC3):
    # name1 = name2 = name3 =[]
    #global count
    cf.count_page = 0
    cf.Run_Machine1_flag = True
    cf.Run_Machine2_flag = True
    cf.Run_Machine3_flag = True
    cf.Turn_Machine1_flag = 0
    cf.Turn_Machine2_flag = 0
    cf.Turn_Machine3_flag = 0
    cf.Number_MC1 = len(MC1)
    cf.Number_MC2 = len(MC2)
    cf.Number_MC3 = len(MC3)
    if(cf.Number_MC1 != 0 or cf.Number_MC2 != 0 or cf.Number_MC3 != 0 ):
        while(True):
            if(cf.error_flag ==  1):
                print("error_flag = 1")
                break
            name_testsuit_1 = "0"
            name_testsuit_2 = "0"
            name_testsuit_3 = "0"
            try:
                name_testsuit_1 = str(MC1[cf.Turn_Machine1_flag])
            except:
                print("name_testsuit_1 is null")
            try:
                name_testsuit_2 = str(MC2[cf.Turn_Machine2_flag])
            except:
                print("name_testsuit_2 is null")
            try:
                name_testsuit_3 = str(MC3[cf.Turn_Machine3_flag])
            except:
                print("name_testsuit_3 is null")
            if(cf.Run_Machine1_flag is True and cf.Turn_Machine1_flag < cf.Number_MC1):
                Edit_MC1(name_testsuit_1)
            else:
                print("MC1: test suit is still running or complete")
            if(cf.Run_Machine2_flag is True and cf.Turn_Machine2_flag < cf.Number_MC2):
                Edit_MC2(name_testsuit_2)
            else:
                print("MC2: test suit is still running or complete")
            if(cf.Run_Machine3_flag is True and cf.Turn_Machine3_flag < cf.Number_MC3):
                Edit_MC3(name_testsuit_3)
            else:
                print("MC3: test suit is still running or complete")
            if(cf.error_flag == 0):
                Check_Result2(name_testsuit_1, name_testsuit_2, name_testsuit_3)
                #cf.save_forloop = i+1
    else:
        #cf.end_flag = 1
        print("no test suite")

def Edit_MC1(name):
    name1 = []
    try:   # Machine 1
            if(cf.error_flag == 0):
                name1 = ["name1", str(name)]
                print("MC1: test suit name =  ", name1[1])
                if(name1[1] != "0"):  # name1 = 0 when that test_suit was run
                    Click_Tag_htlm(cf.text_Tag, cf.timeout, name1)
                    if(cf.error_flag == 0):  # if test_suit was Clicked, page_path + 1
                        cf.count_page = cf.count_page + 1
                    Click_Tag_htlm(cf.aria_label_tag, cf.timeout, cf.Run_btn_arialable, cf.count_page-1)
                    Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Run_testsuit_class, cf.count_page-1)
                    Change_Machine_For_Testcase(cf.timeout, 'TestExecute-PC', Get_TimesPage(cf.timeout))   # Duy_test
                    Edit_build_record()
                    #Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Finish_class)
                    #time.sleep(5)
                    #print(" CLICK CANCEL, PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                    #Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Cancel_testsuit_class)
                    print(" BACKKKKKKKKKK, PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                    cf.driver.back()
                    time.sleep(3)
                    cf.driver.back()
                    #time.sleep(3)
                    # if(cf.error_flag == 0):  # make sure rename test_suit after click "finish"
                    #     MC1[i] = 0
    except:
        print("name1 fail")
        pass    

def Edit_MC2(name):
    name2 = []
    try:   # Machine 1
            if(cf.error_flag == 0):
                name2 = ["name2", str(name)]
                print("MC2: test suit name =  ", name2[1])
                if(name2[1] != "0"):  # name1 = 0 when that test_suit was run
                    Click_Tag_htlm(cf.text_Tag, cf.timeout, name2)
                    if(cf.error_flag == 0):  # if test_suit was Clicked, page_path + 1
                        cf.count_page = cf.count_page + 1
                    Click_Tag_htlm(cf.aria_label_tag, cf.timeout, cf.Run_btn_arialable, cf.count_page-1)
                    Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Run_testsuit_class, cf.count_page-1)
                    Change_Machine_For_Testcase(cf.timeout, 'TestExecute-PC', Get_TimesPage(cf.timeout))   # Duy_test
                    Edit_build_record()
                    #Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Finish_class)
                    #time.sleep(5)
                    #print(" CLICK CANCEL, PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                    #Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Cancel_testsuit_class)
                    print(" BACKKKKKKKKKK, PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                    cf.driver.back()
                    time.sleep(3)
                    cf.driver.back()
                    #time.sleep(3)
                    # if(cf.error_flag == 0):  # make sure rename test_suit after click "finish"
                    #     MC1[i] = 0
    except:
        print("name2 fail")
        pass   

def Edit_MC3(name):
    name3 = []
    try:   # Machine 1
            if(cf.error_flag == 0):
                name3 = ["name1", str(name)]
                print("MC3: test suit name =  ", name3[1])
                if(name3[1] != "0"):  # name1 = 0 when that test_suit was run
                    Click_Tag_htlm(cf.text_Tag, cf.timeout, name3)
                    if(cf.error_flag == 0):  # if test_suit was Clicked, page_path + 1
                        cf.count_page = cf.count_page + 1
                    Click_Tag_htlm(cf.aria_label_tag, cf.timeout, cf.Run_btn_arialable, cf.count_page-1)
                    Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Run_testsuit_class, cf.count_page-1)
                    Change_Machine_For_Testcase(cf.timeout, 'TestExecute-PC', Get_TimesPage(cf.timeout))   # Duy_test
                    Edit_build_record()
                    #Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Finish_class)
                    #time.sleep(5)
                    #print(" CLICK CANCEL, PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                    #Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Cancel_testsuit_class)
                    print(" BACKKKKKKKKKK, PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                    cf.driver.back()
                    time.sleep(3)
                    cf.driver.back()
                    #time.sleep(3)
                    # if(cf.error_flag == 0):  # make sure rename test_suit after click "finish"
                    #     MC1[i] = 0
    except:
        print("name3 fail")
        pass        


def Edit_testSuit_record():    
    if(cf.error_flag == 0):
        if(cf.get_data_excel == 0):
            cf.MC1 = find_setup_MC1(cf.TestPlan_linktext)
            cf.MC2 = find_setup_MC2(cf.TestPlan_linktext)
            cf.MC3 = find_setup_MC3(cf.TestPlan_linktext)
            # print("MC1: " + str(MC1))
            # print("MC2: " + str(MC2))
            # print("MC3: " + str(MC3))
            MC_Array = [cf.MC1, cf.MC2, cf.MC3]
            find_max_ArrMachine(MC_Array)
            cf.get_data_excel = 1
        Edit_Machine2(cf.MC1, cf.MC2, cf.MC3)

# if __name__ == "__main__":
#     main()
