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
    Click_LinkText(timeout, ID_test_linktext)
    # Click Planning & Browse
    Click_button_id(timeout, Plannningbox_id)
    Click_Text(timeout, Browse_TestPlan_text)
    Click_FilterText_TestPlan(timeout, filter_TestPlan)
    Click_LinkText(timeout, TestPlan_linktext)
    #Click Test suit execution records
    Click_Text(timeout, Testsuit_records_text)




def main():
    setup()
    login()
    

if __name__ == "__main__":
    main()
    


