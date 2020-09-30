from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from variable import *
import time


PATH = r"C:\Users\pdo2\Desktop\Script Tool\Src\Driver\chromedriver84.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://rationalcld.dl.net/qm")
driver.maximize_window()


def Click_button_id(timeout_item, path_item):
    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.LINK_TEXT, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
    item =  driver.find_element_by_id(path_item)
    item.click()

def Click_button_xpath(timeout_item, path_item):  
    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.LINK_TEXT, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
    item =  driver.find_element_by_xpath(path_item)
    # get = item.get_attribute("type")
    # print(get)
    item.click()

def Click_LinkText(timeout_item, path_item):
    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.LINK_TEXT, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
    item =  driver.find_element_by_link_text(path_item)
    item.click()
    

def Send_key_id(timeout_item, path_item, string):
    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.LINK_TEXT, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
    item =  driver.find_element_by_id(path_item)
    item.send_keys(string)
    

def Send_key_xpath(timeout_item, path_item, string):
    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.LINK_TEXT, path_item[0])), message=("Can not find: " + path_item[1]))        # wait until item exits
    item =  driver.find_element_by_xpath(path_item)
    item.send_keys(string)
    

# def login():  
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, IDuser_id)))        # wait until IDbox exits
#     #Find path
#     IDuser = driver.find_element_by_id(IDuser_id)
#     pass_login = driver.find_element_by_id(password_id)
#     login_button = driver.find_element_by_xpath(login_button_xpath)
    
#     # Edit login
#     IDuser.send_keys( "lhoang")
#     pass_login.send_keys("D@talogic7")
#     login_button.click()
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, "ID (Test)")))        # wait until ID(test) exits
#     ID_test = driver.find_element_by_link_text("ID (Test)")
#     ID_test.click()

def login():
    Send_key_id(timeout,IDuser_id,login_ID)
    Send_key_id(timeout, password_id, login_password)
    #Click_button_xpath(timeout,login_button_xpath)
    Click_LinkText(timeout, ID_test_id)



def Click_Planning():
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, Plannningbox_id)))        # wait until planning box exits
    Planning_box = driver.find_elements_by_id(Plannningbox_id)
    Planning_box.click()
     
    
def test():
     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, Plannningbox_id)))        # wait until planning box exits

def main():
    login()
    Click_Planning()

if __name__ == "__main__":
    main()
    


