from action_funtion import *

# ============================= Script =====================
def login():
    # Login to webpage
    Send_key_id(timeout,IDuser_id, login_ID)
    Send_key_id(timeout, password_id, login_password)
    Click_button_xpath(timeout, login_button_xpath)
    # Click link ** ID_test **
    Click_LinkText(timeout, ID_test_id)
    # Click Planning & Browse
    Click_button_id(timeout, Plannningbox_id)
    Click_button_xpath(timeout, Browse_TestPlan_id) 






def main():
    login()

if __name__ == "__main__":
    main()
    


