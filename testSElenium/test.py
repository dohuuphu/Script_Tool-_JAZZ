from action_funtion import *

def setup2():
    driver.get("https://rationalcld.dl.net/qm/web/console/ID%20%28Test%29#action=com.ibm.rqm.planning.home.actionDispatcher&subAction=viewTestPlan&id=1439")
    
    #driver.maximize_window()

    # Login to webpage
    Send_Tag_htlm(ID_tag, timeout, IDuser_id)
    Send_Tag_htlm(ID_tag, timeout, password_id)
    Click_Tag_htlm(text_Tag, timeout, Login_text)
    Click_Tag_htlm(text_Tag, timeout, Testsuit_records_text)
    Check_Result()

    # # Click Run
    # Click_Tag_htlm(aria_label_tag ,timeout, Run_btn_arialable)
    # Click_Tag_htlm(Class_tag, timeout, Run_testsuit_class)
    # Edit_build_record()



def main():
    setup2()


if __name__ == "__main__":
    main()
    