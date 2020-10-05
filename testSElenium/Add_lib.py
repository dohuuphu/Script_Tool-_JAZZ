from action_funtion import *
#import action_funtion as act
# #import action_funtion.*


# ============================= Script =====================
def login_to_testSuit_record():
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
    Click_Tag_htlm(title_tag, timeout, Change_Associated_Build_title)
    Click_Tag_htlm(title_tag, timeout, Clear_Table_Filters)
    #Click_Tag_htlm(aria_label_tag, timeout, Filter_record_arialable)
    Send_Tag_htlm(aria_label_tag, timeout,Filter_record_arialable, "adf" )




def main():
    setup()
    login_to_testSuit_record()
    Run_TestSuit()
    Edit_build_record()



if __name__ == "__main__":
    main()
    


