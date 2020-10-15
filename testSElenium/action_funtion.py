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
from variable_duy import *
import time

global driver

print(cf.PATH)
cf.driver = webdriver.Chrome(cf.PATH)
def setup():
    
    cf.driver.get("https://rationalcld.dl.net/qm")
    #cf.driver.maximize_window()

def Click_button_id(timeout_item, path_item):
    WebDriverWait(cf.driver, timeout_item).until(EC.presence_of_element_located((By.ID, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
    cf.driver.find_element_by_id(path_item[0]).click()
    print("buttin_id was clicked")
 
def Click_button_xpath(timeout_item, path_item):  
    WebDriverWait(cf.driver, timeout_item).until(EC.element_to_be_clickable((By.XPATH, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
    cf.driver.find_element_by_xpath(path_item[0]).click()

def Click_button_name(timeout_item, path_item):  ########
    WebDriverWait(cf.driver, timeout_item).until(EC.element_to_be_clickable((By.NAME, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
    cf.driver.find_element_by_name(path_item[0]).click()
    print("asdasdasd")

def Click_LinkText(timeout_item, path_item):
    global error_flag
    if(cf.error_flag == 0):
        try:        # USE try to fix error: "Message: stale element reference: element is not attached to the page document"
            WebDriverWait(cf.driver, timeout_item).until(EC.presence_of_element_located((By.LINK_TEXT, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
            cf.driver.find_element_by_link_text(path_item[0]).click()
        except: 
            cf.error_flag = 1
    else:
        print("error_Flag =1")
    
def Click_Text(timeout_item, path_item):
    count = 0
    while(count < timeout_item):
        try:
            #time.sleep(2) # it still run click() if not sleep, but won't actually click
            xpath = "//*[text()='"+path_item[1]+"']"
            time.sleep(1)
            count = count + 1
            print(xpath)
            find_element = cf.driver.find_elements_by_xpath(xpath)[0]
            WebDriverWait(cf.driver, timeout_item).until(EC.element_to_be_clickable((By.XPATH, xpath)), message=("Can not find: " + path_item[1])) # check if the path is clickable                       
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
                find_element = cf.driver.find_elements_by_xpath(xpath)[index]
                display = find_element.is_displayed()  # check if the path displays
                time.sleep(1)
                count = count + 1
                if(display is True):
                    WebDriverWait(cf.driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, xpath)), message=("Can not find: "+path_item[0])) # check if the path is clickable          
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
                find_element = cf.driver.find_elements_by_xpath(xpath)[index]
                time.sleep(1)
                count = count + 1
                display = find_element.is_displayed()  # check if the path displays
                if(display is True):
                    WebDriverWait(cf.driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, xpath)), message=("Can not find " + path_item[0] )) # check if the path is clickable          
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
                find_element = cf.driver.find_elements_by_xpath(xpath)[index]
                time.sleep(1)
                count = count + 1
                display = find_element.is_displayed()  # check if the path displays
                if(display is True):
                    WebDriverWait(cf.driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, xpath)), message=("Can not find: "+path_item[0])) # check if the path is clickable          
                    actionChains = ActionChains(cf.driver)
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
                find_element = cf.driver.find_elements_by_xpath(xpath)[index]
                time.sleep(1)
                count = count + 1 
                display = find_element.is_displayed()  # check if the path displays
                if(display is True):
                    WebDriverWait(cf.driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, xpath)), message=("Can not find: "+path_item[0])) # check if the path is clickable          
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
                find_element = cf.driver.find_elements_by_xpath(xpath)[index]
                time.sleep(1)
                count = count + 1 
                display = find_element.is_displayed()  # check if the path displays
                if(display is True):
                    WebDriverWait(cf.driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, xpath)), message=("Can not find: "+path_item[0])) # check if the path is clickable          
                    actionChains = ActionChains(cf.driver)
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
                find_element = cf.driver.find_elements_by_xpath(xpath)[index]
                time.sleep(1)
                count = count + 1 
                display = find_element.is_displayed()  # check if the path displays
                if(display is True):
                    WebDriverWait(cf.driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, xpath)), message=("Can not find " + path_item[0] )) # check if the path is clickable          
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
      

def Send_key_id(timeout_item, path_item):
    WebDriverWait(cf.driver, timeout_item).until(EC.presence_of_element_located((By.ID, path_item[1])) )        # wait until item exits
    cf.driver.find_element_by_id(path_item[1]).send_keys(path_item[2])
    

def Send_key_xpath(timeout_item, path_item):
    WebDriverWait(cf.driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, path_item[1])))        # wait until item exits
    cf.driver.find_element_by_xpath(path_item[1]).send_keys(path_item[2])

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
                find_element = cf.driver.find_elements_by_xpath(xpath)[index]
                time.sleep(1)
                count = count + 1 
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


def Get_NoItem(attribute):
    global error_flag
    if(cf.error_flag == 0):
        time.sleep(1) # waiting for update attribute
        xpath = "//*[text()='No items found.']"
        print(xpath)
        find_element = cf.driver.find_elements_by_xpath(xpath)
        for i in range(len(find_element)):
            value = find_element[i].get_attribute(attribute)
            if(value == "display: block;"):
                print("no item found is exist")
                return True
            else:
                return False
     


def Check_element_isDisplay(path_item):
    try:
        xpath = path_item
        find_element = cf.driver.find_elements_by_xpath(xpath)[0]
        display = find_element.is_displayed()  # check if the path displays
        if(display is True):
            return True
        else:
            return False
    except:
        pass
                         

#================== specific function===================
def Click_FilterText_TestPlan(timeout_item,string):
    global error_flag
    count = 0
    done = 0
    if(cf.error_flag == 0):
        while(count < timeout_item):
            try:
                xpath = "//input[@aria-label='This is Test Plans table: filter text input']"
                find_element = cf.driver.find_elements_by_xpath(xpath)[0]
                display = find_element.is_displayed()  # check if the path displays
                time.sleep(1)
                count = count + 1 
                if(display is True):
                    WebDriverWait(cf.driver, timeout_item).until(EC.element_to_be_clickable((By.XPATH, xpath)), message=("Can not find: Filter Test plan ")) # check if the path is clickable          
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
    Click_Father_Son_Tag_htlm(cf.title_tag, cf.timeout, cf.Testsuit_ExcutionRecord_table, cf.Show_slider_TSExcution_title) # click expand filter
    Click_Father_Son_Tag_htlm(cf.Name_tag, cf.timeout, cf.Testsuit_ExcutionRecord_table, cf.Clear_name)
    Click_Father_Son_Tag_htlm(cf.Class_tag, cf.timeout, cf.Testsuit_ExcutionRecord_table, cf.LastResult_TSExcution_expand_class)    # click last result
    Click_Father_Son_Tag_htlm(cf.text_Tag, cf.timeout, cf.LastResult_TSExcution_table, cf.InProgress_text)  # click incomplete
    while(cf.complete_flag == 0 and cf.error_flag ==  0):
        Click_Father_Son_Tag_htlm(cf.text_Tag, cf.timeout, cf.Testsuit_ExcutionRecord_table, cf.Run_text) # click Run
        Nofound = Get_NoItem(cf.style) 
        if(Nofound is True):
            cf.complete_flag = 1
            cf.save_forloop = cf.save_forloop + 1       # save for_loop +1 when complete 1 turn
        else:
            cf.complete_flag = 0
        time.sleep(10)
    # uncheck In_progress
    # Click_Father_Son_Tag_htlm(cf.Class_tag, cf.timeout, cf.Testsuit_ExcutionRecord_table, cf.LastResult_TSExcution_expand_class)    # click last result
    # Click_Father_Son_Tag_htlm(cf.text_Tag, cf.timeout, cf.LastResult_TSExcution_table, cf.InProgress_text)  # click incomplete
    Click_Father_Son_Tag_htlm(cf.Name_tag, cf.timeout, cf.Testsuit_ExcutionRecord_table, cf.Clear_name)
    Click_Father_Son_Tag_htlm(cf.text_Tag, cf.timeout, cf.Testsuit_ExcutionRecord_table, cf.Run_text) # click Run
    Click_Father_Son_Tag_htlm(cf.title_tag, cf.timeout, cf.Testsuit_ExcutionRecord_table, cf.Hide_slider_TSExcution_title)
    print("done")

def Check_result_MC1(machine):
    machine1_flag = False
    Click_Father_Son_Tag_htlm(cf.Name_tag, cf.timeout, cf.Testsuit_ExcutionRecord_table, cf.Clear_name)
    cf.Machine_name[2] = machine
    Send_Father_SonTag_htlm(cf.Name_tag, cf.timeout, cf.Testsuit_ExcutionRecord_table, cf.Machine_name)
    Click_Father_Son_Tag_htlm(cf.Class_tag, cf.timeout, cf.Testsuit_ExcutionRecord_table, cf.LastResult_TSExcution_expand_class)    # click last result
    Click_Father_Son_Tag_htlm(cf.text_Tag, cf.timeout, cf.LastResult_TSExcution_table, cf.InProgress_text)  # click incomplete
    Click_Father_Son_Tag_htlm(cf.text_Tag, cf.timeout, cf.Testsuit_ExcutionRecord_table, cf.Run_text) # click Run
    Nofound = Get_NoItem(cf.style) 
    if(Nofound is True):
        machine1_flag = True
        return True # return true to break out of loop
    
        
    


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

# #     find_element = cf.driver.find_element_by_xpath(xpath)
# #     print(find_element)
# #     actionChains = ActionChains(cf.driver)
# #     actionChains.double_click(find_element).perform()
# #     print("1")
# #    # ActionChains.double_click(find_element).perform()
# #     print("2")
    #cf.driver.back()


def Get_Text_Element(timeout_item):
    #global Get_Machine_from_Web
    global error_flag
    count = 0
    done = 0
    if(cf.error_flag == 0):
        while(count < timeout_item):
            try:
                # Click_Tag_htlm(Class_tag, timeout, Run_testsuit_class)
                Machine_Element_link= '//td[@class="table-cell-editable"]//div[@class="clip-cell-nowrap table-cell-resize-marker"]//span'
                Machine_Element = cf.driver.find_elements_by_xpath(Machine_Element_link)
                cf.Get_Machine_from_Web = Machine_Element[5].text
                LenText = len(cf.Get_Machine_from_Web)
                time.sleep(1)
                count = count + 1
                print("length",LenText )
                print('Get_Machine_from_Web: ',cf.Get_Machine_from_Web)
                if( LenText != 0):
                    done = 1
                    break  
            except:
                time.sleep(1)
                print("Waiting for element display")
                count = count + 1
        if(done == 0):   # try: was not run
            cf.error_flag = 1 # have error
    else:
        print("error_Flag = 1")
   
   