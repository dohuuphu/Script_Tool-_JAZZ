from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.remote.webelement import WebElement
#from selenium.webdriver.support.select import Select
import variable as cf
#from variable import *
#from variable_duy import vd
import time


PATH = r"C:\Users\pdo2\Desktop\Script Tool\Src\Driver\chromedriver84.exe"
#PATH = r"C:\Users\dnguyen4\Documents\Script_Tool-_JAZZ\Driver\chromedriver85.exe"
# PATH = r"C:\Users\dnguyen4\Documents\Script_Tool-_JAZZ\Driver\chromedriver84.exe"
driver = webdriver.Chrome(PATH)

def setup():
    driver.get("https://rationalcld.dl.net/qm")
    #driver.maximize_window()

def Click_button_id(timeout_item, path_item):
    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.ID, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
    driver.find_element_by_id(path_item[0]).click()
    print("buttin_id was clicked")
 
def Click_button_xpath(timeout_item, path_item):  
    WebDriverWait(driver, timeout_item).until(EC.element_to_be_clickable((By.XPATH, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
    driver.find_element_by_xpath(path_item[0]).click()

def Click_button_name(timeout_item, path_item):  ########
    WebDriverWait(driver, timeout_item).until(EC.element_to_be_clickable((By.NAME, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
    driver.find_element_by_name(path_item[0]).click()
    print("asdasdasd")

def Click_LinkText(timeout_item, path_item):
    global error_flag
    if(cf.error_flag == 0):
        try:        # USE try to fix error: "Message: stale element reference: element is not attached to the page document"
            WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.LINK_TEXT, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
            driver.find_element_by_link_text(path_item[0]).click()
        except: 
            WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.LINK_TEXT, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
            driver.find_element_by_link_text(path_item[0]).click()
    else:
        print("error_Flag =1")
    
def Click_Text(timeout_item, path_item):
    count = 0
    while(count < timeout_item):
        try:
            time.sleep(2) # it still run click() if not sleep, but won't actually click
            xpath = "//*[text()="+path_item+"]"
            #print(driver.find_elements_by_xpath(xpath))
            find_element = driver.find_elements_by_xpath(xpath)[0]
            display = find_element.is_displayed()  # check if the path displays
            if(display is True):
                print("display: " + str(display))
                WebDriverWait(driver, timeout_item).until(EC.element_to_be_clickable((By.XPATH, xpath)), message=("Can not find: " + path_item[1])) # check if the path is clickable                       
                find_element.click()   
                print("good: Text was clicked")             
                break         
        except:
            time.sleep(1)
            print("Waiting for Click_Text")
            count = count + 1

def Click_Father_Son_Tag_htlm(tag, timeout_item,father, path_item,index = 0):
    global error_flag
    count = 0
    done = 0
    if(cf.error_flag == 0):  
        while(count < timeout_item):
            try:
                xpath = father + "//*[" +tag+ "=\"" +path_item[1]+ "\"]"
                print(xpath)
                time.sleep(1)
                count = count + 1 
                find_element = driver.find_elements_by_xpath(xpath)[index]
                display = find_element.is_displayed()  # check if the path displays
                if(display is True):
                    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, xpath)), message=("Can not find: "+path_item[0])) # check if the path is clickable          
                    #print("display: " + str(display))
                    #time.sleep(1)
                    find_element.click()
                    print("good: "+ tag + " was clicked")
                    done = 1 
                    break
            except:
                time.sleep(1)
                print("Waiting for Click " + tag)
                count = count + 1   
        if(done == 0):   # try: was not run
            cf.error_flag = 1 # have error
    else:
        print("error_Flag =1")

def Send_Father_SonTag_htlm(tag, timeout_item, father, path_item, index = 0):
    global error_flag
    count = 0
    done = 0
    if(cf.error_flag == 0):
        while(count < timeout_item):
            try:
                xpath = father + "//*["+tag+"=\""+path_item[1]+"\"]"
                print(xpath)
                time.sleep(1)
                count = count + 1 
                find_element = driver.find_elements_by_xpath(xpath)[index]
                display = find_element.is_displayed()  # check if the path displays
                if(display is True):
                    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, xpath)), message=("Can not find " + path_item[0] )) # check if the path is clickable          
                    #print("display: " + str(display))
                    find_element.send_keys(path_item[2])
                    print("good: "+ tag + " was sent")
                    done = 1 
                    break
            except:
                time.sleep(1)
                print("Waiting for send " + tag)
                count = count + 1   
        if(done == 0):   # try: was not run
            cf.error_flag = 1 # have error
    else:
        print("error_Flag =1")

def Click_Father_Son_Tag_htlm_Dbl(tag, timeout_item,father, path_item, index = 0):
    global error_flag
    count = 0
    done = 0
    if(cf.error_flag == 0):  
        while(count < timeout_item):
            try:
                xpath = father + "//*[" +tag+ "=\"" +path_item[1]+ "\"]"
                print(xpath)
                time.sleep(1)
                count = count + 1 
                find_element = driver.find_elements_by_xpath(xpath)[index]
                display = find_element.is_displayed()  # check if the path displays
                if(display is True):
                    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, xpath)), message=("Can not find: "+path_item[0])) # check if the path is clickable          
                    actionChains = ActionChains(driver)
                    actionChains.double_click(find_element).perform()
                    print("good: "+ tag + " was clicked")
                    done = 1 
                    break
            except:
                time.sleep(1)
                print("Waiting for Click " + tag)
                count = count + 1   
        if(done == 0):   # try: was not run
            cf.error_flag = 1 # have error
    else:
        print("error_Flag =1")


def Click_Tag_htlm(tag, timeout_item, path_item,index = 0):
    global error_flag
    count = 0
    done = 0
    if(cf.error_flag == 0):  
        while(count < timeout_item):
            try:
                xpath = "//*[" +tag+ "=\"" +path_item[1]+ "\"]"
                print(xpath)
                time.sleep(1)
                count = count + 1 
                find_element = driver.find_elements_by_xpath(xpath)[index]
                display = find_element.is_displayed()  # check if the path displays
                if(display is True):
                    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, xpath)), message=("Can not find: "+path_item[0])) # check if the path is clickable          
                    #print("display: " + str(display))
                    #time.sleep(1)
                    find_element.click()
                    print("good: "+ tag + " was clicked")
                    done = 1 
                    break
            except:
                time.sleep(1)
                print("Waiting for Click " + tag)
                count = count + 1   
        if(done == 0):   # try: was not run
            cf.error_flag = 1 # have error
    else:
        print("error_Flag =1")

def Click_Tag_htlm_Dbl(tag, timeout_item, path_item, index = 0):
    global error_flag
    count = 0
    done = 0
    if(cf.error_flag == 0):  
        while(count < timeout_item):
            try:
                xpath = "//*[" +tag+ "=\"" +path_item[1]+ "\"]"
                print(xpath)
                time.sleep(1)
                count = count + 1 
                find_element = driver.find_elements_by_xpath(xpath)[index]
                display = find_element.is_displayed()  # check if the path displays
                if(display is True):
                    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, xpath)), message=("Can not find: "+path_item[0])) # check if the path is clickable          
                    actionChains = ActionChains(driver)
                    actionChains.double_click(find_element).perform()
                    print("good: "+ tag + " was clicked")
                    done = 1 
                    break
            except:
                time.sleep(1)
                print("Waiting for Click " + tag)
                count = count + 1   
        if(done == 0):   # try: was not run
            cf.error_flag = 1 # have error
            print("got a error, cf.error_flang= ", cf.error_flag)
    else:
        print("error_Flag = 1")

def Send_Tag_htlm(tag, timeout_item,path_item, index = 0):
    global error_flag
    count = 0
    done = 0
    if(cf.error_flag == 0):
        while(count < timeout_item):
            try:
                xpath = "//*["+tag+"=\""+path_item[1]+"\"]"
                print(xpath)
                time.sleep(1)
                count = count + 1 
                find_element = driver.find_elements_by_xpath(xpath)[index]
                display = find_element.is_displayed()  # check if the path displays
                if(display is True):
                    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, xpath)), message=("Can not find " + path_item[0] )) # check if the path is clickable          
                    #print("display: " + str(display))
                    find_element.send_keys(path_item[2])
                    print("good: "+ tag + " was sent")
                    done = 1 
                    break
            except:
                time.sleep(1)
                print("Waiting for send " + tag)
                count = count + 1   
        if(done == 0):   # try: was not run
            cf.error_flag = 1 # have error
            print("got a error, cf.error_flang= ", cf.error_flag)
    else:
        print("error_Flag =1")
      

def Send_key_id(timeout_item, path_item, string):
    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.ID, path_item[0])), message=("Can not find: "))        # wait until item exits
    driver.find_element_by_id(path_item[0]).send_keys(string)
    

def Send_key_xpath(timeout_item, path_item, string):
    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
    driver.find_element_by_xpath(path_item[0]).send_keys(string)

def Get_attribute_Father_Son(tag, timeout_item, father, path_item, attribute, index = 0):
    global error_flag
    count = 0
    done = 0
    if(cf.error_flag == 0):
        while(count < timeout_item):
            try:
                time.sleep(1) # waiting for update attribute
                xpath = father + "//*["+tag+"=\""+path_item[1]+"\"]"
                print(xpath)
                time.sleep(1)
                count = count + 1 
                find_element = driver.find_elements_by_xpath(xpath)[index]
                value = find_element.get_attribute(attribute)
                print("good: "+ tag + " was gotten", value)
                done = 1 
                return value
                break
            except:
                time.sleep(1)
                print("Waiting for send " + tag)
                count = count + 1   
        if(done == 0):   # try: was not run
            cf.error_flag = 1 # have error
            print("got a error, cf.error_flang= ", cf.error_flag)
    else:
        print("error_Flag =1")



#================== specific function===================
def Click_FilterText_TestPlan(timeout_item,string):
    global error_flag
    count = 0
    done = 0
    if(cf.error_flag == 0):
        while(count < timeout_item):
            try:
                xpath = "//input[@aria-label='This is Test Plans table: filter text input']"
                time.sleep(1)
                count = count + 1 
                find_element = driver.find_elements_by_xpath(xpath)[0]
                display = find_element.is_displayed()  # check if the path displays
                if(display is True):
                    WebDriverWait(driver, timeout_item).until(EC.element_to_be_clickable((By.XPATH, xpath)), message=("Can not find: Filter Test plan ")) # check if the path is clickable          
                    print("display: " + str(display))
                    find_element.click()
                    print("good: element was clicked")
                    find_element.send_keys(string)
                    done = 1
                    break
            except:
                time.sleep(1)
                print("Waiting for element display")
                count = count + 1
        if(done == 0):   # try: was not run
            cf.error_flag = 1 # have error
    else:
        print("error_Flag =1")

def Check_Result():
    cf.complete_flag = 0
    Click_Father_Son_Tag_htlm(cf.Class_tag, cf.timeout, cf.Testsuit_ExcutionRecord_table, cf.Filter_slider_TSExcution_class) # click expand filter
    Click_Father_Son_Tag_htlm(cf.Name_tag, cf.timeout, cf.Testsuit_ExcutionRecord_table, cf.Clear_name)
    Click_Father_Son_Tag_htlm(cf.Class_tag, cf.timeout, cf.Testsuit_ExcutionRecord_table, cf.LastResult_TSExcution_expand_class)    # click last result
    Click_Father_Son_Tag_htlm(cf.text_Tag, cf.timeout, cf.LastResult_TSExcution_table, cf.InProgress_text)  # click incomplete
    Click_Father_Son_Tag_htlm(cf.text_Tag, cf.timeout, cf.Testsuit_ExcutionRecord_table, cf.Run_text) # click Run
    while(cf.complete_flag == 0):
        Nofound = Get_attribute_Father_Son(cf.text_Tag, cf.timeout, cf.Testsuit_ExcutionRecord_table, cf.NoFound_text, cf.style) 
        if(cf.error_flag ==  1):
            print("dont get complete flag and break")
            break
        if(Nofound != "display: none;"):
            cf.complete_flag = 1
        else:
            cf.complete_flag = 0
    # uncheck In_progress
    Click_Father_Son_Tag_htlm(cf.Class_tag, cf.timeout, cf.Testsuit_ExcutionRecord_table, cf.LastResult_TSExcution_expand_class)    # click last result
    Click_Father_Son_Tag_htlm(cf.text_Tag, cf.timeout, cf.LastResult_TSExcution_table, cf.InProgress_text)  # click incomplete
    Click_Father_Son_Tag_htlm(cf.text_Tag, cf.timeout, cf.Testsuit_ExcutionRecord_table, cf.Run_text) # click Run
    print("done")

# Global Variables
arrMachine1 = [1,9,3,11,15]                       # all of Test suit are selected with Machine 1
arrMachine2 = [2,12,6,4]                          #
arrMachine3 = [5,7,8]                             #
Arr = [arrMachine1, arrMachine2, arrMachine3]
max_len = 0


# def find_max_ArrMachine():
#     for i in Arr:
#         if(len(i) > max_len):
#             max_len = len(i) 
#     print("max length arr: " + str(max_len))

 



def Run_TestSuit(): # example
    #for i in max_len:
        try:
            name_TS1 = ["name_TS1", "CommandlineTest - Load configuration with Script Formatting from PC_Matrix M300N"]  # arrMachine1[i] = name test suit;         #getName_TestSuit(arrMachine1[i])
            Click_Tag_htlm(cf.text_Tag, cf.timeout, name_TS1)
            Click_Tag_htlm(cf.aria_label_tag, cf.timeout, cf.Run_btn_arialable)
            Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Run_testsuit_class)
        except: 
            print("noo")


def Edit_build_record():
    Click_Tag_htlm(cf.title_tag, cf.timeout, cf.Clear_Associated_Build_title)
    Click_Tag_htlm(cf.title_tag, cf.timeout, cf.Change_Associated_Build_title)

    Click_Father_Son_Tag_htlm(cf.title_tag, cf.timeout, cf.ViewBuildRecord_table, cf.Clear_Table_Filters_title)
    Click_Father_Son_Tag_htlm(cf.Name_tag, cf.timeout, cf.ViewBuildRecord_table, cf.Clear_Text_Filter_name) 
    
    Send_Father_SonTag_htlm(cf.aria_label_tag, cf.timeout, cf.ViewBuildRecord_table, cf.Filter_record_arialable)
    time.sleep(2)
    Click_Father_Son_Tag_htlm(cf.Class_tag, cf.timeout, cf.ViewBuildRecord_table, cf.Run_filter_buildrecord_class)
    Click_Father_Son_Tag_htlm(cf.Class_tag, cf.timeout, cf.ViewBuildRecord_table, cf.Select_BuildRecord_class)
    Click_Father_Son_Tag_htlm(cf.Class_tag, cf.timeout, cf.ViewBuildRecord_table, cf.Ok_buildRecord_class)
#     time.sleep(3)
#     xpath = "//tr[@name= '_IMTthl-EEeqc9ZermTj1qQ-row']//span[text()=\"TEST02-PC\"]"

# #     find_element = driver.find_element_by_xpath(xpath)
# #     print(find_element)
# #     actionChains = ActionChains(driver)
# #     actionChains.double_click(find_element).perform()
# #     print("1")
# #    # ActionChains.double_click(find_element).perform()
# #     print("2")
    #driver.back()