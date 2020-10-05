from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.remote.command import Command
from variable import *
import time


PATH = r"C:\Users\pdo2\Desktop\Script Tool\Src\Driver\chromedriver84.exe"
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
    try:        # USE try to fix error: "Message: stale element reference: element is not attached to the page document"
        WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.LINK_TEXT, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
        driver.find_element_by_link_text(path_item[0]).click()
    except: 
        WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.LINK_TEXT, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
        driver.find_element_by_link_text(path_item[0]).click()
    
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

def Click_Tag_htlm(tag, timeout_item,path_item):
    count = 0
    while(count < timeout_item):
        try:
            xpath = "//*[" +tag+ "=\"" +path_item+ "\"]"
            #print(xpath)
            find_element = driver.find_elements_by_xpath(xpath)[0]
            display = find_element.is_displayed()  # check if the path displays
            if(display is True):
                WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, xpath)), message=("Can not find: ")) # check if the path is clickable          
                #print("display: " + str(display))
                #time.sleep(1)
                find_element.click()
                print("good: "+ tag + " was clicked")
                break
        except:
            time.sleep(1)
            print("Waiting for Click " + tag)
            count = count + 1   

def Send_Tag_htlm(tag, timeout_item,path_item, string):
    count = 0
    while(count < timeout_item):
        try:
            xpath = "//*[@"+tag+"=\""+path_item+"\"]"
            #print(xpath)
            find_element = driver.find_elements_by_xpath(xpath)[0]
            display = find_element.is_displayed()  # check if the path displays
            if(display is True):
                WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, xpath)), message=("Can not find ")) # check if the path is clickable          
                #print("display: " + str(display))
                find_element.send_keys(string)
                print("good: "+ tag + " was sent")
                break
        except:
            time.sleep(1)
            print("Waiting for send " + tag)
            count = count + 1   
      

def Send_key_id(timeout_item, path_item, string):
    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.ID, path_item[0])), message=("Can not find: "))        # wait until item exits
    driver.find_element_by_id(path_item[0]).send_keys(string)
    

def Send_key_xpath(timeout_item, path_item, string):
    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
    driver.find_element_by_xpath(path_item[0]).send_keys(string)


#================== specific function===================
def Click_FilterText_TestPlan(timeout_item,string):
    count = 0
    while(count < timeout_item):
        try:
            xpath = "//input[@aria-label='This is Test Plans table: filter text input']"
            find_element = driver.find_elements_by_xpath(xpath)[0]
            display = find_element.is_displayed()  # check if the path displays
            if(display is True):
                WebDriverWait(driver, timeout_item).until(EC.element_to_be_clickable((By.XPATH, xpath)), message=("Can not find: Filter Test plan ")) # check if the path is clickable          
                print("display: " + str(display))
                find_element.click()
                print("good: element was clicked")
                find_element.send_keys(string)
                break
        except:
            time.sleep(1)
            print("Waiting for element display")
            count = count + 1


# Global Variables
arrMachine1 = [1,9,3,11,15]                       # all of Test suit are selected with Machine 1
arrMachine2 = [2,12,6,4]                          #
arrMachine3 = [5,7,8]                             #
Arr = [arrMachine1, arrMachine2, arrMachine3]
max_len = 0


def find_max_ArrMachine():
    for i in Arr:
        if(len(i) > max_len):
            max_len = len(i) 
    print("max length arr: " + str(max_len))

 

def Run_TestSuit(): # example
    #for i in max_len:
        try:
            name_TS1 = "CommandlineTest - Load configuration with Script Formatting from PC_Matrix M300N"  # arrMachine1[i] = name test suit;         #getName_TestSuit(arrMachine1[i])
            Click_Tag_htlm(text_Tag, timeout, name_TS1)
            Click_Tag_htlm(aria_label_tag ,timeout, Run_btn_arialable)
            Click_Tag_htlm(text_Tag, timeout, Run_text)
        except: 
            print("noo")

def Edit_build_record():
    Click_Tag_htlm(title_tag, timeout, Clear_Associated_Build_title)
    Click_Tag_htlm(title_tag, timeout, Change_Associated_Build_title )

