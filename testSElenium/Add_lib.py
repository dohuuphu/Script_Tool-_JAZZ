from action_funtion import *
#import action_funtion as act
# #import action_funtion.*


# ============================= Script =====================
def login():
    # Login to webpage
    Send_key_id(timeout,IDuser_id, login_ID)
    #send_key_test(timeout,IDuser_id, login_ID)
    Send_key_id(timeout, password_id, login_password)
    Click_button_xpath(timeout, login_button_xpath)
    # Click link ** ID_test **
    Click_LinkText(timeout, ID_test_id)
    # Click Planning & Browse
    Click_button_id(timeout, Plannningbox_id)
    Click_Text(timeout, Browse_TestPlan_id)
    #Click_button_name(timeout, filterText_name)
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"com_ibm_asq_common_web_ui_internal_widgets_tableViewer_TableViewer_0\"]/table[1]/tbody/tr[1]/td/span/input")), message=("Can not find: "))        # wait until item exits
    check = driver.find_elements_by_xpath("//*[@id=\"com_ibm_asq_common_web_ui_internal_widgets_tableViewer_TableViewer_0\"]/table[1]/tbody/tr[1]/td/span/input").is_enabled()
    print("asdasdasd")
    print(check)




def main():
    setup()
    login()
    

if __name__ == "__main__":
    main()
    


