from action_funtion import *
#import action_funtion as act
# #import action_funtion.*


# ============================= Script =====================
def login():
    # Login to webpage
    Send_key_id(timeout,IDuser_id, login_ID)
    Send_key_id(timeout, password_id, login_password)
    Click_button_xpath(timeout, login_button_xpath)
   
    # Click link ** ID_test **
    Click_LinkText(timeout, ID_test_linktext)
    
    # Click Planning & Browse
    Click_button_id(timeout, Plannningbox_id)
    #Click_id(timeout, Plannningbox_id)
    Click_Text(timeout, Browse_TestPlan_text)
    # Click_FilterText_TestPlan(timeout, filter_TestPlan)
    Click_aria_lable(timeout, Filter_TsPlan_arialable)
    #print("filled 1439")
    Click_LinkText(timeout, TestPlan_linktext)
    
    #Click Test suit execution records
    Click_Text(timeout, Testsuit_records_text)
    Run_TestSuit()




def main():
    setup()
    login()
    #find_max_ArrMachine()
    # arr = []
    # try:
    #     print("ASd")
    #     print(arr[0])
    # except:
    #     print("no")
    # a= "dhp"
    # b= "'"+a+"'"
    # print(b)

if __name__ == "__main__":
    main()
    


