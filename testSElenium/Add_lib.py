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
    Click_Tag_htlm(title_tag, timeout, Planning_title)
    time.sleep(2) # Browse test plan still run click() if not sleep, but won't actually click
    Click_Tag_htlm(ID_tag, timeout, Browse_testplan_id) # text "browse test plan" can find 2 element => use ID

    Click_FilterText_TestPlan(timeout, filter_TestPlan)
    # Click_Tag_htlm(aria_label_tag, timeout, Filter_TsPlan_arialable)
    # Send_Tag_htlm(aria_label_tag, timeout,Filter_TsPlan_arialable, filter_TestPlan)

    print("filled 1439")
    Click_LinkText(timeout, TestPlan_linktext)
    
    #Click Test suit execution records
    Click_Tag_htlm(text_Tag, timeout, Testsuit_records_text)
    Run_TestSuit()
    Edit_build_record()



def main():
    setup()
    login()


if __name__ == "__main__":
    main()
    


