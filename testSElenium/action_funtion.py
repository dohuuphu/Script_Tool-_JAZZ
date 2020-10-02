from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
 
def Click_button_xpath(timeout_item, path_item):  
    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
    driver.find_element_by_xpath(path_item[0]).click()

def Click_button_name(timeout_item, path_item):  ########
    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.NAME, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
    driver.find_element_by_name(path_item[0]).click()
    print("asdasdasd")

def Click_LinkText(timeout_item, path_item):
    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.LINK_TEXT, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
    driver.find_element_by_link_text(path_item[0]).click()
    
def Click_Text(timeout_item, path_item):
    time.sleep(2) # wait update text tag 
    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, "//*[text()="+path_item+"]")), message="nooooo")        # wait until item exits
    driver.find_elements_by_xpath("//*[text()="+path_item+"]")[-1].click()
    
def Click_Title(timeout_item, path_item):
    time.sleep(1) # wait update text tag 
    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, "//*[title()="+path_item+"]")), message="nooooo")        # wait until item exits
    driver.find_elements_by_xpath("//*[text()="+path_item+"]")[-1]


# def Click_Text(timeout_item, path_item):
#     count = 0
#     while(count < timeout_item):        
#         try:
#             WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, "//*[text()="+path_item+"]")), message="nooooo")        # wait until item exits
#             driver.find_elements_by_xpath("//*[text()="+path_item+"]")[-1].click()
#             count = 10
#             print("was clicked")
#         except:
#             time.sleep(1)
#             count = count + 1 
#             print("except")


    

def Send_key_id(timeout_item, path_item, string):
    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.ID, path_item[0])), message=("Can not find: "))        # wait until item exits
    driver.find_element_by_id(path_item[0]).send_keys(string)
    

def Send_key_xpath(timeout_item, path_item, string):
    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
    driver.find_element_by_xpath(path_item[0]).send_keys(string)




# def send_key_test(timeout_item, path_item, string):
#     last_time = time.time()
#     while(True):
#         try:
#             ite = driver.find_element_by_xpath(path_item[0])
#             #item.send_keys(string)
#             print("was send") 
#             break                                 
#         except:
#             print("Except")
#         delta = time.time() - last_time
#         time.sleep(1)
#         print("detal= " + str(delta))
#         if(delta > timeout_item ):
#             print("Nooo, out of time")
#             break


