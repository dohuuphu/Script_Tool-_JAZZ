from action_funtion import *

def setup2():
    driver.get("https://rationalcld.dl.net/qm/web/console/ID%20%28Test%29#action=com.ibm.rqm.planning.home.actionDispatcher&subAction=viewTestPlan&id=1439")
    
    #driver.maximize_window()

    # Login to webpage
    Send_Tag_htlm(ID_tag, timeout, IDuser_id)
    Send_Tag_htlm(ID_tag, timeout, password_id)
    Click_Tag_htlm(text_Tag, timeout, Login_text)
    time.sleep(20)
    string = driver.find_elements_by_xpath("//div[@id =\"com_ibm_asq_common_web_ui_internal_view_common_EditorSection_10\"]//*[@class=\"content-status-area\"]")[0]
    textcontent = string.textContent
    text= string.get_attribute("text()")
    print("text", text)
    print("textcontent: ", textcontent)

    # # Click Run
    # Click_Tag_htlm(aria_label_tag ,timeout, Run_btn_arialable)
    # Click_Tag_htlm(Class_tag, timeout, Run_testsuit_class)
    # Edit_build_record()



def main():
    setup2()


if __name__ == "__main__":
    main()
    