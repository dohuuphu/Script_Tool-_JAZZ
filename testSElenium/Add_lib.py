#from action_funtion import *
from Read_excel import *
#import action_funtion as act
# #import action_funtion.*

# ============================= Script =====================
def login_to_testSuit_record():
    # Login to webpage
    Send_Tag_htlm(cf.ID_tag, cf.timeout, cf.IDuser_id)
    print("error_flag", cf.error_flag)
    Send_Tag_htlm(cf.ID_tag, cf.timeout, cf.password_id)
    Click_Tag_htlm(cf.text_Tag, cf.timeout, cf.Login_text)
   
    # Click link ** ID_test **
    Click_LinkText(cf.timeout, cf.ID_test_linktext)
    
    # Click Planning & Browse
    Click_Tag_htlm(cf.title_tag, cf.timeout, cf.Planning_title)
    time.sleep(3) # Browse test plan still run click() if not sleep, but won't actually click
    Click_Tag_htlm(cf.ID_tag, cf.timeout, cf.Browse_testplan_id) # text "browse test plan" can find 2 element => use ID

    Click_FilterText_TestPlan(cf.timeout, cf.filter_TestPlan)
    # Click_Tag_htlm(aria_label_tag, timeout, Filter_TsPlan_arialable)
    # Send_Tag_htlm(aria_label_tag, timeout,Filter_TsPlan_arialable, filter_TestPlan)

    print("filled 1439")
    Click_LinkText(cf.timeout, cf.TestPlan_linktext)
    
    #Click Test suit execution records
    Click_Tag_htlm(cf.text_Tag, cf.timeout, cf.Testsuit_records_text)
    






def main():
    setup()
    login_to_testSuit_record()  
    #Run_TestSuit()
    Edit_testSuit_record()  # click finish and backpage 2 time
    driver.delete_all_cookies()



if __name__ == "__main__":
    while(True):
        cf.error_flag = 0
        cf.complete_flag = 0
        cf.end_flag = 0
        print("ok let's start")
        main()
        if(cf.end_flag == 1):
            driver.quit()
            break


