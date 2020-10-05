from action_funtion import *

def setup2():
    driver.get("https://rationalcld.dl.net/qm/web/console/ID%20%28Test%29#action=com.ibm.rqm.planning.home.actionDispatcher&subAction=viewSER&id=244409")
    #driver.maximize_window()

    # Login to webpage
    Send_Tag_htlm(ID_tag, timeout, IDuser_id)
    Send_Tag_htlm(ID_tag, timeout, password_id)
    Click_Tag_htlm(text_Tag, timeout, Login_text)

    # Click Run
    Click_Tag_htlm(aria_label_tag ,timeout, Run_btn_arialable)
    Click_Tag_htlm(text_Tag, timeout, Run_text)
    Edit_build_record()



def main():
    setup2()


if __name__ == "__main__":
    main()
    