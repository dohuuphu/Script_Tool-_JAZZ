#from action_funtion import *
from Read_excel import *
#import action_funtion as act
# #import action_funtion.*

# ============================= Script =====================
def login_to_testSuit_record():
    # Login to webpage
    Send_Tag_htlm(ID_tag, timeout, IDuser_id)
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
    Edit_testSuit_record()
    #Edit_build_record()
    
    # while(True):
    #     try:
    #         print("try try try")
    #         a=0
    #         b=1
    #         break
    #     except:
    #         print("except")



if __name__ == "__main__":
    main()
    if(error_flag != 0):
        try:
            error_flag == 0
            main()
            if(error_flag != 0): 
                print("can't solve")
                exit(1)
            
        except:
            exit(1)
    


