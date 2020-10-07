#from action_funtion import *
from Read_excel import *
#import action_funtion as act
# #import action_funtion.*

# ============================= Script =====================
def login_to_testSuit_record():
    # Login to webpage
    Send_Tag_htlm(ID_tag, timeout, IDuser_id)
    print("error_flag", error_flag)
    Send_Tag_htlm(ID_tag, timeout, password_id)
    Click_Tag_htlm(text_Tag, timeout, Login_text)
   
    # Click link ** ID_test **
    Click_LinkText(timeout, ID_test_linktext)
    
    # Click Planning & Browse
    Click_Tag_htlm(title_tag, timeout, Planning_title)
    time.sleep(3) # Browse test plan still run click() if not sleep, but won't actually click
    Click_Tag_htlm(ID_tag, timeout, Browse_testplan_id) # text "browse test plan" can find 2 element => use ID

    Click_FilterText_TestPlan(timeout, filter_TestPlan)
    # Click_Tag_htlm(aria_label_tag, timeout, Filter_TsPlan_arialable)
    # Send_Tag_htlm(aria_label_tag, timeout,Filter_TsPlan_arialable, filter_TestPlan)

    print("filled 1439")
    Click_LinkText(timeout, TestPlan_linktext)
    
    #Click Test suit execution records
    Click_Tag_htlm(text_Tag, timeout, Testsuit_records_text)
    






def main():
    setup()
    login_to_testSuit_record()  
    #Run_TestSuit()
    Edit_testSuit_record()  # click finish and backpage 2 time



if __name__ == "__main__":
    while(True):
        main()
        if(exit_flag == 1):
            break


